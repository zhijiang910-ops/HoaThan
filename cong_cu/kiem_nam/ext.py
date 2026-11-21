"""Kéo dài lưỡi kiếm của hero_nam theo điểm chuôi/mũi đánh dấu tay, xuất sheet mới có lề."""
import json, math, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
import numpy as np
from PIL import Image, ImageDraw

SRC = HERE / 'hero_nam_goc.png'   # sheet gốc 107x114, chưa nối kiếm
META = json.load(open(HERE / 'meta_goc.json'))['hero_nam']
SH = np.array(Image.open(SRC).convert('RGBA')).astype(int)
W, H = META['w'], META['h']
PAD = 12
RATIO = float(sys.argv[1]) if len(sys.argv) > 1 else 0.30
HIP = [((59, 69), (78, 81))]
# (chuôi, mũi) trong toạ độ frame gốc
B = {
 ('idle', 0): HIP, ('idle', 1): [((59, 69), (80, 81))], ('idle', 2): [((60, 70), (79, 81))], ('idle', 3): [((59, 70), (79, 81))],
 ('run', 0): [((35, 72), (9, 82))], ('run', 1): [((34, 71), (8, 81))], ('run', 2): [((35, 71), (8, 81))], ('run', 3): [((29, 63), (3, 72))],
 ('run', 4): [((35, 66), (7, 76))], ('run', 5): [((39, 72), (11, 82))], ('run', 6): [((34, 70), (8, 80))], ('run', 7): [((31, 66), (7, 75))],
 ('attack', 0): [((59, 69), (78, 82))], ('attack', 1): [((63, 51), (84, 44))], ('attack', 2): [((59, 13), (59, 0))], ('attack', 3): [((65, 37), (76, 11))],
 ('attack', 4): [((70, 65), (80, 91))], ('attack', 5): [((54, 73), (36, 94))], ('attack', 6): [((67, 62), (82, 63))], ('attack', 7): [((64, 47), (80, 35))],
 ('attack2', 0): [((59, 70), (78, 81))], ('attack2', 1): [((59, 70), (78, 81))], ('attack2', 2): [((59, 70), (78, 81)), ((28, 72), (17, 96))],
 ('attack2', 3): [((74, 46), (95, 29))], ('attack2', 4): [((77, 45), (99, 27))], ('attack2', 5): [((65, 54), (87, 32))], ('attack2', 6): [((62, 62), (88, 62))],
 ('attack2', 7): [((58, 69), (78, 81))],
 ('hit', 0): HIP, ('hit', 1): [((56, 65), (79, 69))], ('hit', 2): [((58, 68), (80, 75))], ('hit', 3): [((59, 69), (77, 80))],
 ('death', 0): HIP, ('death', 1): [((65, 87), (86, 94))], ('death', 2): [((81, 100), (96, 101))], ('death', 3): [((91, 102), (104, 102))],
}

def is_blade(px):
    r, g, b, a = px
    if a == 0: return False
    mx, mn = max(r, g, b), min(r, g, b); lum = (r + g + b) / 3
    return (mx - mn <= 40 and lum >= 70) or lum <= 48

def refine(fr, base, tip):
    """Dời mũi tới pixel lưỡi xa nhất dọc trục (sai số đánh dấu tay ±2px)."""
    b = np.array(base, float); t = np.array(tip, float)
    ax = (t - b) / np.linalg.norm(t - b); nrm = np.array([-ax[1], ax[0]])
    best = 0
    for y in range(fr.shape[0]):
        for x in range(fr.shape[1]):
            p = np.array([x, y], float) - b
            u, v = p @ ax, p @ nrm
            if abs(v) <= 2.6 and u > best and is_blade(fr[y, x]) and sum(fr[y, x][:3]) / 3 >= 70:
                best = u
    L = max(best, np.linalg.norm(t - b) * .8)
    return b, ax, nrm, L

