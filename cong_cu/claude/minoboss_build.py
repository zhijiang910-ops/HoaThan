# Xử lý ảnh mini-boss ChatGPT: cắt bbox, alpha cứng, bỏ viền rác, thu BOX về cao H, lượng tử hóa màu.
import sys
from PIL import Image
import numpy as np
D='nguon/master_amgioi/minoboss_chatgpt/'
H={'nghiethoa':140,'thietlao':140,'vongxuyenqt':140,'dethinh':150}
for k,h in H.items():
    im=Image.open(D+k+'_goc.png').convert('RGBA');a=np.array(im)
    m=a[...,3]>128
    # bỏ nền đen gần như tuyệt đối ở rìa trong suốt
    a[...,3]=np.where(m,255,0);im=Image.fromarray(a);im=im.crop(im.getbbox())
    w=round(im.width*h/im.height)
    p=im.convert('RGBa').resize((w,h),Image.BOX).convert('RGBA')
    b=np.array(p);b[...,3]=np.where(b[...,3]>110,255,0)
    q=Image.fromarray(b).convert('RGB').quantize(72,dither=Image.NONE).convert('RGB');b2=np.array(q);o=np.dstack([b2,b[...,3]])
    o[o[...,3]==0,:3]=0
    Image.fromarray(o,'RGBA').save(D+k+'_thu.png');print(k,w,h)
