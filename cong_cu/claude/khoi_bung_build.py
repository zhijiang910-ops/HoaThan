# Khói bùng từ mặt đất cho cổng Quỷ Môn Quan (28/11): video phông xanh chủ game gửi -> tách nền, xóa logo TikTok,
# nhuộm khói đen tím (sáng ở mép trên như khói_den cũ), đóng tấm 8x6 = 48 khung (15 khung/s của video gốc, đoạn 0,27–3,4 s).
# python3 cong_cu/claude/khoi_bung_build.py <thư_mục_khung_png_15fps>
import sys,glob,numpy as np
from PIL import Image
D=sys.argv[1];fs=sorted(glob.glob(D+'/*.png'))[4:52]
X0,X1,Y0,Y1=0,576,452,648;W,H=288,96;C,R=8,6
sheet=Image.new('RGBA',(W*C,H*R))
dark=np.array([34,28,42.]);mid=np.array([92,82,106.]);light=np.array([196,186,210.])
f0=np.array(Image.open(sorted(glob.glob(D+'/*.png'))[0]).convert('RGB')).astype(int)[Y0:Y1,X0:X1]
lm=(f0[...,1]-np.maximum(f0[...,0],f0[...,2]))<60
lm2=lm.copy()
for dy in(-2,-1,0,1,2):
    for dx in(-2,-1,0,1,2):lm2|=np.roll(np.roll(lm,dy,0),dx,1)
lm=lm2;print('logo px',lm.sum())
def inpaint(a,m,it=60):
    a=a.copy();a[m]=0;w=(~m).astype(float)
    for _ in range(it):
        s_=sum(np.roll(np.roll(a*w[...,None],dy,0),dx,1) for dy,dx in((1,0),(-1,0),(0,1),(0,-1)))
        n=sum(np.roll(np.roll(w,dy,0),dx,1) for dy,dx in((1,0),(-1,0),(0,1),(0,-1)))
        upd=m&(n>0);a[upd]=s_[upd]/n[upd][:,None];w=np.where(upd,1.0,w)
    return a
for i,f in enumerate(fs):
    a=inpaint(np.array(Image.open(f).convert('RGB')).astype(float)[Y0:Y1,X0:X1],lm)
    r,g,b=a[...,0],a[...,1],a[...,2];mx=np.maximum(r,b)
    d=g-mx                                   # nền ~75, khói trắng ~0..20
    al=np.clip((68-d)/52,0,1)
    yy,xx=np.mgrid[Y0:Y1,X0:X1]
    al*=np.clip((575-xx)/40,0,1)*np.clip(xx/30,0,1)
    g2=np.minimum(g,mx+6);L=(0.3*r+0.59*g2+0.11*b)
    t=np.clip((L-90)/150,0,1)[...,None]
    col=np.where(t<.5,dark+(mid-dark)*(t/.5),mid+(light-mid)*((t-.5)/.5))
    out=np.dstack([col,(al*255*0.96)[...,None]]).astype('uint8')
    im=Image.fromarray(out,'RGBA')
    A=np.array(im).astype(float);A[...,:3]*=A[...,3:]/255
    s=np.array(Image.fromarray(A.astype('uint8'),'RGBA').resize((W,H),Image.LANCZOS)).astype(float)
    sa=s[...,3:];s[...,:3]=np.where(sa>0,s[...,:3]*255/np.maximum(sa,1),0)
    sheet.paste(Image.fromarray(np.clip(s,0,255).astype('uint8'),'RGBA'),((i%C)*W,(i//C)*H))
sheet.save('/home/user/HoaThan/game/assets/ui/lobby/khoi_bung.webp',quality=86,method=6);print('frames',len(fs),sheet.size)
