"""Kiểm frame Ngộ Không: gậy (đỏ/vàng) phủ đúng đường gậy mong đợi cả 2 đầu, đủ dài; đuôi; lông vũ; màu ≥97%; không đốm lẻ.
qc_wk.py <tools_dir> <wkp_dir> <out_png> anim..."""
import sys,json,glob,math
sys.path.insert(0,sys.argv[1]);import qc,numpy as np
from PIL import Image,ImageDraw,ImageFont
D=sys.argv[2].rstrip('/')+'/';OUT=sys.argv[3];ANIMS=sys.argv[4:];S=192
P=json.load(open(D+'wk_poses.json'));M=qc.load(D+'wk_first.png');pal=qc.palette_set(M).astype(float)
C0={p['label']:(p['x']*S,p['y']*S) for p in json.load(open(D+'wk_cust_meta.json'))['frames'][0]};MIX0=qc.torso_mix2(M,C0)
def staffpx(a):
    r,g,b,al=a[...,0],a[...,1],a[...,2],a[...,3]
    red=(r>=110)&(g<=80)&(b<=80)&(r-g>=60);gold=(r>=170)&(g>=110)&(b<=110)&(r-b>=80)
    return (al>128)&(red|gold)
def furpx(a):
    r,g,b,al=a[...,0],a[...,1],a[...,2],a[...,3]
    return (al>128)&(r>=90)&(r-b>=35)&(g>=50)&(g<=170)
def cov(m,p0,p1,rad=2,n=None):
    H,W=m.shape;L=math.dist(p0,p1);n=n or max(6,int(L));h=0
    for i in range(n):
        t=i/(n-1);x=p0[0]+(p1[0]-p0[0])*t;y=p0[1]+(p1[1]-p0[1])*t;xi,yi=int(x),int(y)
        if 0<=xi<W and 0<=yi<H and m[max(0,yi-rad):yi+rad+1,max(0,xi-rad):xi+rad+1].any():h+=1
    return h/n
def best(m,g,th,dF,dB,rad=2):
    bestv=(-1,None)
    for da in range(-24,25,3):
        for dx in(-4,0,4):
            for dy in(-4,0,4):
                gg=(g[0]+dx,g[1]+dy);t=math.radians(th+da);u=(math.cos(t),math.sin(t))
                f=(gg[0]+u[0]*dF,gg[1]+u[1]*dF);b=(gg[0]-u[0]*dB,gg[1]-u[1]*dB)
                c=(cov(m,gg,f,rad)+cov(m,gg,b,rad))/2
                if c>bestv[0]:bestv=(c,(gg,f,b,th+da))
    return bestv
def grayc(a):
    r,g,b,al=a[...,0],a[...,1],a[...,2],a[...,3];mx=np.maximum(np.maximum(r,g),b);mn=np.minimum(np.minimum(r,g),b)
    return int(((al>10)&(mx-mn<25)&(mx>70)&(mx<200)).sum())
GRAY0=grayc(M)
def extra_staff(sm,gg,fe,be,w=9):
    H,W=sm.shape;yy,xx=np.mgrid[0:H,0:W];vx,vy=fe[0]-be[0],fe[1]-be[1];L=vx*vx+vy*vy or 1
    t=np.clip(((xx-be[0])*vx+(yy-be[1])*vy)/L,0,1);dd=np.hypot(xx-be[0]-t*vx,yy-be[1]-t*vy)
    return int((sm&(dd>w)).sum())
rows=[];rep=[]
for an in ANIMS:
    fs=sorted(glob.glob(D+f'out/wk_{an}_0*.png'));row=[]
    for i,(f,kp) in enumerate(zip(fs,P[an])):
        d={q['label']:(q['x']*S,q['y']*S) for q in kp}
        g=d['staff_grip'];ft=d['staff_front_tip'];bt=d['staff_back_tip']
        dF=math.dist(g,ft);dB=math.dist(g,bt);th=math.degrees(math.atan2(ft[1]-g[1],ft[0]-g[0]))
        A=qc.load(f);sm=staffpx(A);c,(gg,fe,be,tt)=best(sm,g,th,dF,dB)
        u=(math.cos(math.radians(tt)),math.sin(math.radians(tt)))
        fend=cov(sm,(gg[0]+u[0]*dF*.85,gg[1]+u[1]*dF*.85),fe);bend=cov(sm,(gg[0]-u[0]*dB*.85,gg[1]-u[1]*dB*.85),be)
        fm=furpx(A);tail=cov(fm,d['tail_2'],d['tail_tip'],rad=4)
        cs=qc.costume12(A,pal);st=qc.stray(A);tm=qc.mix_dist(qc.torso_mix2(A,d),MIX0)
        e=[];ex=extra_staff(sm,gg,fe,be);gc=grayc(A)
        if gc>GRAY0*1.6:e.append(f'vệt mờ ({gc})')
        if c<0.8:e.append(f'gậy thiếu ({c:.2f})')
        if fend<0.5 or bend<0.5:e.append('gậy ngắn')
        if tail<0.5:e.append('mất đuôi')
        if cs<0.97:e.append(f'màu {cs*100:.1f}%')
        if st:e.append(f'đốm x{len(st)}')
        if False and tm>0.07:e.append(f'đổi trang phục {tm:.2f}')
        row.append((f,e));rep.append((an,i,e,round(c,2),round(tail,2),round(cs*100,1)))
    rows.append((an,row))
FT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',12)
Z=1.5;CW=int(S*Z);o=Image.new('RGB',(CW*9,(CW+22)*len(rows)),'#2a2f38');dr=ImageDraw.Draw(o)
for r,(an,row) in enumerate(rows):
    y=r*(CW+22);dr.text((6,y+3),an,fill='#ffd987',font=FT)
    for c,(f,e) in enumerate([(D+'wk_first.png',None)]+row):
        im=Image.open(f).convert('RGBA').resize((CW,CW),Image.NEAREST);bg=Image.new('RGBA',(CW,CW),(70,78,90,255));bg.alpha_composite(im);o.paste(bg.convert('RGB'),(c*CW,y+20))
        lab='MASTER' if e is None else ('LỖI: '+', '.join(e) if e else 'ĐẠT');dr.text((c*CW+4,y+22),lab[:34],fill='#9cc4ff' if e is None else ('#ff6a5a' if e else '#8fe0a8'),font=FT)
        if e:dr.rectangle((c*CW,y+20,c*CW+CW-1,y+20+CW-1),outline='#ff4030',width=3)
o.save(OUT)
for x in rep:print(('LỖI ' if x[2] else 'ĐẠT '),x[0],x[1],x[2],'gậy',x[3],'đuôi',x[4],'màu',x[5])
