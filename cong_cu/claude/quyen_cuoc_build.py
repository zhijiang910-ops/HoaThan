"""Dựng tài nguyên bộ Quyền Cước (Thiên Cương Môn) từ gói chủ game gửi 28/11.

Chạy: python3 -I cong_cu/claude/quyen_cuoc_build.py <thư mục gói đã giải nén> [thư mục game]
Gói gốc (đã bỏ raw_originals/*.jpg) lưu ở nguon/master_amgioi/quyen_cuoc/.

- Icon 256 -> 160 px WebP (HUD ~41-54 CSS px, iPhone DPR3 ~ 123-160 px).
- VFX: cắt sát vùng có alpha, thu về ~2 lần cỡ hiển thị trong thế giới, WebP có alpha.
- Hạt khói mềm: ghi đè ui/lobby/khoi_hat.webp (cổng Quỷ Môn Quan dùng chung ảnh).
"""
import os, sys
from PIL import Image

src = sys.argv[1]
game = sys.argv[2] if len(sys.argv) > 2 else 'game'
A = os.path.join(src, 'assets') if os.path.isdir(os.path.join(src, 'assets')) else src
ui = os.path.join(game, 'assets/ui/quyen'); vfx = os.path.join(game, 'assets/vfx')
os.makedirs(ui, exist_ok=True)

def shrink(im, w=None, h=None):
    im = im.convert('RGBA')
    W, H = im.size
    k = (w / W) if w else (h / H)
    if k >= 1: return im
    # thu premultiplied để mép trong suốt không viền đen
    pm = im.copy(); r, g, b, a = pm.split()
    from PIL import ImageChops
    r = ImageChops.multiply(r, a); g = ImageChops.multiply(g, a); b = ImageChops.multiply(b, a)
    pm = Image.merge('RGBA', (r, g, b, a)).resize((max(1, round(W * k)), max(1, round(H * k))), Image.LANCZOS)
    r, g, b, a = pm.split()
    px = pm.load(); out = Image.new('RGBA', pm.size)
    op = out.load()
    for y in range(pm.size[1]):
        for x in range(pm.size[0]):
            R, G, B, AA = px[x, y]
            if AA == 0: op[x, y] = (0, 0, 0, 0)
            else: op[x, y] = (min(255, R * 255 // AA), min(255, G * 255 // AA), min(255, B * 255 // AA), AA)
    return out

def crop(im, thr=6):
    a = im.convert('RGBA').split()[3].point(lambda v: 255 if v > thr else 0)
    bb = a.getbbox(); return im.crop(bb) if bb else im

icons = {'icon_attack_phuc_ma_lien_quyen': 'qc_basic', 'icon_dash_bo_hu_luu_phu': 'qc_dash',
         'icon_q_phuoc_hon_cuong_quyen': 'qc_q', 'icon_f_thien_cuong_dap_tinh_cuoc': 'qc_f',
         'icon_e_toai_phach_bat_cuc_chuong': 'qc_e', 'icon_r_quy_mon_tran_nguc_an': 'qc_r'}
for a, b in icons.items():
    shrink(Image.open(f'{A}/icons/{a}.png'), 160).save(f'{ui}/{b}.webp', quality=90, method=6)
for k in 'qfer':
    n = {'q': 'phuoc', 'f': 'chan', 'e': 'pha', 'r': 'diet'}[k]
    shrink(Image.open(f'{A}/icons_seal/seal_{k}_{n}.png'), 160).save(f'{ui}/qc_seal_{k}.webp', quality=90, method=6)

# (tên game, file gói, bề rộng hoặc cao đích)
# 29/11 hotfix: đạn Q và bàn tay R vẽ to hơn nhiều nên giữ độ phân giải cao (hết mờ trên màn 3x); ấn Chu Sa cắt sát lõi (alpha>120)
V = [('qc_fist', 'vfx_q_fist_projectile', dict(w=520)),
     ('qc_mark', 'vfx_passive_chu_sa_mark', dict(h=120)),
     ('qc_burst', 'vfx_e_talisman_burst', dict(w=320)),
     ('qc_palm', 'vfx_r_giant_exorcist_palm', dict(h=533)),  # 29/11 (3): bàn tay Thiên Cương (ấn Kim Cang Tinh Mang), giữ nguyên độ phân giải
     ('qc_tinhluan', 'vfx_f_thien_cuong_tinh_luan', dict(w=512)),  # F: Tinh Luân Bắc Đẩu
     ('qc_crater', 'vfx_r_bagua_crater_decal', dict(w=700)),
     ('qc_puff', 'vfx_soft_ghost_smoke_puff', dict(w=128))]
for n, f, kw in V:
    im = crop(Image.open(f'{A}/vfx/{f}.png').convert('RGBA'), 120 if n == 'qc_mark' else 6)
    im = shrink(im, **kw)
    im.save(f'{vfx}/{n}.webp', quality=88, method=6)
    print(n, im.size, os.path.getsize(f'{vfx}/{n}.webp'))
# cổng Quỷ Môn Quan ở sảnh: hạt khói mềm dùng chung ảnh mới (giữ tên cũ)
shrink(Image.open(f'{A}/vfx/vfx_soft_ghost_smoke_puff.png'), 128).save(f'{game}/assets/ui/lobby/khoi_hat.webp', quality=88, method=6)
