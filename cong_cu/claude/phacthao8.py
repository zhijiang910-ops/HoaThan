import sys,subprocess
P2=sys.argv[0].replace('phacthao8','phacthao2');src=open(P2).read();src=src[:src.index('B=[\n')];sys.argv[0]=P2
exec(src)
WIDE=(((10,10),(15,27)),((-10,10),(-15,27)))
BAL=((-6,6),(-13,7))
def whirl(d,ox,oy,v):
    cx,cy,rx,a0,a1,front=v
    bb=(ox+(cx-rx)*SC,oy+(cy-rx*0.32)*SC,ox+(cx+rx)*SC,oy+(cy+rx*0.32)*SC)
    d.arc(bb,a0,a1,fill=CY,width=9);d.arc(bb,a0,a1,fill=WH,width=3)
def swoosh(d,ox,oy,v):
    cx,cy,r=v;bb=(ox+(cx-r)*SC,oy+(cy-r*0.55)*SC,ox+(cx+r)*SC,oy+(cy+r*0.55)*SC)
    d.arc(bb,20,160,fill=CY,width=16);d.arc(bb,30,150,fill=WH,width=5)
FX['wback']=lambda d,ox,oy,v:whirl(d,ox,oy,(*v,180,360,0))
FX['wfront']=lambda d,ox,oy,v:whirl(d,ox,oy,(*v,0,180,1))
FX['swoosh']=swoosh
MOV='/root/.claude/uploads/f578bff3-154a-5e94-b344-26c188d551d1/3b4e5485-ScreenRecording_11-22-2026_01-27-45_1.mov'
B6=dict(dx=0,dy=10,lean=5,farm=((9,6),(17,11)),narm=BAL,th=40,nleg=(((13,7),(21,23))),fleg=((-15,11),(-27,21)))
K=[
 (6.20,'= cuối đòn B',pose(**B6),[]),
 (6.15,'đứng tấn, kiếm duỗi ngang ra sau',pose(dy=5,farm=((-8,0),(-17,1)),narm=((6,4),(12,2)),th=180,nleg=WIDE[0],fleg=WIDE[1]),[]),
 (6.30,'XOAY: kiếm quét ngang ra trước (trúng)',pose(dx=1,dy=5,lean=2,farm=((9,0),(19,0)),narm=BAL,th=0,nleg=WIDE[0],fleg=WIDE[1]),[('wback',(66,82,52)),('wfront',(66,82,52)),('swoosh',(70,112,60))]),
 (6.35,'xoay tiếp: kiếm ngang ra sau',pose(dx=1,dy=5,farm=((-8,0),(-17,1)),narm=((6,4),(12,2)),th=180,nleg=WIDE[0],fleg=WIDE[1]),[('wback',(66,82,58)),('wfront',(66,82,58))]),
 (6.45,'vòng 2 rộng hơn (trúng)',pose(dx=2,dy=5,lean=2,farm=((9,0),(19,0)),narm=BAL,th=0,nleg=WIDE[0],fleg=WIDE[1]),[('wback',(66,82,64)),('wfront',(66,82,64)),('swoosh',(72,114,70))]),
 (7.20,'thu kiếm về thế đứng',pose(dx=2),[]),
]
times=[0.05,0.0,6.30,6.40,7.25,7.45]
sk=board2('x',[(l,P,fx) for _,l,P,fx in K],'ĐÒN C (+9) · CHÉM LỐC: đứng tấn xoay tại chỗ 2 vòng, dải lốc trắng-xanh quấn ngang hông','Nửa sau vòng elip vẽ sau người, nửa trước đè lên người (như clip). Trúng mọi phía quanh người, không lao.')
top=Image.new('RGB',(sk.width,280),(24,24,28));idx=[None,0,126,128,144,148]
for i,f in enumerate(idx):
    if f is None:continue
    top.paste(Image.open('/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/ref6/c%03d.png'%(f+1)).crop((150,100,650,490)).resize((256,200)),(10+i*270,40))
ImageDraw.Draw(top).text((12,8),'Clip (khung tương ứng)',fill=(255,224,150),font=F)
o=Image.new('RGB',(sk.width,sk.height+280));o.paste(top,(0,0));o.paste(sk,(0,280))
o.save(sys.argv[1]+'/PHAC_THAO_C_LOC.png');print(o.size)
