import sys,json,math;sys.path.insert(0,'tools');import qc
import numpy as np
from PIL import Image,ImageDraw
N=128;R={'nam':((77,79),(96,93)),'nu':((76,77),(100,96))}
def overlay(p,g,posefile,i,lab):
    kp=json.load(open(posefile))[i];P={x['label']:(x['x']*N,x['y']*N) for x in kp}
    w='far_wrist' if g=='nam' else 'left_wrist'
    ang=math.atan2(P['sword_tip'][1]-P[w][1],P['sword_tip'][0]-P[w][0])
    A=qc.load(p);bm=qc.blade_px(A);c,ww,aa=qc.best_line(bm,P[w],math.degrees(ang),30);a=math.radians(aa)
    ys,xs=np.nonzero(bm);pts=[(x,y) for x,y in zip(xs,ys) if abs(-(x-ww[0])*math.sin(a)+(y-ww[1])*math.cos(a))<3]
    tip=max(pts,key=lambda q:(q[0]-ww[0])*math.cos(a)+(q[1]-ww[1])*math.sin(a)) if pts else ww
    L=math.dist(*R[g]);hilt=(tip[0]-math.cos(a)*L,tip[1]-math.sin(a)*L)
    im=Image.open(p).convert('RGBA').resize((N*3,N*3),Image.NEAREST);d=ImageDraw.Draw(im)
    d.line([(hilt[0]*3,hilt[1]*3),(tip[0]*3,tip[1]*3)],fill=(0,255,0),width=2);d.ellipse((hilt[0]*3-5,hilt[1]*3-5,hilt[0]*3+5,hilt[1]*3+5),outline=(0,255,0),width=2)
    d.text((4,4),lab,fill='yellow');return im
items=[x.split(':') for x in sys.argv[2:]]
o=Image.new('RGBA',(len(items)*390,390),(40,44,52,255))
for k,(p,g,pf,i) in enumerate(items):o.alpha_composite(overlay(p,g,pf,int(i),p.split('/')[-1]),(k*390,0))
o.save(sys.argv[1])
