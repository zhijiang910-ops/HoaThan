# Gắn lá bùa vàng chữ đỏ (tóc + ngực) lên hero_{g}_ms.png theo vị trí mặt của Master. Chạy SAU build_outfit.py và fix_ribbon.py. Không dùng PixelLab.
import json,sys,numpy as np
from PIL import Image
F=[tuple(x) for x in json.load(open('nguon/pixellab/trangphuc/frames.json'))]
SKIP={(1920,128),(2080,128),(2240,128)}  # trúng đòn / ngã: đầu không dựng
O=(40,26,12,255);Y1=(246,210,70,255);Y2=(214,160,36,255);R=(184,40,26,255)
def tag(h):
    # rộng 5 (viền+3+viền); h dòng ruột; chữ đỏ so le
    im=np.zeros((h+2,5,4),np.uint8)
    im[:]=O
    for j in range(h):
        for i in range(3):
            im[j+1,i+1]=Y1 if i<2 else Y2
        if j%2==1 and 0<j<h-1: im[j+1,2]=R;im[j+1,1 if j%4==1 else 3]=R
    im[0,0]=im[0,4]=im[h+1,0]=im[h+1,4]=(0,0,0,0)
    im[h+1,2]=(0,0,0,0)
    return im
def paste(b,t,x,y):
    H,W=b.shape[:2]
    for j in range(t.shape[0]):
        for i in range(t.shape[1]):
            if t[j,i,3]>0 and 0<=y+j<H and 0<=x+i<W:b[y+j,x+i]=t[j,i]
def skin(a):
    r,g,b,al=[a[...,i].astype(int) for i in range(4)]
    return (al>200)&(r>170)&(r<255)&(g>110)&(g<200)&(b>70)&(b<160)&(r-b>45)&(r>g)
for gname in('nam','nu'):
    ns=np.array(Image.open(f'game/assets/hero_{gname}_ns.png').convert('RGBA'));ms=np.array(Image.open(f'game/assets/hero_{gname}_ms.png').convert('RGBA'));n=0
    for x,y in F:
        if (x,y) in SKIP:continue
        a=ns[y:y+128,x:x+160];b=ms[y:y+128,x:x+160]
        ys=np.where(a[...,3]>40)[0]
        if not len(ys):continue
        t=ys.min();m=skin(a);m[:t]=False;m[t+34:]=False
        yy,xx=np.where(m)
        if len(yy)<12:continue
        cx=int(xx.mean());cy=int(yy.mean());bot=int(yy.max());top=int(yy.min())
        # bùa tóc: sau tai/ cạnh gáy, rủ xuống
        paste(b,tag(9),cx-10,cy-4);
        # bùa ngực: trước ngực dưới cổ
        paste(b,tag(10),cx-3,bot+3);n+=1
    Image.fromarray(ms).save(f'game/assets/hero_{gname}_ms.png');print(gname,'khung gắn',n)
