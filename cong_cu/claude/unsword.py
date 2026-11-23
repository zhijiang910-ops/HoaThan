"""Tách kiếm khỏi frame nhân vật theo khớp kiếm (sword_grip/tip) của khung xương. unsword.py job.json outprefix framepattern"""
import json,math,sys
from PIL import Image
def sd(px,py,a,b):
  dx,dy=b[0]-a[0],b[1]-a[1];L=dx*dx+dy*dy or 1;u=max(0,min(1,((px-a[0])*dx+(py-a[1])*dy)/L));return math.hypot(px-a[0]-dx*u,py-a[1]-dy*u)
def lum(p):return (p[0]*3+p[1]*6+p[2])/10
def sat(p):return max(p[:3])-min(p[:3])
def run(K,src,dst):
  im=Image.open(src).convert('RGBA');W,H=im.size;px=im.load()
  P={k['label']:(k['x']*W,k['y']*H) for k in K}
  g,t=P['sword_grip'],P['sword_tip'];ux,uy=t[0]-g[0],t[1]-g[1];L=math.hypot(ux,uy);ux/=L;uy/=L
  a=(g[0]+ux*3,g[1]+uy*3);b=(t[0]+ux*5,t[1]+uy*5)
  rm=set()
  for y in range(H):
    for x in range(W):
      p=px[x,y]
      if p[3]==0 or math.hypot(x+.5-g[0],y+.5-g[1])<3.5:continue
      if sd(x+.5,y+.5,a,b)<=4.2 and lum(p)>120 and sat(p)<60:rm.add((x,y))
  # viền tối sát lưỡi kiếm
  for (x,y) in list(rm):
    for dx in (-1,0,1):
      for dy in (-1,0,1):
        q=(x+dx,y+dy)
        if 0<=q[0]<W and 0<=q[1]<H and q not in rm and px[q][3]>0 and lum(px[q])<70 and sd(q[0]+.5,q[1]+.5,a,b)<=4.6 and math.hypot(q[0]+.5-g[0],q[1]+.5-g[1])>=3.5:
          # chỉ xóa viền nếu phía bên kia là nền trống (không ăn vào thân)
          if sum(1 for ex,ey in [(-1,0),(1,0),(0,-1),(0,1)] if 0<=q[0]+ex<W and 0<=q[1]+ey<H and (px[q[0]+ex,q[1]+ey][3]==0 or (q[0]+ex,q[1]+ey) in rm))>=2:rm.add(q)
  out=im.copy();po=out.load()
  for q in rm:po[q]=(0,0,0,0)
  # dọn mảnh vụn rời trong dải kiếm
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
      if len(comp)<=8 and all(sd(c[0]+.5,c[1]+.5,a,b)<=5 for c in comp):
        for c in comp:po[c]=(0,0,0,0);rm.add(c)
  out.save(dst)
  return {'grip':g,'tip':t,'ang':math.degrees(math.atan2(uy,ux)),'removed':len(rm)}
if __name__=='__main__':
  j=json.load(open(sys.argv[1]));res=[]
  for i,K in enumerate(j['keypoints']):
    r=run(K,sys.argv[3]%i,sys.argv[2]%i);res.append(r);print(i,{k:(round(v[0],1),round(v[1],1)) if isinstance(v,tuple) else round(v,1) if isinstance(v,float) else v for k,v in r.items()})
  json.dump(res,open(sys.argv[2].replace('%02d','sock')+'.json','w'))
