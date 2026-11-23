"""Bản phác thảo combo: người que + kiếm + đường đi VFX cho từng phương án đòn C / Lướt Trảm. Không gọi PixelLab."""
import json,math,sys
from PIL import Image,ImageDraw,ImageFont
OUT=sys.argv[1];N=128;SC=2
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15);Fs=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
B=json.load(open('/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/pl/xt_nam_rigB_body.json'))
R0={p['label']:(p['x']*N,p['y']*N) for p in B['first_frame_keypoints']};par={j['name']:j['parent'] for j in B['rig']};names=[j['name'] for j in B['rig']]
sub=lambda a,b:(a[0]-b[0],a[1]-b[1]);add=lambda a,b:(a[0]+b[0],a[1]+b[1])
off={n:sub(R0[n],R0[par[n]]) for n in names if par[n]};SL=math.dist(R0['sword_grip'],R0['sword_tip'])
def pose(dx=0,dy=0,lean=0,farm=None,narm=None,nleg=None,fleg=None,th=None,turn=0):
    P={'hips':add(R0['hips'],(dx,dy))}
    for n in names:
        if n=='hips' or n.startswith('sword'):continue
        o=off[n]
        if turn and n in('near_shoulder','far_shoulder','near_hip','far_hip'):o=(o[0]*(1-2*turn),o[1])  # quay lưng: đổi vai
        if n in('chest','neck','head'):o=(o[0]+lean*{'chest':.5,'neck':.4,'head':.3}[n],o[1])
        for k,v,base in (('far_elbow',farm,'far_shoulder'),('far_wrist',farm,'far_shoulder'),('near_elbow',narm,'near_shoulder'),('near_wrist',narm,'near_shoulder')):
            pass
        if n=='far_elbow' and farm:P[n]=add(P['far_shoulder'],farm[0]);continue
        if n=='far_wrist' and farm:P[n]=add(P['far_shoulder'],farm[1]);continue
        if n=='near_elbow' and narm:P[n]=add(P['near_shoulder'],narm[0]);continue
        if n=='near_wrist' and narm:P[n]=add(P['near_shoulder'],narm[1]);continue
        if n=='near_knee' and nleg:P[n]=add(P['near_hip'],nleg[0]);continue
        if n=='near_ankle' and nleg:P[n]=add(P['near_hip'],nleg[1]);continue
        if n=='far_knee' and fleg:P[n]=add(P['far_hip'],fleg[0]);continue
        if n=='far_ankle' and fleg:P[n]=add(P['far_hip'],fleg[1]);continue
        P[n]=add(P[par[n]],o)
    g=P['far_wrist'];t=math.radians(th if th is not None else 45);P['sword_tip']=(g[0]+math.cos(t)*SL,g[1]+math.sin(t)*SL);P['sword_grip']=g
    return P
STEP=(((6,14),(10,30)),((-6,16),(-12,31)));LUNGE=(((11,11),(18,27)),((-10,15),(-19,28)));CROUCH=(((5,13),(9,28)),((-4,15),(-8,30)))
AIR=(((8,6),(4,20)),((-2,8),(-10,18)))
def draw_fig(d,P,ox,oy,col=(230,230,240),sw=(255,255,255)):
    T=lambda p:(ox+p[0]*SC,oy+p[1]*SC)
    for n in names:
        if par[n] and not n.startswith('sword') and not n.startswith('hair'):
            c=(120,200,255) if n.startswith('far') else (255,140,200) if n.startswith('near') else col
            d.line([T(P[par[n]]),T(P[n])],fill=c,width=5)
    h=T(P['head']);d.ellipse((h[0]-11,h[1]-11,h[0]+11,h[1]+11),outline=col,width=4)
    d.line([T(P['sword_grip']),T(P['sword_tip'])],fill=sw,width=4)
