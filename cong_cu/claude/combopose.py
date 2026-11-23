"""Khung xương đòn C (nhát kết combo, chém ngang vòng rộng) và Lướt Trảm cho rig 24 khớp của nhân vật chính (canvas 128, mặt hướng đông).
Kiếm luôn ở tay xa (far_wrist), chiều dài kiếm giữ nguyên như rig gốc. combopose.py <rig_body.json> <outdir> <tag>"""
import json,sys,math
from PIL import Image,ImageDraw
src,od,tag=sys.argv[1:4];N=128
B=json.load(open(src));rig=B['rig'];F0=B['first_frame_keypoints']
# rig nữ đặt tên khác: đổi sang tên chung để dựng tư thế, xuất lại đúng tên gốc
MAP={'pelvis':'hips','left_shoulder':'far_shoulder','left_elbow':'far_elbow','left_wrist':'far_wrist','sword_pivot':'sword_grip','right_shoulder':'near_shoulder','right_elbow':'near_elbow','right_wrist':'near_wrist',
 'left_hip':'far_hip','left_knee':'far_knee','left_ankle':'far_ankle','left_toe':'far_toe','right_hip':'near_hip','right_knee':'near_knee','right_ankle':'near_ankle','right_toe':'near_toe',
 'hair_tail_1':'hair_1','hair_tail_2':'hair_2','hair_tail_3':'hair_3','hair_tail_4':'hair_4','hair_tail_5':'hair_5'} if any(j['name']=='sword_pivot' for j in rig) else {}
