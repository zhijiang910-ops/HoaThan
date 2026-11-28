"""Quỷ Môn Quan v2 (28/11): khói tím đen ánh đỏ từ atlas gốc + tấm khói phủ màn.
Chạy: python3 cong_cu/claude/cong_fx_build.py"""
import numpy as np
from PIL import Image
src='nguon/master_amgioi/sanh_fx/quy-mon-quan-smoke_goc.png'
out='game/assets/ui/lobby/'
a=np.array(Image.open(src).convert('RGBA')).astype(float)
H,W=a.shape[:2];cw,ch=256,112
L=a[...,:3].mean(-1);t=np.clip((L-22)/50,0,1)          # vân sáng tối trong khói
al=a[...,3]/255
yy,xx=np.mgrid[0:H,0:W];cx=xx%cw;cy=yy%ch
d=np.sqrt(((cx-128)/70)**2+((cy-96)/34)**2);red=np.exp(-d*d)   # gần chân cổng (128,91) được ánh đỏ hắt lên
rim=np.clip(1-al/0.55,0,1)*(al>0.02)                    # mép mỏng = xám lạnh
body=np.array([30,16,38.]);hi=np.array([92,64,110.]);rimc=np.array([128,120,150.]);redc=np.array([176,40,34.])
col=body[None,None]*(1-t[...,None])+hi*t[...,None]
col=col*(1-rim[...,None]*.7)+rimc*rim[...,None]*.7
col=col*(1-red[...,None]*.5)+redc*red[...,None]*.5
A=np.clip(al*1.6,0,1)**.85
o=np.dstack([np.clip(col,0,255),A*255]).astype(np.uint8)
# 28/11 chủ game: đáy ô bị cắt phẳng -> làm mờ 26 px cuối mỗi ô (và 14 px hai bên), đệm thêm 48 px trong suốt dưới mỗi ô (ô mới 256x160, neo (128,91) giữ nguyên)
PAD=48;F=26;FS=14
def feather(cell):
    h,w=cell.shape[:2];m=np.ones((h,w))
    r=np.arange(h);m*=np.clip((h-1-r)/F,0,1)[:,None]**1.6
    c=np.arange(w);m*=np.clip(np.minimum(c,w-1-c)/FS,0,1)[None,:]
    cell=cell.copy();cell[...,3]=cell[...,3]*m;return cell
O=np.zeros((5*(ch+PAD),6*cw,4),np.uint8)
for k in range(30):
    cx0,cy0=(k%6)*cw,(k//6)*ch
    cell=feather(o[cy0:cy0+ch,cx0:cx0+cw].astype(float)).astype(np.uint8)
    O[(k//6)*(ch+PAD):(k//6)*(ch+PAD)+ch,cx0:cx0+cw]=cell
Image.fromarray(O,'RGBA').save(out+'khoi_cong.webp',quality=86,method=6)
# hạt khói mềm (soft puff) 128px: tím xám, mép mờ, dưới ửng đỏ
n=128;yy,xx=np.mgrid[0:n,0:n];r=np.sqrt((xx-n/2)**2+(yy-n/2)**2)/(n/2)
# tấm khói phủ màn: đám mây mềm từ nhiễu fbm (tím đen), lặp ghép để phình từ cổng ra
rng=np.random.default_rng(7);N=384
def fbm(n):
    s=np.zeros((n,n))
    for k,amp in [(4,1),(8,.5),(16,.25),(32,.12)]:
        g=rng.random((k+1,k+1));img=Image.fromarray((g*255).astype(np.uint8)).resize((n,n),Image.BICUBIC)
        s+=np.array(img)/255*amp
    return s/1.87
f=fbm(N);yy,xx=np.mgrid[0:N,0:N];r=np.sqrt((xx-N/2)**2+(yy-N/2)**2)/(N/2)
m=np.clip((1-r)*1.6,0,1)**1.2
A=np.clip((f-.25)*2.2,0,1)*m
c=np.dstack([7+f*20,4+f*10,11+f*24])
o=np.dstack([np.clip(c,0,255),A*255]).astype(np.uint8)
Image.fromarray(o,'RGBA').save(out+'khoi_man.webp',quality=82,method=6)
n=128;yy,xx=np.mgrid[0:n,0:n];r=np.sqrt((xx-n/2)**2+(yy-n/2)**2)/(n/2)
f2=fbm(128);A=np.clip(1-r,0,1)**1.5*np.clip(.55+f2*.7,0,1)
lowr=np.clip((yy/n-.35)/.65,0,1)
col=np.dstack([78+f2*60+lowr*70,58+f2*40,96+f2*50-lowr*20])
Image.fromarray(np.dstack([np.clip(col,0,255),np.clip(A*235,0,255)]).astype(np.uint8),'RGBA').save(out+'khoi_hat.webp',quality=86,method=6)
print('ok')
