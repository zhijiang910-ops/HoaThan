"""Ảnh nền TẠM cho giữa màn tạo nhân vật (25/11): đường Hoàng Tuyền dẫn tới Quỷ Môn Quan dưới trăng đỏ, hoa bỉ ngạn hai bên, sương.
Ghép bằng code từ vật có sẵn (Dp_quanmon, Dp_hoa1/2, Dp_loncong, Dp_caychet, Dp_xuong, nền g_hoangtuyen). Vẽ ở 512x576 rồi phóng x2 NEAREST => 1024x1152 (khối pixel 2 px như map).
Chủ game có ảnh thật thì chỉ cần thay game/assets/ui/nen_tao_nhan_vat.jpg. Chạy: python3 cong_cu/claude/nen_tao_nv.py"""
import numpy as np,random,math
from PIL import Image,ImageDraw
random.seed(7);np.random.seed(7)
W,H=512,576;HZ=300;A='game/assets/map/'
def load(n):return Image.open(A+n).convert('RGBA')
def put(base,im,x,y,sc=1.0,dark=1.0,alpha=1.0):
    w,h=max(1,round(im.width*sc)),max(1,round(im.height*sc));r=im.resize((w,h),Image.NEAREST if sc>=1 else Image.BOX)
    a=np.array(r).astype(float);a[...,:3]*=dark;a[...,3]*=alpha;r=Image.fromarray(a.clip(0,255).astype('uint8'),'RGBA')
    base.alpha_composite(r,(int(x-w/2),int(y-h)))
# ---- trời: gradient tím đỏ + sao
sky=np.zeros((HZ,W,3));
for y in range(HZ):
    t=y/HZ;sky[y,:]=np.array([10,4,12])*(1-t)+np.array([84,22,26])*t
img=Image.new('RGBA',(W,H),(0,0,0,255));img.paste(Image.fromarray(sky.astype('uint8'),'RGB'),(0,0))
d=ImageDraw.Draw(img)
for _ in range(70):
    x,y=random.randrange(W),random.randrange(0,190);c=random.choice([(200,190,170),(150,140,130),(230,210,180)]);d.point((x,y),c)
# ---- trăng đỏ: quầng dither + đĩa + vân
cx,cy,R=256,150,58
yy,xx=np.mgrid[0:H,0:W];dist=np.hypot(xx-cx,yy-cy)
arr=np.array(img).astype(float)
glow=np.clip(1-(dist-R)/150,0,1)**2;bay=((xx+yy)%2==0)
for k,c in enumerate([(150,40,36),(190,52,40)]):
    pass
arr[...,0]+=glow*120;arr[...,1]+=glow*18;arr[...,2]+=glow*10
disk=dist<=R;shade=np.clip((cy-yy)/R*0.5+0.5,0,1)
col=np.zeros((H,W,3));col[...,0]=170+60*shade;col[...,1]=34+34*shade;col[...,2]=30+24*shade
arr[disk,:3]=col[disk]
for (mx,my,mr) in [(236,134,11),(278,168,15),(262,128,7),(228,172,9)]:
    m=np.hypot(xx-mx,yy-my)<=mr;arr[m&disk,:3]*=0.80
rim=(dist>R-2)&(dist<=R);arr[rim,:3]=(230,110,70)
img=Image.fromarray(arr[...,:3].clip(0,255).astype('uint8'),'RGB').convert('RGBA');d=ImageDraw.Draw(img)
# ---- núi xa (hai lớp)
def ridge(base,amp,seed,col):
    random.seed(seed);pts=[(0,HZ)];x=0;y0=base
    while x<=W:
        y0=base-amp*(0.5+0.5*math.sin(x*0.021+seed)+0.35*math.sin(x*0.067+seed*2))*random.uniform(0.75,1.1);pts.append((x,y0));x+=random.randint(7,16)
    pts+=[(W,HZ)];d.polygon(pts,fill=col)
ridge(262,62,1,(34,12,22,255));ridge(280,46,5,(18,6,14,255))
# ---- mặt đất: chiếu phối cảnh nền g_hoangtuyen, đường ở giữa
tex=np.array(Image.open(A+'g_hoangtuyen.jpg').convert('RGB')).astype(float);TH,TW=tex.shape[:2]
ground=np.zeros((H-HZ,W,3))
for j in range(H-HZ):
    y=HZ+j;s=(j+4)/(H-HZ);z=1/(s+0.03);v=int(z*38)%TH
    us=((np.arange(W)-256)*z*0.22).astype(int)%TW;row=tex[v,us]
    road=np.abs(np.arange(W)-256)<(14+s*150)
    k=np.where(road,0.62,0.30)*(0.35+0.65*s);edge=np.clip((np.abs(np.arange(W)-256)-(14+s*150))/10,-1,1)
    row=row*k[:,None]
    ground[j]=row
