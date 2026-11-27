"""Dựng ô đất lặp 512x512 pixel art 1:1 cho map Âm Giới (tự làm bằng code, 27/11, ChatGPT hết lượt). Bản 2: cục đất có sáng-tối, đá nhiều cỡ có viền, cỏ khô, nứt ngắn.
Dùng: python3 o_dat.py <map> <x0,y0,x1,y1 vùng sân trong bg 1600x1140> <ra.png> [seed]"""
import sys, numpy as np
from PIL import Image
key, box, out = sys.argv[1], [int(v) for v in sys.argv[2].split(',')], sys.argv[3]
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 7
rng = np.random.default_rng(seed)
N = 512
a = np.asarray(Image.open(f'game/assets/map/bg_{key}.png').convert('RGB').crop(box)).reshape(-1, 3).astype(float)
lum = a @ [0.3, 0.59, 0.11]
lo_, hi_ = np.quantile(lum, [0.12, 0.97]); k = (lum > lo_) & (lum < hi_); a, lum = a[k], lum[k]
base = a.mean(0)
def tone(f, warm=0.0):
    c = base * f; c = c + np.array([1, 0.6, -0.4]) * warm
    return np.clip(c, 0, 255)
# bảng: 0 viền tối, 1 bóng sâu, 2 đất tối, 3 đất, 4 đất sáng, 5 cục sáng, 6 đỉnh sáng, 7 cỏ khô tối, 8 cỏ khô sáng, 9 đá tối, 10 đá, 11 đá sáng
P = np.array([tone(.42), tone(.64), tone(.87), tone(.94), tone(1.01), tone(1.16, 6), tone(1.32, 10),
              tone(.98, 6) * [1, 1, .9], tone(1.2, 10) * [1, 1, .85],
              tone(.6) * .55 + np.array([1,1,1]) * base.mean() * .6 * .45, tone(.9) * .55 + np.array([1,1,1]) * base.mean() * .9 * .45, tone(1.2) * .55 + np.array([1,1,1]) * base.mean() * 1.2 * .45])
def pnoise(cells):
    g = rng.random((cells, cells)); x = np.arange(N) * cells / N
    i0 = np.floor(x).astype(int); f = x - i0; f = f * f * (3 - 2 * f); i1 = (i0 + 1) % cells
    r0 = g[i0][:, i0] * (1 - f)[None, :] + g[i0][:, i1] * f[None, :]
    r1 = g[i1][:, i0] * (1 - f)[None, :] + g[i1][:, i1] * f[None, :]
    return r0 * (1 - f)[:, None] + r1 * f[:, None]
h = 0.42 * pnoise(6) + 0.24 * pnoise(16) + 0.2 * pnoise(48) + 0.14 * pnoise(160)
idx = (2 + np.searchsorted(np.quantile(h, [0.28, 0.74]), h)).astype(int)  # 2,3,4: mảng đất lớn mềm
moist = pnoise(10)
def put(y, x, v): idx[y % N, x % N] = v
def get(y, x): return idx[y % N, x % N]
# cục đất nhỏ: thân = tông nền +1, mép trên 1px sáng, mép dưới 1px tối
for _ in range(2300):
    cy, cx = rng.integers(0, N, 2); w = int(rng.choice([1, 2, 2, 3, 3, 4])); hh = int(rng.choice([1, 1, 2]))
    b = get(cy, cx)
    for dx in range(w):
        put(cy - 1, cx + dx, min(6, b + 2) if (0 < dx < w - 1 or w < 3) else b)
        for dy in range(hh): put(cy + dy, cx + dx, min(5, b + 1))
        put(cy + hh, cx + dx, max(1, b - 1))
# đá nhiều cỡ: hình bất quy tắc, 3 tông + viền tối 1px phía dưới-phải
for _ in range(95):
    cy, cx = rng.integers(0, N, 2); r = float(rng.choice([1.5, 2, 2, 2.5, 3, 3.5, 4.5, 6], p=[.2, .2, .15, .15, .12, .08, .06, .04]))
    ry = r * rng.uniform(.55, .8); ph = rng.random(6) * 6.28
    cells = []
    for dy in range(-int(ry) - 1, int(ry) + 2):
        for dx in range(-int(r) - 1, int(r) + 2):
            ang = np.arctan2(dy / max(ry, .5), dx / r); wob = 1 + .18 * np.sin(3 * ang + ph[0]) + .1 * np.sin(5 * ang + ph[1])
            if (dx / r) ** 2 + (dy / max(ry, .5)) ** 2 <= wob * wob: cells.append((dy, dx))
    S = set(cells)
    for dy, dx in cells:
        s = -dx / r - 1.6 * dy / max(ry, .5)
        put(cy + dy, cx + dx, 11 if s > .55 else 10 if s > -.5 else 9)
    for dy, dx in cells:
        for ey, ex in ((1, 0), (0, 1), (1, 1)):
            if (dy + ey, dx + ex) not in S: put(cy + dy + ey, cx + dx + ex, 0 if ey else 1)
    for dx in range(-int(r), int(r) + 3): 
        if (int(ry) + 2, dx) not in S and get(cy + int(ry) + 2, cx + dx) < 9: put(cy + int(ry) + 2, cx + dx, 1)
# cỏ khô: cụm 2-5 lá chữ V, chỗ đất ẩm (moist cao)
for _ in range(130):
    cy, cx = rng.integers(0, N, 2)
    if moist[cy, cx] < .45 and rng.random() < .7: continue
    for _ in range(int(rng.integers(2, 6))):
        x = cx + int(rng.integers(-3, 4)); L = int(rng.integers(2, 6)); lean = rng.choice([-1, 0, 0, 1])
        for t in range(L):
            put(cy - t, x + (lean * t) // 2, 8 if t >= L - 2 else 7)
        put(cy + 1, x, 1)
# nứt ngắn gấp khúc
for _ in range(14):
    y, x = rng.integers(0, N, 2); ang = rng.random() * 6.28
    for s in range(int(rng.integers(10, 28))):
        if rng.random() < .25: ang += rng.choice([-.9, .9])
        y += int(round(np.sin(ang))); x += int(round(np.cos(ang)))
        if get(y, x) < 9: put(y, x, 0); 
        if get(y + 1, x) < 7: put(y + 1, x, 5)
img = Image.fromarray(P[idx].clip(0, 255).astype(np.uint8))
img.save(out, optimize=True)
print(out, img.size, len(img.getcolors(4096)), 'màu')
