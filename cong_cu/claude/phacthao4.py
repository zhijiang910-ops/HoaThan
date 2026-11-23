import sys
P2=sys.argv[0].replace('phacthao4','phacthao2');src=open(P2).read();src=src[:src.index('B=[\n')];sys.argv[0]=P2
exec(src)
def M(P):return {k:(128-v[0],v[1]) for k,v in P.items()}   # quay người 180°: lật sprite
OPT=[
('COMBO SỬA · kiếm luôn ở trước người hoặc trên đầu, không bao giờ xuyên qua thân',[
 ('A1 kiếm thủ trước ngực',pose(lean=-1,farm=((3,3),(8,-2)),th=-40,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
 ('A2 quét ngang ra trước',pose(dx=2,lean=3,farm=((9,1),(19,2)),th=0,nleg=STEP[0],fleg=STEP[1]),[('ring',(66,112,46,10,170))]),
 ('A3 kết: kiếm chéo xuống trước',pose(dx=2,lean=3,farm=((7,4),(12,8)),th=35,nleg=STEP[0],fleg=STEP[1]),[]),
 ('B1 XOAY NGƯỜI (lật hướng)',M(pose(dx=-2,lean=-1,farm=((3,3),(8,-2)),th=-40,nleg=CROUCH[0],fleg=CROUCH[1])),[]),
 ('B2 quét ngang về phía sau',M(pose(dx=2,lean=3,farm=((9,1),(19,2)),th=0,nleg=STEP[0],fleg=STEP[1])),[('ring',(62,112,46,190,350))]),
 ('B3 kết: kiếm giơ chéo cao',M(pose(dx=2,lean=1,farm=((3,-8),(7,-16)),th=-60)),[]),
 ('C1 xoay lại, kiếm qua đầu',pose(dx=1,lean=1,farm=((-1,-11),(2,-20)),th=-100,nleg=STEP[0],fleg=STEP[1]),[('glow',(66,118,30))]),
 ('C2 vòng 1 quanh người',pose(dx=4,lean=4,farm=((9,1),(19,2)),th=0,nleg=LUNGE[0],fleg=LUNGE[1]),[('ring',(66,112,50,150,390))]),
 ('C3 lật hướng, vòng 2 rộng',M(pose(dx=4,lean=4,farm=((9,-2),(18,-4)),th=-15,nleg=LUNGE[0],fleg=LUNGE[1])),[('ring',(62,112,62,170,370)),('glow',(62,118,40))]),
 ('C4 xoay về, thu kiếm',pose(dx=2,lean=2,farm=((6,6),(11,13)),th=55),[])],
 'Nửa sau của vòng xoay = nhân vật QUAY NGƯỜI (lật hướng) rồi chém trước mặt, như mọi game 2D. Tay cầm kiếm luôn nhìn thấy, kiếm luôn đủ dài.'),
]
ims=[board2(str(i),b[1],b[0],b[2]) for i,b in enumerate(OPT)]
o=ims[0];o.save(sys.argv[1]+'/PHAC_THAO_COMBO_SUA.png');print(o.size)
