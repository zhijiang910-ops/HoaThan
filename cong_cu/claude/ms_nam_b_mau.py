# Khớp màu thân dưới 3 khung giữa đòn B của Mao Sơn nam (ô x=1440,1600,1760 y=256) theo khung 7,8 (quần xám đậm, ủng đen). Không PixelLab.
from PIL import Image
import numpy as np
P='game/assets/hero_nam_ms.png';SRC='nguon/vfx_goc/hero_nam_ms_truoc_khi_chinh_mau.png'
im=Image.open(SRC).convert('RGBA');a=np.array(im);cw,ch,Y0,SPLIT,BOOT=160,128,256,72,108
lum=lambda r:r[...,0]*.3+r[...,1]*.59+r[...,2]*.11
def sat(r):
    r=r.astype(float);return (r.max(1)-r.min(1))/np.maximum(r.max(1),1)
def gold(r):return (sat(r)>0.4)&(r[:,0].astype(int)>r[:,2].astype(int)+40)
def reg(c,lo,hi):
    cell=a[Y0:Y0+ch,c*cw:(c+1)*cw];m=cell[:,:,3]>0;m[:lo]=False;m[hi:]=False;return cell,m
refl=[];refb=[]
for c in (7,8):
    cell,m=reg(c,SPLIT,BOOT);px=cell[m][:,:3];refl.append(px[~gold(px)])
    cell,m=reg(c,BOOT,ch);px=cell[m][:,:3];refb.append(px[~gold(px)])
refl=np.concatenate(refl);refl=refl[np.argsort(lum(refl.astype(float)))]
refb=np.concatenate(refb);refb=refb[np.argsort(lum(refb.astype(float)))]
def remap(px,ref):
    l=lum(px.astype(float));o=np.argsort(l,kind='stable');r=np.empty(len(l));r[o]=np.arange(len(l))/max(len(l)-1,1)
    return ref[np.minimum((r*(len(ref)-1)).astype(int),len(ref)-1)]
for c in (0,1,2,3,4,5,9,10,11,12,13,14,18,19,20,21,22):
    # thân dưới (trừ ủng): pixel không vàng -> khớp theo bảng quần/vạt áo; vàng (viền áo, đai) giữ nguyên
    cell,m=reg(c,SPLIT,BOOT);idx=np.where(m);px=cell[m][:,:3];g=gold(px)
    new=px.copy();new[~g]=remap(px[~g],refl);cell[idx[0],idx[1],:3]=new
    # ủng: mọi pixel (cả vàng) -> bảng ủng đen
    cell,m=reg(c,BOOT,ch);idx=np.where(m);px=cell[m][:,:3];cell[idx[0],idx[1],:3]=remap(px,refb)
Image.fromarray(a).save(P)
old=Image.open(SRC).convert('RGBA');new=Image.open(P).convert('RGBA');cols=[0,1,12,13,18,19,22];S=2
out=Image.new('RGBA',(len(cols)*cw*S,ch*S*2+10),(70,70,70,255))
for i,c in enumerate(cols):
    for j,s in enumerate((old,new)):
        out.alpha_composite(s.crop((c*cw,Y0,(c+1)*cw,Y0+ch)).resize((cw*S,ch*S),Image.NEAREST),(i*cw*S,j*(ch*S+10)))
out.save('nguon/tham_chieu/maoson_nam_b_truoc_sau.png')
