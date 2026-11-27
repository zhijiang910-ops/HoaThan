"""Dựng ô đất lặp 512x512 pixel art 1:1 cho map Âm Giới (tự làm bằng code, 27/11; ChatGPT hết lượt, CẤM PixelLab).
Luật 11: giữ phong cách game + bối cảnh âm phủ. Mỗi map một mẫu (PRESET) có chi tiết riêng.
Dùng: python3 cong_cu/claude/o_dat.py <map|all> [seed]   -> game/assets/map/Dt_<map>.png"""
import sys, numpy as np
from PIL import Image
N = 512
PRESET = {
 # box = vùng sân đất trong bg_<map>.png (1600x1140) để lấy màu
 'hoangtuyen': dict(box=(100, 250, 1500, 1000), clods=2300, stones=95, grass=60, bones=45, ash=500, blood=10, cracks=14),
 'quanmon':    dict(box=(200, 440, 1400, 1000), clods=2000, stones=130, grass=30, bones=35, ash=350, blood=6, cracks=18, chain=9),
 'biangan':    dict(box=(200, 400, 1400, 1000), clods=1900, stones=70, grass=20, bones=25, ash=250, blood=8, cracks=12, petals=170, acc=[(170, 32, 40), (120, 18, 30), (70, 10, 20)]),
 'nghiepkinh': dict(box=(200, 450, 1400, 950), clods=1700, stones=120, grass=0, bones=25, ash=300, blood=4, cracks=22, shards=70, acc=[(205, 230, 225), (140, 175, 180), (70, 90, 100)]),
 'uongtu':     dict(box=(200, 450, 1400, 1000), clods=1800, stones=90, grass=0, bones=40, ash=900, blood=8, cracks=20, char=14, embers=130, acc=[(250, 170, 70), (215, 80, 30), (120, 30, 20)]),
 'vongxuyen':  dict(box=(200, 700, 1400, 1100), clods=2000, stones=80, grass=25, bones=25, ash=200, blood=3, cracks=8, puddles=18, acc=[(95, 140, 140), (40, 72, 78), (20, 38, 44)]),
 'diemla':     dict(box=(200, 500, 1400, 1000), clods=300, stones=10, grass=0, bones=18, ash=260, blood=14, cracks=30, flag=70),
}
def build(key, seed=7):
    C = PRESET[key]; rng = np.random.default_rng(seed)
    a = np.asarray(Image.open(f'game/assets/map/bg_{key}.png').convert('RGB').crop(C['box'])).reshape(-1, 3).astype(float)
    lum = a @ [0.3, 0.59, 0.11]; lo_, hi_ = np.quantile(lum, [0.12, 0.97]); k = (lum > lo_) & (lum < hi_); a = a[k]
    base = a.mean(0); g = base.mean()
    def tone(f, warm=0.0): return np.clip(base * f + np.array([1, .6, -.4]) * warm, 0, 255)
    acc = np.array(C.get('acc', [(150, 140, 120)] * 3), float)
    P = np.array([tone(.42), tone(.64), tone(.87), tone(.94), tone(1.01), tone(1.16, 6), tone(1.32, 10),
                  tone(.78) * .6 + g * .78 * .4, tone(.98) * .6 + g * .98 * .4,
                  tone(.6) * .55 + g * .6 * .45, tone(.9) * .55 + g * .9 * .45, tone(1.2) * .55 + g * 1.2 * .45,
                  (172, 162, 138), (124, 114, 96), (88, 30, 24), np.clip(tone(.8) * .4 + g * .9 * .6, 0, 255),
                  acc[0], acc[1], acc[2], (38, 36, 40), (96, 94, 100)])
    # 0 viền | 1 bóng | 2-4 đất | 5-6 sáng | 7-8 cỏ chết | 9-11 đá | 12-13 xương | 14 máu khô | 15 tro | 16-18 nhấn | 19-20 sắt
    def pnoise(cells):
        G = rng.random((cells, cells)); x = np.arange(N) * cells / N
        i0 = np.floor(x).astype(int); f = x - i0; f = f * f * (3 - 2 * f); i1 = (i0 + 1) % cells
        r0 = G[i0][:, i0] * (1 - f)[None, :] + G[i0][:, i1] * f[None, :]
        r1 = G[i1][:, i0] * (1 - f)[None, :] + G[i1][:, i1] * f[None, :]
        return r0 * (1 - f)[:, None] + r1 * f[:, None]
    h = 0.42 * pnoise(6) + 0.24 * pnoise(16) + 0.2 * pnoise(48) + 0.14 * pnoise(160)
    idx = (2 + np.searchsorted(np.quantile(h, [0.28, 0.74]), h)).astype(int)
    moist = pnoise(10)
    def put(y, x, v): idx[y % N, x % N] = v
    def get(y, x): return idx[y % N, x % N]
    if C.get('flag'):  # đá phiến cổ (Diêm La): tảng không đều lặp liền, kẽ đất tối lởm chởm, mép trên sáng, mép dưới bóng, góc mòn
        ns = C['flag']; pts = []
        while len(pts) < ns:
            q = rng.random(2) * N
            ok = all(min(abs(q[0]-a0), N-abs(q[0]-a0))**2 + min(abs(q[1]-a1), N-abs(q[1]-a1))**2 > 44**2 for a0, a1 in pts)
            if ok or rng.random() < .002: pts.append(q)
        yy, xx = np.mgrid[0:N, 0:N]
        d1 = np.full((N, N), 1e9); d2 = np.full((N, N), 1e9); lab = np.zeros((N, N), int)
        wob = (pnoise(32) - .5) * 7 + (pnoise(96) - .5) * 3
        for k, (py, px) in enumerate(pts):
            dy = np.abs(yy - py); dy = np.minimum(dy, N - dy); dx = np.abs(xx - px); dx = np.minimum(dx, N - dx)
            d = np.sqrt(dx * dx + dy * dy * 1.3)
            m = d < d1; d2 = np.where(m, d1, np.minimum(d2, d)); lab = np.where(m, k, lab); d1 = np.where(m, d, d1)
        gap = d2 - d1 + wob * .35
        tone_c = rng.choice([2, 3, 3, 4, 4], len(pts))
        tex = pnoise(48) + .5 * pnoise(128)
        idx[:] = np.clip(tone_c[lab] + (tex > np.quantile(tex, .8)) - (tex < np.quantile(tex, .18)), 2, 4)
        J = gap < 2.6 + (pnoise(64) > .6) * 1.2  # kẽ, chỗ dày chỗ mảnh
        idx[J] = 1; idx[J & (gap < 1.4)] = 0
        up = np.roll(J, 1, 0) | np.roll(J, 2, 0); dn = np.roll(J, -1, 0)
        idx[~J & up & ~np.roll(J, 1, 1)] = 5   # mép trên tảng sáng
        idx[~J & dn] = 1                      # mép dưới tảng bóng
        for _ in range(1400):  # đất, tro lấp kẽ và góc sứt
            y, x = rng.integers(0, N, 2)
            if gap[y, x] < 4.5: put(y, x, int(rng.choice([1, 15, 2, 0])))
    if C.get('slabs'):  # đá lát điện Diêm La: hàng so le 32x24, mạch vữa tối, mép trên sáng
        SW, SH = 48, 40
        for r in range(N // SH + 1):
            off = (r % 2) * SW // 2
            for c in range(-1, N // SW + 1):
                x0, y0 = c * SW + off, r * SH; t = int(rng.choice([2, 3, 3, 4]))
                for yy in range(y0, y0 + SH):
                    for xx in range(x0, x0 + SW):
                        e = (yy == y0 or xx == x0)
                        v = 1 if e else (5 if (yy == y0 + 1 and rng.random() < .6) else t)
                        if not e and rng.random() < .05: v = max(2, t - 1)
                        put(yy, xx, v)
    if C.get('char'):  # mảng đất cháy đen (Uổng Tử)
        ch = pnoise(8) + 0.35 * pnoise(96); thr = np.quantile(ch, .8)
        m = ch > thr; idx[m] = 2; idx[m & (ch > np.quantile(ch, .9))] = 1
        edge = (ch > thr - .04) & ~m; idx[edge & (rng.random((N, N)) < .5)] = 15
    # cục đất nhỏ
    for _ in range(C['clods']):
        cy, cx = rng.integers(0, N, 2); w = int(rng.choice([1, 2, 2, 3, 3, 4])); hh = int(rng.choice([1, 1, 2])); b = get(cy, cx)
        if b < 2 or b > 4: continue
        for dx in range(w):
            put(cy - 1, cx + dx, min(6, b + 2) if (0 < dx < w - 1 or w < 3) else b)
            for dy in range(hh): put(cy + dy, cx + dx, min(5, b + 1))
            put(cy + hh, cx + dx, max(1, b - 1))
    # đá
    for _ in range(C['stones']):
        cy, cx = rng.integers(0, N, 2); r = float(rng.choice([1.5, 2, 2, 2.5, 3, 3.5, 4.5, 6], p=[.2, .2, .15, .15, .12, .08, .06, .04]))
        ry = r * rng.uniform(.55, .8); ph = rng.random(2) * 6.28; cells = []
        for dy in range(-int(ry) - 1, int(ry) + 2):
            for dx in range(-int(r) - 1, int(r) + 2):
                ang = np.arctan2(dy / max(ry, .5), dx / r); wob = 1 + .18 * np.sin(3 * ang + ph[0]) + .1 * np.sin(5 * ang + ph[1])
                if (dx / r) ** 2 + (dy / max(ry, .5)) ** 2 <= wob * wob: cells.append((dy, dx))
        S = set(cells)
        for dy, dx in cells:
            s = -dx / r - 1.6 * dy / max(ry, .5); put(cy + dy, cx + dx, 11 if s > .55 else 10 if s > -.5 else 9)
        for dy, dx in cells:
            for ey, ex in ((1, 0), (0, 1), (1, 1)):
                if (dy + ey, dx + ex) not in S: put(cy + dy + ey, cx + dx + ex, 0 if ey else 1)
    # cỏ chết xám, rủ
    for _ in range(C['grass']):
        cy, cx = rng.integers(0, N, 2)
        if moist[cy, cx] < .45 and rng.random() < .7: continue
        for _ in range(int(rng.integers(2, 5))):
            x = cx + int(rng.integers(-3, 4)); L = int(rng.integers(2, 4)); lean = rng.choice([-2, -1, 1, 2])
            for t in range(L): put(cy - t, x + (lean * t) // 2, 7 if t < L - 1 else 8)
            put(cy + 1, x, 1)
    # vũng nước tù (Vong Xuyên): elip tối, viền trên sáng, 1 đốm phản chiếu
    for _ in range(C.get('puddles', 0)):
        cy, cx = rng.integers(0, N, 2); rx = rng.uniform(6, 16); ry = rx * rng.uniform(.35, .5)
        for dy in range(-int(ry) - 1, int(ry) + 2):
            for dx in range(-int(rx) - 1, int(rx) + 2):
                d = (dx / rx) ** 2 + (dy / ry) ** 2 + .12 * np.sin(dx * .7 + dy)
                if d <= 1: put(cy + dy, cx + dx, 18 if d < .55 else 17)
                elif d <= 1.25 and dy > 0: put(cy + dy, cx + dx, 1)
        put(cy - int(ry * .3), cx - int(rx * .3), 16); put(cy - int(ry * .3), cx - int(rx * .3) + 1, 16)
    # xương vụn
    for _ in range(C['bones']):
        cy, cx = rng.integers(0, N, 2); L = int(rng.integers(3, 8)); d = [(0, 1), (1, 1), (1, -1), (0, 1)][int(rng.integers(4))]
        for t in range(L):
            y, x = cy + d[0] * t, cx + d[1] * t; put(y, x, 12); put(y + 1, x, 13 if t not in (0, L - 1) else 1)
        for e in (0, L - 1):
            y, x = cy + d[0] * e, cx + d[1] * e; put(y - 1, x, 12); put(y, x + (1 if d[1] >= 0 else -1), 13)
    # xích sắt gãy (Quỷ Môn Quan): mắt xích 3x2 nối nhau theo đường cong
    for _ in range(C.get('chain', 0)):
        y, x = rng.integers(0, N, 2); ang = rng.random() * 6.28
        for i in range(int(rng.integers(5, 11))):
            ang += rng.normal(0, .3); y += int(round(np.sin(ang) * 3)); x += int(round(np.cos(ang) * 3))
            if i % 2 == 0:
                for dx in range(3): put(y - 1, x + dx, 20); put(y + 1, x + dx, 19)
                put(y, x, 19); put(y, x + 2, 19); put(y + 2, x + 1, 0)
            else:
                put(y - 1, x + 1, 20); put(y, x + 1, 19); put(y + 1, x + 1, 19); put(y + 2, x + 1, 0)
    # cánh hoa bỉ ngạn rụng: mảnh 2-4 px cong, 3 tông đỏ
    for _ in range(C.get('petals', 0) // 5):
        ccy, ccx = rng.integers(0, N, 2)
        for _ in range(int(rng.integers(2, 9))):
            cy, cx = ccy + int(rng.integers(-14, 15)), ccx + int(rng.integers(-10, 11)); L = int(rng.integers(3, 7)); dx0 = int(rng.choice([-1, 1]))
            for t in range(L):
                y, x = cy + (t * t) // 4, cx + dx0 * t; put(y, x, 16 if t < 2 else 17); put(y + 1, x, 18 if t < L - 1 else 1)
    # mảnh gương vỡ (Nghiệt Kính): tam giác nhỏ lạnh, 1 điểm loé
    for _ in range(C.get('shards', 0)):
        cy, cx = rng.integers(0, N, 2); s = int(rng.integers(2, 5)); fl = int(rng.choice([-1, 1]))
        for yy in range(s):
            for xx in range(s - yy): put(cy + yy, cx + fl * xx, 17 if xx + yy < s - 1 else 18)
        put(cy, cx, 16); put(cy + s, cx, 1)
    # tro + máu khô
    for _ in range(C['ash']):
        y, x = rng.integers(0, N, 2)
        if get(y, x) < 9: put(y, x, 15)
    for _ in range(C['blood']):
        cy, cx = rng.integers(0, N, 2); r = rng.uniform(1.5, 4)
        for dy in range(-3, 4):
            for dx in range(-5, 6):
                if (dx / r) ** 2 + (dy / (r * .6)) ** 2 <= 1 and rng.random() < .8 and get(cy + dy, cx + dx) < 7: put(cy + dy, cx + dx, 14)
    # than hồng (Uổng Tử): lõi cam, viền đỏ sẫm, nằm trên đất cháy
    for _ in range(C.get('embers', 0)):
        cy, cx = rng.integers(0, N, 2); big = rng.random() < .3
        put(cy, cx, 16 if big else 17)
        for ey, ex in ((0, 1), (1, 0), (0, -1), (-1, 0)) if big else ((0, 1),):
            if get(cy + ey, cx + ex) < 7: put(cy + ey, cx + ex, 18)
    # nứt
    for _ in range(C['cracks']):
        y, x = rng.integers(0, N, 2); ang = rng.random() * 6.28
        for s in range(int(rng.integers(10, 28))):
            if rng.random() < .25: ang += rng.choice([-.9, .9])
            y += int(round(np.sin(ang))); x += int(round(np.cos(ang)))
            if get(y, x) < 9: put(y, x, 0)
            if get(y + 1, x) < 7: put(y + 1, x, 5)
    img = Image.fromarray(P[idx].clip(0, 255).astype(np.uint8))
    out = f'game/assets/map/Dt_{key}.png'; img.save(out, optimize=True)
    print(out, len(img.getcolors(4096)), 'màu')
if __name__ == '__main__':
    ks = list(PRESET) if sys.argv[1] == 'all' else [sys.argv[1]]
    for k in ks: build(k, int(sys.argv[2]) if len(sys.argv) > 2 else 7)
