"""Cắt bớt dải lụa + đổi màu trang phục cho sheet nữ.
python nu_edit.py <hero_nu.png> <out.png> <bảng_màu> <bán_kính_giữ_lụa>"""
import sys,colorsys,numpy as np
from PIL import Image
src,out,scheme,R=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])
a=np.array(Image.open(src).convert('RGBA')).astype(np.int32)
r,g,b,al=a[...,0],a[...,1],a[...,2],a[...,3]
op=al>0
def dil(m,n):
    m=m.copy()
    for _ in range(n):
        m=m|np.roll(m,1,0)|np.roll(m,-1,0)|np.roll(m,1,1)|np.roll(m,-1,1)
    return m
mx=np.maximum(np.maximum(r,g),b);mn=np.minimum(np.minimum(r,g),b);L=(mx+mn)/510
blue=op&(b>r+15)&(b>=g)
light_blue=blue&(L>0.55)&(b-r>=38)   # dải lụa + nơ (xanh đậm sắc; lưỡi kiếm xám bạc b-r nhỏ → giữ)
dark_blue=blue&(L<=0.55)&(b-r>=38)  # viền áo / đai / viền lụa
skin=op&(r-b>55)&(r>200)
cream=op&(L>0.62)&(r>=b)&(r-b<=45)&~skin   # thân váy trắng ngà (loại lưỡi kiếm xám lạnh)
def ero(m,n):
    m=m.copy()
    for _ in range(n):
        m=m&np.roll(m,1,0)&np.roll(m,-1,0)&np.roll(m,1,1)&np.roll(m,-1,1)
    return m
solidish=op&(cream|blue)
mass=dil(ero(solidish,2),4)          # thân váy/áo (dày), không gồm lưỡi kiếm mảnh
cream=cream&mass
core=cream|skin
keep_zone=dil(core,R)
cut=(light_blue|dark_blue)&~keep_zone if R>=0 else np.zeros_like(op)
if R<0: cut=np.zeros_like(op)
a2=a.copy();a2[cut,3]=0
# viền tối mồ côi: điểm tối không còn kề điểm sáng/màu nào
op2=a2[...,3]>0
dark=op2&(L<0.18)
def nb(m):
    return [np.roll(np.roll(m,dy,0),dx,1) for dy in(-1,0,1) for dx in(-1,0,1) if dy or dx]
solid=op2&~dark
near_solid=np.zeros_like(op2)
for k in nb(solid):near_solid|=k
wasribbon=dil(cut,2)
hair=op2&(L<0.4)&(r>b+3)
near_hair=np.zeros_like(op2)
for k in nb(hair):near_hair|=k
orphan=dark&~near_solid&~hair&~near_hair&wasribbon
a2[orphan,3]=0
# vá lỗ: điểm bị cắt có >=5 hàng xóm đặc → lấp bằng màu hàng xóm (tóc phía sau lụa)
for _ in range(3):
    op2=a2[...,3]>0;hole=(cut|orphan)&~op2
    cnt=sum(k.astype(int) for k in nb(op2))
    fill=hole&(cnt>=5)
    if not fill.any():break
    acc=np.zeros(a.shape[:2]+(3,));n=np.zeros(a.shape[:2])
    for dy in(-1,0,1):
        for dx in(-1,0,1):
            if not(dy or dx):continue
            s=np.roll(np.roll(a2,dy,0),dx,1);m=s[...,3]>0
            acc+=s[...,:3]*m[...,None];n+=m
    nn=np.maximum(n,1)[...,None];a2[fill,:3]=(acc/nn)[fill].astype(int);a2[fill,3]=255
from collections import deque
op2=a2[...,3]>0;H,W=op2.shape;seen=np.zeros_like(op2);near=dil(cut,3)
ys,xs=np.nonzero(op2&near)
for y0,x0 in zip(ys,xs):
    if seen[y0,x0]:continue
    q=deque([(y0,x0)]);seen[y0,x0]=1;comp=[]
    while q:
        y,x=q.popleft();comp.append((y,x))
        if len(comp)>60:break
        for dy in(-1,0,1):
            for dx in(-1,0,1):
                yy,xx=y+dy,x+dx
                if 0<=yy<H and 0<=xx<W and op2[yy,xx] and not seen[yy,xx]:seen[yy,xx]=1;q.append((yy,xx))
    if len(comp)<40:
        for y,x in comp:a2[y,x,3]=0
# đổi màu theo dải sáng-tối
SCHEMES={
 'goc':None,
 'do':   dict(body=[(70,18,24),(150,36,40),(205,70,64),(236,140,120)],trim=[(40,22,10),(120,80,24),(200,150,60),(240,205,120)]),
 'tim':  dict(body=[(52,34,70),(110,80,150),(170,140,205),(226,210,240)],trim=[(30,16,40),(80,40,100),(140,80,160),(200,150,215)]),
 'den':  dict(body=[(14,14,20),(34,34,44),(62,62,76),(98,98,114)],trim=[(60,10,14),(140,24,30),(200,50,50),(240,110,100)]),
 'xanhla':dict(body=[(36,60,50),(70,120,96),(130,180,150),(210,232,215)],trim=[(30,40,20),(110,90,40),(180,150,70),(230,205,130)]),
}
S=SCHEMES[scheme]
def ramp(stops,t):
    t=np.clip(t,0,1)*(len(stops)-1);i=np.minimum(t.astype(int),len(stops)-2);f=(t-i)[...,None]
    st=np.array(stops,float);return st[i]*(1-f)+st[i+1]*f
if S:
    op2=a2[...,3]>0
    rr,gg,bb=a2[...,0],a2[...,1],a2[...,2];LL=(np.maximum(np.maximum(rr,gg),bb)+np.minimum(np.minimum(rr,gg),bb))/510
    cm=cream&op2; bm=blue&mass&op2&~cream
    # thân váy: L 0.62..1 → dải body
    a2[cm,:3]=ramp(S['body'],(LL[cm]-0.55)/0.45).astype(int)
    a2[bm,:3]=ramp(S['trim'],LL[bm]/0.9).astype(int)
Image.fromarray(a2.astype(np.uint8),'RGBA').save(out)
print(out,'cut',int(cut.sum()),'orphan',int(orphan.sum()))
