"""Dựng sheet elip đòn C (24/11): nhát chém cong dày-mỏng, vẽ dần rồi tan từ đuôi. Ra k5c_behind.png / k5c_front.png.
Giữ kích thước ô cũ (334x125 / 334x121, 15 khung, 4 cột) để không đổi SPX."""
import math,random
from PIL import Image,ImageDraw
V='game/assets/vfx/'
N=15;CW=334;COLS=4
RX,RY=148,50
TH=(('o',34,(36,122,120,255)),('b',25,(128,224,208,255)),('c',10,(250,255,252,255)))   # viền / thân / lõi (bảng màu A-B)
def ang(u):return math.radians(200+330*u)
def pts(t0,t1,n=70):return [t0+(t1-t0)*i/n for i in range(n+1)]
def sheet(name,CH,py,front):
    cy=py-40
    out=Image.new('RGBA',(CW*COLS,CH*((N+COLS-1)//COLS)),(0,0,0,0))
    random.seed(7 if front else 3)
    for f in range(N):
        p=(f+0.5)/N;head=min(1,p*1.2);tail=head*min(1,max(0,(p-0.42)/0.5))**1.1
        im=Image.new('RGBA',(CW,CH),(0,0,0,0));d=ImageDraw.Draw(im)
        if head-tail>0.02:
            for key,th,col in TH:
                us=pts(tail,head);P=[]
                for u in us:
                    s=(u-tail)/max(1e-6,head-tail)
                    w=th*(max(0.0,math.sin(math.pi*(min(1.0,s)**0.8)))**0.75)
                    if key!='o':w*=1.0
                    a=ang(u);x=CW/2+RX*math.cos(a);y=cy+RY*math.sin(a)
                    nx,ny=math.cos(a)/RX,math.sin(a)/RY;nl=math.hypot(nx,ny);nx/=nl;ny/=nl
                    P.append((u,x,y,nx*w/2,ny*w/2))
                for i in range(len(P)-1):
                    u,x,y,dx,dy=P[i];u2,x2,y2,dx2,dy2=P[i+1]
                    isfront=math.sin(ang((u+u2)/2))>0
                    if isfront!=front:continue
                    d.polygon([(x+dx,y+dy),(x2+dx2,y2+dy2),(x2-dx2,y2-dy2),(x-dx,y-dy)],fill=col)
            if front:   # vài hạt sáng gần đầu nhát chém
                a=ang(head);hx=CW/2+RX*math.cos(a);hy=cy+RY*math.sin(a)
                if math.sin(a)>0:
                    for _ in range(7):
                        d.point((int(hx+random.uniform(-16,16)),int(hy+random.uniform(-12,12))),fill=(250,255,252,255))
        out.paste(im,((f%COLS)*CW,(f//COLS)*CH))
    out.save(V+name)
sheet('k5c_behind.png',125,107,False)
sheet('k5c_front.png',121,99,True)
