"""Tia sét đánh xuống cho Thiên Xu (24/11, chủ game bảo tự làm, không PixelLab). Ra game/assets/vfx/set_bolt.png: 12 khung 80x120, 4 cột, điểm đánh ở (40,108).
Khung 0-5: tia sét dày gấp khúc đổi hình mỗi khung + chớp tròn dẹt dưới đất; 6-11: chớp tan dần, tia lửa."""
import random,math
from PIL import Image,ImageDraw,ImageFilter
W,H=80,240;GX,GY=40,228;N=12;COLS=4
def bolt_path(rnd,x0=40,y0=2,x1=GX,y1=GY,seg=16,amp=5):
    pts=[(x0,y0)]
    for i in range(1,seg):
        t=i/seg;pts.append((x0+(x1-x0)*t+rnd.uniform(-amp,amp)*(1-0.3*t),y0+(y1-y0)*t))
    pts.append((x1,y1));return pts
def draw_poly(d,pts,w,col):
    d.line(pts,fill=col,width=w,joint='curve')
def frame(f):
    rnd=random.Random(100+f*7)
    im=Image.new('RGBA',(W,H),(0,0,0,0))
    alive=f<=5
    layers=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(layers)
    if alive:
        k=1.0 if f<=3 else 0.7
        main=bolt_path(rnd);branches=[]
        for _ in range(2):
            i=rnd.randint(5,13);bx,by=main[i];dx=rnd.choice([-1,1])*rnd.uniform(8,16);bp=[(bx,by)]
            for j in range(1,4):bp.append((bx+dx*j/3+rnd.uniform(-3,3),by+j*rnd.uniform(8,13)))
            branches.append(bp)
        glow=Image.new('L',(W,H),0);gd=ImageDraw.Draw(glow)
        for pl,w in [(main,4)]+[(b,3) for b in branches]:draw_poly(gd,pl,w,255)
        glow=glow.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
        g=Image.new('RGBA',(W,H),(40,120,255,0));g.putalpha(glow.point(lambda v:int(min(255,v*0.45*k))));layers.alpha_composite(g)
        d=ImageDraw.Draw(layers)
        for pl,w in [(main,3)]+[(b,2) for b in branches]:draw_poly(d,pl,w,(110,200,255,255))
        for pl,w in [(main,1)]+[(b,1) for b in branches]:draw_poly(d,pl,w,(255,255,255,255))
    # chớp tròn dẹt dưới đất
    fl=Image.new('RGBA',(W,H),(0,0,0,0));fd=ImageDraw.Draw(fl)
    if f>=1:
        q=(f-1)/10.0;rx=int(10+24*min(1,q*1.6));ry=max(3,int(rx*0.38));a=int(255*max(0,1-q*1.05))
        fd.ellipse([GX-rx,GY-ry,GX+rx,GY+ry],outline=(150,215,255,a),width=2)
        fd.ellipse([GX-rx//2,GY-ry//2,GX+rx//2,GY+ry//2],fill=(230,248,255,int(a*0.8)))
        for _ in range(8 if f<9 else 3):
            ang=rnd.uniform(0,math.tau);r=rnd.uniform(rx*0.6,rx*1.3);sx=GX+math.cos(ang)*r;sy=GY+math.sin(ang)*r*0.5-rnd.uniform(0,10)*q
            fd.rectangle([sx,sy,sx+1,sy+1],fill=(255,255,255,a))
    im.alpha_composite(layers);im.alpha_composite(fl)
    # bỏ khử răng cưa: alpha về 0/255 cho đúng chất pixel
    a=im.getchannel('A').point(lambda v:0 if v<50 else 255 if v>150 else 150);im.putalpha(a)
    return im
sheet=Image.new('RGBA',(W*COLS,H*((N+COLS-1)//COLS)),(0,0,0,0))
for f in range(N):sheet.paste(frame(f),((f%COLS)*W,(f//COLS)*H))
sheet.save('game/assets/vfx/set_bolt.png')
