"""Chuyển nhân vật gói Wuxia Vol.2 (frame rời, hướng east) thành sheet + meta theo định dạng CHM của game.

python wuxia_sheet.py <thư_mục_04_Integrated> "<tên nhân vật trong ANIMATION_LIBRARY>" <id_game> <thư_mục_ra>
Xuất <id>.png và <id>.json (w,h,ax,ay,anims{idle,run,attack,attack2,hit,death[,cast]}).
"""
import json, sys, os
from PIL import Image
R, NAME, ID, OUT = sys.argv[1].rstrip('/') + '/', sys.argv[2], sys.argv[3], sys.argv[4]
lib = json.load(open(R + 'Characters/ANIMATION_LIBRARY.json', encoding='utf-8'))
ch = next(c for c in lib['characters'] if c['name'] == NAME)
MAP = [('idle', 'idle'), ('run', 'walk'), ('attack', 'attack'), ('attack2', 'attack_secondary'), ('hit', 'hurt'), ('death', 'death'), ('cast', 'cast')]
clips = {}
for game, src in MAP:
    v = ch['clips'].get(src)
    if not v: continue
    e = v.get('east') or v[next(iter(v))]
    ims = [Image.open(R + f).convert('RGBA') for f in e['files']]
    ms = e.get('durations_ms') or [1000 / (e.get('fps') or 10)] * len(ims)
    clips[game] = dict(ims=ims, ax=e['anchor'][0], ay=e['anchor'][1], fps=round(1000 / (sum(ms) / len(ms)), 2))
if 'attack2' not in clips: clips['attack2'] = clips['attack']
# khung chung theo điểm neo
L = max(c['ax'] for c in clips.values()); U = max(c['ay'] for c in clips.values())
Rr = max(c['ims'][0].width - c['ax'] for c in clips.values()); D = max(c['ims'][0].height - c['ay'] for c in clips.values())
W, H = L + Rr, U + D
cells = []
for k, c in clips.items():
    for im in c['ims']:
        cell = Image.new('RGBA', (W, H)); cell.paste(im, (L - c['ax'], U - c['ay'])); cells.append((k, cell))
# cắt lề trống chung
bb = None
for _, cimg in cells:
    b = cimg.getbbox()
    if b: bb = b if bb is None else (min(bb[0], b[0]), min(bb[1], b[1]), max(bb[2], b[2]), max(bb[3], b[3]))
x0, y0, x1, y1 = bb; x0 = max(0, x0 - 2); y0 = max(0, y0 - 2); x1 = min(W, x1 + 2); y1 = max(y1, U + 2)
cw, chh = x1 - x0, y1 - y0
COLS = max(1, min(16, 4096 // cw))
sheet = Image.new('RGBA', (COLS * cw, ((len(cells) + COLS - 1) // COLS) * chh))
anims = {}
for i, (k, cimg) in enumerate(cells):
    px, py = (i % COLS) * cw, (i // COLS) * chh
    sheet.paste(cimg.crop((x0, y0, x1, y1)), (px, py))
    anims.setdefault(k, {'fps': clips[k]['fps'], 'f': []})['f'].append([px, py])
os.makedirs(OUT, exist_ok=True)
sheet.save(os.path.join(OUT, ID + '.png'), optimize=True)
meta = {'w': cw, 'h': chh, 'ax': L - x0, 'ay': U - y0, 'anims': anims, 'src': 'assets/' + ID + '.png', 'realRun': True, 'wuxia': NAME}
json.dump(meta, open(os.path.join(OUT, ID + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print(ID, sheet.size, 'cell', cw, chh, 'anchor', meta['ax'], meta['ay'], {k: len(v['f']) for k, v in anims.items()})
