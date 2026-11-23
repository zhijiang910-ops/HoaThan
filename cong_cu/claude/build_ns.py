"""Tạo sheet nhân vật không kiếm + lớp nắm tay + socket vũ khí cho mọi frame đang dùng. build_ns.py <nam|nu>"""
import json,math,sys
sys.path.insert(0,'/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/tools')
from detsword import detect
from PIL import Image
S='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/'
g=sys.argv[1]
sh=Image.open('/home/user/HoaThan/game/assets/hero_%s.png'%g).convert('RGBA')
used=json.load(open(S+'wl/frames_used.json'))['hero_'+g]
cells=sorted({(f[0],f[1]) for v in used.values() for f in v})
rmap=json.load(open(S+'wl/row256_map.json'))[g]
det=json.load(open(S+'wl/det/det_%s.json'%g))
MAN={'nam':{'1440,256':((112,53),(132.5,36.5),'b'),'1120,0':((95.7,79.6),(116.5,89.3),'b'),'2240,0':((107,49),(141.5,41),'f'),'2240,128':((110,112),(129.5,112),'f'),'2080,128':((118,111),(132.5,111),'f')},
     'nu':{'2080,128':((106,111),(150.5,108),'f'),'2240,128':((113,113),(153.5,110),'f'),'160,256':((96,38),(128.5,20.5),'b'),'960,256':((101,65),(131.5,88.5),'b'),'3520,256':((101,61),(133.5,80.5),'b')}}[g]
def lum(p):return (p[0]*3+p[1]*6+p[2])/10
def sat(p):return max(p[:3])-min(p[:3])
def sd(px,py,a,b):
  dx,dy=b[0]-a[0],b[1]-a[1];L=dx*dx+dy*dy or 1;u=max(0,min(1,((px-a[0])*dx+(py-a[1])*dy)/L));return math.hypot(px-a[0]-dx*u,py-a[1]-dy*u)
def erase(im,g0,t0,front):
  W,H=im.size;px=im.load();ux,uy=t0[0]-g0[0],t0[1]-g0[1];L=math.hypot(ux,uy);ux/=L;uy/=L
  a=(g0[0]+ux*3,g0[1]+uy*3);b=(t0[0]+ux*13,t0[1]+uy*13);HR=3.5
  rm=set()
  for y in range(H):
    for x in range(W):
      p=px[x,y]
      if p[3]==0 or math.hypot(x+.5-g0[0],y+.5-g0[1])<HR:continue
      dd=sd(x+.5,y+.5,a,b)
      if (dd<=3.6 and ((lum(p)>120 and sat(p)<60) or (lum(p)>88 and sat(p)<38))) or (dd<=4.8 and lum(p)>72 and sat(p)<30):rm.add((x,y))
  for (x,y) in list(rm):
    for dx in (-1,0,1):
      for dy in (-1,0,1):
        q=(x+dx,y+dy)
        if 0<=q[0]<W and 0<=q[1]<H and q not in rm and px[q][3]>0 and lum(px[q])<75 and sd(q[0]+.5,q[1]+.5,a,b)<=5.4 and math.hypot(q[0]+.5-g0[0],q[1]+.5-g0[1])>=HR:
          if sum(1 for ex,ey in [(-1,0),(1,0),(0,-1),(0,1)] if 0<=q[0]+ex<W and 0<=q[1]+ey<H and (px[q[0]+ex,q[1]+ey][3]==0 or (q[0]+ex,q[1]+ey) in rm))>=2:rm.add(q)
  out=im.copy();po=out.load()
  for q in rm:po[q]=(0,0,0,0)
  seen=set()
  for y in range(H):
    for x in range(W):
      if po[x,y][3]==0 or (x,y) in seen:continue
      comp=[(x,y)];seen.add((x,y));k=0
      while k<len(comp):
        cx,cy=comp[k];k+=1
        for dx in (-1,0,1):
          for dy in (-1,0,1):
            q=(cx+dx,cy+dy)
            if 0<=q[0]<W and 0<=q[1]<H and q not in seen and po[q][3]>0:seen.add(q);comp.append(q)
      b2=(t0[0]+ux*30,t0[1]+uy*30)
      if (len(comp)<=8 and all(sd(c[0]+.5,c[1]+.5,a,b)<=5.5 for c in comp)) or (len(comp)<=30 and all(sd(c[0]+.5,c[1]+.5,a,b2)<=9 for c in comp)):
        for c in comp:po[c]=(0,0,0,0);rm.add(c)
  hand=Image.new('RGBA',im.size);ph=hand.load()
  if front:
    for y in range(H):
      for x in range(W):
        if math.hypot(x+.5-g0[0],y+.5-g0[1])<3.3 and po[x,y][3]:ph[x,y]=po[x,y]
  return out,hand,len(rm)
