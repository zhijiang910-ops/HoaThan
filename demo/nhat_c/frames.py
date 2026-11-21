import json,re,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
from PIL import Image,ImageDraw,ImageFont
s=open(ROOT/'game'/'index.html',encoding='utf-8').read()
i=s.find('CHM=');j=s.find(';',i)
# parse JSON up to matching braces
k=i+4;depth=0
for n,ch in enumerate(s[k:]):
    if ch=='{':depth+=1
    elif ch=='}':
        depth-=1
        if depth==0: end=k+n+1;break
CHM=json.loads(s[k:end])
json.dump({g:CHM[g] for g in ['hero_nam','hero_nu']},open(HERE/'meta.json','w'))
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
for g in ['hero_nam','hero_nu']:
    m=CHM[g];sh=Image.open(ROOT/'game'/'assets'/f'{g}.png').convert('RGBA')
    rows=[]
    for an in ['idle','run','attack','attack2']:
        fr=m['anims'][an]['f']
        row=Image.new('RGB',(len(fr)*(m['w']*2+4),m['h']*2+16),'#446')
        d=ImageDraw.Draw(row)
        for q,(x,y) in enumerate(fr):
            c=sh.crop((x,y,x+m['w'],y+m['h'])).resize((m['w']*2,m['h']*2),Image.NEAREST)
            row.paste(c,(q*(m['w']*2+4),14),c)
            d.text((q*(m['w']*2+4)+2,0),f'{an}{q}',font=F,fill='#ff0')
            ax=q*(m['w']*2+4)+m['ax']*2;d.line((ax,14+m['ay']*2-4,ax,14+m['ay']*2+4),fill='red')
        rows.append(row)
    W=max(r.width for r in rows);out=Image.new('RGB',(W,sum(r.height for r in rows)),'#223')
    y=0
    for r in rows: out.paste(r,(0,y));y+=r.height
    out.save(HERE/f'{g}_frames.png')
