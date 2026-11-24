"""Elip đòn C v3 (24/11) bám ảnh tham chiếu của chủ game: elip dẹt rộng quanh nhân vật, chùm nhiều sợi mảnh song song,
dày dần về cuối (dưới-trái), lõi trắng - rìa xanh lam - quầng sáng, vệt gió ngoài vòng; vẽ dần từ sau lưng rồi tan từ đuôi.
Ra k5c_behind.png / k5c_front.png: ô 360x160, 15 khung, 4 cột. python3 c_ellipse.py [thư mục ra]"""
import math,random,sys
from PIL import Image,ImageDraw,ImageFilter
OUT=sys.argv[1] if len(sys.argv)>1 else 'game/assets/vfx/'
VAR=sys.argv[2] if len(sys.argv)>2 else 'spark'  # mặc định: tia sao ở đầu nhát chém (chủ game chọn 24/11)
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

def ring_small(d,front,rx,ry,tail,head,wmax,nst,seed):
    """vòng nhỏ phía trong (24/11, chủ game xin thêm): chùm sợi mảnh sáng, quét nhanh hơn, tan sớm hơn vòng lớn"""
    rr=random.Random(seed)
    for i in range(nst):
        off=(i/(nst-1))*2-1;a0=rr.uniform(0,0.1);b0=rr.uniform(0.9,1.0);n=60;pts=[]
        u0=tail+(head-tail)*a0;u1=tail+(head-tail)*b0
        for j in range(n+1):
            u=u0+(u1-u0)*j/n;sv=(u-tail)/max(1e-6,head-tail)
            W=wmax*prof(sv);a=ang(u);r=off*W/2
            nx,ny=math.cos(a)/rx,math.sin(a)/ry;nl=math.hypot(nx,ny);nx/=nl;ny/=nl
            pts.append((a,CX+rx*math.cos(a)+nx*r,CY+ry*math.sin(a)+ny*r,sv))
        for j in range(n):
            a,x,y,sv=pts[j];a2,x2,y2,_=pts[j+1]
            if (math.sin((a+a2)/2)>0)!=front:continue
            k=abs(off);col=colour(min(1,k*0.8+0.05))
            d.line([(x,y),(x2,y2)],fill=col+(255,),width=2 if k<0.3 else 1)
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
            # vòng nhỏ trong: bắt đầu trễ 0,12, quét nhanh, tan trước vòng lớn
            h2=min(1,max(0,(p-0.12)*1.7));t2=h2*min(1,max(0,(p-0.5)/0.38))**1.1
            if VAR=='' and h2-t2>0.03:ring_small(d,front,RX*0.46,RY*0.46,t2,h2,26,12,91+(1 if front else 0))
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
        if VAR=='cross' and head-tail>0.03:
            # vòng thứ hai cùng cỡ, nghiêng ngược chiều, mờ hơn: nhìn như hai vành xoáy bắt chéo
            im2=im.rotate(-16,center=(CX,CY),resample=Image.BICUBIC);r_,g_,b_,a_=im2.split();a_=a_.point(lambda v:int(v*0.7));im2=Image.merge('RGBA',(r_,g_,b_,a_))
            im=Image.alpha_composite(im2,im.rotate(7,center=(CX,CY),resample=Image.BICUBIC))
        if VAR=='ground' and not front:
            # sóng xung kích dưới chân: vành elip dẹt nở dần ra rồi mờ, kèm bụi
            dd=ImageDraw.Draw(im);q=min(1,max(0,(p-0.15)/0.7))
            if 0<q<1:
                for k_,(rf,wd,cc) in enumerate(((1.0,3,PAL[2]),(0.86,2,PAL[1]),(0.7,1,PAL[0]))):
                    rx_=30+190*q*rf;ry_=rx_*0.34;al=int(255*(1-q)**0.8)
                    dd.ellipse([CX-rx_,CY+38-ry_,CX+rx_,CY+38+ry_],outline=cc+(al,),width=wd)
        if VAR=='spark' and front and head-tail>0.03 and p>0.2:
            # tia sao ở đầu nhát chém + tia lửa bắn ra ngoài
            dd=ImageDraw.Draw(im);a=ang(head);hx=CX+RX*math.cos(a);hy=CY+RY*math.sin(a);fade=max(0,1-max(0,p-0.75)/0.25)
            if math.sin(a)>0:
                for L_,w_ in ((26,3),(14,7)):
                    dd.polygon([(hx,hy-L_),(hx+w_,hy),(hx,hy+L_),(hx-w_,hy)],fill=PAL[0]+(int(255*fade),));dd.polygon([(hx-L_,hy),(hx,hy-w_),(hx+L_,hy),(hx,hy+w_)],fill=PAL[0]+(int(255*fade),))
                rr=random.Random(f)
                for _ in range(14):
                    th=rr.uniform(-1.2,1.2)+math.pi*0.1;L_=rr.uniform(10,34);dd.line([(hx+math.cos(th)*8,hy+math.sin(th)*8),(hx+math.cos(th)*L_,hy+math.sin(th)*L_)],fill=rr.choice([PAL[0],PAL[1],PAL[2]])+(int(230*fade),),width=1)
        out.paste(im,((f%COLS)*CW,(f//COLS)*CH))
    out.save(OUT+name)
sheet('k5c_behind.png',False)
sheet('k5c_front.png',True)
