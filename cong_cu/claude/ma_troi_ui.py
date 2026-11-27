# Tách 4 ngọn ma trơi từ ảnh chủ game gửi, thu về pixel thật, tạo bản xanh ngọc pha lam cho popup.
# Chạy: python3 cong_cu/claude/ma_troi_ui.py  -> game/assets/ui/matroi/mt_{ngoc,tim,do}_{H}.png
from PIL import Image
import numpy as np, colorsys, os
SRC='nguon/master_amgioi/ma_troi_4_mau_goc.png'; OUT='game/assets/ui/matroi'; os.makedirs(OUT,exist_ok=True)
A=np.array(Image.open(SRC).convert('RGBA'))
SEG={'tim':(110,426),'do':(590,1060),'lam':(1187,1536),'luc':(1769,2067)}
def cut(k):
    x0,x1=SEG[k]; B=A[:,x0:x1].copy(); B[B[...,3]<24]=0
    ys,xs=np.where(B[...,3]>0); return B[ys.min():ys.max()+1,xs.min():xs.max()+1]
def hue(B,dh,sat=1.0):
    C=B.copy().astype(np.float32)/255.; out=C.copy()
    import colorsys
    rgb=C[...,:3]; mx=rgb.max(-1); mn=rgb.min(-1)
    # chuyển HSV vector hóa
    h=np.zeros_like(mx); d=mx-mn+1e-6
    r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
    h=np.where(mx==r,((g-b)/d)%6,np.where(mx==g,(b-r)/d+2,(r-g)/d+4))/6
    s=np.where(mx>0,d/np.maximum(mx,1e-6),0)*sat; v=mx; h=(h+dh/360)%1
    i=np.floor(h*6); f=h*6-i; p=v*(1-s); q=v*(1-f*s); t=v*(1-(1-f)*s); i=i%6
    R=np.choose(i.astype(int),[v,q,p,p,t,v]);G=np.choose(i.astype(int),[t,v,v,q,p,p]);Bb=np.choose(i.astype(int),[p,p,t,v,v,q])
    out[...,0],out[...,1],out[...,2]=R,G,Bb; return (out*255).clip(0,255).astype('uint8')
def shrink(B,H):
    im=Image.fromarray(B,'RGBA'); W=round(H*im.width/im.height)
    P=np.asarray(im).astype(np.float32); al=P[...,3:4]/255.
    pm=Image.fromarray(np.concatenate([P[...,:3]*al,P[...,3:4]],-1).astype('uint8'),'RGBA').resize((W,H),Image.BOX)
    Q=np.asarray(pm).astype(np.float32); al=Q[...,3:4]/255.
    rgb=np.where(al>0,Q[...,:3]/np.maximum(al,1e-3),0)
    a=Q[...,3]
    # alpha pixel: 4 bậc (quầng mờ thành bậc như pixel art, bỏ lốm đốm viền)
    aq=np.select([a<40,a<110,a<190],[0,110,180],255)
    out=np.concatenate([rgb,aq[...,None]],-1).clip(0,255).astype('uint8')
    o=Image.fromarray(out,'RGBA'); q=o.convert('RGB').quantize(24,method=Image.MEDIANCUT,dither=Image.NONE).convert('RGB')
    return Image.merge('RGBA',(*q.split(),o.split()[3]))
lam=cut('lam')
VAR={'ngoc':hue(lam,-28,1.05),'tim':cut('tim'),'do':cut('do')}
for k,B in VAR.items():
    for H in (40,48,64,80,96):
        shrink(B,H).save(f'{OUT}/mt_{k}_{H}.png')
print('ok')
