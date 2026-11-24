"""Đổi màu Thiên Xu (tx_in/tx_loop/tx_out) từ kiếm vàng-trắng sang xanh đen mực như cự kiếm Mực Ảnh (24/11). Gốc: nguon/vfx_goc/tx_*_vang.png"""
import numpy as np
from PIL import Image
def ramp(l):
    # l 0..1 -> navy ink ramp, highlight xanh lam sáng
    stops=[(0.0,(6,8,26)),(0.35,(16,26,70)),(0.6,(34,62,140)),(0.82,(96,170,235)),(1.0,(215,240,255))]
    out=np.zeros(l.shape+(3,))
    for (a,ca),(b,cb) in zip(stops,stops[1:]):
        m=(l>=a)&(l<=b);t=((l-a)/(b-a))[m,None]
        out[m]=np.array(ca)*(1-t)+np.array(cb)*t
    return out
for n in ('tx_in','tx_loop','tx_out'):
    im=np.array(Image.open(f'nguon/vfx_goc/{n}_vang.png').convert('RGBA')).astype(float)
    r,g,b,a=im[...,0],im[...,1],im[...,2],im[...,3]
    mx=im[...,:3].max(-1);mn=im[...,:3].min(-1);sat=(mx-mn)/np.maximum(mx,1)
    lum=(0.3*r+0.59*g+0.11*b)/255
    gold=(r>b+25)&(sat>0.28)             # chuôi/hộ thủ vàng -> sắt tối viền đồng nhạt
    col=ramp(np.clip(lum,0,1)**4.6)
    iron=np.stack([28+70*lum,26+60*lum,46+80*lum],-1)
    col=np.where(gold[...,None],iron,col)
    res=np.dstack([col,a]);Image.fromarray(res.astype(np.uint8),'RGBA').save(f'game/assets/vfx/{n}.png',optimize=True)
    print(n,'ok')
