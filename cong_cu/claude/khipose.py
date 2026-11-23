"""Khung xương khỉ con (rig 29 khớp có gậy, đuôi) -> tư thế đứng/chạy/bổ gậy. khipose.py <k_cust_meta.json> <outdir>
Gậy: grip bám cổ tay gần, mid/tip nằm trên một đường thẳng, giữ nguyên chiều dài gốc."""
import json,sys,math
from PIL import Image,ImageDraw
cm,od=sys.argv[1:3];S=96
C=json.load(open(cm));rig=C['rig'];F0=C['frames'][0]
R0={p['label']:(p['x']*S,p['y']*S) for p in F0};Z={p['label']:int(p.get('z_index',0)//1) for p in F0}
par={j['name']:j['parent'] for j in rig};names=[j['name'] for j in rig]
sub=lambda a,b:(a[0]-b[0],a[1]-b[1]);add=lambda a,b:(a[0]+b[0],a[1]+b[1])
off={n:sub(R0[n],R0[par[n]]) for n in names if par[n]}
gw=sub(R0['staff_grip'],R0['right_wrist'])
dM=math.dist(R0['staff_grip'],R0['staff_mid']);dT=math.dist(R0['staff_grip'],R0['staff_tip'])
TH0=math.degrees(math.atan2(R0['staff_tip'][1]-R0['staff_grip'][1],R0['staff_tip'][0]-R0['staff_grip'][0]))
def rot(v,deg):a=math.radians(deg);return(v[0]*math.cos(a)-v[1]*math.sin(a),v[0]*math.sin(a)+v[1]*math.cos(a))
def pose(lean=0,sink=0,narm=None,farm=None,nleg=None,fleg=None,th=None,tail=0,dx=0):
    P={};hip=add(R0['pelvis'],(dx+lean*.3,sink));P['pelvis']=hip
    for n in names:
        if n=='pelvis' or n.startswith('staff'):continue
        o=off[n]
        if n in('chest','neck','head','head_top'):o=(o[0]+lean*{'chest':.4,'neck':.5,'head':.3,'head_top':.2}[n],o[1])
        if n.startswith('tail') and tail:o=rot(o,tail)
        if n=='right_elbow' and narm:P[n]=add(P['right_shoulder'],narm[0]);continue
        if n=='right_wrist' and narm:P[n]=add(P['right_shoulder'],narm[1]);continue
        if n=='left_elbow' and farm:P[n]=add(P['left_shoulder'],farm[0]);continue
        if n=='left_wrist' and farm:P[n]=add(P['left_shoulder'],farm[1]);continue
        if n=='left_hand' and farm:P[n]=add(P['left_wrist'],(farm[1][0]-farm[0][0])*.35,(farm[1][1]-farm[0][1])*.35) if False else add(P['left_wrist'],off[n]) ;
        if n=='left_hand' and farm:continue
        if n=='right_knee' and nleg:P[n]=add(hip,nleg[0]);continue
        if n=='right_ankle' and nleg:P[n]=add(hip,nleg[1]);continue
        if n=='left_knee' and fleg:P[n]=add(hip,fleg[0]);continue
        if n=='left_ankle' and fleg:P[n]=add(hip,fleg[1]);continue
        if n=='right_foot' and nleg:P[n]=add(P['right_ankle'],off[n]);continue
        if n=='left_foot' and fleg:P[n]=add(P['left_ankle'],off[n]);continue
        P[n]=add(P[par[n]],o)
    g=add(P['right_wrist'],gw);P['staff_grip']=g;t=math.radians(TH0 if th is None else th);u=(math.cos(t),math.sin(t))
    P['staff_mid']=(g[0]+u[0]*dM,g[1]+u[1]*dM);P['staff_tip']=(g[0]+u[0]*dT,g[1]+u[1]*dT)
    return [{'x':round(min(.995,max(.005,P[n][0]/S)),4),'y':round(min(.995,max(.005,P[n][1]/S)),4),'label':n,'z_index':Z[n]} for n in names]
# toạ độ gốc để tham chiếu
sh=R0['right_shoulder'];el=sub(R0['right_elbow'],sh);wr=sub(R0['right_wrist'],sh)
fsh=R0['left_shoulder'];fel=sub(R0['left_elbow'],fsh);fwr=sub(R0['left_wrist'],fsh)
hip=R0['pelvis'];nk=sub(R0['right_knee'],hip);na=sub(R0['right_ankle'],hip);fk=sub(R0['left_knee'],hip);fa=sub(R0['left_ankle'],hip)
print('TH0',round(TH0),'staff',round(dT,1),'leg',na,fa)
IDLE=[pose(sink=s,tail=t) for s,t in [(0,0),(1,3),(1,5),(0,2)]]
# CHẠY: chu kỳ chân (đơn vị độ dài chân ~17px), thân nghiêng, gậy kéo sau thấp, tay xa đánh ngược chân
L=17
# chân thật lúc đứng: mắt cá thấp hơn hông ~12px (0.70 L) -> chạm đất y=.70, nhấc chân y nhỏ hơn
CYC=[((.30,.36),(.50,.70)),((.15,.38),(.20,.70)),((-.05,.38),(-.20,.69)),((-.20,.34),(-.52,.58)),((-.18,.30),(-.58,.42)),((.05,.30),(-.22,.46)),((.30,.24),(.18,.52)),((.38,.30),(.44,.64))]
RUN=[];BOB=[0,1,0,-1,0,1,0,-1]
for i in range(8):
    a=CYC[i];b=CYC[(i+4)%8];k=lambda p:(p[0]*L,p[1]*L)
    sw=math.sin(i/8*2*math.pi)
    RUN.append(pose(lean=4,sink=BOB[i],nleg=(k(a[0]),k(a[1])),fleg=(k(b[0]),k(b[1])),
        narm=((el[0]-1-sw*2,el[1]),(wr[0]-2-sw*3,wr[1]+1)),farm=((fel[0]+sw*4,fel[1]+2),(fwr[0]+sw*6-3,fwr[1]+5)),th=150-sw*6,tail=-8+sw*6))
# BỔ GẬY: thế -> thu -> giơ gậy qua đầu -> nhảy -> bổ xuống trước -> chạm -> giữ -> về
ATK=[pose(),
 pose(sink=2,narm=((el[0]+1,el[1]-1),(wr[0]+2,wr[1]-3)),th=160,tail=4),
 pose(sink=1,lean=-1,narm=((-1,-8),(1,-15)),th=-125,farm=((fel[0]-1,fel[1]-2),(fwr[0]-3,fwr[1]-1)),tail=6),
 pose(sink=-5,lean=1,narm=((1,-9),(4,-16)),th=-105,nleg=((nk[0]+2,nk[1]-3),(na[0]+3,na[1]-6)),fleg=((fk[0]+1,fk[1]-3),(fa[0]+2,fa[1]-6)),tail=10,dx=2),
 pose(sink=-2,lean=4,narm=((7,-3),(13,0)),th=-20,dx=4,tail=0),
 pose(sink=2,lean=5,narm=((7,1),(13,5)),th=25,dx=5,tail=-6),
 pose(sink=2,lean=4,narm=((6,2),(12,6)),th=30,dx=5,tail=-4),
 pose(sink=1,lean=1,dx=2)]
for k,v in {'idle':IDLE,'run':RUN,'atk':ATK}.items():json.dump(v,open(f'{od}/pose_{k}.json','w'))
# ảnh kiểm tra
img=Image.open(f'{od}/k_first.png').convert('RGBA')
for k,v in {'idle':IDLE,'run':RUN,'atk':ATK}.items():
    o=Image.new('RGBA',(len(v)*S*3,S*3),(40,44,52,255));d=ImageDraw.Draw(o)
    for i,fr in enumerate(v):
        bg=img.resize((S*3,S*3),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*S*3,0))
        P={p['label']:(p['x']*S*3+i*S*3,p['y']*S*3) for p in fr}
        for n in names:
            if par[n]:d.line([P[par[n]],P[n]],fill=(255,200,0) if n.startswith('staff') else (0,255,255) if n.startswith('right') else (255,80,200) if n.startswith('left') else (220,220,220),width=3)
        d.line([P['staff_grip'],P['staff_tip']],fill=(255,60,30),width=5)
    o.save(f'{od}/dbg_{k}.png')
