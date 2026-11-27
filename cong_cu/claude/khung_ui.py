# Thu 3 ảnh khung (ô đá, khung gỗ, nút đỏ) về cỡ pixel thật trong game: nét viền ~1 px như sprite nhân vật.
# Chạy: python3 cong_cu/claude/khung_ui.py  (đọc nguon/master_amgioi/khung_ui/*_goc.png, ghi game/assets/ui/khung/)
from PIL import Image, ImageFilter
import os, sys
SRC='nguon/master_amgioi/khung_ui'; OUT='game/assets/ui/khung'; os.makedirs(OUT,exist_ok=True)
def crop(im):
    a=im.split()[3].point(lambda v:255 if v>40 else 0); return im.crop(a.getbbox())
def shrink(im,w,h,colors=40):
    im=im.convert('RGBA')
    # premultiplied BOX để mép không viền đen
    r,g,b,a=im.split()
    import numpy as np
    A=np.asarray(im).astype(np.float32); al=A[...,3:4]/255.
    P=np.concatenate([A[...,:3]*al,A[...,3:4]],-1)
    Pi=Image.fromarray(P.clip(0,255).astype('uint8'),'RGBA').resize((w,h),Image.BOX)
    Q=np.asarray(Pi).astype(np.float32); al=Q[...,3:4]/255.
    rgb=np.where(al>0,Q[...,:3]/np.maximum(al,1e-3),0)
    out=np.concatenate([rgb,np.where(Q[...,3:4]>110,255,0)],-1).clip(0,255).astype('uint8')
    o=Image.fromarray(out,'RGBA')
    # tăng tương phản nhẹ để chi tiết không chìm khi nhỏ
    from PIL import ImageEnhance
    rgbI=ImageEnhance.Contrast(o.convert('RGB')).enhance(1.18)
    rgbI=ImageEnhance.Sharpness(rgbI).enhance(1.6)
    o=Image.merge('RGBA',(*rgbI.split(),o.split()[3]))
    q=o.convert('RGB').quantize(colors,method=Image.MEDIANCUT,dither=Image.NONE).convert('RGB')
    return Image.merge('RGBA',(*q.split(),o.split()[3]))
def outline(im):
    # viền tối 1 px quanh khối như sprite nhân vật
    import numpy as np
    A=np.array(im); al=A[...,3]>0
    sh=np.zeros_like(al)
    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
        sh|=np.roll(np.roll(al,dy,0),dx,1)
    edge=sh&~al
    A[edge]=(20,14,14,255); return Image.fromarray(A,'RGBA')

# Mỗi cỡ hiển thị có một ảnh riêng thu thẳng từ ảnh gốc (không phóng ảnh nhỏ lên): game chọn ảnh vừa khoang và vẽ 1:1 CSS px.
# Ô đá và khung gỗ đã bỏ (chủ game 27/11), chỉ còn nút đỏ.
nd=crop(Image.open(f'{SRC}/nut_do_goc.png'))
for n in (34,40,48):
    shrink(nd,round(n*nd.width/nd.height),n,48).save(f"{OUT}/nut_do_raw_{n}.png")
print('ok')
# Nút đỏ 9-slice: giữ nguyên hai đầu sắt (mỗi bên 25% bề ngang, gồm đai sắt + một đoạn sơn nứt),
# giữa là MỘT cột sơn đỏ sạch (trung vị từng hàng của vùng giữa) để CSS giãn ngang mà không ra sọc.
import numpy as np
for n in (34,40,48):
    A=np.array(Image.open(f'{OUT}/nut_do_raw_{n}.png')); W=A.shape[1]; L=round(W*.25)
    mid=A[:,round(W*.35):round(W*.65)]
    col=np.median(mid,axis=1).round().astype('uint8')[:,None,:]
    col[...,3]=np.where(mid[...,3].mean(1)>127,255,0)[:,None]
    B=np.concatenate([A[:,:L],col,A[:,W-L:]],1)
    Image.fromarray(B,'RGBA').save(f'{OUT}/nut_do_{n}.png'); print('nut',n,B.shape[1],'cap',L)
for n in (34,40,48):
    try: os.remove(f'{OUT}/nut_do_raw_{n}.png')
    except OSError: pass
