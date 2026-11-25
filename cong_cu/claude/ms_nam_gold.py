# Đồng bộ MÀU VÀNG (đai, viền áo, bùa) của Mao Sơn nam: mọi pixel vàng ở khung đánh (hàng y=256 ô 0-23, hàng y=0 ô 14, 15) khớp theo hạng độ sáng với bảng vàng của khung đứng (hàng 0 ô 0-3). Không PixelLab. Chạy SAU fix_talisman.py và ms_nam_dash_mau.py.
from PIL import Image
import numpy as np
P='game/assets/hero_nam_ms.png';im=Image.open(P).convert('RGBA');a=np.array(im);cw,ch=160,128
lum=lambda p:p[:,0]*.3+p[:,1]*.59+p[:,2]*.11
def gold(p):
    p=p.astype(int);mx=p[:,:3].max(1);mn=p[:,:3].min(1)
    return ((mx-mn)/np.maximum(mx,1)>0.45)&(p[:,0]>p[:,2]+60)&(p[:,1]>p[:,2]+30)&(p[:,0]>150)&(p[:,3]>0)
ref=[]
for c in range(4):
    cell=a[0:ch,c*cw:(c+1)*cw];px=cell.reshape(-1,4);ref.append(px[gold(px)][:,:3])
ref=np.concatenate(ref).astype(float);ref=ref[np.argsort(lum(ref))]
print('bảng vàng chuẩn',len(ref),'pixel; sáng nhất',ref[-1].astype(int).tolist(),'tối nhất',ref[0].astype(int).tolist())
cells=[(c*cw,256) for c in range(24)]+[(14*cw,0),(15*cw,0)]
for x,y in cells:
    cell=a[y:y+ch,x:x+cw];px=cell.reshape(-1,4);m=gold(px)
    if m.sum()==0:continue
    v=px[m][:,:3].astype(float);l=lum(v);o=np.argsort(l,kind='stable');r=np.empty(len(l));r[o]=np.arange(len(l))/max(len(l)-1,1)
    new=ref[np.minimum((r*(len(ref)-1)).astype(int),len(ref)-1)].astype('uint8')
    px[m,:3]=new;cell[:]=px.reshape(ch,cw,4)
Image.fromarray(a).save(P)
