# Thử (chủ game cho phép 24/11): Hắc Vô Thường và Bạch Vô Thường, đổi màu + vẽ thêm mũ cao, lưỡi dài lên sprite có sẵn.
# Ảnh tĩnh, khung idle đầu tiên, chưa vào game. Chạy: python3 boss_vo_thuong_thu.py <thư mục ra>
import sys,json,re,colorsys
import numpy as np
from PIL import Image,ImageDraw
R='/home/user/HoaThan/game/'
s=open(R+'index.html',encoding='utf-8').read()
CHMd=json.loads(re.search(r'const CHM=(\{.*?\});\n',s,re.S).group(1))
def frame(n):
    v=CHMd[n];im=Image.open(R+f'assets/{n}.png').convert('RGBA');x,y=v['anims']['idle']['f'][0];return im.crop((x,y,x+v['w'],y+v['h']))
OUT=sys.argv[1] if len(sys.argv)>1 else '.'
def hsv_shift(a,h=0,sm=1,vm=1,vo=0):
    o=a.copy();ys,xs=np.nonzero(a[...,3]>0)
    for y,x in zip(ys,xs):
        r,g,b=a[y,x,:3]/255;hh,ss,vv=colorsys.rgb_to_hsv(r,g,b);hh=(hh+h)%1;ss=min(1,ss*sm);vv=min(1,vv*vm+(vo if vv>0.12 else 0))
        o[y,x,:3]=np.array(colorsys.hsv_to_rgb(hh,ss,vv))*255
    return o
K=(14,10,12,255);W=(238,236,230,255);W2=(190,190,196,255);RD=(206,36,44,255);RD2=(130,16,24,255)
def glyphs(d,x0,y0,n,col):
    # vài nét giống chữ viết dọc trên mũ (không phải chữ Hán thật)
    for i in range(n):
        y=y0+i*6
        d.line([(x0,y),(x0+6,y)],fill=col);d.line([(x0+3,y-1),(x0+3,y+3)],fill=col);d.point([(x0+1,y+2),(x0+5,y+2)],fill=col)
def hac():
    a=np.array(frame('hacphong')).astype(float)
    o=hsv_shift(a,sm=0.2,vm=0.55)
    im=Image.fromarray(np.clip(o,0,255).astype(np.uint8));d=ImageDraw.Draw(im)
    # mũ cao hình ống đen, vành rộng
    d.rectangle([76,12,99,41],fill=K);d.rectangle([78,14,97,40],fill=(34,32,38,255));d.rectangle([78,14,81,40],fill=(22,20,26,255))
    d.rectangle([72,39,103,43],fill=K);d.rectangle([74,40,101,42],fill=(46,44,52,255))
    d.line([(78,15),(97,15)],fill=W2)
    glyphs(d,85,21,3,W)
    # lưỡi đỏ dài từ miệng xuống ngực
    d.rectangle([97,67,101,69],fill=K);d.rectangle([98,66,100,78],fill=RD);d.rectangle([97,66,101,69],fill=RD2);d.rectangle([98,67,100,76],fill=RD)
    d.rectangle([97,77,101,81],fill=K);d.rectangle([98,77,100,80],fill=RD);d.point([(99,80)],fill=RD2)
    # đai trắng ngang bụng
    d.rectangle([84,96,96,98],fill=W2);d.line([(84,96),(96,96)],fill=W)
    return im
def bach():
    f=frame('daulap');a=np.array(f).astype(float);orig=a.copy()
    yy,xx=np.mgrid[0:a.shape[0],0:a.shape[1]]
    o=hsv_shift(a,sm=0.1,vm=1.3,vo=0.2)
    al=a[...,3]>0
    skin=al&(xx>=64)&(xx<=82)&(yy>=40)&(yy<=58)&(a[...,0]>200)&(a[...,1]>140)&(a[...,2]<200)
    for c,k in enumerate([242,230,222]):o[...,c]=np.where(skin,a[...,c]*0.3+k*0.7,o[...,c])
    px=np.clip(o,0,255).astype(np.uint8)
    px[0:42,:,3]=0                      # xoá nón lá
    px[0:44,:49,3]=0;px[0:43,49:56,3]=0;px[0:43,85:,3]=0   # xoá nốt viền vành nón còn sót hai bên
    im=Image.fromarray(px);d=ImageDraw.Draw(im)
    # đỉnh đầu (tóc đen) vì nón lá che mất phần này
    d.rectangle([58,37,79,43],fill=K);d.rectangle([59,38,78,42],fill=(26,26,34,255))
    # mũ cao trắng
    d.rectangle([60,10,79,38],fill=K);d.rectangle([62,12,77,37],fill=W);d.rectangle([62,12,64,37],fill=W2)
    d.rectangle([56,36,83,40],fill=K);d.rectangle([58,37,81,39],fill=(226,224,220,255))
    d.line([(62,13),(77,13)],fill=K)
    glyphs(d,67,18,3,K)
    # lưỡi đỏ dài
    d.rectangle([76,52,80,54],fill=K);d.rectangle([77,52,79,66],fill=RD);d.rectangle([76,52,80,54],fill=RD2);d.rectangle([77,53,79,63],fill=RD)
    d.rectangle([76,64,80,68],fill=K);d.rectangle([77,64,79,67],fill=RD);d.point([(78,67)],fill=RD2)
    return im
items=[('hac',frame('hacphong'),hac()),('bach',frame('daulap'),bach())]
import os
cw=330;Wd=Image.new('RGBA',(len(items)*2*cw,330),(54,48,52,255))
for k,(nm,b,a) in enumerate(items):
    for j,im in enumerate((b,a)):
        bb1=b.getbbox();bb2=a.getbbox();bb=(min(bb1[0],bb2[0])-4,min(bb1[1],bb2[1])-4,max(bb1[2],bb2[2])+4,max(bb1[3],bb2[3])+4)
        c=im.crop(bb);f=min(300/c.width,300/c.height);c=c.resize((int(c.width*f),int(c.height*f)),Image.NEAREST)
        Wd.alpha_composite(c,((k*2+j)*cw+(cw-c.width)//2,(330-c.height)//2))
Wd.convert('RGB').save(OUT+'/vo_thuong_thu.png')
items[0][2].save(OUT+'/hac_vo_thuong_tu_ve.png');items[1][2].save(OUT+'/bach_vo_thuong_tu_ve.png');print('ok')
