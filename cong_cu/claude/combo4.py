"""Combo theo 3 ảnh chủ game: A lao đâm thấp, B chém vòng xuống khụy thấp, C chém lốc xoay tại chỗ. combo4.py <rig_body.json> <outdir> <tag>"""
import sys
P1=sys.argv[0].replace('combo4','combopose');src=open(P1).read();src=src[:src.index('# chân: bước dài')]
exec(src)
STEPX=(((5,12),(9,28)),((-3,14),(-5,30)));CROUCH=(((5,13),(9,28)),((-4,15),(-8,30)))
LUNGEL=(((14,6),(22,22)),((-16,10),(-29,19)));CROUCHL=(((11,8),(18,24)),((-12,10),(-21,22)));WIDE=(((10,10),(15,27)),((-10,10),(-15,27)))
FING=((6,6),(13,2));BAL=((-6,6),(-13,7))
A_END=dict(dx=7,dy=7,lean=5,farm=((8,4),(15,8)),narm=BAL,th=25,nleg=LUNGEL[0],fleg=LUNGEL[1],hair=3)
B_END=dict(dx=8,dy=10,lean=5,farm=((9,6),(17,11)),narm=BAL,th=40,nleg=CROUCHL[0],fleg=CROUCHL[1],hair=3)
A=[pose(),
 pose(dy=4,lean=1,farm=((3,-9),(8,-15)),narm=FING,th=-40,nleg=CROUCH[0],fleg=CROUCH[1],hair=1),
 pose(dx=7,dy=9,lean=8,farm=((10,1),(21,1)),narm=BAL,th=0,nleg=LUNGEL[0],fleg=LUNGEL[1],hair=6),
 pose(dx=7,dy=9,lean=7,farm=((10,2),(20,3)),narm=BAL,th=5,nleg=LUNGEL[0],fleg=LUNGEL[1],hair=5),
 pose(**A_END)]
B=[pose(**A_END),
 pose(dx=5,dy=4,lean=1,farm=((7,-8),(13,-14)),narm=FING,th=-60,nleg=STEPX[0],fleg=STEPX[1],hair=2),
 pose(dx=7,dy=6,lean=4,farm=((10,-3),(19,-4)),narm=BAL,th=-10,nleg=CROUCHL[0],fleg=CROUCHL[1],hair=4),
 pose(dx=8,dy=9,lean=6,farm=((9,3),(16,9)),narm=BAL,th=45,nleg=CROUCHL[0],fleg=CROUCHL[1],hair=5),
 pose(**B_END)]
C=[pose(**B_END),
 pose(dx=6,dy=5,farm=((2,-12),(6,-21)),narm=((6,4),(12,2)),th=-178,nleg=WIDE[0],fleg=WIDE[1],hair=2),     # xoay: kiếm ngang trên đỉnh đầu chĩa ra sau
 pose(dx=6,dy=5,lean=2,farm=((9,0),(19,0)),narm=BAL,th=0,nleg=WIDE[0],fleg=WIDE[1],hair=4),               # quét ngang ra trước (trúng)
 pose(dx=6,dy=5,farm=((4,-12),(9,-21)),narm=BAL,th=-2,nleg=WIDE[0],fleg=WIDE[1],hair=3),                  # xoay: kiếm ngang trên đầu chĩa ra trước
 pose(dx=6,dy=5,lean=2,farm=((9,2),(18,4)),narm=BAL,th=10,nleg=WIDE[0],fleg=WIDE[1],hair=5),              # vòng 2 (trúng)
 pose(dx=4,dy=2,lean=1,farm=((6,8),(11,15)),narm=BAL,th=45,nleg=STEPX[0],fleg=STEPX[1],hair=1)]
for k,v in {'A4':A,'B4':B,'C4':C}.items():json.dump(v,open(f'{od}/{tag}_pose_{k}.json','w'))
img=Image.open(sys.argv[1].replace('_rigB_body.json','_first.png')).convert('RGBA')
rows=[]
for k,v in {'A4':A,'B4':B,'C4':C}.items():
    o=Image.new('RGBA',(6*N*2,N*2),(40,44,52,255));d=ImageDraw.Draw(o)
    for i,fr in enumerate(v):
        bg=img.resize((N*2,N*2),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*N*2,0))
        Pp={MAP.get(p['label'],p['label']):(p['x']*N*2+i*N*2,p['y']*N*2) for p in fr}
        for n in names:
            if par[n]:d.line([Pp[par[n]],Pp[n]],fill=(255,200,0) if n.startswith('sword') else (0,255,255) if n.startswith('far') else (255,80,200) if n.startswith('near') else (220,220,220),width=3)
    rows.append(o)
o=Image.new('RGBA',(6*N*2,3*N*2))
for i,r in enumerate(rows):o.paste(r,(0,i*N*2))
o.resize((o.width//2,o.height//2)).save(f'{od}/{tag}_dbg.png')