def extend(fr, segs):
    h, w = fr.shape[:2]
    out = np.zeros((h + 2 * PAD, w + 2 * PAD, 4), int); out[PAD:PAD + h, PAD:PAD + w] = fr
    for base, tip in segs:
        b, ax, nrm, L = refine(fr, base, tip)
        add = max(5, L * RATIO)
        # bước nguyên gần trục lưỡi nhất, dài xấp xỉ `add`
        best = None
        for per in np.arange(max(5, add - 3), add + 3.01, .5):
            vv = np.round(ax * per); err = np.linalg.norm(vv - ax * per)
            if best is None or err < best[0]: best = (err, vv.astype(int), np.linalg.norm(vv))
        _, v, per = best
        m = L * .45
        bright = lambda px: px[3] > 0 and sum(px[:3]) / 3 >= 70 and max(px[:3]) - min(px[:3]) <= 40
        band = {}
        for y in range(h):
            for x in range(w):
                p = np.array([x, y], float) - b; u, q = p @ ax, p @ nrm
                if u >= m - per - .5 and u <= L + 2.5 and abs(q) <= 3.6 and is_blade(fr[y, x]):
                    px = fr[y, x]
                    if not bright(px):   # viền tối: chỉ giữ khi sát pixel lưỡi sáng
                        ok = any(0 <= y + dy < h and 0 <= x + dx < w and bright(fr[y + dy, x + dx])
                                 for dy in (-1, 0, 1) for dx in (-1, 0, 1))
                        if not ok: continue
                    band[(x, y)] = (u, px)
        for (x, y), (u, px) in band.items():
            if u >= m: out[y + PAD, x + PAD] = 0
        def put(x, y, px):
            ox, oy = x + PAD, y + PAD
            if 0 <= ox < out.shape[1] and 0 <= oy < out.shape[0]: out[oy, ox] = px
        for (x, y), (u, px) in band.items():          # đoạn chèn: lặp lại một đoạn thân lưỡi
            if m - per <= u < m: put(x + v[0], y + v[1], px)
        for (x, y), (u, px) in band.items():          # nửa ngoài + mũi dời ra
            if u >= m: put(x + v[0], y + v[1], px)
    return out

def build():
    cells = []
    for an, A in META['anims'].items():
        for k, (x, y) in enumerate(A['f']):
            fr = SH[y:y + H, x:x + W]
            segs = B.get((an, k), [])
            cells.append((an, k, extend(fr, segs) if segs else np.pad(fr, ((PAD, PAD), (PAD, PAD), (0, 0)))))
    cw, ch = W + 2 * PAD, H + 2 * PAD
    cols = 16
    rows = math.ceil(len(cells) / cols)
    sheet = np.zeros((rows * ch, cols * cw, 4), 'uint8')
    meta = {'w': cw, 'h': ch, 'ax': META['ax'] + PAD, 'ay': META['ay'] + PAD, 'anims': {}}
    for an in META['anims']:
        meta['anims'][an] = {k: v for k, v in META['anims'][an].items() if k != 'f'}; meta['anims'][an]['f'] = []
    for i, (an, k, c) in enumerate(cells):
        cx, cy = (i % cols) * cw, (i // cols) * ch
        sheet[cy:cy + ch, cx:cx + cw] = c.astype('uint8')
        meta['anims'][an]['f'].append([cx, cy])
    for kk in META:
        if kk not in meta: meta[kk] = META[kk]
    return Image.fromarray(sheet, 'RGBA'), meta

if __name__ == '__main__':
    im, meta = build()
    im.save(HERE / 'hero_nam_long.png', optimize=True)
    meta['pad'] = PAD
    json.dump(meta, open(HERE / 'hero_nam_long.json', 'w'))
    # ảnh so sánh: gốc | mới
    tiles = []
    i = 0
    for an, A in META['anims'].items():
        for k, (x, y) in enumerate(A['f']):
            fr = np.pad(SH[y:y + H, x:x + W], ((PAD, PAD), (PAD, PAD), (0, 0))).astype('uint8')
            nx, ny = meta['anims'][an]['f'][k]
            nw = np.array(im)[ny:ny + meta['h'], nx:nx + meta['w']]
            pair = np.concatenate([fr, nw], 1)
            t = Image.fromarray(pair, 'RGBA'); bg = Image.new('RGBA', t.size, '#4b4f6e'); bg.alpha_composite(t)
            ImageDraw.Draw(bg).text((2, 2), f'{an}{k}', fill='yellow')
            tiles.append(bg.resize((bg.width * 3, bg.height * 3), Image.NEAREST))
    for s in range(0, len(tiles), 6):
        g = tiles[s:s + 6]; sh = Image.new('RGB', (g[0].width * 3, g[0].height * 2), '#222')
        for j, t in enumerate(g): sh.paste(t.convert('RGB'), ((j % 3) * t.width, (j // 3) * t.height))
        sh.save(HERE / f'so_sanh_{s // 6}.png')
