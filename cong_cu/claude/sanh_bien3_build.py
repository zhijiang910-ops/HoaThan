"""3 biển tương tác sảnh (chủ game 29/11): khung chuông nứt -> Xuất Trận, khung lư hương -> Thần Giáng Đàn, khung mặt quỷ -> Quỷ Môn Quan.
Cắt lề alpha, chỉnh độ sáng viền gỗ về cùng mức (~100), thu về cao 120 px, in thông số 9-slice cho CSS.
Thân biển ở giữa (giữa 2 lát L/R) được giãn ngang theo độ dài nhãn (border-image), icon trái và trang trí phải giữ nguyên.
Chạy: python3 -I cong_cu/claude/sanh_bien3_build.py"""
import json
import numpy as np
from PIL import Image
S = 'nguon/master_amgioi/sanh_bien/'
O = 'game/assets/ui/lobby/'
s2 = Image.open(S + 'khung_do_xanh_goc.png').convert('RGBA')
# (tên, ảnh, hàng thân trên/dưới sau khi cắt, đầu/cuối vùng thân trơn, độ sáng gỗ đo được)
F = [('xuattran', Image.open(S + 'khung_chuong_goc.png').convert('RGBA'), (20, 386), (366, 1936), 106),
     ('thangiang', s2.crop((0, 450, s2.width, s2.height)), (30, 306), (350, 1395), 100),
     ('quymon', s2.crop((0, 0, s2.width, 450)), (41, 316), (366, 1539), 90)]
HT = 120; out = {}
for n, im, (p0, p1), (x0, x1), wl in F:
    A = np.array(im).astype(float); a = A[..., 3]
    ys = np.where((a > 20).sum(1) > 3)[0]; xs = np.where((a > 20).sum(0) > 3)[0]
    A = A[ys.min():ys.max() + 1, xs.min():xs.max() + 1]; H, W = A.shape[:2]
    A[..., :3] = np.clip(A[..., :3] * (100 / wl), 0, 255)
    k = HT / H; w = round(W * k)
    img = Image.fromarray(A.astype(np.uint8), 'RGBA').resize((w, HT), Image.LANCZOS)
    img.save(O + f'bien3_{n}.webp', quality=90, method=6)
    L = round((x0 + 16) * k); R = round((W - (x1 - 16)) * k)
    out[n] = dict(w=w, h=HT, L=L, R=R, frac=round((p1 - p0) / H, 3), pt=round(2 * ((p0 + p1) / 2 - H / 2) / H, 3))
print(json.dumps(out))
