import sys
P2=sys.argv[0].replace('phacthao9','phacthao8');src=open(P2).read();src=src[:src.index('MOV=')];sys.argv[0]=P2.replace('phacthao8','phacthao2')
exec(src.replace("P2=sys.argv[0].replace('phacthao8','phacthao2')","P2=sys.argv[0]"))
FING=((6,6),(13,2));STEPX=(((5,12),(9,28)),((-3,14),(-5,30)))
LUNGEL=(((14,6),(22,22)),((-16,10),(-29,19)));CROUCHL=(((11,8),(18,24)),((-12,10),(-21,22)))
YE=(255,220,120);OR=(255,130,90)
def trail(d,ox,oy,v):
    cx,cy,r,a0,a1,col=v;bb=(ox+(cx-r)*SC,oy+(cy-r)*SC,ox+(cx+r)*SC,oy+(cy+r)*SC)
    d.arc(bb,a0,a1,fill=col,width=6)
def streak(d,ox,oy,v):
    x0,x1,y=v
    for dy,w in((0,4),(-5,2),(5,2)):d.line([(ox+x0*SC,oy+(y+dy)*SC),(ox+x1*SC,oy+(y+dy*1.4)*SC)],fill=(255,240,200),width=w)
def big(d,ox,oy,v):
    cx,cy,r=v;bb=(ox+(cx-r)*SC,oy+(cy-r)*SC,ox+(cx+r)*SC,oy+(cy+r)*SC)
    d.arc(bb,-60,95,fill=YE,width=18);d.arc(bb,-50,85,fill=(255,252,225),width=7)
FX['trail']=trail;FX['streak']=streak;FX['big']=big
D=[('A · LAO ĐÂM: hạ thấp lao tới, kiếm duỗi thẳng trước · vệt kiếm vòng sau lưng (đỏ→vàng) + tia đâm ngang',[
 ('thủ kiếm',pose(),[]),
 ('kéo kiếm lên vai, nhún',pose(dy=4,lean=1,farm=((3,-9),(8,-15)),narm=FING,th=-40,nleg=CROUCH[0],fleg=CROUCH[1]),[('trail',(66,78,40,200,290,OR))]),
 ('LAO ĐÂM thấp (trúng)',pose(dx=8,dy=9,lean=8,farm=((10,1),(21,1)),narm=BAL,th=0,nleg=LUNGEL[0],fleg=LUNGEL[1]),[('trail',(70,80,46,150,300,OR)),('trail',(70,80,46,300,330,YE)),('streak',(92,128,72))]),
 ('giữ thế, thu',pose(dx=8,dy=7,lean=5,farm=((8,4),(15,8)),narm=BAL,th=25,nleg=LUNGEL[0],fleg=LUNGEL[1]),[])],'Giống ảnh 1: người gần sát đất, kiếm duỗi ngang chĩa vào quái.'),
('B · CHÉM VÒNG XUỐNG: từ thế đâm vung kiếm lên rồi chém vòng xuống trước · trăng lớn vàng-trắng',[
 ('= cuối đòn A',pose(dx=8,dy=7,lean=5,farm=((8,4),(15,8)),narm=BAL,th=25,nleg=LUNGEL[0],fleg=LUNGEL[1]),[]),
 ('vung kiếm lên chéo trước',pose(dx=6,dy=4,lean=1,farm=((7,-8),(13,-14)),narm=FING,th=-60,nleg=STEPX[0],fleg=STEPX[1]),[]),
 ('CHÉM VÒNG XUỐNG, khụy thấp (trúng)',pose(dx=9,dy=9,lean=6,farm=((9,3),(16,9)),narm=BAL,th=45,nleg=CROUCHL[0],fleg=CROUCHL[1]),[('big',(84,82,38)),('trail',(70,80,50,180,250,OR))]),
 ('kết thấp',pose(dx=9,dy=10,lean=5,farm=((9,6),(17,11)),narm=BAL,th=40,nleg=CROUCHL[0],fleg=CROUCHL[1]),[])],'Giống ảnh 2: người khụy, trăng lớn quét từ trên xuống sát đất trước mặt.'),
]
ims=[board2(str(i),b[1],b[0],b[2]) for i,b in enumerate(D)]
W=max(i.width for i in ims);o=Image.new('RGB',(W,sum(i.height+10 for i in ims)),(18,18,22));y=0
for i in ims:o.paste(i,(0,y));y+=i.height+10
o.save(sys.argv[1]+'/PHAC_THAO_AB_ANH.png');print(o.size)
