# Làm sạch 3 ảnh hiệu ứng sảnh (khói hương, khói đen, mắt đỏ) chủ game gửi 28/11 rồi xuất webp cho game.
# Viền màu lạ do tách nền (đỏ/vàng ở khói hương, tím hồng ở khói đen) được kéo về màu khói, độ đục giảm.
import numpy as np
from PIL import Image
S='/home/user/HoaThan/nguon/master_amgioi/sanh_fx/';O='/home/user/HoaThan/game/assets/ui/lobby/'
def load(n):return np.array(Image.open(S+n).convert('RGBA')).astype(float)
def save(a,name,h=None,w=None):
    im=Image.fromarray(np.clip(a,0,255).astype('uint8'),'RGBA');bb=im.split()[3].point(lambda v:255 if v>10 else 0).getbbox();im=im.crop(bb)
    if h:w=round(im.width*h/im.height)
    else:h=round(im.height*w/im.width)
    A=np.array(im).astype(float);A[...,:3]*=A[...,3:]/255
    r=np.array(Image.fromarray(A.astype('uint8'),'RGBA').resize((w,h),Image.LANCZOS)).astype(float)
    al=r[...,3:];r[...,:3]=np.where(al>0,r[...,:3]*255/np.maximum(al,1),0)
    Image.fromarray(np.clip(r,0,255).astype('uint8'),'RGBA').save(O+name,quality=88,method=6);print(name,w,h,bb)
def fix(a,bad,col,k):
    rgb=a[...,:3];m=bad(rgb)
    a[...,:3]=np.where(m[...,None],col,rgb);a[...,3]=np.where(m,a[...,3]*k,a[...,3]);print('fixed',m.mean().round(4))
    return a
# khói hương: xám ấm; viền đỏ/vàng bão hòa cao
a=load('khoi_huong_goc.png');r,g,b=a[...,0],a[...,1],a[...,2]
sat=lambda rgb:(rgb.max(-1)-rgb.min(-1))/np.maximum(rgb.max(-1),1)
a=fix(a,lambda rgb:sat(rgb)>0.28,np.array([170,164,168]),0.45)
save(a,'khoi_huong.webp',h=360)
# khói đen tím: viền hồng tím sáng (R và B cao, G thấp) => tím xám tối
a=load('khoi_den_goc.png')
a=fix(a,lambda rgb:(sat(rgb)>0.45)&(rgb.max(-1)>120),np.array([96,84,104]),0.6)
save(a,'khoi_den.webp',w=900)
a=load('mat_do_goc.png');save(a,'mat_do.webp',w=640)
