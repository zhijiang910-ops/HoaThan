"""Chữ VẠN (卍) vàng cho Quyền X: lưới 48 px phóng NEAREST x2 (khối 2x2), viền nâu sẫm, thân vàng có sáng trên-trái, quầng sáng mờ nền. Ra game/assets/vfx/van_vang.png (128x128)."""
from PIL import Image,ImageFilter,ImageChops
import numpy as np,os
G=48;m=np.zeros((G,G),bool)
def R(x0,y0,x1,y1):m[y0:y1,x0:x1]=True
R(21,6,27,42);R(6,21,42,27);R(21,6,42,12);R(36,21,42,42);R(6,36,27,42);R(6,6,12,27)
mask=Image.fromarray((m*255).astype('uint8'))
dil=mask.filter(ImageFilter.MaxFilter(3))
out=Image.new('RGBA',(G,G),(0,0,0,0));px=out.load();mk=np.array(mask)>0;dk=np.array(dil)>0
for y in range(G):
    for x in range(G):
        if dk[y,x] and not mk[y,x]:px[x,y]=(70,38,10,255)
        elif mk[y,x]:
            t=(x+y)/(2*G);edge=(not mk[y-1,x] or not mk[y,x-1]) if x>0 and y>0 else True
            if edge:c=(255,238,170)
            elif t<0.38:c=(255,214,96)
            elif t<0.62:c=(236,176,52)
            else:c=(196,126,30)
            px[x,y]=c+(255,)
big=out.resize((G*2,G*2),Image.NEAREST)
S=128;can=Image.new('RGBA',(S,S),(0,0,0,0))
glow=Image.new('RGBA',(S,S),(0,0,0,0));ga=np.zeros((S,S),'float32');ys,xs=np.mgrid[0:S,0:S];d=np.hypot(xs-S/2,ys-S/2)
ga=np.clip(1-d/(S*0.5),0,1)**2*110;glow=Image.fromarray(np.dstack([np.full((S,S),255),np.full((S,S),200),np.full((S,S),80),ga]).astype('uint8'),'RGBA')
can.alpha_composite(glow);can.alpha_composite(big,((S-G*2)//2,(S-G*2)//2))
os.makedirs('game/assets/vfx',exist_ok=True);can.save('game/assets/vfx/van_vang.png',optimize=True);print(can.size)
