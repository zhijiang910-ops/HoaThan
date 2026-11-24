"""Elip đòn C kiểu video Spine 2D 'Weapon Slash Effect' (24/11): cung đặc mượt, đầu sáng (trắng-lam) theo mũi kiếm, đuôi tối dần xanh đậm-tím, đuôi mỏng; 2 lớp cộng sáng; tia sao ở đầu.
python3 c_ellipse2.py [thư mục ra]  -> k5c_behind.png / k5c_front.png (ô 360x224, 15 khung, 4 cột)"""
import math,random,sys
from PIL import Image,ImageDraw
OUT=sys.argv[1] if len(sys.argv)>1 else 'game/assets/vfx/'
N=15;CW,CH=360,224;COLS=4;CX,CY=180,114;RX,RY=150,66
def ang(u):return math.radians(200+330*u)
STOPS=[(0.0,(54,24,120)),(0.3,(40,56,190)),(0.6,(30,110,240)),(0.82,(110,215,255)),(1.0,(255,255,255))]
def grad(s):
    s=max(0,min(1,s))
    for (a,ca),(b,cb) in zip(STOPS,STOPS[1:]):
        if s<=b:
            f=(s-a)/(b-a);return tuple(int(ca[i]+(cb[i]-ca[i])*f) for i in range(3))
    return STOPS[-1][1]
def width(s,W,peak=0.72):      # dày về phía đầu, đầu và đuôi nhọn
    s=min(1,max(0,s));x=s/peak if s<peak else 1-(s-peak)/(1-peak)*0.9
    return W*max(0.0,min(1,x))**0.8*(0.25+0.75*s)
def stroke(d,front,t0,t1,W,rx,ry,bands,bright,rot=0.0):
    n=90
    for i in range(n):
        s0=i/n;s1=(i+1)/n;u0=t0+(t1-t0)*s0;u1=t0+(t1-t0)*s1
        a0=ang(u0)+rot;a1=ang(u1)+rot
        if (math.sin((a0+a1)/2)>0)!=front:continue
        def pt(a,w,r):
            nx,ny=math.cos(a)/rx,math.sin(a)/ry;nl=math.hypot(nx,ny);nx/=nl;ny/=nl
            return (CX+rx*math.cos(a)+nx*w*r/2,CY+ry*math.sin(a)+ny*w*r/2)
        w0=width(s0,W);w1=width(s1,W)
        for b in range(bands):
            r0=-1+2*b/bands;r1=-1+2*(b+1)/bands;rc=abs((r0+r1)/2)
            base=grad((s0+s1)/2*bright+(1-rc)*0.18)       # lõi sáng hơn mép
            col=base+(255,)
            d.polygon([pt(a0,w0,r0),pt(a1,w1,r0),pt(a1,w1,r1),pt(a0,w0,r1)],fill=col)
def sheet(name,front):
    out=Image.new('RGBA',(CW*COLS,CH*((N+COLS-1)//COLS)),(0,0,0,0))
    for f in range(N):
        p=(f+0.5)/N;head=min(1,p*1.25);tail=head*min(1,max(0,(p-0.36)/0.40))
        im=Image.new('RGBA',(CW,CH),(0,0,0,0));d=ImageDraw.Draw(im)
        if head-tail>0.03:
            stroke(d,front,tail,head,70,RX,RY,14,1.0)
            stroke(d,front,tail+(head-tail)*0.3,head,34,RX*0.97,RY*0.97,8,1.25,rot=0.02)   # lớp sáng trên
            if front and p>0.2:
                a=ang(head);hx=CX+RX*math.cos(a);hy=CY+RY*math.sin(a);fade=max(0,1-max(0,p-0.75)/0.25)
                if math.sin(a)>0:
                    for L_,w_ in ((26,3),(14,7)):
                        d.polygon([(hx,hy-L_),(hx+w_,hy),(hx,hy+L_),(hx-w_,hy)],fill=(255,255,255,int(255*fade)));d.polygon([(hx-L_,hy),(hx,hy-w_),(hx+L_,hy),(hx,hy+w_)],fill=(255,255,255,int(255*fade)))
        out.paste(im,((f%COLS)*CW,(f//COLS)*CH))
    out.save(OUT+name)
sheet('k5c_behind.png',False);sheet('k5c_front.png',True)
