# Khớp màu thân dưới 2 khung lướt Q (hàng y=0, cột 14 và 15) của Mao Sơn nam theo khung 7, 8 hàng y=256. Không PixelLab. Chạy SAU ms_nam_b_mau.py.
from PIL import Image
import numpy as np
P='game/assets/hero_nam_ms.png'
a=np.array(Image.open(P).convert('RGBA'));cw,ch,SPLIT,BOOT=160,128,72,108
lum=lambda r:r[...,0]*.3+r[...,1]*.59+r[...,2]*.11
def sat(r):
    r=r.astype(float);return (r.max(1)-r.min(1))/np.maximum(r.max(1),1)
def gold(r):return (sat(r)>0.4)&(r[:,0].astype(int)>r[:,2].astype(int)+40)
def reg(x,y,lo,hi):
    cell=a[y:y+ch,x:x+cw];m=cell[:,:,3]>0;m[:lo]=False;m[hi:]=False;return cell,m
refl=[];refb=[]
for c in (7,8):
    cell,m=reg(c*cw,256,SPLIT,BOOT);px=cell[m][:,:3];refl.append(px[~gold(px)])
    cell,m=reg(c*cw,256,BOOT,ch);px=cell[m][:,:3];refb.append(px[~gold(px)])
refl=np.concatenate(refl);refl=refl[np.argsort(lum(refl.astype(float)))]
refb=np.concatenate(refb);refb=refb[np.argsort(lum(refb.astype(float)))]
def remap(px,ref):
    l=lum(px.astype(float));o=np.argsort(l,kind='stable');r=np.empty(len(l));r[o]=np.arange(len(l))/max(len(l)-1,1)
    return ref[np.minimum((r*(len(ref)-1)).astype(int),len(ref)-1)]
for c in (14,15):
    cell,m=reg(c*cw,0,SPLIT,BOOT);idx=np.where(m);px=cell[m][:,:3];g=gold(px);new=px.copy();new[~g]=remap(px[~g],refl);cell[idx[0],idx[1],:3]=new
    cell,m=reg(c*cw,0,BOOT,ch);idx=np.where(m);px=cell[m][:,:3];cell[idx[0],idx[1],:3]=remap(px,refb)
Image.fromarray(a).save(P)
