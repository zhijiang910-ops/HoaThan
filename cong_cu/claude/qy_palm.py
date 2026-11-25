"""Bàn tay cương khí cho X của Quyền: nhuộm pm_palm (bàn tay Phật vàng, gói Wuxia Kim Cương Tự) sang đỏ chu sa - trắng của Thiên Cương Môn.
Giữ nguyên alpha và hình; ánh xạ độ sáng -> bảng màu. Chạy: python3 cong_cu/claude/qy_palm.py"""
from PIL import Image
import numpy as np
R='/home/user/hoathan/'
im=Image.open(R+'game/assets/vfx/pm_palm.png').convert('RGBA')
a=np.array(im).astype(float)
lum=(a[:,:,0]*0.3+a[:,:,1]*0.59+a[:,:,2]*0.11)/255
stops=[(0,(18,0,8)),(0.25,(110,10,26)),(0.5,(200,40,40)),(0.72,(255,120,90)),(0.88,(255,214,196)),(1,(255,255,255))]
out=np.zeros_like(a)
for ch in range(3):
    xs=[s[0] for s in stops];ys=[s[1][ch] for s in stops]
    out[:,:,ch]=np.interp(np.clip(lum*1.15,0,1),xs,ys)
out[:,:,3]=a[:,:,3]
Image.fromarray(out.astype('uint8')).save(R+'game/assets/vfx/qy_palm.png',optimize=True)
print('ok')
