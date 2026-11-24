# Đóng sheet VFX Xích Diễm Đao Môn (gói Wuxia, xuất từ Godot bằng nguon/godot_bake/Bake.gd) cho class Đao.
# Dùng: python3 dq_pack.py <thư mục chứa out/07_cleave...> <thư mục ra game/assets/vfx>
import sys,glob,json
import numpy as np
from PIL import Image
src,dst=sys.argv[1],sys.argv[2]
CFG={'dq_cleave':('07_cleave',1,0.25),'dq_triple':('08_triple',2,0.25),'dq_ring':('09_ring',2,0.25)}
spx={}
for name,(sid,step,thr) in CFG.items():
    fs=sorted(glob.glob(f'{src}/{sid}/f*.png'))
    cnt=np.array([int((np.array(Image.open(f).convert('RGBA'))[:,:,3]>8).sum()) for f in fs]);mx=cnt.max()
    act=[i for i,c in enumerate(cnt) if c>0.02*mx]
    a0=act[0];pk=int(cnt.argmax());a1=max(i for i in range(pk,len(fs)) if cnt[i]>=thr*mx)   # cắt đuôi tan rã (ô vuông nhiễu)
    sel=list(range(a0,a1+1,step));ims=[Image.open(fs[i]).convert('RGBA') for i in sel]
    bb=None
    for im in ims:
        a=np.array(im)[:,:,3]>8
        if a.any():
            ys,xs=np.nonzero(a);b=(xs.min(),ys.min(),xs.max()+1,ys.max()+1);bb=b if bb is None else (min(bb[0],b[0]),min(bb[1],b[1]),max(bb[2],b[2]),max(bb[3],b[3]))
    w,h=int(bb[2]-bb[0]),int(bb[3]-bb[1]);n=len(ims);c=min(n,max(1,4000//w) if n>8 else n)
    c=min(c,8) if w<400 else min(c,6)
    rows=(n+c-1)//c;sheet=Image.new('RGBA',(c*w,rows*h),(0,0,0,0))
    for k,im in enumerate(ims):sheet.alpha_composite(im.crop((int(bb[0]),int(bb[1]),int(bb[2]),int(bb[3]))),((k%c)*w,(k//c)*h))
    sheet.save(f'{dst}/{name}.png',optimize=True)
    spx[name]=dict(w=w,h=h,c=c,n=n,px=int(300-bb[0]),py=int(560-bb[1]))
    print(name,'khung',sel[0],'->',sel[-1],'n=',n,'ô',w,h,'sheet',sheet.size,'fps',30//step)
print(json.dumps(spx))
