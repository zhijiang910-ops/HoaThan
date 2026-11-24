"""Elip đòn C v3 (24/11) bám ảnh tham chiếu của chủ game: elip dẹt rộng quanh nhân vật, chùm nhiều sợi mảnh song song,
dày dần về cuối (dưới-trái), lõi trắng - rìa xanh lam - quầng sáng, vệt gió ngoài vòng; vẽ dần từ sau lưng rồi tan từ đuôi.
Ra k5c_behind.png / k5c_front.png: ô 360x160, 15 khung, 4 cột. python3 c_ellipse.py [thư mục ra]"""
import math,random,sys
from PIL import Image,ImageDraw,ImageFilter
OUT=sys.argv[1] if len(sys.argv)>1 else 'game/assets/vfx/'
N=15;CW,CH=360,224;COLS=4;CX,CY=180,114
RX,RY=150,66
M=18
PAL=[(255,255,255),(214,244,255),(150,214,255),(86,168,250),(44,112,214),(28,72,160)]
def ang(u):return math.radians(200+330*u)
def prof(s):                       # độ rộng chùm theo vị trí s (0 đuôi → 1 đầu): dày về phía cuối, mỏng nhọn hai đầu
    return (max(0.0,math.sin(math.pi*min(1,s)**0.7))**0.8)*(0.35+0.65*s)
def colour(k):                     # k 0=lõi .. 1=mép
    x=k*(len(PAL)-1);i=int(x);f=x-i
    a=PAL[min(i,len(PAL)-1)];b=PAL[min(i+1,len(PAL)-1)]
    return tuple(int(a[j]+(b[j]-a[j])*f) for j in range(3))
def strands(rnd):
    S=[]
    for i in range(M):
        off=(i/(M-1))*2-1
        S.append(dict(off=off,a=rnd.uniform(0.0,0.14),b=rnd.uniform(0.86,1.0),w=rnd.choice([1,1,2]),d=rnd.uniform(0.5,1.0)))
    return S
def sheet(name,front):
    rnd=random.Random(21);ST=strands(rnd)
    out=Image.new('RGBA',(CW*COLS,CH*((N+COLS-1)//COLS)),(0,0,0,0))
    for f in range(N):
        p=(f+0.5)/N;head=min(1,p*1.22);tail=head*min(1,max(0,(p-0.40)/0.52))**1.15
        im=Image.new('RGBA',(CW,CH),(0,0,0,0));d=ImageDraw.Draw(im)
        gl=Image.new('RGBA',(CW,CH),(0,0,0,0));gd=ImageDraw.Draw(gl)
        if head-tail>0.02:
            for pass_ in (0,1):
                for s in ST:
                    u0=tail+(head-tail)*s['a'];u1=tail+(head-tail)*s['b'];n=70;pts=[]
                    for i in range(n+1):
                        u=u0+(u1-u0)*i/n;sv=(u-tail)/max(1e-6,head-tail)
                        W=64*prof(sv)*(0.6+0.4*s['d'])
                        a=ang(u);r=s['off']*W/2
                        nx,ny=math.cos(a)/RX,math.sin(a)/RY;nl=math.hypot(nx,ny);nx/=nl;ny/=nl
                        pts.append((a,CX+RX*math.cos(a)+nx*r,CY+RY*math.sin(a)+ny*r,sv))
                    # chia theo lớp trước/sau (sin>0 = nửa gần camera)
                    for i in range(n):
                        a,x,y,sv=pts[i];a2,x2,y2,_=pts[i+1]
                        if (math.sin((a+a2)/2)>0)!=front:continue
                        k=abs(s['off'])
                        if pass_==0:
                            gd.line([(x,y),(x2,y2)],fill=(70,150,255,255),width=7)
                        else:
                            col=colour(min(1,k*0.9+0.1*(1-sv)))
                            fade=min(1,sv*5)*(1 if sv>0.0 else 0)
                            d.line([(x,y),(x2,y2)],fill=col+(255,),width=s['w'] if k>0.35 else s['w']+1)
            gl=gl.filter(ImageFilter.GaussianBlur(6))
            al=gl.getchannel('A').point(lambda v:0 if v<45 else 22 if v<110 else 40);gl.putalpha(al)
            base=Image.new('RGBA',(CW,CH),(0,0,0,0));base.alpha_composite(gl);base.alpha_composite(im);im=base;d=ImageDraw.Draw(im)
            # --- sợi mảnh lẻ ở nhiều bán kính (trong & ngoài), dài ngắn khác nhau, như ảnh mẫu
            wr=random.Random(5+f*0+(1 if front else 0))
            for si in range(34):
                sc_=wr.choice([0.5,0.62,0.74,0.86,1.0,1.1,1.2,1.3]) if wr.random()<0.8 else wr.uniform(0.45,1.35)
                a0=wr.uniform(0.0,0.85);L=wr.uniform(0.18,0.55);b0=a0+L
                u0=tail+(head-tail)*a0;u1=tail+(head-tail)*min(1,b0)
                if u1-u0<0.03:continue
                ww=wr.choice([1,1,1,2]);tone=wr.choice([PAL[0],PAL[1],PAL[1],PAL[2],PAL[2],PAL[3]])
                n=50
                for i in range(n):
                    ua=u0+(u1-u0)*i/n;ub=u0+(u1-u0)*(i+1)/n
                    if (math.sin(ang((ua+ub)/2))>0)!=front:continue
                    s_=i/n;al=max(0.0,math.sin(math.pi*s_))**0.6
                    if al<0.25:continue
                    xa=CX+RX*sc_*math.cos(ang(ua));ya=CY+RY*sc_*math.sin(ang(ua));xb=CX+RX*sc_*math.cos(ang(ub));yb=CY+RY*sc_*math.sin(ang(ub))
                    col=tuple(int(tone[j]*al+ (44,112,214)[j]*(1-al)) for j in range(3))
                    d.line([(xa,ya),(xb,yb)],fill=col+(255,),width=ww)
            # vệt gió ngắn ngoài vòng + hạt
            for _ in range(22):
                u=rnd.uniform(tail,head);a=ang(u)
                if (math.sin(a)>0)!=front:continue
                r=rnd.uniform(1.05,1.3);x=CX+RX*r*math.cos(a);y=CY+RY*r*math.sin(a)
                L=rnd.randint(4,11);tx,ty=-math.sin(a)*RX,math.cos(a)*RY;tl=math.hypot(tx,ty)
                d.line([(x,y),(x-tx/tl*L,y-ty/tl*L)],fill=rnd.choice([PAL[0],PAL[1],PAL[2]])+(255,),width=1)
            for _ in range(10):
                a=ang(rnd.uniform(max(0,head-0.2),head))
                if (math.sin(a)>0)!=front:continue
                x=CX+RX*math.cos(a)+rnd.uniform(-22,22);y=CY+RY*math.sin(a)+rnd.uniform(-20,20)
                d.rectangle([x,y,x+rnd.choice([0,1]),y+rnd.choice([0,1])],fill=PAL[rnd.choice([0,1])]+(255,))
        out.paste(im,((f%COLS)*CW,(f//COLS)*CH))
    out.save(OUT+name)
sheet('k5c_behind.png',False)
sheet('k5c_front.png',True)
