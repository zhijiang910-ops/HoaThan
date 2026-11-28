"""Sảnh 28/11: tách 3 khung biển (Xuất Trận, Thần Giáng Đàn, Quỷ Môn Quan) và 3 icon tiền tệ từ ảnh chủ game.
Chạy: python3 cong_cu/claude/sanh_bien_build.py"""
import numpy as np, json
from PIL import Image
S='nguon/master_amgioi/sanh_bien/';O='game/assets/ui/lobby/'
def runs(v):
    r=[];s=None
    for i,x in enumerate(v):
        if x and s is None:s=i
        if not x and s is not None:r.append((s,i));s=None
    if s is not None:r.append((s,len(v)))
    return [(s,e) for s,e in r if e-s>5]
def bbox(a):
    m=a[...,3]>8;ys,xs=np.where(m);return xs.min(),ys.min(),xs.max()+1,ys.max()+1
def down(im,w):
    # thu nhỏ premultiplied cho mép alpha sạch
    a=np.array(im).astype(float);al=a[...,3:]/255;a[...,:3]*=al
    p=Image.fromarray(np.clip(a,0,255).astype(np.uint8),'RGBA')
    h=round(im.height*w/im.width);p=p.resize((w,h),Image.LANCZOS);b=np.array(p).astype(float)
    al=b[...,3:]/255;b[...,:3]=np.where(al>0,b[...,:3]/np.maximum(al,1e-3),0)
    return Image.fromarray(np.clip(b,0,255).astype(np.uint8),'RGBA')
info={}
RATIO={'xuattran':148/38,'thangiang':192/39,'quymon':230/42}
LR={'xuattran':(330,120),'thangiang':(330,120),'quymon':(330,360)}
im=Image.open(S+'khung_3_bien_goc.png').convert('RGBA');A=np.array(im)
rows=runs((A[...,3]>16).sum(1)>3)
for name,(y0,y1) in zip(['xuattran','thangiang','quymon'],rows):
    c=A[y0:y1];x0,yy0,x1,yy1=bbox(c);c=c[yy0:yy1,x0:x1]
    # lòng khung: vùng tối gần như đen ở hàng giữa
    mid=c[c.shape[0]//2];L=mid[...,:3].mean(-1);dark=(L<40)&(mid[...,3]>200)
    xs=np.where(dark)[0];col=c[:,c.shape[1]//2];Lc=col[...,:3].mean(-1);dk=np.where((Lc<40)&(col[...,3]>200))[0]
    info[name]={'w':c.shape[1],'h':c.shape[0],'in':[int(xs.min()),int(dk.min()),int(xs.max()),int(dk.max())]}
    # rút ngắn thân gỗ giữa cho đúng tỉ lệ chủ game ghi (148x38, 192x39, 230x42): cắt bỏ một đoạn giữa, chọn chỗ nối có 2 cột giống nhau nhất
    H,W=c.shape[:2];tw=int(round(H*RATIO[name]));D=W-tw
    lo,hi=LR[name];best=None
    for s0 in range(lo,W-hi-D):
        d=np.abs(c[:,s0-1].astype(int)-c[:,s0+D].astype(int)).sum()
        if best is None or d<best[0]:best=(d,s0)
    s0=best[1];c=np.concatenate([c[:,:s0],c[:,s0+D:]],1);info[name]['cut']=[int(s0),int(D)];info[name]['w2']=c.shape[1]
    out=down(Image.fromarray(c,'RGBA'),640);out.save(O+'bien_'+name+'.webp',quality=90,method=6)
for f,names in [('xu_linhhon_goc',['dongte','linhhon']),('bo_ba_tien_te_goc',[None,'ngoctt',None])]:
    B=np.array(Image.open(S+f+'.png').convert('RGBA'));cols=runs((B[...,3]>16).sum(0)>2)
    for n,(c0,c1) in zip(names,cols):
        if not n:continue
        c=B[:,c0:c1];x0,y0,x1,y1=bbox(c);c=c[y0:y1,x0:x1];h,w=c.shape[:2];s=max(h,w)
        sq=np.zeros((s,s,4),np.uint8);sq[(s-h)//2:(s-h)//2+h,(s-w)//2:(s-w)//2+w]=c
        down(Image.fromarray(sq,'RGBA'),96).save(O+'tt_'+n+'.png')
print(json.dumps(info))
