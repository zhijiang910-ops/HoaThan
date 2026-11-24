"""Dựng sheet elip đòn C v2 (24/11): 3 dải lồng nhau dày-mỏng, gradient viền→thân→lõi, vệt tốc độ, hạt, quầng sáng; vẽ dần rồi tan từ đuôi (đuôi vỡ hạt).
Ra k5c_behind.png / k5c_front.png (ô 334x125 / 334x121, 15 khung, 4 cột)."""
import math,random,sys
from PIL import Image,ImageDraw,ImageFilter
OUT=sys.argv[1] if len(sys.argv)>1 else 'game/assets/vfx/'
N=15;CW=334;COLS=4
RX,RY=140,52
C_OUT=(30,104,112);C_MID=(60,170,170);C_LT=(130,228,214);C_HI=(214,250,242);C_W=(255,255,255)
def ang(u):return math.radians(200+330*u)
def ribbon(d,front,cy,rx,ry,t0,t1,th,cols,rnd,dith=0.0):
    n=110;P=[]
    for i in range(n+1):
        u=t0+(t1-t0)*i/n;s=i/n
        w=th*(max(0.0,math.sin(math.pi*(s**0.75)))**0.7)
        a=ang(u);x=CW/2+rx*math.cos(a);y=cy+ry*math.sin(a)
        nx,ny=math.cos(a)/rx,math.sin(a)/ry;nl=math.hypot(nx,ny)
        P.append((u,x,y,nx/nl,ny/nl,w))
    for (k,(frac,col)) in enumerate(cols):
        for i in range(n):
            u,x,y,nx,ny,w=P[i];u2,x2,y2,nx2,ny2,w2=P[i+1]
            if (math.sin(ang((u+u2)/2))>0)!=front:continue
            # dải lệch về phía ngoài (mép trên) để có chiều sâu: viền ngoài sáng hơn
            off=0.18*w*(1-frac)
            a=w*frac/2;b=w2*frac/2
            q=[(x+nx*(a+off),y+ny*(a+off)),(x2+nx2*(b+0.18*w2*(1-frac)),y2+ny2*(b+0.18*w2*(1-frac))),
               (x2-nx2*(b-0.18*w2*(1-frac)),y2-ny2*(b-0.18*w2*(1-frac))),(x-nx*(a-off),y-ny*(a-off))]
            if dith and k==0 and i<n*0.5 and rnd.random()<dith*(1-i/(n*0.5)):continue
            d.polygon(q,fill=col+(255,))
def sheet(name,CH,py,front):
    cy=py-40;rnd=random.Random(11 if front else 5)
    out=Image.new('RGBA',(CW*COLS,CH*((N+COLS-1)//COLS)),(0,0,0,0))
    for f in range(N):
        p=(f+0.5)/N;head=min(1,p*1.2);tail=head*min(1,max(0,(p-0.42)/0.5))**1.1
        im=Image.new('RGBA',(CW,CH),(0,0,0,0));d=ImageDraw.Draw(im)
        glow=Image.new('RGBA',(CW,CH),(0,0,0,0));gd=ImageDraw.Draw(glow)
        if head-tail>0.02:
            # quầng sáng mềm (viết bằng dải rộng rồi làm mờ, lượng tử về 3 mức alpha cho giữ chất pixel)
            ribbon(gd,front,cy,RX,RY,tail,head,64,[(1.0,(150,235,225))],rnd)
            glow=glow.filter(ImageFilter.GaussianBlur(7))
            a=glow.getchannel('A').point(lambda v:0 if v<40 else 45 if v<90 else 80)
            glow.putalpha(a)
            im.alpha_composite(glow)
            # dải ngoài mảnh, mờ, đến sớm hơn (vệt gió)
            ribbon(d,front,cy,RX*1.12,RY*1.14,max(0,tail-0.04),max(0,head-0.12),10,[(1.0,C_MID),(0.45,C_LT)],rnd,dith=0.6)
            # dải chính dày
            ribbon(d,front,cy,RX,RY,tail,head,44,[(1.0,C_OUT),(0.8,C_MID),(0.6,C_LT),(0.38,C_HI),(0.17,C_W)],rnd)
            # dải trong, ngắn hơn, tụ về đầu
            ribbon(d,front,cy,RX*0.84,RY*0.8,tail+(head-tail)*0.25,head*0.96,20,[(1.0,C_MID),(0.65,C_LT),(0.3,C_W)],rnd)
            # vệt tốc độ + hạt quanh đầu và đuôi
            for _ in range(26):
                u=rnd.uniform(tail,head);a=ang(u)
                if (math.sin(a)>0)!=front:continue
                r=rnd.uniform(0.9,1.28);x=CW/2+RX*r*math.cos(a);y=cy+RY*r*math.sin(a)
                L=rnd.randint(3,9);tx,ty=-math.sin(a)*RX,math.cos(a)*RY;tl=math.hypot(tx,ty);tx/=tl;ty/=tl
                col=rnd.choice([C_LT,C_HI,C_W])
                d.line([(x,y),(x-tx*L,y-ty*L)],fill=col+(255,),width=1)
            for _ in range(14):
                u=rnd.uniform(head-0.18,head);a=ang(u)
                if (math.sin(a)>0)!=front:continue
                x=CW/2+RX*math.cos(a)+rnd.uniform(-18,18);y=cy+RY*math.sin(a)+rnd.uniform(-18,18)
                d.rectangle([x,y,x+rnd.choice([0,1]),y+rnd.choice([0,1])],fill=rnd.choice([C_HI,C_W])+(255,))
        out.paste(im,((f%COLS)*CW,(f//COLS)*CH))
    out.save(OUT+name)
sheet('k5c_behind.png',125,107,False)
sheet('k5c_front.png',121,99,True)
