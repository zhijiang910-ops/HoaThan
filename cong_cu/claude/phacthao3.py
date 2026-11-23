import sys
P2=sys.argv[0].replace('phacthao3','phacthao2');src=open(P2).read();src=src[:src.index('B=[\n')];sys.argv[0]=P2
exec(src)
OPT=[
('PHƯƠNG ÁN 1 · Xuống → Lên → Vòng',[
 ('A bổ chéo xuống',pose(dx=2,lean=4,farm=((8,-2),(15,-3)),th=10,nleg=STEP[0],fleg=STEP[1]),[('crescent',(96,62,16))]),
 ('A kết: kiếm thấp trước',pose(dx=2,lean=3,farm=((6,6),(11,13)),th=55),[]),
 ('B hất chéo lên (từ chỗ A dừng)',pose(dx=3,lean=2,farm=((6,-6),(10,-14)),th=-60,nleg=STEP[0],fleg=STEP[1]),[('sky',(100,118))]),
 ('B kết: kiếm giơ cao',pose(dx=3,lean=1,farm=((-1,-11),(2,-20)),th=-95),[]),
 ('C kéo xuống xoay vòng 1',pose(dx=3,lean=2,farm=((9,2),(19,4)),th=10,nleg=STEP[0],fleg=STEP[1]),[('ring',(66,112,50,150,390))]),
 ('C vòng 2 rộng hơn, kết',pose(dx=3,lean=3,farm=((6,6),(11,13)),th=55),[('ring',(66,112,62,170,370)),('glow',(66,118,40))])],
 'Mỗi đòn bắt đầu đúng chỗ đòn trước dừng. Hiệu ứng: 1 đường bay → 1 cột kiếm khí → cả vùng quanh người.'),
('PHƯƠNG ÁN 2 · Nửa vòng → Nửa vòng ngược → Trọn vòng  (tao đề xuất)',[
 ('A kiếm ra sau, vặn người',pose(lean=-2,farm=((-7,2),(-15,4)),th=175,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
 ('A quét ngang ra trước',pose(dx=2,lean=3,farm=((9,1),(19,2)),th=0,nleg=STEP[0],fleg=STEP[1]),[('ring',(66,112,46,10,170))]),
 ('A kết: kiếm vắt qua người',pose(dx=2,lean=2,farm=((2,4),(-6,6)),th=170),[]),
 ('B quét ngược tay về sau',pose(dx=3,lean=-1,farm=((-6,1),(-15,2)),th=180,nleg=STEP[0],fleg=STEP[1]),[('ring',(66,112,50,190,350))]),
 ('C theo đà xoay trọn vòng',pose(dx=3,lean=2,farm=((9,2),(19,4)),th=10,nleg=STEP[0],fleg=STEP[1]),[('ring',(66,112,50,150,390))]),
 ('C vòng 2 rộng hơn, kết',pose(dx=3,lean=3,farm=((6,6),(11,13)),th=55),[('ring',(66,112,62,170,370)),('glow',(66,118,40))])],
 'A chém nửa vòng phía trước, B chém nửa vòng phía sau, C ghép thành trọn vòng. Đà xoay cộng dồn, không lần nào phải lấy đà lại.'),
]
ims=[board2(str(i),b[1],b[0],b[2]) for i,b in enumerate(OPT)]
W=max(i.width for i in ims);H=sum(i.height for i in ims)+10*len(ims);o=Image.new('RGB',(W,H),(18,18,22));y=0
for i in ims:o.paste(i,(0,y));y+=i.height+10
o.save(sys.argv[1]+'/PHAC_THAO_AB_C.png');print(o.size)
