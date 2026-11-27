# Khung HUD sảnh: xóa avatar/chữ/thanh vẽ sẵn trong lòng khung gỗ xích (ảnh chủ game gửi 27/11), giữ viền + xích + bùa + vải + vuốt,
# rồi cắt bớt một dải giữa cho tỉ lệ ~300x124 (cắt đúng bội chu kỳ mắt xích để nối liền), xuất webp nhiều cỡ.
# python3 cong_cu/claude/hud_khung.py [thư_mục_ra]
import sys,numpy as np
from PIL import Image
SRC='/home/user/HoaThan/nguon/master_amgioi/hud_sanh/khung_go_xich_goc.png'
OUT=sys.argv[1] if len(sys.argv)>1 else '/home/user/HoaThan/game/assets/ui/lobby'
a=np.array(Image.open(SRC).convert('RGBA')).astype(float);H,W=a.shape[:2]
r,g,b=a[:,:,0],a[:,:,1],a[:,:,2];mx=np.maximum(np.maximum(r,g),b);mn=np.minimum(np.minimum(r,g),b)
L=.3*r+.59*g+.11*b;sat=np.where(mx>0,(mx-mn)/np.maximum(mx,1),0)
X0,X1,Y0,Y1=238,1903,118,592
yy,xx=np.mgrid[0:H,0:W]
inside=(xx>=X0)&(xx<X1)&(yy>=Y0)&(yy<Y1)
keep=np.zeros((H,W),bool)
keep|=(xx<272)                                   # cột trái: bùa + xích sát mép
keep|=(xx<300)&(yy<200)                          # xích góc trên trái
gold=(r>140)&(g>100)&(b<110)
cream=(L>140)&(sat>0.18)
cloth=((r>110)&(r>1.8*g))|((r>60)&(r>2.2*g)&(xx>1805))
chain=(sat<0.45)&(L>36)&~gold&~cream
R1=(xx>=1690)&(yy<420)
cm=R1&(cloth|chain)
dil=cm.copy()
for dy in range(-7,8):
    for dx in range(-7,8):
        if dx*dx+dy*dy<=49:dil|=np.roll(np.roll(cm,dy,0),dx,1)
dil&=R1&~gold&~cream&~((r>40)&(r>2.0*g)&(r<110)&(yy>270))  # nở mặt nạ xích/vải để giữ viền tối của mắt xích, trừ vệt dải Lực chiến
keep|=dil
keep&=~((xx>=1690)&(xx<1760)&(yy>=240)&(yy<420)&~cloth)  # đuôi 2 vạch vàng
R3=(yy>=572); keep|=R3&chain
keep&=~((xx>=1690)&(xx<1750)&(yy>=150)&(yy<245)&~cloth)  # số '1' của chữ Cấp 1
claw=(L>110)&(sat<0.3)
R2=(xx>=1860)&(yy>=400); keep|=R2&claw
erase=inside&~keep
# lòng khung: gradient tối ấm + bóng trong viền
t=(yy-Y0)/(Y1-Y0)
base=np.stack([22+8*t,17+6*t,15+5*t],-1)
d=np.minimum.reduce([xx-X0,X1-xx,yy-Y0,Y1-yy]).astype(float)
sh=np.clip(d/26,0,1)*0.45+0.55
rng=np.random.default_rng(3);noise=rng.normal(0,1.6,(H,W,1))
fill=np.clip(base*sh[...,None]+noise,0,255)
a[...,:3]=np.where(erase[...,None],fill,a[...,:3]);a[...,3]=np.where(erase,255,a[...,3])
img=Image.fromarray(a.astype('uint8'),'RGBA')
# cắt dải giữa: tìm độ dời k gần 420 sao cho dải xích đáy (y 585..650) khớp nhất
st=np.array(img).astype(float)
def cost(c0,k):
    A=st[585:655,c0:c0+24,:3];B=st[585:655,c0+k:c0+k+24,:3]
    T=st[60:118,c0:c0+24,:3];U=st[60:118,c0+k:c0+k+24,:3]
    return np.abs(A-B).mean()+np.abs(T-U).mean()
best=min(((cost(c0,k),c0,k) for c0 in range(760,980,8) for k in range(380,470,2)),key=lambda q:q[0])
_,c0,k=best;print('cut',c0,k,round(best[0],2))
left=img.crop((0,0,c0+12,H));right=img.crop((c0+k+12,0,W,H))
out=Image.new('RGBA',(left.width+right.width,H));out.paste(left,(0,0));out.paste(right,(left.width,0))
# trộn 24px quanh mối nối cho liền
o=np.array(out).astype(float)
for i in range(24):  # cột c0+i của bên trái trộn dần sang cột tương ứng của bên phải
    w=i/23;o[:,c0-12+i]=st[:,c0-12+i]*(1-w)+st[:,c0+k-12+i]*w
out=Image.fromarray(o.astype('uint8'))
bb=out.getbbox();out=out.crop(bb);print('size',out.size,'interior x',X0-bb[0],X1-k-bb[0],'y',Y0-bb[1],Y1-bb[1])
out.save('/home/user/HoaThan/nguon/master_amgioi/hud_sanh/khung_long_trong.png')
for w in (300,450,600,900):
    h=round(out.height*w/out.width);out.resize((w,h),Image.LANCZOS).save(f'{OUT}/hud_khung_{w}.webp',quality=90,method=6)
    print(w,h)
