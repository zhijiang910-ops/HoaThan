# Ve lai vac cua Manh Ba to hon (tu lam bang code theo lenh chu game 24/11, khong PixelLab)
from PIL import Image,ImageDraw
import numpy as np,math,random
src='nguon/pixellab/amgioi/sy3/manhba_s7_0.png'
im=Image.open(src).convert('RGBA');im=im.crop(im.getbbox());a=np.array(im)
a[98:,118:,3]=0                      # xoa vac nho + khoi cu
bb=Image.fromarray(a);bb=bb.crop(bb.getbbox())
W0,H0=bb.size
CW,CH=54,46                            # kich co vac
OUTL=(14,14,18,255);B1=(36,37,44,255);B2=(52,54,63,255);B3=(78,80,92,255);RIM=(96,98,110,255)
CW+=6;cv=Image.new("RGBA",(CW,CH+34),(0,0,0,0));d=ImageDraw.Draw(cv)
top=34;bh=CH-8
cx=CW/2
# than vac: hinh bau
for y in range(bh):
    t=y/(bh-1);w=(CW-6)/2*(0.78+0.22*math.sin(min(1,t*1.15)*math.pi/2*1.0))
    if t>0.82:w*=0.9-(t-0.82)*1.4
    x0=int(round(cx-w));x1=int(round(cx+w))
    for x in range(x0,x1+1):
        u=(x-x0)/max(1,(x1-x0))
        c=B2
        if u<0.18:c=B3
        elif u>0.72:c=B1
        if x in(x0,x1) or y==bh-1:c=OUTL
        cv.putpixel((x,top+y),c)
# vanh
for x in range(2,CW-2):
    for y in(top-2,top-1,top):
        c=RIM if y==top-2 else B3 if y==top-1 else B2
        cv.putpixel((x,y),c)
for x in range(2,CW-2):
    cv.putpixel((x,top-3),OUTL)
for y in(top-2,top-1,top):cv.putpixel((1,y),OUTL);cv.putpixel((CW-2,y),OUTL)
# mieng vac toi, nuoc xanh
for x in range(6,CW-6):
    cv.putpixel((x,top-2),(70,150,70,255) if (x//3)%2==0 else (108,190,92,255))
# chan
for lx in(10,CW-13):
    for y in range(bh,bh+6):
        for x in range(lx,lx+4):cv.putpixel((x,top+y),OUTL if x in(lx,lx+3) or y==bh+5 else B1)
# dau lau
sx,sy=int(cx)-9,top+14
SK=["..XXXXXXXXXXXX..",".XWWWWWWWWWWWWX.","XWWWWWWWWWWWWWWX","XWWWWWWWWWWWWWWX","XWWKKWWWWWWKKWWX","XWWKKWWWWWWKKWWX","XWWWWWWKKWWWWWWX",".XWWWWWKKWWWWWX.","..XXWWWWWWWWXX..","....XWWWWWWX....","....XWKWKWKWX...","....XXXXXXXX...."]
pal={'X':OUTL,'W':(222,222,208,255),'K':(20,20,24,255)}
for j,row in enumerate(SK):
    for i,ch in enumerate(row):
        if ch in pal:cv.putpixel((sx-1+i,sy+j),pal[ch])
# khoi xanh
random.seed(4)
for k in range(5):
    x0=cx-14+k*7
    for y in range(top-4,2,-1):
        xx=int(x0+4*math.sin(y/4.0+k*1.7)*(1+(top-y)/40))
        if (y+k)%3==0:continue
        al=int(255*(1-(top-y)/(top+4)))
        for dx in(0,1):
            if 0<=xx+dx<CW:cv.putpixel((xx+dx,y),(168,205,160,al) if (y%2) else (126,172,120,al))
cv=cv.crop(cv.getbbox())
GAP=-26
Wt=W0+cv.width+GAP;Ht=max(H0,cv.height)
out=Image.new('RGBA',(Wt,Ht),(0,0,0,0))
out.alpha_composite(cv,(W0+GAP,Ht-cv.height))
out.alpha_composite(bb,(0,Ht-H0))
out=out.crop(out.getbbox());out.save('game/assets/manhba_am.png');print(out.size)
