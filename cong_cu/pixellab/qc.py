"""Kiểm frame so với master, dựa trên vị trí kiếm mong đợi (từ khung xương).
Dùng như module: check(master_png, master_sword(w,t), frames[(png, wrist_xy, angle_deg)], L)"""
import math,numpy as np
from PIL import Image
from collections import deque
def load(p):return np.array(Image.open(p).convert('RGBA')).astype(int)
def blade_px(a):
    r,g,b,al=a[...,0],a[...,1],a[...,2],a[...,3]
    mx=np.maximum(np.maximum(r,g),b);mn=np.minimum(np.minimum(r,g),b);lum=(r+g+b)/3
    return (al>128)&(mx-mn<=40)&(lum>=95)
def cover(bm,w,ang,L,t0,t1,rad=2):
    H,W=bm.shape;a=math.radians(ang);n=max(6,int(L*(t1-t0)));hit=0
    for i in range(n):
        t=t0+(t1-t0)*i/(n-1);x=w[0]+math.cos(a)*L*t;y=w[1]+math.sin(a)*L*t
        x0,x1=int(max(0,x-rad)),int(min(W-1,x+rad));y0,y1=int(max(0,y-rad)),int(min(H-1,y+rad))
        if 0<=x<W and 0<=y<H and bm[y0:y1+1,x0:x1+1].any():hit+=1
    return hit/n
def best_line(bm,w,ang,L):
    best=(-1,w,ang)
    for da in range(-32,33,2):
        for dx in(-3,0,3):
            for dy in(-3,0,3):
                ww=(w[0]+dx,w[1]+dy);c=cover(bm,ww,ang+da,L,0.2,1.0)
                if c>best[0]:best=(c,ww,ang+da)
    return best
def band(shape,w,ang,L,wid=4,ext=1.25):
    H,W=shape;yy,xx=np.mgrid[0:H,0:W];a=math.radians(ang);ux,uy=math.cos(a),math.sin(a)
    px,py=xx-w[0],yy-w[1];t=px*ux+py*uy;d=np.abs(-px*uy+py*ux)
    return (t>=-6)&(t<=L*ext)&(d<=wid)
def extra_swords(bm,w,ang,L):
    m=bm&~band(bm.shape,w,ang,L,6)
    H,W=m.shape;seen=np.zeros_like(m);found=[]
    for y,x in zip(*np.nonzero(m)):
        if seen[y,x]:continue
        q=deque([(y,x)]);seen[y,x]=1;pts=[]
        while q:
            cy,cx=q.popleft();pts.append((cx,cy))
            for dy in(-1,0,1):
                for dx in(-1,0,1):
                    yy,xx=cy+dy,cx+dx
                    if 0<=yy<H and 0<=xx<W and m[yy,xx] and not seen[yy,xx]:seen[yy,xx]=1;q.append((yy,xx))
        if len(pts)<10:continue
        p=np.array(pts,float);c=p-p.mean(0);_,s,vt=np.linalg.svd(c,full_matrices=False)
        pr=c@vt[0];length=pr.max()-pr.min();wd=len(p)/max(length,1)
        if length>=0.55*L and wd<=3.2:found.append(round(float(length),1))
    return found
def palette_set(a):
    px=a[a[...,3]>128][:,:3];q=np.unique(px//8,axis=0);return q*8+4
def costume(a,pal):
    px=a[a[...,3]>128][:,:3].astype(float)
    d=np.min(np.linalg.norm(px[:,None,:]-pal[None,:,:],axis=2),axis=1)
    return float((d<=30).mean())
def check(master,mw,mang,L,frames):
    M=load(master);pal=palette_set(M).astype(float)
    bm=blade_px(M);mc=cover(bm,mw,mang,L,0.2,1.0);mx=extra_swords(bm,mw,mang,L)
    out=[{'f':'MASTER','sword_cov':round(mc,2),'extra':mx}]
    for f,w,ang in frames:
        A=load(f);bm=blade_px(A)
        if ang is None:
            out.append({'f':f.split('/')[-1],'note':'không cầm kiếm theo thiết kế'});continue
        c,ww,aa=best_line(bm,w,ang,L)
        tip=cover(bm,ww,aa,L,0.85,1.0);over=cover(bm,ww,aa,L,1.12,1.3)
        ex=extra_swords(bm,ww,aa,L);cs=costume(A,pal)
        ok=c>=0.8 and tip>=0.5 and over<=0.5 and cs>=0.95
        out.append({'f':f.split('/')[-1],'pass':ok,'sword_cov':round(c,2),'tip':round(tip,2),'over':round(over,2),'angle_off':aa-ang,'extra':ex,'costume%':round(cs*100,1)})
    return out

# ---- Bàn tay & điểm ảnh rác ----
def skin(a):
    r,g,b,al=a[...,0],a[...,1],a[...,2],a[...,3]
    return (al>128)&(r>=200)&(g>=150)&(g<=215)&(b>=100)&(b<=175)&(r-b>=60)
def hand_ok(a,wrist,rad=7,need=4):
    m=skin(a);H,W=m.shape;x,y=int(wrist[0]),int(wrist[1])
    return int(m[max(0,y-rad):y+rad+1,max(0,x-rad):x+rad+1].sum())>=need
def stray(a,minsize=8,gap=3):
    """Cụm điểm ảnh nhỏ nằm tách khỏi thân chính."""
    al=a[...,3]>40;H,W=al.shape;seen=np.zeros_like(al);comps=[]
    for y,x in zip(*np.nonzero(al)):
        if seen[y,x]:continue
        q=deque([(y,x)]);seen[y,x]=1;n=0
        while q:
            cy,cx=q.popleft();n+=1
            for dy in range(-gap,gap+1):
                for dx in range(-gap,gap+1):
                    yy,xx=cy+dy,cx+dx
                    if 0<=yy<H and 0<=xx<W and al[yy,xx] and not seen[yy,xx]:seen[yy,xx]=1;q.append((yy,xx))
        comps.append(n)
    comps.sort(reverse=True);return [c for c in comps[1:] if c<minsize*4]

def costume12(a,pal):
    px=a[a[...,3]>128][:,:3].astype(float)
    d=np.min(np.linalg.norm(px[:,None,:]-pal[None,:,:],axis=2),axis=1)
    return float((d<=12).mean())
