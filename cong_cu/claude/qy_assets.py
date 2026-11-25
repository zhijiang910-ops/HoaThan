#!/usr/bin/env python3
"""VFX Thiên Cương Môn (Quyền), tự vẽ pixel bằng code (0 lượt PixelLab): trắng bạc + đỏ sẫm.
 qy_an.png  = Thiên Cương ấn dưới đất (vòng bạc, 7 sao Bắc Đẩu nối vạch, vòng đỏ, ba nan)
 qy_hit.png = chớp va chạm quyền: 6 khung 96x96 (sheet 3 cột x 2 hàng): lõi trắng nổ + vòng đỏ + tia tỏa
Chạy: python3 cong_cu/claude/qy_assets.py"""
import math,random
from PIL import Image,ImageDraw,ImageFilter
import numpy as np
OUT='game/assets/vfx/'
SIL=(226,228,236,255);SIL2=(150,154,170,255);RED=(176,36,44,255);RED2=(110,20,28,255);WH=(255,255,255,255)
# ---- ấn ----
S=220;C=110
img=Image.new('RGBA',(S,S),(0,0,0,0))
bg=Image.new('RGBA',(S,S),(0,0,0,0));bd=ImageDraw.Draw(bg)
bd.ellipse((C-104,C-104,C+104,C+104),fill=(150,154,170,40));bd.ellipse((C-62,C-62,C+62,C+62),fill=(176,36,44,52))
img=Image.alpha_composite(bg,img);d=ImageDraw.Draw(img)
def ring(r,w,col):d.ellipse((C-r,C-r,C+r,C+r),outline=col,width=w)
ring(106,2,SIL);ring(101,1,SIL2);ring(64,2,RED);ring(58,1,RED2)
# 7 sao Bắc Đẩu: toạ độ gần chòm gáo, đặt trong vòng 0..56
pts=[(-40,-22),(-24,-30),(-8,-24),(6,-14),(10,6),(32,14),(36,-8)]
for i in range(len(pts)-1):
    d.line((C+pts[i][0],C+pts[i][1],C+pts[i+1][0],C+pts[i+1][1]),fill=SIL2,width=1)
for x,y in pts:
    d.rectangle((C+x-2,C+y-2,C+x+2,C+y+2),fill=WH);d.rectangle((C+x-1,C+y-1,C+x+1,C+y+1),fill=SIL)
# vạch cương: 28 vạch ngắn giữa hai vòng ngoài, 4 vạch dài tại bốn hướng
for i in range(48):
    a=math.radians(i*7.5);r0,r1=(92,98) if i%6 else (86,98)
    d.line((C+math.cos(a)*r0,C+math.sin(a)*r0,C+math.cos(a)*r1,C+math.sin(a)*r1),fill=SIL,width=1 if i%6 else 2)
# ba nan đỏ nối vòng đỏ với vòng ngoài
for i in range(3):
    a=math.radians(90+i*120);d.line((C+math.cos(a)*64,C+math.sin(a)*64,C+math.cos(a)*90,C+math.sin(a)*90),fill=RED,width=3)
    x,y=C+math.cos(a)*78,C+math.sin(a)*78;d.rectangle((x-2,y-2,x+2,y+2),fill=WH)
