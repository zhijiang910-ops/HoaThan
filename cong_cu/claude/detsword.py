"""Dò lưỡi kiếm trong frame không có khung xương: tìm đoạn thẳng mảnh gồm điểm ảnh thép (sáng, ít màu). In grip/tip theo toạ độ ô 160x128."""
import json,math,sys,random
import numpy as np
from PIL import Image,ImageDraw
def steel(p):
  r,g,b,a=p
  if a<200:return False
  mx,mn=max(r,g,b),min(r,g,b);l=(r*3+g*6+b)/10
  return l>150 and mx-mn<55
def detect(cell):
  W,H=cell.size;px=cell.load()
  pts=[(x,y) for y in range(H) for x in range(W) if steel(px[x,y])]
  # bỏ điểm "dày" (có >=3 điểm thép theo cả ngang và dọc quanh nó) -> vạt áo trắng
  S=set(pts);thin=[]
  for (x,y) in pts:
    h=sum((x+d,y) in S for d in (-2,-1,1,2));v=sum((x,y+d) in S for d in (-2,-1,1,2))
    near=any(0<=x+dx<W and 0<=y+dy<H and px[x+dx,y+dy][3]==0 for dx in range(-3,4) for dy in range(-3,4))
    if not(h>=3 and v>=3) and near:thin.append((x,y))
  best=None;rnd=random.Random(1)
  for _ in range(4000):
    if len(thin)<2:break
    a,b=rnd.sample(thin,2);L=math.dist(a,b)
    if L<8:continue
    ux,uy=(b[0]-a[0])/L,(b[1]-a[1])/L
    inl=[p for p in thin if abs((p[0]-a[0])*uy-(p[1]-a[1])*ux)<=1.1]
    if len(inl)<8:continue
    t=sorted(((p[0]-a[0])*ux+(p[1]-a[1])*uy) for p in inl)
    # đoạn liền mạch dài nhất (khe hở <=3)
    segs=[];s0=t[0];prev=t[0]
    for v in t[1:]:
      if v-prev>3:segs.append((s0,prev));s0=v
      prev=v
    segs.append((s0,prev));s0,s1=max(segs,key=lambda q:q[1]-q[0]);ln=s1-s0
    if best is None or ln>best[0]:best=(ln,(a[0]+ux*s0,a[1]+uy*s0),(a[0]+ux*s1,a[1]+uy*s1))
  return best
if __name__=='__main__':
  g=sys.argv[1];cells=json.loads(sys.argv[2]);out=sys.argv[3]
  sh=Image.open('/home/user/HoaThan/game/assets/hero_%s.png'%g).convert('RGBA');res={}
  for x,y in cells:
    c=sh.crop((x,y,x+160,y+128));b=detect(c);res['%d,%d'%(x,y)]=b and [round(b[0],1),[round(v,1) for v in b[1]],[round(v,1) for v in b[2]]]
  json.dump(res,open(out,'w'));print(json.dumps(res))
