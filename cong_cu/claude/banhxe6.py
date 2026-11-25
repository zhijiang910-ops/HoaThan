"""Sprite BÁNH XE LỤC ĐẠO LUÂN HỒI (25/11) cho sàn tầng 18 (Luân Hồi Đài): đĩa dẹt phối cảnh, 6 phần = 6 cõi (thiên, a-tu-la, nhân, súc sinh, ngạ quỷ, địa ngục), mỗi phần một biểu tượng, tâm = heo, gà, rắn (tam độc), vành đá có rune tím.
Vẽ bằng code (PIL/numpy, không PixelLab). Ra game/assets/map/Dp_banhxe.png 360x230 (neo giữa-đáy, vật `flat` như Dp_daitron). Chạy: python3 cong_cu/claude/banhxe6.py"""
import numpy as np,math
from PIL import Image
W,H=360,230;CX,CY=180,104;RX,RY=170,98;T=14
img=np.zeros((H,W,4),np.uint8)
def put(x,y,c,a=255):
    if 0<=x<W and 0<=y<H:img[y,x]=(c[0],c[1],c[2],a)
SEC=[('thien',(214,186,104)),('atula',(168,48,52)),('nhan',(52,142,108)),('suc',(150,98,50)),('nga',(112,96,136)),('diangu',(58,16,18))]
GLY={'thien':["..###..",".#####.","#######","#######",".#####.","...#...","..###.."],
 'atula':["#.....#",".#...#.","..#.#..","...#...","..#.#..",".#...#.","#.....#"],
 'nhan':["..###..","..###..",".#####.","#.###.#","..###..",".#...#.","#.....#"],
 'suc':["#.#.#.#",".#.#.#.","..###..",".#####.","#######","#######",".#####."],
 'nga':[".#####.","#######","#.###.#","#######",".#####.",".#.#.#.","......."],
 'diangu':["...#...","..###..","..###..",".#####.",".#####.","#######",".#####."]}
# thân (độ dày) dưới đĩa
yy,xx=np.mgrid[0:H,0:W]
for dy in range(T,0,-1):
    nx=(xx-CX)/RX;ny=(yy-dy-CY)/RY;m=nx*nx+ny*ny<=1
    k=0.35+0.4*(1-dy/T);col=np.array([54,42,76])*k
    for y,x in zip(*np.where(m)):img[y,x]=(col[0],col[1],col[2],255)
# mặt đĩa
nx=(xx-CX)/RX;ny=(yy-CY)/RY;r=np.hypot(nx,ny);ang=np.arctan2(ny,nx)
top=r<=1
sector=((ang+math.pi)/(2*math.pi)*6).astype(int)%6
rng=np.random.RandomState(3)
for y,x in zip(*np.where(top)):
    rr=r[y,x];a=ang[y,x]
    if rr<0.20:c=(22,14,34)
    elif rr<0.86:
        name,base=SEC[sector[y,x]];sh=0.80+0.30*(1-rr)+rng.uniform(-.04,.04)
        if (x//3+y//3)%2==0:sh*=0.94
        c=tuple(int(min(255,v*sh)) for v in base)
        if name=='diangu':
            fl=0.52+0.10*math.sin(x*0.45+y*0.1)+0.06*math.sin(x*1.1)
            c=(30,8,10) if rr<fl*0.8 else (96,22,16) if rr<fl else (190,70,26) if rr<fl+0.07 else (236,128,44) if rr<fl+0.12 else (110,28,20)
        # nan hoa: đường thang phân cõi
        sa=(a+math.pi)/(2*math.pi)*6;dsp=abs(sa-round(sa))*rr*RX*2*math.pi/6
        if dsp<2.0:c=(24,16,30)
        elif dsp<3.2:c=tuple(int(v*0.65) for v in c)
        if rr>0.80:c=tuple(int(v*0.78) for v in c)
    else:
        c=(60,48,86) if ((x//5+y//4)%3) else (48,38,70)
        if rr>0.975:c=(204,174,92)
        elif rr<0.875:c=(198,168,88)
    put(x,y,c)
# biểu tượng mỗi cõi (phóng x2, viền tối)
for i,(name,base) in enumerate(SEC):
    ang_c=(i+0.5)/6*2*math.pi-math.pi;gx=int(CX+math.cos(ang_c)*RX*0.54);gy=int(CY+math.sin(ang_c)*RY*0.54)
    g=GLY[name];light={'thien':(255,250,222),'atula':(255,176,168),'nhan':(176,255,224),'suc':(255,206,136),'nga':(234,220,255),'diangu':(255,176,80)}[name]
    for pas,col in ((1,(16,10,22)),(0,light)):
        for j,row in enumerate(g):
            for k,ch in enumerate(row):
                if ch=='#':
                    for dy in range(2):
                        for dx in range(2):put(gx-7+k*2+dx+pas,gy-7+j*2+dy+pas,col)
# tâm: tam độc (heo hồng, gà đỏ, rắn lục) chạy vòng quanh hạt trắng
for yy_ in range(-22,23):
    for xx_ in range(-22,23):
        if (xx_/22)**2+(yy_/13)**2<=1 and (xx_/22)**2+(yy_/13)**2>0.82:put(CX+xx_,CY+yy_,(206,178,96))
for k,(col) in enumerate([(236,146,168),(222,58,46),(66,176,92)]):
    a=k*2*math.pi/3-math.pi/2;bx=int(CX+math.cos(a)*11);by=int(CY+math.sin(a)*6)
    for dy in range(-3,4):
        for dx in range(-4,5):
            if (dx/4)**2+(dy/3)**2<=1:put(bx+dx,by+dy,col)
for dy in range(-2,3):
    for dx in range(-3,4):
        if (dx/3)**2+(dy/2)**2<=1:put(CX+dx,CY+dy,(236,236,255))
# rune tím trên vành
for k in range(24):
    a=k*2*math.pi/24;rx=int(CX+math.cos(a)*RX*0.93);ry=int(CY+math.sin(a)*RY*0.93)
    for dx,dy in ((0,0),(1,0),(0,1),(1,1)):put(rx+dx,ry+dy,(176,132,255))
Image.fromarray(img,'RGBA').save('game/assets/map/Dp_banhxe.png');print('ok',img.shape)
