"""Sảnh 28/11: tách icon thanh menu dưới và icon popup Nhân Vật từ 3 ảnh chủ game (nguon/master_amgioi/sanh_menu/anh{1,2,3}_goc.png).
Ảnh 1 (túi, lầu): xóa viền sáng/trắng ngoài hình (điểm mờ sáng ở mép), giữ chi tiết sáng bên trong. Ảnh 2, 3: giữ alpha gốc.
Mỗi icon cắt sát lề alpha, đặt giữa khung vuông theo cạnh dài, thu 160 px (premultiplied). Chạy: python3 cong_cu/claude/sanh_menu_build.py"""
import numpy as np
from PIL import Image
S='nguon/master_amgioi/sanh_menu/';O='game/assets/ui/lobby/'
def runs(v):
    r=[];s=None
    for i,x in enumerate(v):
        if x and s is None:s=i
        if not x and s is not None:r.append((s,i));s=None
    if s is not None:r.append((s,len(v)))
    return [(s,e) for s,e in r if e-s>8]
def down(a,w):
    a=a.astype(float);al=a[...,3:]/255;a[...,:3]*=al
    p=Image.fromarray(np.clip(a,0,255).astype(np.uint8),'RGBA').resize((w,w),Image.LANCZOS);b=np.array(p).astype(float)
    al=b[...,3:]/255;b[...,:3]=np.where(al>0,b[...,:3]/np.maximum(al,1e-3),0)
    return Image.fromarray(np.clip(b,0,255).astype(np.uint8),'RGBA')
def defringe(c):
    # điểm mép (có điểm trong suốt cạnh bên trong 2 px) mà sáng gần trắng, ít màu => là viền nền trắng: bỏ
    al=c[...,3];tr=al<16;near=np.zeros_like(tr)
    for dy in (-2,-1,0,1,2):
        for dx in (-2,-1,0,1,2):near|=np.roll(np.roll(tr,dy,0),dx,1)
    L=c[...,:3].mean(-1);sat=c[...,:3].max(-1)-c[...,:3].min(-1)
    kill=near&(L>200)&(sat<40)&(al>0);c=c.copy();c[kill,3]=0;return c,int(kill.sum())
for f,names,fix in [('anh1',[None,'nv_tui','nv_lau',None],1),('anh2',['nv_ao','nv_caothi','nv_banghoi'],0),('anh3',['nv_kynang','nv_luyendan','nv_luyenkhi'],0)]:
    A=np.array(Image.open(S+f+'_goc.png').convert('RGBA'));cols=runs((A[...,3]>16).sum(0)>2)
    for n,(c0,c1) in zip(names,cols):
        if not n:continue
        c=A[:,c0:c1]
        if fix:c,k=defringe(c);print(n,'bỏ điểm viền sáng',k)
        m=c[...,3]>8;ys,xs=np.where(m);c=c[ys.min():ys.max()+1,xs.min():xs.max()+1];h,w=c.shape[:2];s=max(h,w)
        sq=np.zeros((s,s,4),np.uint8);sq[(s-h)//2:(s-h)//2+h,(s-w)//2:(s-w)//2+w]=c
        down(sq,160).save(O+n+'.webp',quality=90,method=6);print(n,w,h)
