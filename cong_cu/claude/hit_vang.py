"""VFX va chạm Kiếm đổi sang VÀNG (25/11, chủ game): swqi_vang.png, wx_slash_vang.png = swqi/wx_slash đổi màu theo độ sáng
(lõi trắng kem -> vàng -> cam đồng -> đỏ sẫm ở rìa), giữ alpha. Gốc xanh/tím: swqi.png, wx_slash.png (không bị sửa)."""
import numpy as np
from PIL import Image
OUT='game/assets/vfx/'
stops=[(0,(110,30,10)),(0.25,(205,90,22)),(0.5,(240,160,40)),(0.8,(255,205,80)),(1,(255,236,150))]
def lut(v):
    for i in range(len(stops)-1):
        v0,c0=stops[i];v1,c1=stops[i+1]
        if v<=v1:
            t=(v-v0)/(v1-v0+1e-6);return [c0[k]+(c1[k]-c0[k])*t for k in range(3)]
    return list(stops[-1][1])
for n in ('swqi','wx_slash'):
    a=np.array(Image.open(OUT+n+'.png').convert('RGBA')).astype(float)
    lum=(a[...,:3]*[.3,.59,.11]).sum(2)/255.0
    lum=np.clip(lum*1.0,0,1)
    m=a[...,3]>0
    col=np.zeros(lum.shape+(3,))
    ys,xs=np.nonzero(m)
    for y,x in zip(ys,xs):col[y,x]=lut(lum[y,x])
    a[...,:3]=col
    Image.fromarray(a.clip(0,255).astype(np.uint8),'RGBA').save(OUT+n+'_vang.png');print(n,'ok')
