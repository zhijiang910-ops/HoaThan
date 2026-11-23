"""Combo phương án 2: A nửa vòng trước -> B nửa vòng ngược -> C xoay trọn vòng. Khung cuối A = khung đầu B, cuối B = đầu C."""
import sys
P1=sys.argv[0].replace('combo2','combopose');src=open(P1).read();src=src[:src.index('# chân: bước dài')]
exec(src)
STEP=(((6,14),(10,30)),((-6,16),(-12,31)));LUNGE=(((11,11),(18,27)),((-10,15),(-19,28)));CROUCH=(((5,13),(9,28)),((-4,15),(-8,30)))
A_END=dict(dx=2,dy=1,lean=2,farm=((2,4),(-6,6)),th=170,hair=2,nleg=STEP[0],fleg=STEP[1])       # kiếm vắt qua người
B_END=dict(dx=2,dy=2,lean=-1,farm=((-7,3),(-15,6)),th=175,hair=1,nleg=CROUCH[0],fleg=CROUCH[1])  # kiếm sau lưng thấp, người vặn
A=[pose(),
 pose(dx=0,dy=1,lean=-2,farm=((-7,2),(-15,4)),th=175,hair=1,nleg=CROUCH[0],fleg=CROUCH[1]),   # vặn người kiếm ra sau
 pose(dx=1,dy=1,lean=1,farm=((2,3),(6,3)),th=60,hair=2,nleg=STEP[0],fleg=STEP[1]),            # vung qua hông
 pose(dx=2,dy=1,lean=3,farm=((9,1),(19,2)),th=0,hair=3,nleg=STEP[0],fleg=STEP[1]),            # quét ngang trước (chạm)
 pose(dx=2,dy=1,lean=3,farm=((7,4),(12,8)),th=35,hair=3,nleg=STEP[0],fleg=STEP[1]),           # theo đà: kiếm chéo xuống trước, rõ cả lưỡi
 pose(**A_END)]
B=[pose(**A_END),
 pose(dx=2,dy=1,lean=1,farm=((1,1),(-4,0)),th=-170,hair=2,nleg=STEP[0],fleg=STEP[1]),          # trái tay bắt đầu ra
 pose(dx=2,dy=1,lean=-2,farm=((-6,0),(-15,1)),th=180,hair=1,nleg=STEP[0],fleg=STEP[1]),        # quét ngược ra sau (chạm)
 pose(dx=2,dy=2,lean=-2,farm=((-7,2),(-15,4)),th=150,hair=1,nleg=CROUCH[0],fleg=CROUCH[1]),
 pose(**B_END)]
C=[pose(**B_END),
 pose(dx=3,dy=1,lean=1,farm=((3,4),(8,5)),th=90,hair=3,nleg=STEP[0],fleg=STEP[1]),            # xả đà, kiếm qua hông
 pose(dx=4,dy=2,lean=4,farm=((9,1),(19,2)),th=0,hair=5,nleg=LUNGE[0],fleg=LUNGE[1]),          # vòng 1 (chạm)
 pose(dx=4,dy=2,lean=2,farm=((2,2),(-5,3)),th=175,hair=4,nleg=LUNGE[0],fleg=LUNGE[1]),        # kiếm vòng ra sau
 pose(dx=5,dy=2,lean=4,farm=((9,-2),(18,-4)),th=-20,hair=6,nleg=LUNGE[0],fleg=LUNGE[1]),       # vòng 2: kiếm chếch lên, cùng độ dài
 pose(dx=4,dy=2,lean=4,farm=((8,4),(15,10)),th=40,hair=4,nleg=LUNGE[0],fleg=LUNGE[1]),        # theo đà
 pose(dx=2,dy=1,lean=2,farm=((6,6),(11,13)),th=55,hair=2,nleg=STEP[0],fleg=STEP[1]),
 pose()]
for k,v in {'A2':A,'B2':B,'C2':C}.items():json.dump(v,open(f'{od}/{tag}_pose_{k}.json','w'))
img=Image.open(src.replace('_rigB_body.json','_first.png') if False else sys.argv[1].replace('_rigB_body.json','_first.png')).convert('RGBA')
rows=[]
for k,v in {'A2':A,'B2':B,'C2':C}.items():
    o=Image.new('RGBA',(8*N*2,N*2),(40,44,52,255));d=ImageDraw.Draw(o)
    for i,fr in enumerate(v):
        bg=img.resize((N*2,N*2),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*N*2,0))
        Pp={MAP.get(p['label'],p['label']):(p['x']*N*2+i*N*2,p['y']*N*2) for p in fr}
        for n in names:
            if par[n]:d.line([Pp[par[n]],Pp[n]],fill=(255,200,0) if n.startswith('sword') else (0,255,255) if n.startswith('far') else (255,80,200) if n.startswith('near') else (220,220,220),width=3)
    rows.append(o)
o=Image.new('RGBA',(8*N*2,3*N*2))
for i,r in enumerate(rows):o.paste(r,(0,i*N*2))
o.resize((o.width//2,o.height//2)).save(f'{od}/{tag}_dbg_combo2.png')