ground[...,0]*=1.05;ground[...,2]*=0.85
g=Image.fromarray(ground.clip(0,255).astype('uint8'),'RGB').convert('RGBA');img.alpha_composite(g,(0,HZ))
# ---- vật: cây chết xa, cổng, bóng cổng
quan=load('Dp_quanmon.png');hoa1=load('Dp_hoa1.png');hoa2=load('Dp_hoa2.png');lon=load('Dp_loncong.png');cay=load('Dp_caychet.png');xuong=load('Dp_xuong.png')
put(img,cay,70,HZ+34,0.62,0.55);put(img,cay,450,HZ+30,0.55,0.5)
sh=Image.new('RGBA',(W,H),(0,0,0,0));ImageDraw.Draw(sh).ellipse((256-110,HZ-4,256+110,HZ+14),fill=(0,0,0,150));img.alpha_composite(sh)
put(img,quan,256,HZ+6,0.92,0.95)
# ---- hoa bỉ ngạn hai bên đường theo phối cảnh (xa nhỏ, gần to), lồng đèn
def road_half(y):return 14+((y-HZ)/(H-HZ))*150
rows=[(322,0.22),(334,0.28),(350,0.36),(370,0.46),(396,0.60),(430,0.78),(476,1.0),(536,1.25)]
for y,sc in rows:
    for side in (-1,1):
        for k in range(2 if sc<0.7 else 3):
            ox=road_half(y)+10*sc+k*34*sc+random.randint(0,8)
            put(img,random.choice([hoa1,hoa2]),256+side*ox,y,sc*(1.15 if k else 1.0),0.50+0.45*sc/1.25)
for y,sc in [(420,0.62),(520,0.95)]:
    for side in (-1,1):put(img,lon,256+side*(road_half(y)+30*sc),y,sc,0.85+0.1*sc)
put(img,xuong,70,566,0.8,0.55);put(img,xuong,452,560,0.7,0.5)
# ---- đèn lồng toả sáng + sương + hạt
arr=np.array(img).astype(float)
for y,sc in [(420,0.62),(520,0.95)]:
    for side in (-1,1):
        lx,ly=256+side*(road_half(y)+30*sc),y-lon.height*sc*0.78;dd=np.hypot(xx-lx,yy-ly);gl=np.clip(1-dd/(70*sc+18),0,1)**2
        arr[...,0]+=gl*130;arr[...,1]+=gl*86;arr[...,2]+=gl*30
hz=np.exp(-((yy-(HZ+8))/26.0)**2);arr[...,0]+=hz*60;arr[...,1]+=hz*26;arr[...,2]+=hz*34   # quầng chân trời đỏ
for cy_,amp in [(HZ+40,.16),(HZ+110,.10),(H-60,.10)]:
    fg=np.exp(-((yy-cy_)/24.0)**2)*amp*(0.6+0.4*np.sin(xx*0.03+cy_));arr[...,:3]+=fg[...,None]*np.array([150,110,120])
img=Image.fromarray(arr[...,:3].clip(0,255).astype('uint8'),'RGB').convert('RGBA');d=ImageDraw.Draw(img)
for _ in range(140):
    x,y=random.randrange(W),random.randrange(HZ-30,H);c=random.choice([(200,60,60),(255,120,80),(170,170,190)]);d.point((x,y),c+(random.randint(90,200),))
# ---- vignette mạnh ở rìa để chữ/UI không chói và cắt cover không lộ mép
arr=np.array(img.convert('RGB')).astype(float)
v=np.clip(1-((np.abs(xx-W/2)/(W/2))**2.2*0.55+(np.abs(yy-H*0.52)/(H/2))**2.4*0.60),0.12,1)
arr*=v[...,None]
out=Image.fromarray(arr.clip(0,255).astype('uint8'),'RGB').resize((W*2,H*2),Image.NEAREST)
out.save('game/assets/ui/nen_tao_nhan_vat.jpg',quality=90,optimize=True);print(out.size)
