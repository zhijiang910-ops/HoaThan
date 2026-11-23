"""Combo chốt (phác thảo PHAC_THAO_CHOT đã duyệt): A 5 khung, B 6, C 7. Kiếm 1 tay (tay xa), không ra sau lưng.
combo3.py <rig_body.json> <outdir> <tag>"""
import sys
P1=sys.argv[0].replace('combo3','combopose');src=open(P1).read();src=src[:src.index('# chân: bước dài')]
exec(src)
LUNGE2=(((12,8),(19,25)),((-13,12),(-24,23)));DEEP=(((13,7),(21,23)),((-15,11),(-27,21)))
STEPX=(((5,12),(9,28)),((-3,14),(-5,30)));KICK=(((5,12),(8,29)),((-9,12),(-22,18)))
FING=((6,6),(13,2));BAL=((-6,6),(-13,7))
A5=dict(dx=5,dy=7,lean=1,farm=((6,2),(12,-2)),narm=FING,th=-30,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=2)
B6=dict(dx=11,dy=10,lean=5,farm=((9,6),(17,11)),narm=BAL,th=40,nleg=DEEP[0],fleg=DEEP[1],hair=3)
if tag=='nu':B6=dict(dx=11,dy=10,lean=4,farm=((8,3),(15,7)),narm=BAL,th=40,nleg=DEEP[0],fleg=DEEP[1],hair=3)  # nữ: sát khung 4 hơn
A=[pose(),   # khung 0 = đúng tư thế master (tránh biến hình ở khung đầu)
 pose(dx=2,dy=3,lean=1,farm=((5,-6),(12,-10)),narm=BAL,th=-10,nleg=STEPX[0],fleg=STEPX[1],hair=2),
 pose(dx=4,dy=6,lean=3,farm=((9,-1),(19,-1)),narm=BAL,th=0,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=4),
 pose(dx=5,dy=7,lean=2,farm=((8,3),(15,6)),narm=BAL,th=20,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=3),
 pose(**A5)]
B=[pose(**A5),
 pose(dx=6,dy=4,farm=((7,-8),(13,-14)),narm=FING,th=-70,nleg=STEPX[0],fleg=STEPX[1],hair=1),   # kiếm giơ chéo lên TRƯỚC mặt, tay luôn thấy
 pose(dx=8,dy=2,lean=1,farm=((8,-9),(15,-15)),narm=BAL,th=-50,nleg=STEPX[0],fleg=STEPX[1],hair=2),
 pose(dx=11,dy=6,lean=4,farm=((9,-6),(18,-8)),narm=BAL,th=8,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=5),
 pose(dx=11,dy=8,lean=4,farm=((8,2),(15,6)),narm=BAL,th=35,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=4),
 pose(**B6)]
C=[pose(**B6),
 pose(dx=10,dy=7,lean=2,farm=((5,6),(11,10)),narm=BAL,th=0,nleg=STEPX[0],fleg=STEPX[1],hair=3),
 pose(dx=9,dy=5,lean=5,farm=((7,-5),(13,-10)),narm=FING,th=-65,nleg=KICK[0],fleg=KICK[1],hair=2),
 pose(dx=8,dy=6,lean=5,farm=((4,8),(8,16)),narm=BAL,th=10,nleg=LUNGE2[0],fleg=LUNGE2[1],hair=6),
 pose(dx=7,dy=9,lean=7,farm=((8,8),(15,14)),narm=BAL,th=25,nleg=DEEP[0],fleg=DEEP[1],hair=6),
 pose(dx=7,dy=9,lean=7,farm=((8,8),(15,14)),narm=BAL,th=25,nleg=DEEP[0],fleg=DEEP[1],hair=4),
 pose(dx=4,dy=2,lean=2,farm=((6,8),(11,15)),narm=BAL,th=45,nleg=STEPX[0],fleg=STEPX[1],hair=1)]   # lao tới do game đẩy; trong hình giữ gần giữa khung để kiếm không bị cắt
for k,v in {'A3':A,'B3':B,'C3':C}.items():json.dump(v,open(f'{od}/{tag}_pose_{k}.json','w'))
img=Image.open(sys.argv[1].replace('_rigB_body.json','_first.png')).convert('RGBA')
rows=[]
for k,v in {'A3':A,'B3':B,'C3':C}.items():
    o=Image.new('RGBA',(7*N*2,N*2),(40,44,52,255));d=ImageDraw.Draw(o)
    for i,fr in enumerate(v):
        bg=img.resize((N*2,N*2),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*N*2,0))
        Pp={MAP.get(p['label'],p['label']):(p['x']*N*2+i*N*2,p['y']*N*2) for p in fr}
        for n in names:
            if par[n]:d.line([Pp[par[n]],Pp[n]],fill=(255,200,0) if n.startswith('sword') else (0,255,255) if n.startswith('far') else (255,80,200) if n.startswith('near') else (220,220,220),width=3)
    rows.append(o)
o=Image.new('RGBA',(7*N*2,3*N*2))
for i,r in enumerate(rows):o.paste(r,(0,i*N*2))
o.resize((o.width//2,o.height//2)).save(f'{od}/{tag}_dbg.png')
