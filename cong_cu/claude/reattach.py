"""Gắn vũ khí vào frame không kiếm theo socket; dùng cho kiểm tra và xem thử."""
import json,math
from PIL import Image
S='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/'
def extract_base(g,k):
  sh=Image.open('/home/user/HoaThan/game/assets/hero_%s.png'%g).convert('RGBA');ns=Image.open(S+'wl/hero_%s_ns.png'%g);sock=json.load(open(S+'wl/sock_%s.json'%g))
  x,y=map(int,k.split(','));o=sh.crop((x,y,x+160,y+128));n=ns.crop((x,y,x+160,y+128));gx,gy,ang,z,L=sock[k]
  d=Image.new('RGBA',(160,128));po,pn,pd=o.load(),n.load(),d.load()
  for yy in range(128):
    for xx in range(160):
      if po[xx,yy][3] and not pn[xx,yy][3]:pd[xx,yy]=po[xx,yy]
  big=Image.new('RGBA',(300,300));big.alpha_composite(d,(int(150-gx),int(150-gy)))
  r=big.rotate(ang,center=(150,150),resample=Image.NEAREST)   # về nằm ngang
  bb=r.getbbox();w=r.crop((140,bb[1],bb[2],bb[3]));return w,(10,150-bb[1])
def place(cell,hand,wpn,grip,ang,z,scale=1.0):
  img,(gx,gy)=wpn
  if scale!=1:img=img.resize((max(1,round(img.width*scale)),max(1,round(img.height*scale))),Image.NEAREST);gx*=scale;gy*=scale
  big=Image.new('RGBA',(300,300));big.alpha_composite(img,(int(round(150-gx)),int(round(150-gy))))
  r=big.rotate(-ang,center=(150,150),resample=Image.NEAREST)
  lay=Image.new('RGBA',(160,128));lay.alpha_composite(r,(int(round(grip[0]-150)),int(round(grip[1]-150))) ) if False else None
  lay=Image.new('RGBA',(460,428));lay.alpha_composite(r,(int(round(grip[0]-150))+150,int(round(grip[1]-150))+150));lay=lay.crop((150,150,310,278))
  out=Image.new('RGBA',(160,128))
  if z=='b':out.alpha_composite(lay);out.alpha_composite(cell)
  else:out.alpha_composite(cell);out.alpha_composite(lay);out.alpha_composite(hand)
  return out
