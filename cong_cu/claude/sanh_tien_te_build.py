"""Tách 3 icon tiền tệ từ ảnh ráp thử sảnh của chủ game (29/11): xu đồng, lửa Linh Hồn, rồng ngọc.
Nền là ô nâu tối: loang từ mép vùng cắt qua các điểm tối (max kênh < 46) -> trong suốt; mép mềm theo độ sáng.
Ảnh nguồn nhỏ (~40 px/icon) nên giữ nguyên cỡ, KHÔNG phóng to.
Chạy: python3 -I cong_cu/claude/sanh_tien_te_build.py [ảnh ráp] [thư mục ra]"""
import sys
import numpy as np
from collections import deque
from PIL import Image
src = sys.argv[1] if len(sys.argv) > 1 else 'nguon/master_amgioi/sanh_bien/anh_rap_thu_sanh.png'
out = sys.argv[2] if len(sys.argv) > 2 else 'game/assets/ui/lobby'
A = np.array(Image.open(src).convert('RGB')).astype(int)
BOX = {'dongte2': (1336, 44, 1382, 85), 'linhhon2': (1442, 44, 1492, 85), 'ngoctt2': (1550, 44, 1604, 85)}
for n, (x0, y0, x1, y1) in BOX.items():
    c = A[y0:y1, x0:x1]; L = c.max(-1); H, W = L.shape
    bg = np.zeros((H, W), bool); q = deque()
    for y in range(H):
        for x in (0, W - 1): q.append((y, x))
    for x in range(W):
        for y in (0, H - 1): q.append((y, x))
    while q:
        y, x = q.popleft()
        if bg[y, x] or L[y, x] >= 46: continue
        bg[y, x] = True
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yy, xx = y + dy, x + dx
            if 0 <= yy < H and 0 <= xx < W and not bg[yy, xx]: q.append((yy, xx))
    a = np.where(bg, 0, 255).astype(np.uint8)
    # mép: điểm không nền kề nền và còn tối thì mờ một nửa
    edge = (~bg) & (np.roll(bg, 1, 0) | np.roll(bg, -1, 0) | np.roll(bg, 1, 1) | np.roll(bg, -1, 1))
    a[edge] = np.clip((L[edge] - 20) * 3, 90, 255)
    rgba = np.dstack([c.astype(np.uint8), a])
    ys, xs = np.where(a > 0); rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    h, w = rgba.shape[:2]; s = max(h, w); sq = np.zeros((s, s, 4), np.uint8)
    sq[(s - h) // 2:(s - h) // 2 + h, (s - w) // 2:(s - w) // 2 + w] = rgba
    Image.fromarray(sq, 'RGBA').save(f'{out}/tt_{n}.png')
    print(n, (w, h), s)
# Khung 3 ô tiền tệ (chủ game 29/11, nguon/master_amgioi/sanh_bien/khung_tien_te_goc.png): trên xuống = xu đồng (viền cam), Linh Hồn (xanh ngọc), rồng ngọc (xanh lục).
# Mỗi khung 1012x295 (cắt lề alpha), hốc tròn tâm (171,149) đường kính ~226. Thu về rộng 360.
F = Image.open('nguon/master_amgioi/sanh_bien/khung_tien_te_goc.png').convert('RGBA')
for n, y0 in (('dong', 98), ('hon', 501), ('nap', 905)):
    c = F.crop((102, y0, 1114, y0 + 295))
    c.resize((360, round(295 * 360 / 1012)), Image.LANCZOS).save(f'{out}/tt_khung_{n}.webp', quality=90, method=6)
print('khung xong')
