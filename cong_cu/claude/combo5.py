"""Combo theo bản mẫu 'VFX & ANIMATION MẪU - KIẾM': A Khởi Kiếm 8 khung, B Hồi Kiếm 8, C Phá Thế Trảm 12 (không quay lưng). combo5.py <rig_body.json> <outdir> <tag>"""
import sys
P1=sys.argv[0].replace('combo5','combopose');src=open(P1).read();src=src[:src.index('# chân: bước dài')]
exec(src)
STEPX=(((5,12),(9,28)),((-3,14),(-5,30)));LUNGE2=(((12,8),(19,25)),((-13,12),(-24,23)));WIDE=(((10,10),(15,27)),((-10,10),(-15,27)))
FING=((6,6),(13,2));BAL=((-6,6),(-13,7))
A_END=dict(dx=4,dy=6,lean=3,farm=((8,4),(15,8)),narm=BAL,th=35,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=2)
B_END=dict(dx=5,dy=5,lean=2,farm=((8,0),(17,-1)),narm=BAL,th=-5,nleg=STEPX[0],fleg=STEPX[1],hair=2)
A=[pose(),
 pose(dy=2,farm=((5,-5),(10,-11)),narm=FING,th=-55,nleg=STEPX[0],fleg=STEPX[1],hair=1),        # nâng kiếm chéo trước
 pose(dx=1,dy=3,farm=((6,-9),(11,-17)),narm=FING,th=-40,nleg=STEPX[0],fleg=STEPX[1],hair=2),   # kiếm cao trước mặt
 pose(dx=3,dy=5,lean=2,farm=((9,-4),(18,-6)),narm=BAL,th=15,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=3),
 pose(dx=4,dy=6,lean=3,farm=((10,0),(20,1)) if tag=='nam' else ((9,1),(17,2)),narm=BAL,th=0 if tag=='nam' else 8,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=4),  # chém ngang ra trước (trúng)
 pose(dx=4,dy=6,lean=3,farm=((9,3),(17,6)),narm=BAL,th=25,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=3),
 pose(dx=4,dy=6,lean=3,farm=((8,4),(15,8)),narm=BAL,th=35,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=2),
 pose(**A_END)]
B=[pose(**A_END),
 pose(dx=4,dy=7,lean=3,farm=((7,6),(12,12)),narm=BAL,th=65,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=2),   # hạ kiếm thấp lấy đà
 pose(dx=5,dy=6,lean=3,farm=((9,4),(17,7)),narm=BAL,th=25,nleg=STEPX[0],fleg=STEPX[1],hair=3),
 pose(dx=5,dy=5,lean=2,farm=((10,-1),(19,-3)),narm=BAL,th=-25,nleg=STEPX[0],fleg=STEPX[1],hair=4),  # hất ngược lên (trúng)
 pose(dx=5,dy=4,lean=1,farm=((8,-7),(14,-14)),narm=FING,th=-60,nleg=STEPX[0],fleg=STEPX[1],hair=4),
 pose(dx=5,dy=4,lean=1,farm=((8,-7),(14,-14)),narm=FING,th=-58,nleg=STEPX[0],fleg=STEPX[1],hair=3),
 pose(dx=5,dy=5,lean=2,farm=((9,-3),(17,-5)),narm=BAL,th=-20,nleg=STEPX[0],fleg=STEPX[1],hair=2),
 pose(**B_END)]
C=[pose(**B_END),
 pose(dx=5,dy=7,lean=1,farm=((6,7),(11,13)),narm=BAL,th=45,nleg=WIDE[0],fleg=WIDE[1],hair=2),     # tấn rộng, kiếm về hông
 pose(dx=5,dy=6,lean=2,farm=((10,0),(20,0)),narm=BAL,th=0,nleg=WIDE[0],fleg=WIDE[1],hair=4),      # quét ngang (trúng 1)
 pose(dx=5,dy=6,lean=2,farm=((9,-3),(18,-6)),narm=BAL,th=-25,nleg=WIDE[0],fleg=WIDE[1],hair=4),
 pose(dx=5,dy=5,lean=1,farm=((8,-7),(14,-14)),narm=FING,th=-55,nleg=WIDE[0],fleg=WIDE[1],hair=3),
 pose(dx=5,dy=6,lean=2,farm=((10,-2),(19,-3)),narm=BAL,th=-5,nleg=WIDE[0],fleg=WIDE[1],hair=4),
 pose(dx=5,dy=6,lean=2,farm=((10,0),(20,1)),narm=BAL,th=5,nleg=WIDE[0],fleg=WIDE[1],hair=5),      # quét ngang (trúng 2)
 pose(dx=5,dy=7,lean=2,farm=((8,4),(15,9)),narm=BAL,th=35,nleg=WIDE[0],fleg=WIDE[1],hair=4),
 pose(dx=5,dy=7,lean=1,farm=((6,7),(11,13)),narm=BAL,th=45,nleg=WIDE[0],fleg=WIDE[1],hair=3),
 pose(dx=6,dy=6,lean=3,farm=((10,0),(21,0)),narm=BAL,th=0,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=6),   # quét mạnh (trúng 3)
 pose(dx=6,dy=6,lean=3,farm=((9,3),(17,6)),narm=BAL,th=25,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=4),
 pose(dx=4,dy=1,lean=1,farm=((6,8),(11,15)),narm=BAL,th=45,nleg=STEPX[0],fleg=STEPX[1],hair=1)]
if tag=='nu':   # kiếm nữ dài hơn, đầu kiếm lố mép khung 128 khi duỗi thẳng -> rút tay, lùi người 2px ở các khung duỗi
    import copy
    def pull(fr):
        for p_ in fr:p_['x']=round(p_['x']-2/N,4)
        return fr
    A=[pull(f) if i in (3,4,5) else f for i,f in enumerate(A)]
    C=[pull(f) if i in (2,5,6,9,10) else f for i,f in enumerate(C)]
for k,v in {'A5':A,'B5':B,'C5':C}.items():json.dump(v,open(f'{od}/{tag}_pose_{k}.json','w'))
img=Image.open(sys.argv[1].replace('_rigB_body.json','_first.png')).convert('RGBA')
rows=[]
for k,v in {'A5':A,'B5':B,'C5':C}.items():
    o=Image.new('RGBA',(12*N,N),(40,44,52,255));d=ImageDraw.Draw(o)
    for i,fr in enumerate(v):
        bg=img.copy();bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*N,0))
        Pp={MAP.get(p['label'],p['label']):(p['x']*N+i*N,p['y']*N) for p in fr}
        for n in names:
            if par[n]:d.line([Pp[par[n]],Pp[n]],fill=(255,200,0) if n.startswith('sword') else (0,255,255) if n.startswith('far') else (255,80,200) if n.startswith('near') else (220,220,220),width=2)
    rows.append(o)
o=Image.new('RGBA',(12*N,3*N))
for i,r in enumerate(rows):o.paste(r,(0,i*N))
o.save(f'{od}/{tag}_dbg.png')
