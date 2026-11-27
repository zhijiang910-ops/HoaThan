"""Dựng ô đất lặp 512x512 pixel art 1:1 cho map Âm Giới (tự làm bằng code, 27/11, ChatGPT hết lượt).
Dùng: python3 o_dat.py <map> <x0,y0,x1,y1 vùng sân trong bg 1600x1140> <ra.png> [seed]
Bảng màu lấy từ sân đất của chính ảnh nền map nên khớp màu."""
import sys, numpy as np
from PIL import Image
key, box, out = sys.argv[1], [int(v) for v in sys.argv[2].split(',')], sys.argv[3]
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 7
rng = np.random.default_rng(seed)
N = 512
bg = Image.open(f'game/assets/map/bg_{key}.png').convert('RGB').crop(box)
a = np.asarray(bg).reshape(-1, 3).astype(float)
lum = a @ [0.3, 0.59, 0.11]
lo_, hi_ = np.quantile(lum, [0.12, 0.97]); keep = (lum > lo_) & (lum < hi_); a, lum = a[keep], lum[keep]
qs = np.quantile(lum, [0.12, 0.3, 0.5, 0.7, 0.86, 0.96])
# 7 tông theo độ sáng: tối hơn sân một chút ở đáy, sáng hơn ở đỉnh
pal = []
for lo, hi in zip([0] + list(qs), list(qs) + [999]):
    m = (lum >= lo) & (lum < hi)
    pal.append(a[m].mean(0) if m.any() else a.mean(0))
pal = np.array(pal)
dark = pal[0] * 0.6; light = np.minimum(255, pal[-1] * 1.32 + 14)
P = np.vstack([dark, pal, light])  # 0..8

def pnoise(cells):
    g = rng.random((cells, cells))
    x = np.arange(N) * cells / N
    i0 = np.floor(x).astype(int); f = x - i0; f = f * f * (3 - 2 * f)
    i1 = (i0 + 1) % cells
    r0 = g[i0][:, i0] * (1 - f)[None, :] + g[i0][:, i1] * f[None, :]
    r1 = g[i1][:, i0] * (1 - f)[None, :] + g[i1][:, i1] * f[None, :]
    return r0 * (1 - f)[:, None] + r1 * f[:, None]

h = 0.42 * pnoise(8) + 0.30 * pnoise(16) + 0.18 * pnoise(48) + 0.10 * pnoise(128)
q = np.quantile(h, [0.04, 0.16, 0.38, 0.62, 0.84, 0.95])
idx = 1 + np.searchsorted(q, h)  # 1..7
idx = idx.astype(int)

def put(y, x, v):
    idx[y % N, x % N] = v

# vết nứt: bước ngẫu nhiên, nét 1 px tối, mép dưới 1 px sáng
for _ in range(22):
    y, x = rng.integers(0, N, 2); ang = rng.random() * 6.28
    for s in range(int(rng.integers(14, 46))):
        ang += rng.normal(0, 0.28)
        y += int(round(np.sin(ang))); x += int(round(np.cos(ang)))
        put(y, x, 1); put(y + 1, x, min(8, idx[(y + 1) % N, x % N] + 1))
        if rng.random() < 0.06:
            by, bx, ba = y, x, ang + rng.choice([-1, 1]) * 1.1
            for _ in range(int(rng.integers(4, 12))):
                ba += rng.normal(0, 0.5); by += int(round(np.sin(ba))); bx += int(round(np.cos(ba))); put(by, bx, 1)
# sỏi: khối nhỏ, sáng trên trái, tối dưới phải, bóng 1 px dưới
for _ in range(380):
    cy, cx = rng.integers(0, N, 2); r = rng.choice([1, 1, 1, 2, 2, 3])
    rx = r + int(rng.integers(0, 2))
    for dy in range(-r, r + 1):
        for dx in range(-rx, rx + 1):
            if (dx / (rx + .5)) ** 2 + (dy / (r + .5)) ** 2 > 1: continue
            v = 8 if (dx + dy) < -r * 0.6 else 7 if (dx + dy) <= r * 0.4 else 3
            put(cy + dy, cx + dx, v)
    for dx in range(0, rx + 2): put(cy + r + 1, cx + dx, 1)
# hạt tro/đốm lẻ
for _ in range(1400):
    y, x = rng.integers(0, N, 2); put(y, x, int(rng.choice([2, 3, 6, 7])))
img = Image.fromarray(P[idx].clip(0, 255).astype(np.uint8))
img.save(out, optimize=True)
print(out, img.size, len(img.getcolors(4096)), 'màu')
