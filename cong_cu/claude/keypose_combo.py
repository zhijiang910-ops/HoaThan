import sys,math,os
CP='/home/user/HoaThan/cong_cu/claude/combopose.py'
src=open(CP).read();src=src[:src.index('# chân: bước dài')]
rigf,od,tag=sys.argv[1:4]
sys.argv=[CP,rigf,od,tag];exec(src)
from PIL import ImageFont
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13);Fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15);Ft=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',20)
STEP=(((6,14),(10,30)),((-6,16),(-12,31)));LUNGE=(((11,11),(18,27)),((-10,15),(-19,28)));CROUCH=(((5,13),(9,28)),((-4,15),(-8,30)))
WIDE=(((10,10),(15,27)),((-10,10),(-15,27)));LUNGEL=(((14,6),(22,22)),((-16,10),(-29,19)))
BAL=((-6,6),(-13,7));FING=((6,6),(13,2))
def P(dx=0,dy=0,lean=0,farm=None,narm=BAL,leg=STEP,th=0,hair=1):return pose(dx=dx,dy=dy,lean=lean,farm=farm,narm=narm,nleg=leg[0],fleg=leg[1],th=th,hair=hair)
# (mã, tên, ms, pha, tư thế). Hướng mặt = đông. th: 0 đông, 90 xuống, -90 lên, ±180 tây.
A=[('A1','Chuẩn bị (ready)',70,'Khởi',P(dy=2,lean=-1,farm=((7,3),(12,-3)),th=-25,leg=STEP)),
 ('A2','Nâng / Tụ',70,'Khởi',P(dx=-1,dy=3,lean=-3,farm=((0,-9),(-5,-18)),th=-125,leg=CROUCH)),
 ('A3','Chém xuống',40,'Ra đòn',P(dx=3,dy=4,lean=3,farm=((8,-6),(15,-4)),th=-15,leg=LUNGE)),
 ('A4','ĐIỂM CHẠM (max)',50,'Ra đòn',P(dx=7,dy=6,lean=8,farm=((9,3),(16,9)),th=55,leg=LUNGEL)),
 ('A5','Theo đà',50,'Hồi',P(dx=7,dy=7,lean=6,farm=((7,6),(11,14)),th=78,leg=LUNGEL)),
 ('A6','Hồi (đứng lên)',60,'Hồi',P(dx=5,dy=3,lean=3,farm=((8,3),(14,6)),th=40,leg=LUNGE)),
 ('A7','Sẵn sàng nối',60,'Hồi',P(dx=4,dy=1,lean=2,farm=((9,1),(17,2)),th=15,leg=STEP))]
B=[('B1','Bắt đầu (từ A)',50,'Khởi',P(dx=4,dy=1,lean=2,farm=((9,1),(17,2)),th=15,leg=STEP)),
 ('B2','Kéo kiếm về',60,'Khởi',P(dx=2,dy=3,lean=-4,farm=((-4,5),(-11,9)),th=170,leg=CROUCH)),
 ('B3','Bắt đầu quét',40,'Ra đòn',P(dx=3,dy=4,lean=-1,farm=((1,6),(-3,13)),th=130,leg=WIDE)),
 ('B4','Quét',40,'Ra đòn',P(dx=5,dy=6,lean=4,farm=((7,6),(13,12)),th=65,leg=LUNGEL)),
 ('B5','ĐIỂM CHẠM (quét rộng)',50,'Ra đòn',P(dx=8,dy=7,lean=7,farm=((10,2),(21,3)),th=5,leg=LUNGEL)),
 ('B6','Theo đà',50,'Hồi',P(dx=7,dy=5,lean=5,farm=((9,0),(17,-4)),th=-18,leg=LUNGE)),
 ('B7','Hồi (thu thế)',50,'Hồi',P(dx=5,dy=2,lean=3,farm=((8,2),(14,4)),th=20,leg=STEP))]
C=[('C1','Tụ (từ B)',60,'Khởi',P(dx=5,dy=2,lean=3,farm=((8,2),(14,4)),th=20,leg=STEP)),
 ('C2','Nâng / Lấy đà',70,'Khởi',P(dx=3,dy=3,lean=-2,farm=((3,-10),(6,-20)),th=-100,leg=CROUCH)),
 ('C3','Hạ (bắt đầu)',50,'Khởi',P(dx=4,dy=4,lean=2,farm=((7,-7),(12,-12)),th=-55,leg=WIDE)),
 ('C4','CHÉM XUỐNG (điểm chạm 1)',50,'Ra đòn',P(dx=7,dy=7,lean=7,farm=((9,2),(16,8)),th=45,leg=LUNGEL)),
 ('C5','Mở rộng (quét)',40,'Ra đòn',P(dx=7,dy=8,lean=6,farm=((10,3),(20,6)),th=10,leg=LUNGEL)),
 ('C6','Elip: vòng trước',40,'Ra đòn',P(dx=7,dy=8,lean=5,farm=((10,2),(21,2)),th=0,leg=LUNGEL)),
 ('C7','Elip: bên hông',40,'Ra đòn',P(dx=6,dy=8,lean=4,farm=((10,2),(21,1)),th=-4,leg=WIDE)),
 ('C8','Elip: vòng sau',40,'Ra đòn',P(dx=6,dy=7,lean=3,farm=((9,1),(18,-2)),th=-10,leg=WIDE)),
 ('C9','Mờ dần (đuôi)',50,'Hồi',P(dx=5,dy=5,lean=3,farm=((8,3),(15,3)),th=10,leg=LUNGE)),
 ('C10','Tan',60,'Hồi',P(dx=5,dy=4,lean=2,farm=((8,3),(14,5)),th=25,leg=LUNGE)),
 ('C11','Hồi (đứng lên)',70,'Hồi',P(dx=4,dy=2,lean=2,farm=((8,2),(14,5)),th=30,leg=STEP)),
 ('C12','Kết (sẵn sàng)',70,'Hồi',P(dx=3,dy=0,lean=1,farm=((9,1),(16,3)),th=15,leg=STEP))]
