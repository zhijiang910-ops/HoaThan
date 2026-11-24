import json,re,colorsys
import numpy as np
from PIL import Image,ImageDraw
R='/home/user/HoaThan/game/'
s=open(R+'index.html',encoding='utf-8').read()
d=json.loads(re.search(r'const CHM=(\{.*?\});\n',s,re.S).group(1))
def frame(n):
    if n=='quytuong':return Image.open(R+'assets/quytuong.png').convert('RGBA').crop((0,0,145,149))
    if n=='quysai_am':return Image.open(R+'assets/quysai_am.png').convert('RGBA')
    v=d[n];im=Image.open(R+f'assets/{n}.png').convert('RGBA');x,y=v['anims']['idle']['f'][0];return im.crop((x,y,x+v['w'],y+v['h']))
def rc(im,h=0,sm=1,vm=1,vo=0,tint=None):
    a=np.array(im).astype(float)/255;rgb=a[:,:,:3]
    mx=rgb.max(2);mn=rgb.min(2);df=mx-mn
    # rgb->hsv
    hh=np.zeros_like(mx);m=df>1e-6
    r,g,b=rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
    hh=np.where(m&(mx==r),((g-b)/np.where(m,df,1))%6,hh);hh=np.where(m&(mx==g),(b-r)/np.where(m,df,1)+2,hh);hh=np.where(m&(mx==b),(r-g)/np.where(m,df,1)+4,hh)
    hh=(hh/6+h)%1;ss=np.where(mx>0,df/np.where(mx>0,mx,1),0)*sm;ss=np.clip(ss,0,1);vv=np.clip(mx*vm+vo*(mx>0.05),0,1)
    i=np.floor(hh*6).astype(int)%6;f=hh*6-np.floor(hh*6);p=vv*(1-ss);q=vv*(1-f*ss);t=vv*(1-(1-f)*ss)
    out=np.zeros_like(rgb)
    for k,(rr,gg,bb) in enumerate([(vv,t,p),(q,vv,p),(p,vv,t),(p,q,vv),(t,p,vv),(vv,p,q)]):
        w=i==k;out[:,:,0]=np.where(w,rr,out[:,:,0]);out[:,:,1]=np.where(w,gg,out[:,:,1]);out[:,:,2]=np.where(w,bb,out[:,:,2])
    if tint:out=out*(1-tint[3])+np.array(tint[:3])/255*tint[3]*(0.4+0.6*vv[:,:,None]) 
    a2=np.dstack([np.clip(out,0,1),a[:,:,3]]);return Image.fromarray((a2*255).astype(np.uint8))
items=[('Ngưu Đầu (hình Ngưu Ma Vương)','quytuong',{}),
('Mã Diện (từ hổ, nâu ngựa)','ho',dict(h=-0.03,sm=0.55,vm=0.9)),
('Hắc Vô Thường (từ kiếm khách)','hacphong',dict(sm=0.2,vm=0.55)),
('Bạch Vô Thường (từ nón lá)','daulap',dict(sm=0.1,vm=1.35,vo=0.18)),
('Mạnh Bà (từ cô gái)','bachhoa',dict(h=0.55,sm=0.45,vm=0.8)),
('Phán Quan (từ kiếm khách, đỏ)','hacphong',dict(h=-0.02,sm=1.6,vm=1.05,tint=(150,20,20,0.55))),
('Diêm Vương (từ Ngưu Ma Vương, đỏ đen)','quytuong',dict(h=-0.05,sm=1.5,vm=0.7,tint=(140,10,15,0.5))),
('Tinh Anh: Huyết Sát (Quỷ Sai đỏ)','quysai_am',dict(h=-0.30,sm=1.4,vm=1.0)),
('Tinh Anh: Nghiệt Hỏa (cam lửa)','quysai_am',dict(h=-0.22,sm=1.5,vm=1.15)),
('Tinh Anh: Thiết Lao (xám sắt)','quysai_am',dict(sm=0.25,vm=0.95)),
('Tinh Anh: Vong Xuyên (xanh nước)','quysai_am',dict(h=0.12,sm=1.1,vm=1.0)),
('Tinh Anh: Đế Thính (vàng tím)','quysai_am',dict(h=0.28,sm=0.9,vm=1.1))]
CW,CH_=250,215;cols=4;rows=(len(items)+cols-1)//cols
W=Image.new('RGBA',(CW*cols,CH_*rows),(54,48,52,255));dr=ImageDraw.Draw(W)
for k,(nm,src,kw) in enumerate(items):
    im=frame(src);im=rc(im,**kw) if kw else im
    sc=1.0 if im.width<190 else 1.0
    x=(k%cols)*CW;y=(k//cols)*CH_
    W.alpha_composite(im,(x+(CW-im.width)//2,y+8+(170-im.height)//2 if im.height<170 else y+8))
    dr.text((x+6,y+CH_-30),nm,fill=(240,230,210,255))
W.convert('RGB').save('/tmp/claude-0/-home-user-HoaThan/a832d12c-e51d-5bff-8200-3e97690e9294/scratchpad/boss_recolor.png');print(W.size)
