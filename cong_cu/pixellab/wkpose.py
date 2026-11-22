"""Khung xương Ngộ Không (rig có gậy, đuôi, lông vũ) cho đứng/chạy/đòn A/đòn B/trúng đòn/gục.
wkpose.py <wk_cust_meta.json> <out.json> <dbg.png>   (toạ độ điểm ảnh trên khung 192)"""
import json,sys,math
from PIL import Image,ImageDraw
cm,out,dbg=sys.argv[1:4];S=192
C=json.load(open(cm));rig=C['rig'];R0={p['label']:(p['x']*S,p['y']*S) for p in C['frames'][0]};Z={p['label']:int(p.get('z_index',0)//1) for p in C['frames'][0]}
par={j['name']:j['parent'] for j in rig};names=[j['name'] for j in rig]
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def add(a,b):return(a[0]+b[0],a[1]+b[1])
off={n:sub(R0[n],R0[par[n]]) for n in names if par[n]}
grip_w=sub(R0['staff_grip'],R0['near_wrist'])
FRONT=['staff_front_mid','staff_front_tip'];BACK=['staff_back_1','staff_back_2','staff_back_tip']
dF=[math.dist(R0['staff_grip'],R0[n]) for n in FRONT];dB=[math.dist(R0['staff_grip'],R0[n]) for n in BACK]
TH0=math.degrees(math.atan2(R0['staff_front_tip'][1]-R0['staff_grip'][1],R0['staff_front_tip'][0]-R0['staff_grip'][0]))
LEGRUN=[((.06,.10),(.09,.24)),((.03,.12),(.01,.26)),((-.02,.12),(-.07,.25)),((-.05,.11),(-.13,.19)),((-.04,.09),(-.12,.12)),((.02,.08),(-.05,.14)),((.08,.05),(.04,.14)),((.09,.07),(.11,.19))]
LEGRUN=[((k[0]*128,k[1]*128),(a[0]*128,a[1]*128)) for k,a in LEGRUN]
def pose(lean=0,sink=0,narm=None,farm=None,nleg=None,fleg=None,th=None,tail=0,plume=0,rot=0):
    P={};hip=add(R0['hips'],(lean*.3,sink))
    P['hips']=hip
    for n in names:
        if n=='hips':continue
        p=par[n]
        if n in FRONT or n in BACK or n=='staff_grip':continue
        o=off[n]
        if n in('chest','neck'):o=(o[0]+lean*(.4 if n=='chest' else .6),o[1])
        if n=='head':o=(o[0]+lean*.4,o[1])
        if n.startswith('plume') and plume:o=(o[0]-abs(o[1])*plume*.5,o[1]+abs(o[0])*plume*.2)
        if n.startswith('tail') and tail:
            a=math.radians(tail);o=(o[0]*math.cos(a)-o[1]*math.sin(a),o[0]*math.sin(a)+o[1]*math.cos(a))
        if n=='near_elbow' and narm:P[n]=add(P['near_shoulder'],narm[0]);continue
        if n=='near_wrist' and narm:P[n]=add(P['near_shoulder'],narm[1]);continue
        if n=='far_elbow' and farm:P[n]=add(P['far_shoulder'],farm[0]);continue
        if n=='far_wrist' and farm:P[n]=add(P['far_shoulder'],farm[1]);continue
        if n=='near_knee' and nleg:P[n]=add(hip,nleg[0]);continue
        if n=='near_ankle' and nleg:P[n]=add(hip,nleg[1]);continue
        if n=='far_knee' and fleg:P[n]=add(hip,fleg[0]);continue
        if n=='far_ankle' and fleg:P[n]=add(hip,fleg[1]);continue
        P[n]=add(P[p],o)
    g=add(P['near_wrist'],grip_w);P['staff_grip']=g
    t=math.radians(TH0 if th is None else th);u=(math.cos(t),math.sin(t))
    for n,d in zip(FRONT,dF):P[n]=(g[0]+u[0]*d,g[1]+u[1]*d)
    for n,d in zip(BACK,dB):P[n]=(g[0]-u[0]*d,g[1]-u[1]*d)
    return [{'x':round(min(.995,max(.005,P[n][0]/S)),4),'y':round(min(.995,max(.005,P[n][1]/S)),4),'label':n,'z_index':Z[n]} for n in names]
A=[]
# ĐỨNG thở: hạ người 0-1-2-1 px, lông vũ và đuôi đung đưa
IDLE=[pose(sink=s,tail=t,plume=p) for s,t,p in [(0,0,0),(1,4,.05),(2,6,.08),(1,3,.04)]]
# CHẠY: chân như nhân vật chính, gậy giữ chéo sau lưng như lúc đứng, tay xa đánh ngược chân
RUN=[]
BOB=[1.5,2,.5,-2.5,1.5,2,.5,-2.5]
for i in range(8):
    nl=LEGRUN[i];fl=LEGRUN[(i+4)%8];s=nl[1][0]/14
    RUN.append(pose(lean=4.5,sink=BOB[i],nleg=nl,fleg=fl,farm=((-2+8*s,17),(6+12*s,27)),tail=-8+6*math.sin(i/8*6.28),plume=.18))
# ĐÒN A · quét ngang: kéo gậy ra sau → vòng qua → quét ngang trước ngực (chạm) → hất → thu
SH=sub(R0['near_shoulder'],(0,0))
A_=[dict(lean=-3,sink=1,narm=((-10,12),(-16,22)),th=185,nleg=((3,14),(6,31)),fleg=((10,12),(12,28)),tail=6),
    dict(lean=-4,sink=2,narm=((-12,8),(-20,14)),th=200,nleg=((4,14),(8,31)),fleg=((12,12),(15,28)),tail=8),
    dict(lean=2,sink=2,narm=((2,12),(6,20)),th=120,nleg=((8,12),(14,30)),fleg=((-6,13),(-12,30)),tail=-4,plume=.1),
    dict(lean=7,sink=3,narm=((12,6),(24,8)),th=-5,nleg=((12,11),(18,29)),fleg=((-8,12),(-16,29)),tail=-10,plume=.2),
    dict(lean=6,sink=2,narm=((12,2),(22,0)),th=-25,nleg=((12,11),(18,29)),fleg=((-8,12),(-16,29)),tail=-8,plume=.15),
    dict(lean=1,sink=0,tail=-2)]
# ĐÒN B · bổ gậy từ trên xuống: giơ gậy cao → kéo ra sau đầu → bổ xuống (chạm đất trước mặt) → giữ → thu
B_=[dict(lean=-2,sink=0,narm=((-2,-10),(2,-26)),th=-95,tail=4),
    dict(lean=-4,sink=-1,narm=((-6,-12),(-6,-28)),th=-140,nleg=((2,13),(4,31)),fleg=((10,12),(13,28)),tail=6),
    dict(lean=3,sink=1,narm=((6,-10),(14,-20)),th=-55,nleg=((8,12),(14,30)),fleg=((-6,13),(-12,30)),tail=-4,plume=.1),
    dict(lean=9,sink=5,narm=((12,4),(22,12)),th=28,nleg=((14,9),(20,28)),fleg=((-10,12),(-20,28)),tail=-12,plume=.25),
    dict(lean=8,sink=5,narm=((12,5),(21,14)),th=32,nleg=((14,9),(20,28)),fleg=((-10,12),(-20,28)),tail=-10,plume=.2),
    dict(lean=1,sink=0,tail=-2)]
HIT=[pose(lean=-6,sink=1,th=TH0-10,tail=10,plume=-.1),pose(lean=-8,sink=2,th=TH0-15,tail=14,plume=-.15),pose(lean=-3,sink=1,tail=6)]
res={'rig':rig,'first':pose(),'idle':IDLE,'run':RUN,'A':[pose(**d) for d in A_],'B':[pose(**d) for d in B_],'hit':HIT,'grip_len':[dF,dB],'th0':TH0}
json.dump(res,open(out,'w'))
SS=150;keys=['idle','run','A','B','hit'];o=Image.new('RGB',(SS*9,SS*len(keys)),'#334');d=ImageDraw.Draw(o)
for r,k in enumerate(keys):
    for f,kp in enumerate([res['first']]+res[k]):
        M={p['label']:(f*SS+p['x']*SS,r*SS+p['y']*SS) for p in kp}
        for n in names:
            if par[n]:d.line([M[par[n]],M[n]],fill='#ffcc33' if n.startswith('staff') else ('#f84' if 'near' in n else ('#4cf' if 'far' in n else '#aaa')),width=3 if n.startswith('staff') else 2)
o.save(dbg);print('ok TH0',round(TH0),'staff',[round(x) for x in dF+dB])

# ---- Bản 2: bỏ thế kẹp gậy dưới nách ----
# ĐỨNG: gậy dựng thẳng đứng trước ngực, tay gần nắm ngang ngực, đầu gậy dưới chạm đất trước mũi chân.
# CHẠY: gậy vác chéo qua vai, tay gần nắm phía trước vai.
NEUTRAL=dict(narm=((9,12),(21,16)),th=90)
IDLE2=[pose(sink=s,tail=t,plume=p,**NEUTRAL) for s,t,p in [(0,0,0),(1,4,.05),(2,6,.08),(1,3,.04)]]
IDLE3=[pose(sink=s,tail=t,plume=p,narm=((13,11),(29,15)),th=90) for s,t,p in [(0,0,0),(1,3,.04),(1.5,5,.06),(1,3,.03)]]
NEUTRAL_OLD=dict(narm=((8,12),(18,16)),th=90)
RUN2=[]
for i in range(8):
    nl=LEGRUN[i];fl=LEGRUN[(i+4)%8];s_=nl[1][0]/14
    RUN2.append(pose(lean=4.5,sink=BOB[i],nleg=nl,fleg=fl,narm=((8,6),(12,2)),th=40,farm=((-2+8*s_,17),(6+12*s_,27)),tail=-8+6*math.sin(i/8*6.28),plume=.18))
HIT2=[pose(lean=-6,sink=1,narm=((11,12),(25,17)),th=100,tail=10,plume=-.1),pose(lean=-8,sink=2,narm=((10,12),(23,18)),th=106,tail=14,plume=-.15),pose(lean=-3,sink=1,narm=((12,11),(27,16)),th=94,tail=6)]
res.update(idle3=IDLE3,neutral_old=pose(sink=2,tail=6,plume=.08,**NEUTRAL_OLD),idle2=IDLE2,run2=RUN2,hit2=HIT2,neutral=pose(**NEUTRAL))
json.dump(res,open(out,'w'))
o2=Image.new('RGB',(SS*9,SS*3),'#334');d2=ImageDraw.Draw(o2)
for r,k in enumerate(['idle2','run2','hit2']):
    for f,kp in enumerate([res['first']]+res[k]):
        M={p['label']:(f*SS+p['x']*SS,r*SS+p['y']*SS) for p in kp}
        for n in names:
            if par[n]:d2.line([M[par[n]],M[n]],fill='#ffcc33' if n.startswith('staff') else ('#f84' if 'near' in n else ('#4cf' if 'far' in n else '#aaa')),width=3 if n.startswith('staff') else 2)
o2.save(dbg.replace('.png','_2.png'))

# ---- Bản 3: đòn đánh xuất phát từ thế dựng gậy, gậy luôn ở trước người ----
# th = hướng đoạn gậy ngắn; đoạn dài (đầu đánh) = th+180. Dựng đứng: th=90 (đầu dài chĩa lên).
A3=[dict(lean=-3,sink=1,narm=((7,8),(17,6)),th=60,tail=4),            # nghiêng đầu gậy ra sau, lấy đà
    dict(lean=1,sink=1,narm=((10,4),(22,0)),th=115,tail=0,plume=.1),    # vung qua đầu
    dict(lean=6,sink=3,narm=((13,6),(27,8)),th=180,tail=-8,plume=.2),   # bổ ngang ra trước (chạm)
    dict(lean=7,sink=4,narm=((12,9),(25,14)),th=205,tail=-10,plume=.2), # đầu gậy chúi xuống
    dict(lean=3,sink=2,narm=((10,10),(24,14)),th=130,tail=-4)]          # thu về
B3=[dict(lean=-2,sink=1,narm=((9,11),(23,14)),th=160,tail=2),           # hạ gậy ngang
    dict(lean=-5,sink=2,narm=((-2,12),(2,16)),th=180,tail=6),           # kéo tay về sau
    dict(lean=7,sink=2,narm=((13,9),(29,10)),th=180,tail=-8,plume=.2),  # đâm thẳng (chạm)
    dict(lean=8,sink=2,narm=((14,9),(30,10)),th=180,tail=-10,plume=.22),# giữ
    dict(lean=3,sink=1,narm=((11,10),(25,14)),th=130,tail=-4)]          # thu về
res.update(A3=[pose(**d) for d in A3],B3=[pose(**d) for d in B3])
json.dump(res,open(out,'w'))
o3=Image.new('RGB',(SS*6,SS*2),'#334');d3=ImageDraw.Draw(o3)
for r,k in enumerate(['A3','B3']):
    for f,kp in enumerate([res['idle3'][0]]+res[k]):
        M={p['label']:(f*SS+p['x']*SS,r*SS+p['y']*SS) for p in kp}
        for n in names:
            if par[n]:d3.line([M[par[n]],M[n]],fill='#ffcc33' if n.startswith('staff') else ('#f84' if 'near' in n else ('#4cf' if 'far' in n else '#aaa')),width=3 if n.startswith('staff') else 2)
o3.save(dbg.replace('.png','_3.png'))
