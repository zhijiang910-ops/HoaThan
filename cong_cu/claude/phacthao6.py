import sys,subprocess
P2=sys.argv[0].replace('phacthao6','phacthao2');src=open(P2).read();src=src[:src.index('B=[\n')];sys.argv[0]=P2
exec(src)
MOV='/root/.claude/uploads/f578bff3-154a-5e94-b344-26c188d551d1/50a000de-v15044gf0000d7ccta7og65jf689vqsg.mov'
SH=(9,-3)
def p2(farm,**k):
    e,w=farm;return pose(farm=farm,narm=((e[0]+SH[0]*.6,e[1]+SH[1]*.6+2),(w[0]+SH[0]-2,w[1]+SH[1]+2)),**k)
HORSE=(((14,7),(21,22)),((-14,7),(-21,22)))          # tấn mã bộ: hông hạ 10, 2 gối mở rộng
LUNGE2=(((12,8),(19,25)),((-13,12),(-24,23)))         # tấn cung dài: gối trước gập, chân sau duỗi
STEPX=(((5,12),(9,28)),((-3,14),(-5,30)))
KICK=(((5,12),(8,29)),((-9,12),(-22,18)))             # chân sau đá lên khi gập người
FX['crack']=lambda d,ox,oy,v:[d.line([(ox+v[0]*SC,oy+v[1]*SC),(ox+(v[0]+math.cos(math.radians(a))*24)*SC,oy+(v[1]+math.sin(math.radians(a))*6)*SC)],fill=(255,150,60),width=3) for a in(-170,-130,-50,-10)]
FX['afterimg']=lambda d,ox,oy,v:[draw_fig(d,p2(((3,10),(7,20)),dx=x,dy=6,lean=5,th=15,nleg=LUNGE2[0],fleg=LUNGE2[1]),ox,oy,col=(80,90,110),sw=(80,90,110)) for x in v]
FX['cleave']=lambda d,ox,oy,v:(d.arc((ox+(v[0]-v[2])*SC,oy+(v[1]-v[2])*SC,ox+(v[0]+v[2])*SC,oy+(v[1]+v[2])*SC),-80,70,fill=CY,width=14),d.arc((ox+(v[0]-v[2])*SC,oy+(v[1]-v[2])*SC,ox+(v[0]+v[2])*SC,oy+(v[1]+v[2])*SC),-75,65,fill=WH,width=4))
D=[
('ĐÒN A · rút kiếm quét ngang → tấn mã bộ',[
 (1.20,'kiếm vác vai',pose(farm=((-3,-6),(-1,-12)),th=-165),[]),
 (1.55,'bước ra, 2 tay nâng kiếm ngang đầu',p2(((4,-8),(10,-14)),dx=2,dy=3,lean=1,th=-5,nleg=STEPX[0],fleg=STEPX[1]),[]),
 (1.80,'quét ngang ngang ngực, hạ người',p2(((9,-2),(18,-3)),dx=4,dy=6,lean=2,th=0,nleg=LUNGE2[0],fleg=LUNGE2[1]),[('ring',(84,110,58,10,170))]),
 (2.10,'tấn mã bộ, kiếm chếch lên trước ngực',p2(((5,6),(10,3)),dx=4,dy=10,th=-35,nleg=HORSE[0],fleg=HORSE[1]),[])],'Lao 0,5 thân. Vệt trăng phẳng sát đất trước mặt.'),
('ĐÒN B · nâng kiếm qua đầu → bước tới bổ → hạ tấn kiếm sát đất',[
 (3.30,'giữ tấn, 2 tay giơ kiếm qua đầu',p2(((1,-11),(4,-20)),dx=4,dy=10,th=-155,nleg=HORSE[0],fleg=HORSE[1]),[]),
 (3.60,'bước tới, kiếm vẫn trên đầu',p2(((2,-12),(6,-21)),dx=8,dy=2,lean=1,th=-178,nleg=STEPX[0],fleg=STEPX[1]),[]),
 (3.80,'bổ: kiếm ngang tầm đầu chém tới',p2(((9,-6),(18,-8)),dx=11,dy=7,lean=4,th=8,nleg=LUNGE2[0],fleg=LUNGE2[1]),[('cleave',(110,64,40))]),
 (3.90,'kiếm chém tiếp xuống ngực',p2(((8,2),(15,6)),dx=11,dy=9,lean=4,th=35,nleg=LUNGE2[0],fleg=LUNGE2[1]),[]),
 (4.20,'tấn mã bộ thấp, kiếm sát đất',p2(((5,10),(9,20)),dx=11,dy=12,lean=2,th=10,nleg=HORSE[0],fleg=HORSE[1]),[('crack',(124,120))])],'Lao 1 thân. Vệt bổ lớn + nứt đất ở điểm kết.'),
('ĐÒN C (+9) · kiếm ngang hông → gập người vắt vai → lao tấn dài → đâm thấp',[
 (5.05,'kiếm ngang hông, xoay người',p2(((3,10),(8,20)),dx=0,dy=5,lean=1,th=0,nleg=STEPX[0],fleg=STEPX[1]),[('ring',(66,112,52,150,390))]),
 (5.30,'gập người, kiếm vắt vai, chân sau đá lên',p2(((2,-2),(5,-6)),dx=2,dy=4,lean=7,th=-125,nleg=KICK[0],fleg=KICK[1]),[('glow',(66,118,34))]),
 (6.55,'lao tấn dài, 2 tay ở hông',p2(((3,10),(7,20)),dx=12,dy=6,lean=5,th=15,nleg=LUNGE2[0],fleg=LUNGE2[1]),[('afterimg',(-16,-4)),('dash',(0,110,74,(200,220,240)))]),
 (6.95,'tấn cung sâu, đâm chếch xuống đất',p2(((6,10),(12,18)),dx=14,dy=10,lean=8,th=28,nleg=LUNGE2[0],fleg=LUNGE2[1]),[('ring',(104,112,60,170,370)),('flash',(124,96))])],'Xoay = vòng sáng (không vẽ quay lưng). Lao 1,5 thân có dư ảnh, kết bằng vòng nổ.'),
]
rows=[]
for title,keys,note in D:
    sk=board2('x',[(l,P,fx) for _,l,P,fx in keys],title,note)
    top=Image.new('RGB',(sk.width,330),(24,24,28))
    for i,(t,_,_,_) in enumerate(keys):
        subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(t),'-i',MOV,'-frames:v','1','/tmp/_k.png'])
        top.paste(Image.open('/tmp/_k.png').crop((0,200,576,1000)).resize((232,322)),(22+i*270,4))
    r=Image.new('RGB',(sk.width,sk.height+330));r.paste(top,(0,0));r.paste(sk,(0,330));rows.append(r)
W=max(r.width for r in rows);o=Image.new('RGB',(W,sum(r.height+10 for r in rows)),(10,10,12));y=0
for r in rows:o.paste(r,(0,y));y+=r.height+10
o.save(sys.argv[1]+'/SO_CLIP_PHACTHAO.png');print(o.size)
