import sys
P9=sys.argv[0].replace('phacthao10','phacthao9');src=open(P9).read();src=src[:src.index('D=[')];sys.argv[0]=P9
exec(src)
D=[('A · KHỞI KIẾM — chém ngang tại chỗ: rút kiếm từ hông sau, bước chân gần lên, kiếm quét ngang trước mặt · trăng khuyết trắng xanh bay ra',[
 ('thủ kiếm',pose(),[]),
 ('rút kiếm về hông sau, vặn người',pose(lean=-3,farm=((-5,6),(-12,9)),narm=BAL,th=170,nleg=STEP[0],fleg=STEP[1]),[]),
 ('QUÉT NGANG (trúng)',pose(dx=4,lean=4,farm=((9,0),(19,-1)),narm=BAL,th=5,nleg=STEPX[0],fleg=STEPX[1]),[('crescent',(100,62,17)),('trail',(70,72,34,-50,50,CY))]),
 ('thu kiếm, giữ thế',pose(dx=4,lean=2,farm=((7,3),(13,6)),narm=BAL,th=30,nleg=STEPX[0],fleg=STEPX[1]),[])],
 'Tay cầm kiếm ở tay xa, kiếm giữ đúng độ dài master. Vệt chém nằm TRƯỚC mặt, đúng hướng chém.'),
('B · HỒI KIẾM — chém ngược hất chéo lên: kiếm hạ thấp bên hông rồi hồi ngược từ dưới lên · trăng khuyết lớn mở ngược lên',[
 ('= cuối đòn A',pose(dx=4,lean=2,farm=((7,3),(13,6)),narm=BAL,th=30,nleg=STEPX[0],fleg=STEPX[1]),[]),
 ('hạ kiếm thấp, gối khuỵu',pose(dx=3,dy=3,lean=-1,farm=((6,10),(12,16)),narm=BAL,th=75,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
 ('HẤT CHÉO LÊN (trúng)',pose(dx=6,dy=1,lean=3,farm=((8,-6),(16,-12)),narm=FING,th=-45,nleg=STEPX[0],fleg=STEPX[1]),[('big',(86,56,36)),('trail',(72,76,34,-70,20,CY))]),
 ('kiếm giơ cao, thu',pose(dx=5,lean=1,farm=((5,-9),(9,-17)),narm=BAL,th=-95,nleg=STEPX[0],fleg=STEPX[1]),[])],
 'Nối liền từ A: kiếm đi từ thấp lên cao, nhịp trả ngược lại A để thành combo liền mạch.'),
('C (+6) · PHÁ THẾ TRẢM — khuỵu thấp tụ lực, bật dậy xoay chém: người KHÔNG lật sprite, vòng elip VFX lo cảm giác xoay',[
 ('= cuối đòn B',pose(dx=5,lean=1,farm=((5,-9),(9,-17)),narm=BAL,th=-95,nleg=STEPX[0],fleg=STEPX[1]),[]),
 ('khuỵu thấp, kiếm kéo sau lưng',pose(dy=6,lean=-2,farm=((-7,3),(-15,5)),narm=BAL,th=175,nleg=CROUCHL[0],fleg=CROUCHL[1]),[('glow',(66,118,30))]),
 ('QUÉT 360° (trúng)',pose(dx=2,dy=2,lean=2,farm=((10,1),(21,2)),narm=BAL,th=5,nleg=WIDE[0],fleg=WIDE[1]),[('ring',(66,112,58,150,390)),('ring',(66,108,44,160,380)),('glow',(66,118,36))]),
 ('kết thế, vòng tan',pose(dx=2,lean=1,farm=((7,4),(13,9)),narm=BAL,th=35,nleg=STEP[0],fleg=STEP[1]),[('glow',(66,118,24))])],
 'Vòng elip dày nhiều lớp (trước/giữa/sau nhân vật) trúng mọi phía. Quái bị đẩy lùi.')]
ims=[board2(str(i),b[1],b[0],b[2]) for i,b in enumerate(D)]
W=max(i.width for i in ims);o=Image.new('RGB',(W,sum(i.height+10 for i in ims)),(18,18,22));y=0
for i in ims:o.paste(i,(0,y));y+=i.height+10
o.save(sys.argv[1]+'/PHAC_THAO_COMBO_KIEM_MOI.png');print(o.size)
