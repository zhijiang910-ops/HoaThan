# Dựng vật + nền cho 7 map Âm Giới (không PixelLab): bỏ nền 5 vật đặc, cắt khung, chép vào game/assets/map, in dòng MM để dán vào index.html
import os,json,numpy as np
from PIL import Image,ImageDraw
import colorsys
SRC='nguon/pixellab/maps/c/';DST='game/assets/map/'
# tên -> (tên trong game, kiểu va chạm, cờ)
# col: [x1,y1,x2,y2]/(w,h) theo tỉ lệ; None = không va chạm
P={'quanmon':('Dp_quanmon',None,0),'bienngan_hoa':('Dp_hoa1',None,0),'bienngan_hoa2':('Dp_hoa2',None,0),'vonghuong':('Dp_vonghuong',(.33,.24),0),
'nghiepkinh':('Dp_guong',(.22,.06),0),'samla':('Dp_samla',(.33,.17),0),'cotden':('Dp_cotden',(.16,.06),0),'vacdong':('Dp_vac',(.34,.2),0),
'loncong':('Dp_loncong',None,0),'tuongdo':('Dp_tuongdo',(.38,.22),0),'naiha':('Dp_naiha',None,1),'manhba':('Dp_manhba',(.36,.24),0),
'ngai':('Dp_ngai',(.36,.2),0),'cotdo':('Dp_cotdo',(.16,.05),0),'banphan':('Dp_banphan',(.4,.22),0),'luanhoi':('Dp_luanhoi',(.3,.12),0),'daitron':('Dp_daitron',None,1)}
SOLID=['daitron','naiha','quanmon','samla','vonghuong']
MM={}
for k,(n,col,flat) in P.items():
    im=Image.open(SRC+k+'.png').convert('RGBA')
    if k in SOLID:
        for pt in[(0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1),(im.width//2,0),(0,im.height//2),(im.width-1,im.height//2)]:
            if im.getpixel(pt)[3]>0:ImageDraw.floodfill(im,pt,(0,0,0,0),thresh=34)
    if k=='quanmon':
        for pt in[(128,150),(128,175),(110,140),(146,140)]:
            if im.getpixel(pt)[3]>0:ImageDraw.floodfill(im,pt,(0,0,0,0),thresh=30)
    im=im.crop(im.getbbox());im.save(DST+n+'.png')
    w,h=im.size;e={'src':'assets/map/'+n+'.png','w':w,'h':h,'ax':w//2,'ay':h-2}
    e['col']=[-round(w*col[0]),-round(h*col[1]),round(w*col[0]),-2] if col else None
    if flat:e['flat']=1
    MM[n]=e
open('/tmp/mm_dp.json','w').write(json.dumps(MM,ensure_ascii=False))
# nền theo map: nhuộm từ nền có sẵn
def tint(src,dst,hue,sat,val):
    im=Image.open(DST+src).convert('RGB');a=np.array(im).astype(float)/255;out=np.zeros_like(a)
    r,g,b=a[...,0],a[...,1],a[...,2]
    mx=a.max(2);mn=a.min(2);v=mx;s=np.where(mx>0,(mx-mn)/np.maximum(mx,1e-6),0)
    h=np.full_like(v,hue);s=np.clip(s*sat+0.0,0,1);v=np.clip(v*val,0,1)
    import colorsys
    # vectorized hsv->rgb
    i=np.floor(h*6).astype(int)%6;f=h*6-np.floor(h*6);p=v*(1-s);q=v*(1-f*s);t=v*(1-(1-f)*s)
    R=np.choose(i,[v,q,p,p,t,v]);G=np.choose(i,[t,v,v,q,p,p]);B=np.choose(i,[p,p,t,v,v,q])
    Image.fromarray((np.dstack([R,G,B])*255).astype(np.uint8)).save(DST+dst,quality=90)
tint('g_mieu.jpg','g_biangan.jpg',0.93,0.55,0.8)      # Bỉ Ngạn: tím đỏ nhạt
tint('g_pave.jpg','g_nghiep.jpg',0.62,0.5,0.7)        # Nghiệt Kính: xanh lạnh
tint('g_dirt.jpg','g_vongxuyen.jpg',0.52,0.6,0.7)      # Vong Xuyên: xanh nước
print(len(MM),'vật')
