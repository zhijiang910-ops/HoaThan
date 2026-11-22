"""Dựng khung xương 8 frame chạy (quay phải) từ khung xương tư thế đứng. Tay cầm kiếm giữ nguyên kiểu cầm."""
import json,sys,math
from PIL import Image,ImageDraw
src,out,dbg=sys.argv[1],sys.argv[2],sys.argv[3]
K={p['label']:p for p in json.load(open(src))['keypoints']}
P=lambda n:(K[n]['x'],K[n]['y'])
hip=((K['LEFT HIP']['x']+K['RIGHT HIP']['x'])/2,(K['LEFT HIP']['y']+K['RIGHT HIP']['y'])/2)
# tay nào ở phía trước (x lớn hơn) là tay cầm kiếm
sw='LEFT' if K['LEFT ARM']['x']>K['RIGHT ARM']['x'] else 'RIGHT'; fr='RIGHT' if sw=='LEFT' else 'LEFT'
# chu kỳ 1 chân: (gối dx,dy),(cổ chân dx,dy) so với hông
LEG=[((.06,.10),(.09,.24)),((.03,.12),(.01,.26)),((-.02,.12),(-.07,.25)),((-.05,.11),(-.13,.19)),
     ((-.04,.09),(-.12,.12)),((.02,.08),(-.05,.14)),((.08,.05),(.04,.14)),((.09,.07),(.11,.19))]
BOB=[.012,.016,.004,-.018,.012,.016,.004,-.018]
LEAN=.035
frames=[]
for i in range(8):
    b=BOB[i];kp=[]
    def add(lbl,x,y):
        z=K[lbl]['z_index'];kp.append({'x':round(min(.99,max(.01,x)),4),'y':round(min(.99,max(.01,y)),4),'label':lbl,'z_index':z})
    for lbl in ['NOSE','NECK','LEFT EYE','RIGHT EYE','LEFT EAR','RIGHT EAR','LEFT SHOULDER','RIGHT SHOULDER']:
        x,y=P(lbl);add(lbl,x+LEAN,y+b)
    # tay cầm kiếm: giữ nguyên vị trí tương đối, chỉ theo thân
    for j in ['ELBOW','ARM']:
        x,y=P(f'{sw} {j}');add(f'{sw} {j}',x+LEAN*0.8,y+b)
    # tay không: đánh ngược chân cùng bên
    near_leg_fwd=LEG[i][1][0]   # chân phía gần (RIGHT) dùng pha i
    s=near_leg_fwd/0.12
    if fr=='RIGHT': s=s
    else: s=LEG[(i+4)%8][1][0]/0.12
    sx,sy=P(f'{fr} SHOULDER');sx+=LEAN;sy+=b
    add(f'{fr} ELBOW',sx-0.06*s,sy+0.09)
    add(f'{fr} ARM',sx-0.10*s+0.02,sy+0.15-0.03*abs(s))
    hx,hy=hip[0]+0.01,hip[1]+b
    for side,ph in [('RIGHT',i),('LEFT',(i+4)%8)]:
        x,y=P(f'{side} HIP');add(f'{side} HIP',x+0.01,y+b)
        (kx,ky),(ax,ay)=LEG[ph]
        add(f'{side} KNEE',hx+kx,hy+ky);add(f'{side} LEG',hx+ax,hy+ay)
    frames.append(kp)
json.dump({'first':list(K.values()),'frames':frames,'sword_hand':sw},open(out,'w'))
# ảnh soát
EDG=[('NECK','NOSE'),('LEFT SHOULDER','LEFT ELBOW'),('LEFT ELBOW','LEFT ARM'),('RIGHT SHOULDER','RIGHT ELBOW'),('RIGHT ELBOW','RIGHT ARM'),('LEFT HIP','LEFT KNEE'),('LEFT KNEE','LEFT LEG'),('RIGHT HIP','RIGHT KNEE'),('RIGHT KNEE','RIGHT LEG'),('LEFT SHOULDER','RIGHT SHOULDER'),('LEFT HIP','RIGHT HIP'),('LEFT SHOULDER','LEFT HIP'),('RIGHT SHOULDER','RIGHT HIP')]
S=256;o=Image.new('RGB',(S*9,S),'#334');d=ImageDraw.Draw(o)
for f,kp in enumerate([list(K.values())]+frames):
    M={p['label']:(f*S+p['x']*S,p['y']*S) for p in kp}
    for a,c in EDG:
        if a in M and c in M:d.line([M[a],M[c]],fill='#f84' if 'RIGHT' in a+c else '#4cf',width=3)
    d.ellipse([M[sw+' ARM'][0]-5,M[sw+' ARM'][1]-5,M[sw+' ARM'][0]+5,M[sw+' ARM'][1]+5],outline='#ff0',width=2)
    d.line([(f*S,0.92*S),(f*S+S,0.92*S)],fill='#888')
o.save(dbg);print('sword hand',sw)
