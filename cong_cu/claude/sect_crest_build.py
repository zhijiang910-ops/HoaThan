"""6 huy hiệu môn phái (chủ game 29/11, nguon/master_amgioi/sect_crests/crest_*.png 256x256 RGBA).
Cắt sát vùng có alpha, đặt giữa ô vuông, thu premultiplied LANCZOS về 128 px (đủ cho màn 3x ở 34 CSS px).
Ảnh nguồn không phải lưới pixel chuẩn nên KHÔNG thu nearest (răng cưa).
Chạy: python3 -I cong_cu/claude/sect_crest_build.py"""
from PIL import Image, ImageChops
S = 'nguon/master_amgioi/sect_crests/'; O = 'game/assets/ui/phai/'
M = {'thiencuong': 'crest_1_thien_cuong_mon', 'maoson': 'crest_2_mao_son_phai', 'phucma': 'crest_3_pha_sat_mon',
     'tramyeu': 'crest_4_doan_hon_coc', 'huyenlinh': 'crest_5_cuu_u_tong', 'truyhon': 'crest_6_truy_nguyet_cac'}
for k, f in M.items():
    im = Image.open(S + f + '.png').convert('RGBA')
    im = im.crop(im.split()[3].point(lambda v: 255 if v > 8 else 0).getbbox())
    w, h = im.size; s = max(w, h); sq = Image.new('RGBA', (s, s)); sq.paste(im, ((s - w) // 2, (s - h) // 2))
    r, g, b, a = sq.split()
    pm = Image.merge('RGBA', (ImageChops.multiply(r, a), ImageChops.multiply(g, a), ImageChops.multiply(b, a), a)).resize((128, 128), Image.LANCZOS)
    px = pm.load()
    for y in range(128):
        for x in range(128):
            R, G, B, A = px[x, y]
            px[x, y] = (0, 0, 0, 0) if A < 4 else (min(255, R * 255 // A), min(255, G * 255 // A), min(255, B * 255 // A), A)
    pm.save(O + f'crest_{k}.png'); print(k, (w, h))