BACK={v:k for k,v in MAP.items()}
rig=[{**j,'name':MAP.get(j['name'],j['name']),'parent':MAP.get(j['parent'],j['parent'])} for j in rig]
F0=[{**p,'label':MAP.get(p['label'],p['label'])} for p in F0]
R0={p['label']:(p['x']*N,p['y']*N) for p in F0};Z={p['label']:p['z_index'] for p in F0}
par={j['name']:j['parent'] for j in rig};names=[j['name'] for j in rig]
sub=lambda a,b:(a[0]-b[0],a[1]-b[1]);add=lambda a,b:(a[0]+b[0],a[1]+b[1])
off={n:sub(R0[n],R0[par[n]]) for n in names if par[n]}
gw=sub(R0['sword_grip'],R0['far_wrist']);dM=math.dist(R0['sword_grip'],R0['sword_mid']);dT=math.dist(R0['sword_grip'],R0['sword_tip'])
def pose(dx=0,dy=0,lean=0,farm=None,narm=None,nleg=None,fleg=None,th=None,hair=0,front=False):
    """farm/narm=(khuỷu,cổ tay) so với vai; nleg/fleg=(gối,cổ chân) so với hông tương ứng; th=góc kiếm (độ, 0=hướng đông, 90=xuống)"""
    P={'hips':add(R0['hips'],(dx,dy))}
    for n in names:
        if n=='hips' or n.startswith('sword'):continue
        o=off[n]
        if n in('chest','neck','head'):o=(o[0]+lean*{'chest':.5,'neck':.4,'head':.3}[n],o[1])
        if n.startswith('hair') and hair:o=(o[0]-hair,o[1]-hair*.3)
        if n=='far_elbow' and farm:P[n]=add(P['far_shoulder'],farm[0]);continue
        if n=='far_wrist' and farm:P[n]=add(P['far_shoulder'],farm[1]);continue
        if n=='near_elbow' and narm:P[n]=add(P['near_shoulder'],narm[0]);continue
        if n=='near_wrist' and narm:P[n]=add(P['near_shoulder'],narm[1]);continue
        if n=='near_knee' and nleg:P[n]=add(P['near_hip'],nleg[0]);continue
        if n=='near_ankle' and nleg:P[n]=add(P['near_hip'],nleg[1]);continue
        if n=='far_knee' and fleg:P[n]=add(P['far_hip'],fleg[0]);continue
        if n=='far_ankle' and fleg:P[n]=add(P['far_hip'],fleg[1]);continue
        P[n]=add(P[par[n]],o)
    g=add(P['far_wrist'],gw if th is None else (0,0));P['sword_grip']=g
    t=math.radians(math.degrees(math.atan2(*reversed(sub(R0['sword_tip'],R0['sword_grip'])))) if th is None else th);u=(math.cos(t),math.sin(t))
    P['sword_mid']=(g[0]+u[0]*dM,g[1]+u[1]*dM);P['sword_tip']=(g[0]+u[0]*dT,g[1]+u[1]*dT)
    zz=lambda n:3 if front and (n.startswith('far_elbow') or n.startswith('far_wrist') or n.startswith('sword')) else int(Z[n]//1)   # tay cầm kiếm + kiếm vẽ đè lên thân
    return [{'x':round(min(.995,max(.005,P[n][0]/N)),4),'y':round(min(.995,max(.005,P[n][1]/N)),4),'label':BACK.get(n,n),'z_index':zz(n)} for n in names]
# chân: bước dài (chân gần ra trước, chân xa ra sau)
STEP=(((6,14),(10,30)),((-6,16),(-12,31)))
LUNGE=(((11,11),(18,27)),((-10,15),(-19,28)))
CROUCH=(((5,13),(9,28)),((-4,15),(-8,30)))
C=[pose(),
 # 1 lấy đà: lùi người, kiếm vung ngược ra sau lưng cao
 pose(dx=-2,dy=1,lean=-3,farm=((-6,-6),(-12,-12)),narm=((4,8),(10,10)),th=-150,hair=2,nleg=CROUCH[0],fleg=CROUCH[1]),
 # 2 kiếm qua đỉnh đầu, người dồn tới
 pose(dx=1,dy=1,lean=2,farm=((-2,-11),(4,-19)),narm=((5,8),(11,9)),th=-30,hair=3,nleg=STEP[0],fleg=STEP[1]),
 # 3 chém ngang rộng: tay duỗi thẳng trước ngực, kiếm nằm ngang hướng đông (chạm)
 pose(dx=4,dy=2,lean=5,farm=((9,0),(19,1)),narm=((2,10),(-4,14)),th=2,hair=5,nleg=LUNGE[0],fleg=LUNGE[1]),
 # 4 vung theo đà: kiếm quét tiếp xuống thấp
 pose(dx=4,dy=3,lean=5,farm=((9,4),(16,10)),narm=((2,10),(-4,14)),th=45,hair=4,nleg=LUNGE[0],fleg=LUNGE[1]),
 # 5 thu kiếm thấp trước, giữ thế
 pose(dx=3,dy=2,lean=3,farm=((6,8),(11,15)),th=60,hair=2,nleg=STEP[0],fleg=STEP[1]),
 pose(dx=1,dy=1,lean=1,hair=1),
 pose()]
L=[pose(),
 # 1 hạ thấp, kiếm kéo thấp ra sau hông
 pose(dx=-2,dy=3,lean=-2,farm=((-5,9),(-12,13)),narm=((5,7),(11,9)),th=160,nleg=CROUCH[0],fleg=CROUCH[1]),
 # 2 phóng tới: bước dài, kiếm bắt đầu vung lên từ dưới
 pose(dx=6,dy=4,lean=6,farm=((1,9),(5,13)),narm=((-3,9),(-9,11)),th=165,hair=6,nleg=LUNGE[0],fleg=LUNGE[1]),
 # 3 lướt chém: tay duỗi xa, kiếm ngang trước (chạm)
 pose(dx=8,dy=4,lean=7,farm=((10,1),(20,2)),narm=((-3,9),(-10,10)),th=-5,hair=7,nleg=LUNGE[0],fleg=LUNGE[1]),
 # 4 kiếm hất chéo lên kết thúc
 pose(dx=8,dy=3,lean=6,farm=((10,-2),(19,-4)),narm=((-2,9),(-8,11)),th=-18,hair=6,nleg=LUNGE[0],fleg=LUNGE[1]),
 # 5 thu về
 pose(dx=5,dy=2,lean=3,farm=((6,4),(12,8)),th=40,hair=3,nleg=STEP[0],fleg=STEP[1]),
 pose(dx=2,dy=1,lean=1,hair=1),
 pose()]
for k,v in {'C':C,'L':L}.items():json.dump(v,open(f'{od}/{tag}_pose_{k}.json','w'))
img=Image.open(src.replace('_rigB_body.json','_first.png')).convert('RGBA')
for k,v in {'C':C,'L':L}.items():
    o=Image.new('RGBA',(len(v)*N*2,N*2),(40,44,52,255));d=ImageDraw.Draw(o)
    for i,fr in enumerate(v):
        bg=img.resize((N*2,N*2),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*N*2,0))
        P={MAP.get(p['label'],p['label']):(p['x']*N*2+i*N*2,p['y']*N*2) for p in fr}
        for n in names:
            if par[n]:d.line([P[par[n]],P[n]],fill=(255,200,0) if n.startswith('sword') else (0,255,255) if n.startswith('far') else (255,80,200) if n.startswith('near') else (220,220,220),width=3)
    o.save(f'{od}/{tag}_dbg_{k}.png')
