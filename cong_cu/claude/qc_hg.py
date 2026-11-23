import sys,os,json
import numpy as np
from PIL import Image,ImageDraw,ImageFont
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',10)
g=sys.argv[1];ks=sorted(f[:-4] for f in os.listdir('out_'+g));C=8;W=2*128;H=140
o=Image.new('RGB',(C*W,((len(ks)+C-1)//C)*H),(92,96,92));d=ImageDraw.Draw(o);rep=[]
for i,k in enumerate(ks):
  a=Image.open('cells/%s_%s.png'%(g,k)).convert('RGBA');b=Image.open('out_%s/%s.png'%(g,k)).convert('RGBA')
  A=np.asarray(a)[...,3]>0;B=np.asarray(b)[...,3]>0;iou=(A&B).sum()/max(1,(A|B).sum())
  ba,bb=a.getbbox(),b.getbbox();rep.append((k,round(iou,3),ba,bb))
  t=Image.new('RGBA',(256,128),(92,96,92,255));t.alpha_composite(a,(0,0));t.alpha_composite(b,(128,0));o.paste(t,((i%C)*W,(i//C)*H+12));d.text(((i%C)*W+2,(i//C)*H),'%s iou %.2f'%(k,iou),fill=(255,255,160) if iou>0.8 else (255,120,120),font=F)
o.save('qc_%s.png'%g);print(sorted(rep,key=lambda r:r[1])[:8])
