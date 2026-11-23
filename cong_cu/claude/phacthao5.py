import sys
P2=sys.argv[0].replace('phacthao5','phacthao2');src=open(P2).read();src=src[:src.index('B=[\n')];sys.argv[0]=P2
exec(src)
SH=(9,-3)  # vai xa - vai gần: tay gần nắm cùng chuôi (cầm 2 tay như clip)
def p2(farm,**k):
    e,w=farm;return pose(farm=farm,narm=((e[0]+SH[0]*.6,e[1]+SH[1]*.6+2),(w[0]+SH[0]-2,w[1]+SH[1]+2)),**k)
WIDE=(((8,9),(15,24)),((-8,9),(-15,24)));LONG=(((12,10),(20,24)),((-12,12),(-22,24)))
FX['afterimg']=lambda d,ox,oy,v:[draw_fig(d,p2(((10,4),(19,8)),dx=x,dy=5,lean=7,th=20,nleg=LONG[0],fleg=LONG[1]),ox,oy,col=(80,90,110),sw=(80,90,110)) for x in v]
FX['cleave']=lambda d,ox,oy,v:(d.arc((ox+(v[0]-v[2])*SC,oy+(v[1]-v[2])*SC,ox+(v[0]+v[2])*SC,oy+(v[1]+v[2])*SC),-80,70,fill=CY,width=14),d.arc((ox+(v[0]-v[2])*SC,oy+(v[1]-v[2])*SC,ox+(v[0]+v[2])*SC,oy+(v[1]+v[2])*SC),-75,65,fill=WH,width=4))
FX['crack']=lambda d,ox,oy,v:[d.line([(ox+v[0]*SC,oy+v[1]*SC),(ox+(v[0]+math.cos(math.radians(a))*24)*SC,oy+(v[1]+math.sin(math.radians(a))*6)*SC)],fill=(255,150,60),width=3) for a in(-170,-130,-50,-10)]
OPT=[
('ĐÒN A · Rút kiếm quét ngang, hạ tấn rộng (clip đòn 1)',[
 ('kiếm vác vai',pose(farm=((-3,-6),(-1,-12)),th=-165),[]),
 ('bước ra, rút kiếm',p2(((5,-4),(11,-8)),dx=2,lean=2,th=-15,nleg=STEP[0],fleg=STEP[1]),[]),
 ('quét ngang trước người',p2(((10,0),(20,0)),dx=4,dy=3,lean=3,th=0,nleg=WIDE[0],fleg=WIDE[1]),[('ring',(80,110,58,10,170))]),
 ('kết: tấn rộng, kiếm ngang',p2(((7,2),(14,2)),dx=4,dy=4,lean=1,th=-8,nleg=WIDE[0],fleg=WIDE[1]),[])],
 'Lao 0,5 thân. Vệt trăng phẳng sát đất trước mặt, rộng ~3 thân người.'),
('ĐÒN B · Nâng kiếm qua đầu, bổ xuống (clip đòn 2) — bắt đầu đúng thế tấn rộng của A',[
 ('nâng kiếm khỏi tấn',p2(((5,-6),(9,-13)),dx=4,dy=4,th=-60,nleg=WIDE[0],fleg=WIDE[1]),[]),
 ('kiếm qua đầu, 2 tay',p2(((1,-11),(4,-19)),dx=4,dy=3,lean=-1,th=-150,nleg=WIDE[0],fleg=WIDE[1]),[]),
 ('bước tới bổ xuống',p2(((9,-1),(17,3)),dx=9,dy=3,lean=5,th=55,nleg=STEP[0],fleg=STEP[1]),[('cleave',(98,70,40))]),
 ('kết thấp, kiếm sát đất',p2(((8,6),(15,12)),dx=10,dy=7,lean=6,th=25,nleg=WIDE[0],fleg=WIDE[1]),[('crack',(112,120))])],
 'Lao 1 thân. Vệt bổ dọc lớn + nứt đất, bụi văng ở điểm bổ.'),
('ĐÒN C (+9) · Xoay người lấy đà, lao đâm thấp (clip đòn 3) — bắt đầu đúng thế thấp của B',[
 ('từ thế thấp vòng kiếm lên',p2(((6,-2),(12,-6)),dx=0,dy=5,lean=2,th=-40,nleg=WIDE[0],fleg=WIDE[1]),[('ring',(66,112,52,150,390))]),
 ('kiếm vắt qua vai (lấy đà)',p2(((0,-6),(4,-12)),dx=0,dy=3,lean=-2,th=-160,nleg=CROUCH[0],fleg=CROUCH[1]),[('glow',(66,118,34))]),
 ('lao tới tấn dài',p2(((9,2),(17,4)),dx=12,dy=5,lean=7,th=10,nleg=LONG[0],fleg=LONG[1]),[('afterimg',(-16,-4)),('dash',(0,110,74,(200,220,240)))]),
 ('đâm thấp duỗi hết',p2(((10,4),(19,8)),dx=14,dy=6,lean=8,th=20,nleg=LONG[0],fleg=LONG[1]),[('ring',(100,112,60,170,370)),('flash',(122,74))])],
 'Xoay = vòng sáng quanh người (động tác không quay lưng). Lao 1,5 thân có dư ảnh, kết bằng vòng nổ + chớp tím.'),
]
ims=[board2(str(i),b[1],b[0],b[2]) for i,b in enumerate(OPT)]
W=max(i.width for i in ims);H=sum(i.height for i in ims)+10*len(ims);o=Image.new('RGB',(W,H),(18,18,22));y=0
for i in ims:o.paste(i,(0,y));y+=i.height+10
o.save(sys.argv[1]+'/PHAC_THAO_3DON_CLIP.png');print(o.size)
