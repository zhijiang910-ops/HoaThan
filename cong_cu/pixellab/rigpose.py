"""Chuyển khung xương người (18 khớp) + góc lưỡi kiếm từng frame sang rig tùy chỉnh có kiếm.
rigpose.py <cust_meta.json> <humanoid_skel.json> <atkskel.json> <out.json> <dbg.png>"""
import json,sys,math
from PIL import Image,ImageDraw
cm,hs,ak,out,dbg=sys.argv[1:6]
C=json.load(open(cm));rig=C['rig'];R0={p['label']:p for p in C['frames'][0]}
H0={p['label']:(p['x'],p['y']) for p in json.load(open(hs))['keypoints']}
AK=json.load(open(ak))
# đổi tên chuỗi bị nhận nhầm là kiếm sau lưng (thật ra là đuôi tóc)
ren={}
for j in rig:
    if j['name'].startswith('back_sword'):ren[j['name']]=j['name'].replace('back_sword','hair')
for j in rig:
    j['name']=ren.get(j['name'],j['name']);j['parent']=ren.get(j['parent'],j['parent'])
R0={ren.get(k,k):v for k,v in R0.items()}
for k,v in R0.items():v['label']=k
names=[j['name'] for j in rig];par={j['name']:j['parent'] for j in rig};est={j['name']:j['estimate'] for j in rig}
SW=[n for n in names if n.startswith('sword')]  # chuỗi kiếm theo thứ tự cha→con
wrist=par[SW[0]]
w0=(R0[wrist]['x'],R0[wrist]['y']);t0=(R0[SW[-1]]['x'],R0[SW[-1]]['y'])
L=math.dist(w0,t0)
def mid(a,b):return((a[0]+b[0])/2,(a[1]+b[1])/2)
def pose(hum,ang,flut=0.0):
    h={p['label']:(p['x'],p['y']) for p in hum}
    P={}
    hip0=mid(H0['LEFT HIP'],H0['RIGHT HIP']);hipN=mid(h['LEFT HIP'],h['RIGHT HIP'])
    for n in names:
        if est[n]:P[n]=h[est[n]];continue
        if n in SW:continue
        if par[n] is None:P[n]=hipN;continue
        if n=='chest':
            t=(R0[n]['y']-hip0[1])/(H0['NECK'][1]-hip0[1]);P[n]=(hipN[0]+(h['NECK'][0]-hipN[0])*t,hipN[1]+(h['NECK'][1]-hipN[1])*t);continue
        p=par[n];dx=R0[n]['x']-R0[p]['x'];dy=R0[n]['y']-R0[p]['y']
        if n.startswith('hair') or n.startswith('cape'):dx-=flut*abs(dx)/0.06;dy+=flut*0.3
        P[n]=(P[p][0]+dx,P[p][1]+dy)
    if ang is None:   # giữ hướng kiếm như tư thế đứng
        ang=math.degrees(math.atan2(t0[1]-w0[1],t0[0]-w0[0]))
    a=math.radians(ang);wx,wy=P[wrist];k=len(SW)
    for i,n in enumerate(SW):
        f=[0.12,0.55,1.0] if k==3 else [(i+1)/k for i in range(k)]
        P[n]=(wx+math.cos(a)*L*f[i],wy+math.sin(a)*L*f[i])
    return [{'x':round(min(.995,max(.005,P[n][0])),4),'y':round(min(.995,max(.005,P[n][1])),4),'label':n,'z_index':int(R0[n].get('z_index',0)//1)} for n in names]
ANG={'A':[-95,-120,-15,40,60,None],'B':[165,185,100,0,-20,None]}
FL={'A':[0,.01,.02,.03,.02,0],'B':[0,.01,.02,.03,.02,0]}
res={'rig':rig,'first':pose([{'x':x,'y':y,'label':l} for l,(x,y) in H0.items()],None)}
for key in 'AB':res[key]=[pose(AK[key][i],ANG[key][i],FL[key][i]) for i in range(6)]
json.dump(res,open(out,'w'))
S=200;o=Image.new('RGB',(S*7,S*2),'#334');d=ImageDraw.Draw(o)
for r,key in enumerate('AB'):
    for f,kp in enumerate([res['first']]+res[key]):
        M={p['label']:(f*S+p['x']*S,r*S+p['y']*S) for p in kp}
        for n in names:
            if par[n]:d.line([M[par[n]],M[n]],fill='#ddd' if n in SW else ('#f84' if 'near' in n or 'right' in n else '#4cf'),width=4 if n in SW else 2)
o.save(dbg);print('ok L',round(L,3),'sword chain',SW,'wrist',wrist)
