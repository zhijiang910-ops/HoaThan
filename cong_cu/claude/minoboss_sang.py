# Làm sáng mini-boss: đường cong gamma lên tông giữa + sáng, giữ nguyên viền tối. Gốc: nguon/vfx_goc/<k>_am_truoc_sang.png
import numpy as np
from PIL import Image
G={'nghiethoa':0.80,'thietlao':0.78,'vongxuyenqt':0.88}
for k,g in G.items():
    a=np.array(Image.open(f'nguon/vfx_goc/{k}_am_truoc_sang.png').convert('RGBA')).astype(float)
    rgb=a[...,:3]/255;lum=(rgb*[.3,.59,.11]).sum(2,keepdims=True)
    new=np.power(rgb,g)
    w=np.clip((lum-0.10)/0.12,0,1)  # viền/vùng rất tối giữ nguyên
    out=rgb*(1-w)+new*w
    a[...,:3]=np.clip(out*255+0.5,0,255);a[a[...,3]==0,:3]=0
    Image.fromarray(a.astype(np.uint8),'RGBA').save(f'game/assets/{k}_am.png')
    l=(a[...,:3]*[.3,.59,.11]).sum(2)[a[...,3]>0];print(k,round(l.mean(),1))
