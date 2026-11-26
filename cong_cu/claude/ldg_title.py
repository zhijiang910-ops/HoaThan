# Dựng tiêu đề màn chờ: "Khử Tà Diệt Ma" thư pháp ngà cũ + con dấu đỏ 驅邪 -> PNG trong suốt.
# Font: Charmonman Bold (có đủ dấu tiếng Việt), Yuji Boku (chữ Hán phồn thể cho con dấu). Tải font từ github google/fonts vào thư mục FONTS.
import sys,random
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageChops
import numpy as np
FONTS=sys.argv[1];OUT=sys.argv[2]
random.seed(7);np.random.seed(7)
T='Khử Tà Diệt Ma';S=2  # 2x để nét trên màn 3x
ft=ImageFont.truetype(FONTS+'/Charmonman-Bold.ttf',150*S//2*1)
W,H=1500,330
mask=Image.new('L',(W,H),0);d=ImageDraw.Draw(mask)
x=40
for ch in T:
    d.text((x,60),ch,font=ft,fill=255);x+=int(d.textlength(ch,font=ft))+(10 if ch!=' ' else 22)
bb=mask.getbbox();print('bbox chữ',bb)
# tô màu ngà cũ: dọc từ ngà sáng xuống vàng nâu, thêm vân loang
arr=np.zeros((H,W,4),np.uint8)
yy=np.linspace(0,1,H)[:,None]
top=np.array([244,236,212]);bot=np.array([196,176,128])
col=(top[None,None,:]*(1-yy[...,None])+bot[None,None,:]*yy[...,None])
noise=np.random.rand(H//6+1,W//6+1);noise=np.array(Image.fromarray((noise*255).astype(np.uint8)).resize((W,H),Image.BICUBIC))/255.0
col=col*(0.86+0.18*noise[...,None])
arr[...,:3]=np.clip(col,0,255).astype(np.uint8)
m=np.array(mask).astype(np.float32)/255
# lốm đốm mất mực nhẹ
spk=(np.random.rand(H,W)<0.012).astype(np.float32);spk=np.array(Image.fromarray((spk*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))/255
m=m*(1-0.0*spk)
arr[...,3]=(m*255).astype(np.uint8)
txt=Image.fromarray(arr,'RGBA')
# viền tối mảnh quanh chữ
edge=mask.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(1.2))
shadow=Image.new('RGBA',(W,H),(20,10,8,0));shadow.putalpha(edge.point(lambda v:int(v*0.85)))
out=Image.alpha_composite(shadow,txt)
# con dấu đỏ 驅邪
sz=150
seal=Image.new('RGBA',(sz,sz),(0,0,0,0));sd=ImageDraw.Draw(seal)
sd.rounded_rectangle((4,4,sz-5,sz-5),radius=10,fill=(168,28,34,255))
sd.rounded_rectangle((12,12,sz-13,sz-13),radius=6,outline=(110,14,20,255),width=3)
fj=ImageFont.truetype(FONTS+'/YujiBoku-Regular.ttf',74)
for i,ch in enumerate('驅邪'):
    bx=fj.getbbox(ch);w=bx[2]-bx[0]
    sd.text((sz//2-w//2-bx[0],8+i*68-bx[1]+4),ch,font=fj,fill=(244,226,200,255))
# bào mòn mép + vân
sa=np.array(seal).astype(np.float32)
er=(np.random.rand(sz,sz)<0.025)
er=np.array(Image.fromarray((er*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))>0
sa[...,3]=np.where(er,sa[...,3]*0.5,sa[...,3])
seal=Image.fromarray(sa.astype(np.uint8),'RGBA').rotate(-4,resample=Image.BICUBIC,expand=True)
sx=bb[2]+26;sy=bb[1]+int((bb[3]-bb[1])*0.30)
out.alpha_composite(seal,(sx,sy))
bb2=out.getbbox();out=out.crop((max(0,bb2[0]-6),max(0,bb2[1]-6),bb2[2]+6,bb2[3]+6))
out.save(OUT);print(out.size)
