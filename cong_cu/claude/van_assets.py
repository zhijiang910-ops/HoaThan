"""Chữ VẠN (卍) cho Quyền X, theo phong cách game: pixel 1 px thật (không phóng), nét mảnh 3 px, viền tối mảnh 1 px, màu vàng dịu, tô bóng ít (1 mép sáng, 1 mép tối), quầng rất nhạt. Ra game/assets/vfx/van_vang.png (32x32, vẽ tỉ lệ 1)."""
from PIL import Image,ImageFilter
import numpy as np,os
G=24;m=np.zeros((G,G),bool)
def R(x0,y0,x1,y1):m[y0:y1,x0:x1]=True
R(10,3,13,21);R(3,10,21,13);R(10,3,21,6);R(18,10,21,21);R(3,18,13,21);R(3,3,6,13)
S=32;o=(S-G)//2
mk=np.zeros((S,S),bool);mk[o:o+G,o:o+G]=m
dil=np.array(Image.fromarray((mk*255).astype('uint8')).filter(ImageFilter.MaxFilter(3)))>0
img=Image.new('RGBA',(S,S),(0,0,0,0));px=img.load()
# quầng rất nhạt
halo=np.array(Image.fromarray((mk*255).astype('uint8')).filter(ImageFilter.GaussianBlur(3)),float)/255
for y in range(S):
    for x in range(S):
        a=int(min(1,halo[y,x]*1.6)*46)
        if a>2:px[x,y]=(232,196,110,a)
for y in range(S):
    for x in range(S):
        if dil[y,x] and not mk[y,x]:px[x,y]=(34,26,22,255)           # viền đen mảnh
        elif mk[y,x]:
            up=not mk[y-1,x];lf=not mk[y,x-1];dn=not mk[y+1,x];rt=not mk[y,x+1]
            if up or lf:c=(238,214,142)
            elif dn or rt:c=(158,120,58)
            else:c=(206,168,84)
            px[x,y]=c+(255,)
os.makedirs('game/assets/vfx',exist_ok=True);img.save('game/assets/vfx/van_vang.png',optimize=True);print(img.size)
