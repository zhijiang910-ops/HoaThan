"""Dựng tài nguyên Mao Sơn tầm xa (gói chủ game 29/11) vào game.
Chạy: python3 -I cong_cu/claude/mao_son_build.py <thư mục gói có assets/> game
"""
import sys,os
from PIL import Image
src,game=sys.argv[1],sys.argv[2]
I=os.path.join(src,'assets','icons_mao_son');V=os.path.join(src,'assets','vfx_mao_son')
ou=os.path.join(game,'assets','ui','maoson');ov=os.path.join(game,'assets','vfx');os.makedirs(ou,exist_ok=True)
for k in('dash','q','f','c','x_ult'):
    im=Image.open(os.path.join(I,'icon_ms_%s.png'%k)).convert('RGBA').resize((160,160),Image.LANCZOS)
    im.save(os.path.join(ou,'ms_%s.webp'%('x' if k=='x_ult' else k)),quality=90,method=6)
def crop(n):
    im=Image.open(os.path.join(V,n)).convert('RGBA');return im.crop(im.getbbox())
m={'vfx_ms_flying_sword.png':'ms_sword','vfx_ms_talisman_proj.png':'ms_tal','vfx_ms_talisman_burst.png':'ms_burst',
   'vfx_ms_bagua_seal.png':'ms_bagua','vfx_ms_colossal_sword.png':'ms_colossal','vfx_ms_soft_mist_puff.png':'ms_mist'}
for a,b in m.items():crop(a).save(os.path.join(ov,b+'.webp'),quality=92,method=6)
# ấn: chỉ phần vuông có nội dung (106x160 gốc, phần dưới trống)
mk=crop('vfx_ms_passive_mark.png');mk.save(os.path.join(ov,'ms_mark.webp'),quality=92,method=6)
# hố đá: giữ nguyên khung (đo lòng hố theo toạ độ ảnh gốc 640x348: tâm (309,175.5), rộng 234, cao 155)
cr=Image.open(os.path.join(V,'vfx_ms_crater_ring.png')).convert('RGBA');cr.save(os.path.join(ov,'ms_crater.webp'),quality=92,method=6)
# vành đá đè mép ấn: khoét lòng hố (điểm mờ tối alpha<=215 trong elip lòng hố)
rim=cr.copy();px=rim.load();W,H=rim.size
for y in range(H):
    for x in range(W):
        p=px[x,y]
        if ((x-309)/122)**2+((y-175.5)/82)**2<=1 and p[3]<=215:px[x,y]=(0,0,0,0)
rim.save(os.path.join(ov,'ms_crater_rim.webp'),quality=92,method=6)
print('ok')