def vfx_arc(d,cx,cy,r,a0,a1,ox,oy,col=(255,214,90),w=10,core=(255,250,220)):
    """vệt chém lưỡi liềm: góc a0→a1 (độ), tâm (cx,cy) theo toạ độ khung 128"""
    bb=(ox+(cx-r)*SC,oy+(cy-r)*SC,ox+(cx+r)*SC,oy+(cy+r)*SC);s,e=(a0,a1) if a0<a1 else (a1,a0)
    d.arc(bb,s,e,fill=col,width=w);d.arc(bb,s,e,fill=core,width=max(2,w//3))
def arrow(d,p0,p1,ox,oy,col=(255,120,80)):
    a=(ox+p0[0]*SC,oy+p0[1]*SC);b=(ox+p1[0]*SC,oy+p1[1]*SC);d.line([a,b],fill=col,width=3)
    ang=math.atan2(b[1]-a[1],b[0]-a[0])
    for s in(2.6,-2.6):d.line([b,(b[0]+12*math.cos(ang+s),b[1]+12*math.sin(ang+s))],fill=col,width=3)
def ground(d,ox,oy,W):d.line([(ox,oy+120*SC),(ox+W,oy+120*SC)],fill=(90,100,115),width=2)
# ---------- các phương án ----------
A_keys=[('A1 giơ kiếm',pose(farm=((-2,-11),(2,-20)),th=-100),[]),
        ('A2 bổ chéo xuống',pose(dx=2,lean=4,farm=((8,-2),(15,-3)),th=10,nleg=STEP[0],fleg=STEP[1]),[('arc',(70,62,34,-80,40))]),
        ('A3 kết: kiếm thấp trước',pose(dx=2,lean=3,farm=((6,6),(11,13)),th=55),[])]
B_keys=[('B1 kéo kiếm sau hông',pose(lean=-2,farm=((-5,9),(-11,13)),th=165),[]),
        ('B2 hất ngược lên + đâm',pose(dx=3,lean=4,farm=((9,1),(19,0)),th=-5,nleg=STEP[0],fleg=STEP[1]),[('arc',(72,70,30,100,200)),('arc',(72,70,30,-20,10))]),
        ('B3 kết: thủ thấp',pose(dx=1,lean=1,farm=((6,8),(11,15)),th=60),[])]
PA={
'C1':('C1 · Chém ngang vòng rộng (bản PixelLab vừa làm)',[
  ('lấy đà, kiếm qua vai',pose(dx=-2,lean=-3,farm=((-6,-6),(-12,-12)),th=-150,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
  ('chém ngang duỗi tay',pose(dx=4,lean=5,farm=((9,0),(19,1)),th=2,nleg=LUNGE[0],fleg=LUNGE[1]),[('arc',(70,62,40,150,390))]),
  ('theo đà quét xuống',pose(dx=4,lean=5,farm=((9,4),(16,10)),th=45,nleg=LUNGE[0],fleg=LUNGE[1]),[])],'Vệt trăng ngang lớn quanh người, rung nhẹ. Dễ đọc nhưng hơi giống A ở đoạn đầu.'),
'C2':('C2 · Nhảy bổ dọc xuống đất',[
  ('nhún, kiếm giơ cao',pose(dy=4,farm=((-2,-11),(2,-20)),th=-95,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
  ('bật lên, kiếm sau đầu',pose(dx=3,dy=-14,lean=2,farm=((-4,-10),(-6,-19)),th=-140,nleg=AIR[0],fleg=AIR[1]),[('arrow',((60,110),(78,92)))]),
  ('bổ thẳng xuống đất',pose(dx=8,dy=4,lean=7,farm=((8,6),(14,14)),th=80,nleg=LUNGE[0],fleg=LUNGE[1]),[('arc',(80,70,34,-90,80)),('crack',(96,120))])],'Vệt dọc từ trên xuống + nứt đất, bụi văng ra 2 bên. Khác hẳn A/B, nặng tay nhất.'),
'C3':('C3 · Xoay người 360° quét vòng',[
  ('vặn người, kiếm ra sau',pose(lean=-2,farm=((-7,2),(-15,4)),th=175,nleg=STEP[0],fleg=STEP[1]),[]),
  ('quay lưng giữa vòng xoay',pose(dx=2,lean=1,farm=((-3,0),(-6,2)),th=180,turn=1),[('ring',(68,82,46))]),
  ('ra hết vòng, kiếm trước',pose(dx=4,lean=4,farm=((9,0),(19,1)),th=5,nleg=LUNGE[0],fleg=LUNGE[1]),[('arc',(68,70,44,-40,30))])],'Vòng xoáy kiếm khí quanh người (trúng mọi phía). Cần thêm khung quay lưng, khó vẽ đúng hơn.'),
'C4':('C4 · Đâm xuyên kết liễu',[
  ('thu kiếm ngang hông',pose(lean=-2,farm=((-4,6),(-2,10)),th=0,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
  ('bước dài đâm thẳng',pose(dx=8,dy=3,lean=7,farm=((10,1),(21,2)),th=0,nleg=LUNGE[0],fleg=LUNGE[1]),[('beam',(100,55))]),
  ('rút kiếm, thủ',pose(dx=4,lean=3,farm=((6,6),(11,13)),th=55),[])],'Tia kiếm khí thẳng xuyên hàng quái. Ngắn gọn, nhưng giống động tác đâm ở cuối B.'),
'L1':('Lướt Trảm L1 · Lướt chém ngang (bản PixelLab vừa làm)',[
  ('hạ người, kiếm thấp sau',pose(dx=-2,dy=3,lean=-2,farm=((-5,9),(-12,13)),th=160,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
  ('lướt tới chém duỗi',pose(dx=8,dy=4,lean=7,farm=((10,1),(20,2)),th=-5,nleg=LUNGE[0],fleg=LUNGE[1]),[('streak',(0,70,110)),('arc',(80,66,30,-40,20))]),
  ('thu về',pose(dx=5,dy=2,lean=3,farm=((6,4),(12,8)),th=40,nleg=STEP[0],fleg=STEP[1]),[])],'Vệt lướt dài sau lưng + 1 nhát ngang ở đích.'),
'L2':('Lướt Trảm L2 · Rút kiếm nhanh (iaido)',[
  ('tay đặt chuôi, cúi thấp',pose(dy=4,lean=4,farm=((4,8),(6,10)),th=170,nleg=CROUCH[0],fleg=CROUCH[1]),[]),
  ('lướt qua, chém 1 đường mảnh',pose(dx=10,dy=4,lean=8,farm=((10,-2),(19,-6)),th=-20,nleg=LUNGE[0],fleg=LUNGE[1]),[('line',(0,80,120,40))]),
  ('đứng thẳng, quái sau lưng mới nổ',pose(dx=6,farm=((6,6),(11,13)),th=60),[('pop',(20,70))])],'Đường chém mảnh xuyên qua, quái nổ trễ 0,2 giây sau lưng. Rất "kiếm hiệp".'),
}
def board(key,keys,title,note):
    W=len(keys)*270+20;H=330;o=Image.new('RGB',(W,H),(32,34,40));d=ImageDraw.Draw(o)
    d.text((12,8),title,fill=(255,224,150),font=F);d.text((12,H-24),note,fill=(200,200,205),font=Fs)
    for i,(lab,P,fx) in enumerate(keys):
        ox=10+i*270;oy=34;ground(d,ox,oy,256)
        for k,v in fx:
            if k=='arc':vfx_arc(d,*v,ox,oy)
            elif k=='ring':
                cx,cy,r=v;d.ellipse((ox+(cx-r)*SC,oy+(cy-r*0.5)*SC,ox+(cx+r)*SC,oy+(cy+r*0.5)*SC),outline=(255,214,90),width=8)
            elif k=='beam':
                x,y=v;d.line([(ox+80*SC,oy+y*SC),(ox+x*SC+60,oy+y*SC)],fill=(255,214,90),width=10);d.line([(ox+80*SC,oy+y*SC),(ox+x*SC+60,oy+y*SC)],fill=(255,250,220),width=3)
            elif k=='streak':
                x0,y,x1=v;d.line([(ox+x0*SC,oy+y*SC),(ox+(x1-50)*SC,oy+y*SC)],fill=(160,200,255),width=12)
            elif k=='line':
                x0,y0,x1,y1=v;d.line([(ox+x0*SC,oy+y0*SC),(ox+x1*SC,oy+y1*SC)],fill=(255,250,220),width=3)
            elif k=='crack':
                x,y=v
                for a in(-160,-120,-60,-20):d.line([(ox+x*SC,oy+y*SC),(ox+(x+math.cos(math.radians(a))*22)*SC,oy+(y+math.sin(math.radians(a))*6)*SC)],fill=(255,150,60),width=3)
            elif k=='pop':
                x,y=v;d.ellipse((ox+(x-8)*SC,oy+(y-8)*SC,ox+(x+8)*SC,oy+(y+8)*SC),outline=(255,120,80),width=4)
            elif k=='arrow':arrow(d,*v,ox,oy)
        draw_fig(d,P,ox,oy)
        d.text((ox+4,oy+250),f'{i+1}. {lab}',fill='white',font=Fs)
    o.save(f'{OUT}/{key}.png');return o
imgs=[board('AB_hien_tai',A_keys+B_keys,'A → B hiện có (giữ nguyên) — C sẽ nối từ tư thế cuối của B','A bổ chéo xuống, B hất ngược lên rồi đâm. Hai đòn kết thúc đều ở thế kiếm thấp trước người.')]
for k,(t,keys,n) in PA.items():imgs.append(board(k,keys,t,n))
W=max(i.width for i in imgs);H=sum(i.height for i in imgs)+10*len(imgs)
o=Image.new('RGB',(W,H),(18,18,22));y=0
for i in imgs:o.paste(i,(0,y));y+=i.height+10
o.save(f'{OUT}/TONG_HOP.png');print(o.size)
