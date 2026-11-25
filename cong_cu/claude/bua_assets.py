#!/usr/bin/env python3
"""Hình bùa chú cho bộ Kiếm Mao Sơn (25/11, chủ game duyệt: tự vẽ pixel bằng code, 0 lượt PixelLab):
 bagua_vang.png (bát quái vàng dưới đất), bua_vang.png (lá bùa vàng chữ đỏ), set_bolt_vang.png (sấm vàng, đổi màu set_bolt.png).
Chạy: python3 cong_cu/claude/bua_assets.py"""
import math,random
from PIL import Image,ImageDraw,ImageFilter
import numpy as np
OUT='game/assets/vfx/'
GOLD=(236,196,92,255);GOLD2=(168,128,44,255);RED=(190,50,42,255);PALE=(255,244,200,255)
# ---- bát quái ----
S=220;C=S//2
img=Image.new('RGBA',(S,S),(0,0,0,0));d=ImageDraw.Draw(img)
def ring(r,w,col):
    d.ellipse((C-r,C-r,C+r,C+r),outline=col,width=w)
# nền mờ
bg=Image.new('RGBA',(S,S),(0,0,0,0));bd=ImageDraw.Draw(bg)
bd.ellipse((C-104,C-104,C+104,C+104),fill=(120,70,10,60));bd.ellipse((C-56,C-56,C+56,C+56),fill=(190,50,42,46))
img=Image.alpha_composite(bg,img);d=ImageDraw.Draw(img)
ring(106,2,GOLD);ring(101,1,GOLD2);ring(62,2,GOLD);ring(57,1,RED);ring(30,1,GOLD2)
tri=[0b111,0b011,0b101,0b001,0b110,0b010,0b100,0b000]  # Càn Đoài Ly Chấn Tốn Khảm Cấn Khôn
for i,bits in enumerate(tri):
    ang=math.radians(i*45-90)
    for j in range(3):                                  # 3 vạch từ ngoài vào trong
        r=92-j*10
        solid=(bits>>(2-j))&1
        a0,a1=ang-math.radians(15),ang+math.radians(15)
        segs=[(a0,a1)] if solid else [(a0,ang-math.radians(3.5)),(ang+math.radians(3.5),a1)]
        for s0,s1 in segs:
            d.arc((C-r,C-r,C+r,C+r),math.degrees(s0),math.degrees(s1),fill=GOLD,width=3)
    # chấm đỏ chu sa giữa hai quẻ
    am=ang+math.radians(22.5);x=C+math.cos(am)*80;y=C+math.sin(am)*80
    d.rectangle((x-1,y-1,x+1,y+1),fill=RED)
# nan hoa mảnh nối vòng trong - quẻ
for i in range(8):
    am=math.radians(i*45-90+22.5)
    d.line((C+math.cos(am)*30,C+math.sin(am)*30,C+math.cos(am)*57,C+math.sin(am)*57),fill=GOLD2,width=1)
# thái cực giữa
d.ellipse((C-26,C-26,C+26,C+26),fill=(20,14,10,255),outline=GOLD,width=2)
d.pieslice((C-26,C-26,C+26,C+26),90,270,fill=(236,196,92,255))
d.ellipse((C-13,C-26,C+13,C),fill=(236,196,92,255));d.ellipse((C-13,C,C+13,C+26),fill=(20,14,10,255))
d.ellipse((C-4,C-17,C+4,C-9),fill=(20,14,10,255));d.ellipse((C-4,C+9,C+4,C+17),fill=(236,196,92,255))
# quầng sáng cộng
glow=img.filter(ImageFilter.GaussianBlur(3));a=np.array(glow).astype(float);a[...,3]*=0.9
final=Image.alpha_composite(Image.fromarray(a.clip(0,255).astype(np.uint8)),img)
final.save(OUT+'bagua_vang.png');print('bagua',final.size)
# ---- lá bùa ----
W,H=16,38
b=Image.new('RGBA',(W,H),(0,0,0,0));p=b.load()
edge=(120,84,24,255);paper=(232,200,96,255);paper2=(206,168,64,255)
for y in range(H):
    for x in range(W):
        if y>=H-3 and (x+y)%3==0:continue       # đáy răng cưa
        p[x,y]=paper if (x+y)%7 else paper2
for x in range(W):p[x,0]=edge;p[x,H-4 if False else H-1]=(0,0,0,0)
for y in range(H):p[0,y]=edge;p[W-1,y]=edge
for x in range(W):p[x,1]=RED if 2<x<W-3 else p[x,1]
for x in range(3,W-3):p[x,2]=RED
random.seed(5)
# chữ bùa giả: các nét đỏ
glyph=[(7,7,9),(5,10,10),(7,13,9),(4,17,4),(9,17,3),(6,21,8),(8,25,5),(5,28,3),(9,28,3),(7,32,2)]
for gx,gy,l in glyph:
    for k in range(l):p[min(W-2,gx+k-(l//2)),gy]=RED;p[min(W-2,gx+k-(l//2)),gy+1]=RED if k%2==0 else p[min(W-2,gx+k-(l//2)),gy+1]
for y in range(6,34):p[7,y]=RED if y%4 else p[7,y]
b.save(OUT+'bua_vang.png');print('bua',b.size)
# ---- sấm vàng ----
src=Image.open(OUT+'set_bolt.png').convert('RGBA');a=np.array(src).astype(float)
lum=(a[...,:3]*[.3,.59,.11]).sum(2)/255.0
stops=[(0,(100,52,10)),(0.45,(240,180,60)),(0.8,(255,230,140)),(1,(255,252,230))]
def lut(v):
    for i in range(len(stops)-1):
        v0,c0=stops[i];v1,c1=stops[i+1]
        if v<=v1:t=(v-v0)/(v1-v0+1e-6);return [c0[k]+(c1[k]-c0[k])*t for k in range(3)]
    return list(stops[-1][1])
col=np.zeros(lum.shape+(3,));
for y in range(lum.shape[0]):
    for x in range(lum.shape[1]):
        if a[y,x,3]>0:col[y,x]=lut(lum[y,x])
a[...,:3]=col;Image.fromarray(a.clip(0,255).astype(np.uint8),'RGBA').save(OUT+'set_bolt_vang.png');print('bolt',src.size)
