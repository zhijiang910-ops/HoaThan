"""Tách ảnh 2 khung (chủ game 29/11): khung đỏ mặt quỷ -> bien_quymon.webp, khung xanh đen lư hương -> bien_thangiang.webp.
Chạy: python3 -I cong_cu/claude/sanh_bien2_build.py [ảnh gốc] [thư mục ra]"""
import sys
from PIL import Image, ImageChops
src = sys.argv[1] if len(sys.argv) > 1 else 'nguon/master_amgioi/sanh_bien/khung_do_xanh_goc.png'
out = sys.argv[2] if len(sys.argv) > 2 else 'game/assets/ui/lobby'
im = Image.open(src).convert('RGBA')
def shrink(c, w):
    r, g, b, a = c.split()
    pm = Image.merge('RGBA', (ImageChops.multiply(r, a), ImageChops.multiply(g, a), ImageChops.multiply(b, a), a))
    pm = pm.resize((w, round(c.height * w / c.width)), Image.LANCZOS)
    px = pm.load()
    for y in range(pm.height):
        for x in range(pm.width):
            R, G, B, A = px[x, y]
            px[x, y] = (0, 0, 0, 0) if A < 8 else (min(255, R * 255 // A), min(255, G * 255 // A), min(255, B * 255 // A), A)
    return pm
for name, box in (('bien_quymon', (0, 0, im.width, 450)), ('bien_thangiang', (0, 450, im.width, im.height))):
    c = im.crop(box)
    bb = c.split()[3].point(lambda v: 255 if v > 20 else 0).getbbox()
    c = shrink(c.crop(bb), 720)
    c.save(f'{out}/{name}.webp', quality=90, method=6)
    print(name, bb, c.size, round(c.width / c.height, 3))
