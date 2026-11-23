import sys,math
src=open(sys.argv[0].replace('phacthao2','phacthao')).read();src=src[:src.index('# ---------- các phương án')]
sys.argv=[sys.argv[0],sys.argv[1]];exec(src)
from PIL import Image,ImageDraw
CY=(170,235,255);WH=(250,252,255);PU=(190,140,255);RD=(255,110,90)
def ell(d,ox,oy,cx,cy,rx,ry,a0,a1,col,w):
    d.arc((ox+(cx-rx)*SC,oy+(cy-ry)*SC,ox+(cx+rx)*SC,oy+(cy+ry)*SC),a0,a1,fill=col,width=w)
def crescent(d,ox,oy,x,y,s,col):
    d.arc((ox+(x-s)*SC,oy+(y-s*1.4)*SC,ox+(x+s)*SC,oy+(y+s*1.4)*SC),-70,70,fill=col,width=9);d.arc((ox+(x-s)*SC,oy+(y-s*1.4)*SC,ox+(x+s)*SC,oy+(y+s*1.4)*SC),-60,60,fill=WH,width=3)
FX={
 'crescent':lambda d,ox,oy,v:crescent(d,ox,oy,*v,CY),
 'sky':lambda d,ox,oy,v:(d.line([(ox+v[0]*SC-30,oy+0),(ox+v[0]*SC,oy+v[1]*SC)],fill=CY,width=14),d.line([(ox+v[0]*SC-30,oy+0),(ox+v[0]*SC,oy+v[1]*SC)],fill=WH,width=5)),
 'ring':lambda d,ox,oy,v:(ell(d,ox,oy,v[0],v[1],v[2],v[2]*0.38,v[3],v[4],CY,12),ell(d,ox,oy,v[0],v[1],v[2],v[2]*0.38,v[3],v[4],WH,4)),
 'glow':lambda d,ox,oy,v:d.ellipse((ox+(v[0]-v[2])*SC,oy+(v[1]-v[2]*0.4)*SC,ox+(v[0]+v[2])*SC,oy+(v[1]+v[2]*0.4)*SC),outline=PU,width=3),
 'dash':lambda d,ox,oy,v:(d.line([(ox+v[0]*SC,oy+v[2]*SC),(ox+v[1]*SC,oy+v[2]*SC)],fill=v[3],width=10),d.line([(ox+v[0]*SC+20,oy+v[2]*SC),(ox+v[1]*SC,oy+v[2]*SC)],fill=WH,width=3)),
 'flash':lambda d,ox,oy,v:[d.line([(ox+v[0]*SC,oy+v[1]*SC),(ox+(v[0]+math.cos(a)*12)*SC,oy+(v[1]+math.sin(a)*12)*SC)],fill=PU,width=4) for a in [i*math.pi/4 for i in range(8)]],
 'ghost':lambda d,ox,oy,v:[draw_fig(d,pose(dx=k,dy=3,lean=6,farm=((10,1),(20,2)),th=-5,nleg=LUNGE[0],fleg=LUNGE[1]),ox,oy,col=(80,90,110),sw=(80,90,110)) for k in v],
}
def board2(key,keys,title,note):
    W=len(keys)*270+20;H=330;o=Image.new('RGB',(W,H),(32,34,40));d=ImageDraw.Draw(o)
    d.text((12,8),title,fill=(255,224,150),font=F);d.text((12,H-24),note,fill=(200,200,205),font=Fs)
    for i,(lab,P,fx) in enumerate(keys):
        ox=10+i*270;oy=34;ground(d,ox,oy,256)
        back=[f for f in fx if f[0] in('ring','glow','ghost')];front=[f for f in fx if f not in back]
        for k,v in back:FX[k](d,ox,oy,v)
        draw_fig(d,P,ox,oy)
        for k,v in front:FX[k](d,ox,oy,v)
        d.text((ox+4,oy+250),f'{i+1}. {lab}',fill='white',font=Fs)
    return o