ns=sh.copy();hd=Image.new('RGBA',sh.size);sock={};log=[]
for (x,y) in cells:
  k='%d,%d'%(x,y);cell=sh.crop((x,y,x+160,y+128))
  if k in MAN:g0,t0,_z=MAN[k];z=None
  elif y==256 and str(x) in rmap:
    jn,fi,_=rmap[str(x)];K=json.load(open(S+'combo5/job_%s_%s.json'%(g,jn)))['keypoints'][fi]
    P={q['label']:(q['x']*128+16,q['y']*128,q.get('z_index',1)) for q in K}
    gk='sword_grip' if 'sword_grip' in P else 'sword_pivot';g0=P[gk][:2];t0=P['sword_tip'][:2];z=None
  elif k in MAN:g0,t0,_z=MAN[k];z=None
  else:
    d=det.get(k)
    if not d:log.append((k,'NO SWORD'));continue
    p1,p2=d[1],d[2];cx,cy=80,70   # đầu gần thân là chuôi
    if math.dist(p1,(cx,cy))>math.dist(p2,(cx,cy)):p1,p2=p2,p1
    ux,uy=p2[0]-p1[0],p2[1]-p1[1];L=math.hypot(ux,uy);ux/=L;uy/=L
    g0=(p1[0]-ux*4,p1[1]-uy*4);t0=(p2[0]+ux*.5,p2[1]+uy*.5)
    # chuôi bị thân che (không có điểm da/tay quanh chuôi) -> kiếm nằm sau thân
    cp=cell.load();skin=sum(1 for xx in range(int(g0[0])-3,int(g0[0])+4) for yy in range(int(g0[1])-3,int(g0[1])+4) if 0<=xx<160 and 0<=yy<128 and cp[xx,yy][3] and cp[xx,yy][0]>170 and cp[xx,yy][1]>110 and cp[xx,yy][2]<140 and cp[xx,yy][0]-cp[xx,yy][2]>50)
    z=None
  out,hand,n=erase(cell,g0,t0,True)
  if n<60 and k not in MAN:
    # khung xương lệch khỏi lưỡi kiếm thật -> dò lưỡi kiếm trên ảnh, đầu gần chuôi khung xương là chuôi
    d=detect(cell)
    if d:
      p1,p2=d[1],d[2]
      if math.dist(p1,g0)>math.dist(p2,g0):p1,p2=p2,p1
      ux,uy=p2[0]-p1[0],p2[1]-p1[1];L=math.hypot(ux,uy);ux/=L;uy/=L
      g1=(p1[0]-ux*4,p1[1]-uy*4);t1=(p2[0]+ux*.5,p2[1]+uy*.5);o2,h2,n2=erase(cell,g1,t1,True)
      if n2>n:out,hand,n,g0,t0=o2,h2,n2,g1,t1;log.append((k,'detfix',n2))
  if z is None:
    po=out.load();cp=cell.load();ux,uy=t0[0]-g0[0],t0[1]-g0[1];L=math.hypot(ux,uy);nx,ny=-uy/L,ux/L;ov=0
    for xx in range(160):
      for yy in range(128):
        if cp[xx,yy][3] and not po[xx,yy][3]:
          a1=(int(round(xx+nx*2)),int(round(yy+ny*2)));a2=(int(round(xx-nx*2)),int(round(yy-ny*2)))
          if all(0<=q[0]<160 and 0<=q[1]<128 and po[q][3] for q in (a1,a2)):ov+=1
    z='f' if ov>=4 else 'b'
  if z=='b':hand=Image.new('RGBA',cell.size)
  ns.paste(Image.new('RGBA',(160,128)),(x,y));ns.alpha_composite(out,(x,y));hd.alpha_composite(hand,(x,y))
  ang=math.degrees(math.atan2(t0[1]-g0[1],t0[0]-g0[0]));sock[k]=[round(g0[0],1),round(g0[1],1),round(ang,1),z,round(math.dist(g0,t0),1)]
  log.append((k,z,n))
ns.save(S+'wl/hero_%s_ns.png'%g);hd.save(S+'wl/hero_%s_hand.png'%g);json.dump(sock,open(S+'wl/sock_%s.json'%g,'w'))
print(g,len(sock),[l for l in log if l[1]=='NO SWORD' or (len(l)>2 and l[2]<20)])
print({k:v[3] for k,v in sock.items()})