img=Image.open(rigf.replace('_rigB_body.json','_first.png')).convert('RGBA')
Z=1.75;W=int(N*Z);CW=W;COLS=7;HDR=64
PH={'Khởi':(110,150,200),'Ra đòn':(230,110,90),'Hồi':(110,190,130)}
def tipxy(p):
    d={MAP.get(q['label'],q['label']):(q['x']*N,q['y']*N) for q in p};return d
def cell(dr,o,x0,y0,code,name,ms,ph,p,t0,trail,imp):
    bg=img.resize((W,W),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(x0,y0+24))
    ImageDraw.Draw(o).rectangle([x0,y0,x0+CW-2,y0+22],fill=PH[ph])
    dr=ImageDraw.Draw(o);dr.text((x0+4,y0+3),f'{code} {name}',fill=(10,10,14),font=F)
    d=tipxy(p);Pp={k:(v[0]*Z+x0,v[1]*Z+y0+24) for k,v in d.items()}
    if len(trail)>1:
        dr.line([(a[0]*Z+x0,a[1]*Z+y0+24) for a in trail],fill=(255,215,90),width=2)
    for n in names:
        if par[n] and not n.startswith('sword'):dr.line([Pp[par[n]],Pp[n]],fill=(0,230,255) if n.startswith('far') else (255,90,200) if n.startswith('near') else (225,225,225),width=3)
    dr.line([Pp['sword_grip'],Pp['sword_tip']],fill=(255,255,255),width=4)
    for w_ in ('near_wrist','far_wrist'):x,y=Pp[w_];dr.ellipse([x-4,y-4,x+4,y+4],fill=(255,210,90))
    gy=int(y0+24+W*0.93);dr.line([(x0+8,gy),(x0+W-8,gy)],fill=(70,76,86),width=1)
    dr.text((x0+4,y0+W+26),f'{t0:03d} ms · giữ {ms} ms'+('  ★ chạm' if imp else ''),fill=(255,230,120) if imp else (190,195,205),font=F)
rows=[('A · Khởi Kiếm — chém chéo xuống · 7 khung · 400 ms',A,4),('B · Hồi Kiếm — quét ngang rộng, nối từ A · 7 khung · 340 ms',B,5),('C (+6) · Phá Thế Trảm — chém xuống rồi elip một vòng · 12 khung · 640 ms',C,4)]
lines=[]
for title,seq,ip in rows:
    for k in range(0,len(seq),COLS):lines.append((title if k==0 else '',seq[k:k+COLS],ip,k))
RH=W+24+26+10
H=HDR+len(lines)*(RH+30)+60
o=Image.new('RGBA',(COLS*CW,H),(22,24,30,255));dr=ImageDraw.Draw(o)
dr.text((10,8),f'COMBO KIẾM MỚI — BẢNG KEY POSE ({tag}) theo Sword Combo Keyframe Guide',fill=(255,225,140),font=Ft)
dr.text((10,36),'Xanh lơ = tay xa (cầm kiếm) · hồng = tay gần · trắng = kiếm · vàng = đường mũi kiếm (chú thích, không phải VFX) · thanh màu: xanh=Khởi, đỏ=Ra đòn, lục=Hồi',fill=(170,180,195),font=F)
y=HDR;t_acc={}
for title,seq,ip,k0 in lines:
    if title:dr.text((10,y+4),title,fill=(255,255,255),font=Fb)
    y+=26
    allseq=[s for s in (A,B,C) if seq[0] in s][0]
    for i,(code,name,ms,ph,p) in enumerate(seq):
        gi=k0+i;t0=sum(s[2] for s in allseq[:gi])
        trail=[tipxy(allseq[j][4])['sword_tip'] for j in range(max(0,gi-3),gi+1)]
        cell(dr,o,i*CW,y,code,name,ms,ph,p,t0,trail,gi==ip-1 or (allseq is C and gi==3))
    y+=RH+4
dr.text((10,y+4),'Chuyển tiếp: cuối A (A7) = bắt đầu B (B1) = bắt đầu C (C1) cùng một thế đứng; cửa nối đòn mở ở A6–A7 và B6–B7. Tổng A+B+C = 1380 ms. C (+6) dài 640 ms bằng nhịp Phá Thế Trảm hiện có.',fill=(150,220,170),font=F)
o.crop((0,0,o.width,y+30)).save(f'{od}/KEYPOSE_COMBO_KIEM_{tag}.png');print('ok',tag)