glow=img.filter(ImageFilter.GaussianBlur(3));a=np.array(glow).astype(float);a[...,3]*=0.85
Image.alpha_composite(Image.fromarray(a.clip(0,255).astype(np.uint8)),img).save(OUT+'qy_an.png')
# ---- chớp va chạm ----
W=96;N=6;sheet=Image.new('RGBA',(W*3,W*2),(0,0,0,0))
random.seed(11)
rays=[(random.uniform(0,2*math.pi),random.uniform(0.7,1.25)) for _ in range(12)]
for f in range(N):
    k=f/(N-1);fr=Image.new('RGBA',(W,W),(0,0,0,0));fd=ImageDraw.Draw(fr);cx=cy=W//2
    r=6+k*34;al=int(255*(1-k**1.6))
    core=int(16*(1-k)+3)
    fd.ellipse((cx-core,cy-core,cx+core,cy+core),fill=(255,255,255,al))
    fd.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(220,226,240,al),width=2)
    r2=r*0.62;fd.ellipse((cx-r2,cy-r2,cx+r2,cy+r2),outline=(176,36,44,int(al*0.95)),width=2)
    for ang,ln in rays:
        l0=r*0.6;l1=r*(0.9+0.55*ln)
        fd.line((cx+math.cos(ang)*l0,cy+math.sin(ang)*l0,cx+math.cos(ang)*l1,cy+math.sin(ang)*l1),fill=(255,236,230,int(al*0.9)),width=1)
    gl=fr.filter(ImageFilter.GaussianBlur(2));g=np.array(gl).astype(float);g[...,3]*=0.6
    fr=Image.alpha_composite(Image.fromarray(g.clip(0,255).astype(np.uint8)),fr)
    sheet.alpha_composite(fr,((f%3)*W,(f//3)*W))
sheet.save(OUT+'qy_hit.png');print('qy ok')

# ---- (25/11, theo clip tham chiếu Roblox) vệt đấm dài, vòng gió xoáy, cung gió nổ cuối ----
import math,random
def sheet(name,fw,fh,cols,rows,drawf,n):
    sh=Image.new('RGBA',(fw*cols,fh*rows),(0,0,0,0))
    for f in range(n):
        fr=Image.new('RGBA',(fw,fh),(0,0,0,0));drawf(ImageDraw.Draw(fr),f,n,fr)
        gl=fr.filter(ImageFilter.GaussianBlur(1.6));g=np.array(gl).astype(float);g[...,3]*=0.55
        fr=Image.alpha_composite(Image.fromarray(g.clip(0,255).astype(np.uint8)),fr)
        sh.alpha_composite(fr,((f%cols)*fw,(f//cols)*fh))
    sh.save(OUT+name+'.png')
WHITE=(255,255,255);SILV=(218,224,238);PINK=(255,214,206)
# vệt đấm: đầu trái (neo), kéo dài sang phải, thon, tan dần; 6 khung 128x24
def streak(d,f,n,fr):
    k=f/(n-1);L=int(30+80*min(1,k*1.6));al=int(255*(1-max(0,k-0.45)/0.55))
    cy=12
    d.polygon([(0,cy),(L*0.35,cy-3),(L,cy-0.5),(L+10,cy),(L,cy+0.5),(L*0.35,cy+3)],fill=WHITE+(al,))
    d.line((2,cy,L+6,cy),fill=WHITE+(al,),width=1)
    d.line((8,cy-6,int(L*0.7),cy-5),fill=SILV+(int(al*0.8),),width=1)
    d.line((8,cy+6,int(L*0.7),cy+5),fill=SILV+(int(al*0.8),),width=1)
    d.line((14,cy-9,int(L*0.45),cy-8),fill=PINK+(int(al*0.6),),width=1)
    d.line((14,cy+9,int(L*0.45),cy+8),fill=PINK+(int(al*0.6),),width=1)
sheet('qy_streak',128,24,3,2,streak,6)
# vòng gió xoáy quanh người: 3 cung elip mảnh quay, 6 khung 128x72
def wind(d,f,n,fr):
    cx,cy=64,36
    for j,(rx,ry,w) in enumerate([(58,22,2),(48,17,1),(38,13,1)]):
        ph=f*(55+j*20)+j*120
        a0=ph;a1=ph+100+30*j
        pts=[]
        for t in range(0,41):
            a=math.radians(a0+(a1-a0)*t/40);pts.append((cx+math.cos(a)*rx,cy+math.sin(a)*ry))
        al=int(230-60*j)
        d.line(pts,fill=WHITE+(al,),width=w)
        d.line([(x,y-3) for x,y in pts[8:30]],fill=SILV+(int(al*0.5),),width=1)
sheet('qy_wind',128,72,3,2,wind,6)
# cung gió nổ cuối (đòn kết): các cung elip lớn mảnh toả ra + tia ngắn, 6 khung 192x128
random.seed(23)
SEG=[(random.uniform(0,360),random.uniform(70,170)) for _ in range(9)]
def bigarc(d,f,n,fr):
    k=(f+1)/n;cx,cy=96,80
    for j,(a0,sp) in enumerate(SEG):
        r=26+k*(34+j*8)+j*3;ry=r*0.42
        al=int(235*(1-k)**0.8*(0.6+0.4*((j%3)/2)))
        pts=[]
        for t in range(0,31):
            a=math.radians(a0+sp*t/30+k*40);pts.append((cx+math.cos(a)*r,cy+math.sin(a)*ry))
        d.line(pts,fill=(WHITE if j%2==0 else SILV)+(al,),width=2 if j%3==0 else 1)
    for q in range(14):
        a=math.radians(q*360/14+f*9);r0=18+k*30;r1=r0+14+10*random.random()
        d.line((cx+math.cos(a)*r0,cy+math.sin(a)*r0*0.45,cx+math.cos(a)*r1,cy+math.sin(a)*r1*0.45),fill=PINK+(int(220*(1-k)),),width=1)
    c0=int(14*(1-k)+2);d.ellipse((cx-c0,cy-c0*0.6,cx+c0,cy+c0*0.6),fill=WHITE+(int(255*(1-k)),))
sheet('qy_arc',192,128,3,2,bigarc,6)
print('qy streak/wind/arc ok')