B=[
('A · Chém tới, trăng khuyết bay ra (video ảnh 3)',[
 ('A1 giơ kiếm',pose(farm=((-2,-11),(2,-20)),th=-100),[]),
 ('A2 bổ chéo xuống',pose(dx=2,lean=4,farm=((8,-2),(15,-3)),th=10,nleg=STEP[0],fleg=STEP[1]),[('crescent',(96,62,16))]),
 ('A3 trăng bay xa ~1,5 thân',pose(dx=2,lean=3,farm=((6,6),(11,13)),th=55),[('crescent',(118,64,14))])],
 'Giữ động tác A hiện có. Thêm trăng khuyết trắng xanh bay về trước, xuyên quái trên đường đi.'),
('B · Hất lên, kiếm khí dọc giáng xuống (video ảnh 2)',[
 ('B1 kéo kiếm sau hông',pose(lean=-2,farm=((-5,9),(-11,13)),th=165),[]),
 ('B2 hất kiếm lên trời',pose(dx=2,lean=1,farm=((3,-10),(6,-19)),th=-80,nleg=STEP[0],fleg=STEP[1]),[('sky',(78,30))]),
 ('B3 kiếm khí giáng trước mặt',pose(dx=1,lean=1,farm=((6,8),(11,15)),th=60),[('sky',(100,118))])],
 'Giữ động tác B. Đổi hiệu ứng: một luồng kiếm khí dọc từ trên trời đâm xuống ngay trước mặt, choáng ngắn.'),
('C (+9) · Xoay chém, vòng sáng ẹp sát mặt đất (video ảnh 4, 6)',[
 ('C1 vặn người lấy đà',pose(lean=-2,farm=((-7,2),(-15,4)),th=175,nleg=CROUCH[0],fleg=CROUCH[1]),[('glow',(66,118,30))]),
 ('C2 xoay chém một vòng',pose(dx=2,lean=2,farm=((9,2),(19,4)),th=10,nleg=STEP[0],fleg=STEP[1]),[('ring',(66,112,50,150,390))]),
 ('C3 vòng 2 rộng hơn, kết',pose(dx=2,lean=3,farm=((6,6),(11,13)),th=55),[('ring',(66,112,62,170,370)),('glow',(66,118,40))])],
 'Nhát kết: hai vòng sáng trắng xanh nằm phẳng trên đất quanh người, ánh tím dưới chân, trúng mọi phía, quái tóe lửa.'),
('Lướt Trảm · Lướt xuyên qua đám quái (video ảnh 1, 5)',[
 ('L1 hạ người',pose(dx=-2,dy=3,lean=-2,farm=((-5,9),(-12,13)),th=160,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
 ('L2 lướt xuyên, để bóng mờ',pose(dx=14,dy=3,lean=6,farm=((10,1),(20,2)),th=-5,nleg=LUNGE[0],fleg=LUNGE[1]),[('ghost',(-30,-12)),('dash',(0,120,70,(200,220,240)))]),
 ('L3 dừng ở đích, chớp tím',pose(dx=14,farm=((6,6),(11,13)),th=60),[('flash',(112,66)),('dash',(0,96,70,RD))])],
 'Lướt xuyên 1 đoạn, mọi quái trên đường bị chém. Vệt trắng dài + bóng mờ, ở đích chớp tím, quái sau lưng tóe máu đỏ.'),
]
ims=[board2(str(i),b[1],b[0],b[2]) for i,b in enumerate(B)]
W=max(i.width for i in ims);H=sum(i.height for i in ims)+10*len(ims);o=Image.new('RGB',(W,H),(18,18,22));y=0
for i in ims:o.paste(i,(0,y));y+=i.height+10
o.save(sys.argv[1]+'/PHAC_THAO_THEO_VIDEO.png');print(o.size)
