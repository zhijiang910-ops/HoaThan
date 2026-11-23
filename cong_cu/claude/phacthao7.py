import sys
P2=sys.argv[0].replace('phacthao7','phacthao2');src=open(P2).read();src=src[:src.index('B=[\n')];sys.argv[0]=P2
exec(src)
LUNGE2=(((12,8),(19,25)),((-13,12),(-24,23)));DEEP=(((13,7),(21,23)),((-15,11),(-27,21)))
STEPX=(((5,12),(9,28)),((-3,14),(-5,30)));KICK=(((5,12),(8,29)),((-9,12),(-22,18)))
FING=((6,6),(13,2))      # tay không cầm kiếm: kiếm chỉ ra trước
BAL=((-6,6),(-13,7))     # tay không cầm kiếm: giữ thăng bằng phía sau
FX['cleave']=lambda d,ox,oy,v:(d.arc((ox+(v[0]-v[2])*SC,oy+(v[1]-v[2])*SC,ox+(v[0]+v[2])*SC,oy+(v[1]+v[2])*SC),-80,70,fill=CY,width=14),d.arc((ox+(v[0]-v[2])*SC,oy+(v[1]-v[2])*SC,ox+(v[0]+v[2])*SC,oy+(v[1]+v[2])*SC),-75,65,fill=WH,width=4))
FX['crack']=lambda d,ox,oy,v:[d.line([(ox+v[0]*SC,oy+v[1]*SC),(ox+(v[0]+math.cos(math.radians(a))*24)*SC,oy+(v[1]+math.sin(math.radians(a))*6)*SC)],fill=(255,150,60),width=3) for a in(-170,-130,-50,-10)]
FX['afterimg']=lambda d,ox,oy,v:[draw_fig(d,pose(dx=x,dy=6,lean=5,farm=((4,8),(8,16)),narm=BAL,th=10,nleg=LUNGE2[0],fleg=LUNGE2[1]),ox,oy,col=(80,90,110),sw=(80,90,110)) for x in v]
A5=dict(dx=5,dy=7,lean=1,farm=((6,2),(12,-2)),narm=FING,th=-30,nleg=LUNGE2[0],fleg=LUNGE2[1])
B6=dict(dx=11,dy=10,lean=5,farm=((7,8),(13,16)),narm=BAL,th=15,nleg=DEEP[0],fleg=DEEP[1])
D=[
('ĐÒN A · 5 khung · rút kiếm quét ngang → tấn cung (lao 0,5 thân)',[
 ('thủ kiếm thấp',pose(farm=((4,10),(8,20)),narm=FING,th=40),[]),
 ('bước ra, kiếm lên ngang đầu',pose(dx=2,dy=3,lean=1,farm=((5,-6),(12,-10)),narm=BAL,th=-10,nleg=STEPX[0],fleg=STEPX[1]),[]),
 ('QUÉT NGANG ngực (trúng)',pose(dx=4,dy=6,lean=3,farm=((9,-1),(19,-1)),narm=BAL,th=0,nleg=LUNGE2[0],fleg=LUNGE2[1]),[('ring',(86,110,58,10,170))]),
 ('theo đà',pose(dx=5,dy=7,lean=2,farm=((8,3),(15,6)),narm=BAL,th=20,nleg=LUNGE2[0],fleg=LUNGE2[1]),[]),
 ('kết: tấn cung, kiếm chỉ',pose(**A5),[])],'Vệt trăng phẳng sát đất trước mặt, rộng ~3 thân.'),
('ĐÒN B · 6 khung · khung đầu = khung cuối A · nâng qua đầu → bổ → kiếm sát đất (lao 1 thân)',[
 ('= cuối đòn A',pose(**A5),[]),
 ('nâng kiếm qua đầu',pose(dx=6,dy=4,farm=((1,-10),(4,-19)),narm=FING,th=-150,nleg=STEPX[0],fleg=STEPX[1]),[]),
 ('bước tới, kiếm trên đầu',pose(dx=8,dy=2,lean=1,farm=((2,-11),(6,-20)),narm=BAL,th=-178,nleg=STEPX[0],fleg=STEPX[1]),[]),
 ('BỔ ngang tầm đầu (trúng)',pose(dx=11,dy=6,lean=4,farm=((9,-6),(18,-8)),narm=BAL,th=8,nleg=LUNGE2[0],fleg=LUNGE2[1]),[('cleave',(110,64,40))]),
 ('kéo xuống ngực',pose(dx=11,dy=8,lean=4,farm=((8,2),(15,6)),narm=BAL,th=35,nleg=LUNGE2[0],fleg=LUNGE2[1]),[]),
 ('kết: tấn sâu, kiếm sát đất',pose(**B6),[('crack',(124,120))])],'Vệt bổ lớn, nứt đất ở điểm kết.'),
('ĐÒN C (+9) · 7 khung · khung đầu = khung cuối B · vòng kiếm → vắt vai → lao → đâm thấp (lao 1,5 thân)',[
 ('= cuối đòn B',pose(**B6),[]),
 ('vòng kiếm ngang hông',pose(dx=11,dy=7,lean=2,farm=((5,6),(11,10)),narm=BAL,th=0,nleg=STEPX[0],fleg=STEPX[1]),[('ring',(77,112,52,150,390))]),
 ('gập 20°, kiếm vắt vai',pose(dx=11,dy=5,lean=5,farm=((3,-4),(6,-10)),narm=FING,th=-115,nleg=KICK[0],fleg=KICK[1]),[('glow',(77,118,34))]),
 ('lao tấn cung',pose(dx=16,dy=6,lean=5,farm=((4,8),(8,16)),narm=BAL,th=10,nleg=LUNGE2[0],fleg=LUNGE2[1]),[('afterimg',(4,10)),('dash',(10,110,74,(200,220,240)))]),
 ('ĐÂM THẤP (trúng)',pose(dx=19,dy=9,lean=7,farm=((8,8),(15,14)),narm=BAL,th=25,nleg=DEEP[0],fleg=DEEP[1]),[('ring',(110,112,60,170,370)),('flash',(127,98))]),
 ('giữ thế',pose(dx=19,dy=9,lean=6,farm=((8,8),(15,14)),narm=BAL,th=25,nleg=DEEP[0],fleg=DEEP[1]),[]),
 ('thu về đứng',pose(dx=19,farm=((4,10),(8,20)),narm=FING,th=40),[])],'Xoay = vòng sáng quanh người. Dư ảnh khi lao, kết bằng vòng nổ + chớp tím.'),
]
ims=[board2(str(i),b[1],b[0],b[2]) for i,b in enumerate(D)]
W=max(i.width for i in ims);o=Image.new('RGB',(W,sum(i.height+10 for i in ims)),(18,18,22));y=0
for i in ims:o.paste(i,(0,y));y+=i.height+10
o.save(sys.argv[1]+'/PHAC_THAO_CHOT.png');print(o.size)
