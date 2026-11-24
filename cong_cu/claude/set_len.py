"""Sét NỔ TRỒI LÊN từ mặt đất ở chân mũi cự kiếm (24/11, tự làm). Ra game/assets/vfx/set_len_do.png: 12 khung 240x230, 4 cột, gốc nổ ở (120,208).
Các tia sét gấp khúc bung ra mọi hướng quanh tâm (ép dẹt theo mặt đất, vài tia bắn lên), đổi hình mỗi khung; viền đen, thân đỏ, lõi sáng."""
import random,math
from PIL import Image,ImageDraw,ImageFilter
W,H=240,230;CX,CY=120,208;N=12;COLS=4
def arc(rnd,ang,length,flat=0.5,seg=9,amp=7):
    pts=[(CX,CY)]
    for i in range(1,seg+1):
        t=i/seg;r=length*t;a=ang+rnd.uniform(-0.13,0.13)*(0.4+t)
        up=-abs(math.sin(ang))*0.0
        pts.append((CX+math.cos(a)*r+rnd.uniform(-amp,amp)*0.3,CY+math.sin(a)*r*flat+rnd.uniform(-amp,amp)*0.4*flat))
    return pts
def frame(f):
    rnd=random.Random(500+f*13)
    im=Image.new('RGBA',(W,H),(0,0,0,0))
    q=f/(N-1);grow=min(1,f/4.0);fade=1.0 if f<=6 else max(0,1-(f-6)/5.5)
    arcs=[]
    if fade>0:
        n=10 if f<=6 else 7
        for i in range(n):
            if i<n-3:
                ang=-math.pi/2+(i/(n-4)-0.5)*1.05+rnd.uniform(-0.12,0.12);L=rnd.uniform(110,200)*(0.3+0.7*grow)*(0.8+0.2*fade);fl=1.0
            else:
                ang=rnd.choice([0,math.pi])+rnd.uniform(-0.25,0.25);L=rnd.uniform(55,95)*(0.35+0.65*grow)*(0.8+0.2*fade);fl=0.35
            main=arc(rnd,ang,L,flat=fl)
            arcs.append((main,1.0))
            if len(main)>5 and rnd.random()<0.8:
                k=rnd.randint(3,6);bx,by=main[k];ba=ang+rnd.choice([-1,1])*rnd.uniform(0.5,0.9)
                bp=[(bx,by)]
                for j in range(1,4):
                    bp.append((bx+math.cos(ba)*L*0.13*j+rnd.uniform(-3,3),by+math.sin(ba)*L*0.13*j*0.55+rnd.uniform(-2,2)))
                arcs.append((bp,0.6))
    glow=Image.new('L',(W,H),0);gd=ImageDraw.Draw(glow)
    for pl,s in arcs:gd.line(pl,fill=255,width=int(7*s),joint='curve')
    ell=int(34*min(1,0.4+grow)*fade+2)
    gd.ellipse([CX-ell,CY-int(ell*0.45),CX+ell,CY+int(ell*0.45)],fill=200)
    glow=glow.filter(ImageFilter.GaussianBlur(3))
    g=Image.new('RGBA',(W,H),(190,10,25,0));g.putalpha(glow.point(lambda v:int(min(255,v*0.55*fade))));im.alpha_composite(g)
    d=ImageDraw.Draw(im)
    for pl,s in arcs:d.line(pl,fill=(14,2,6,255),width=int(5*s)+1,joint='curve')
    for pl,s in arcs:d.line(pl,fill=(215,24,34,255),width=max(1,int(3*s)),joint='curve')
    for pl,s in arcs:d.line(pl,fill=(255,170,140,255),width=1,joint='curve')
    # chớp lõi tại tâm nổ
    if f<=7:
        a=int(255*(1-f/8.0));rx=int(8+22*min(1,f/3.0));ry=max(3,int(rx*0.42))
        d.ellipse([CX-rx,CY-ry,CX+rx,CY+ry],fill=(12,2,6,int(a*0.9)))
        d.ellipse([CX-rx*2//3,CY-ry*2//3,CX+rx*2//3,CY+ry*2//3],fill=(235,30,40,a))
        d.ellipse([CX-rx//3,CY-ry//3,CX+rx//3,CY+ry//3],fill=(255,200,170,a))
    # tia lửa
    for _ in range(14 if f<8 else 4):
        ang=rnd.uniform(0,math.tau);r=rnd.uniform(30,115)*grow;sx=CX+math.cos(ang)*r;sy=CY+math.sin(ang)*r*0.5-rnd.uniform(0,18)*q
        d.rectangle([sx,sy,sx+1,sy+1],fill=(255,120,90,int(255*fade)))
    a=im.getchannel('A').point(lambda v:0 if v<50 else 255 if v>150 else 150);im.putalpha(a)
    return im
sheet=Image.new('RGBA',(W*COLS,H*((N+COLS-1)//COLS)),(0,0,0,0))
for f in range(N):sheet.paste(frame(f),((f%COLS)*W,(f//COLS)*H))
sheet.save('game/assets/vfx/set_len_do.png')
bg=Image.new('RGBA',sheet.size,(150,160,170,255));bg.alpha_composite(sheet);bg.save('/tmp/claude-0/-home-user-HoaThan/22bfe91b-3fff-5268-9261-53695ffcbebb/scratchpad/set_len_prev.png')
