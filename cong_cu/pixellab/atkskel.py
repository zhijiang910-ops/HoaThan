"""Khung xương đòn A (bổ chéo từ trên xuống) và B (kéo sau rồi chém ngang ra trước). Tay cầm kiếm = tay trước, không đổi tay."""
import json,sys
from PIL import Image,ImageDraw
src,out,dbg=sys.argv[1:4]
K={p['label']:p for p in json.load(open(src))['keypoints']}
sw='LEFT' if K['LEFT ARM']['x']>K['RIGHT ARM']['x'] else 'RIGHT';fr='RIGHT' if sw=='LEFT' else 'LEFT'
# chân trước = chân có cổ chân x lớn hơn
fl='LEFT' if K['LEFT LEG']['x']>K['RIGHT LEG']['x'] else 'RIGHT';bl='RIGHT' if fl=='LEFT' else 'LEFT'
P=lambda n:[K[n]['x'],K[n]['y']]
hip=[(K['LEFT HIP']['x']+K['RIGHT HIP']['x'])/2,(K['LEFT HIP']['y']+K['RIGHT HIP']['y'])/2]
sh=P(sw+' SHOULDER')
# mỗi frame: lean(thân), sink(hạ người), (khuỷu tay kiếm dx,dy),(cổ tay kiếm dx,dy) so với vai tay kiếm,
#            (khuỷu tay không),(cổ tay không) so với vai tay đó, chân trước (gối,cổ chân) & chân sau so với hông
A=[ # bổ chéo từ trên xuống
 (-.02,.00,(-.03,-.07),(-.02,-.15),(.02,.08),(.05,.14),((.05,.12),(.07,.27)),((-.03,.13),(-.05,.27))),   # giơ kiếm cao sau đầu
 (.00,.01,(.00,-.10),(.00,-.19),(.00,.08),(.02,.15),((.06,.12),(.09,.26)),((-.04,.13),(-.07,.27))),     # kiếm trên đỉnh đầu
 (.04,.03,(.08,-.03),(.15,-.04),(-.04,.07),(-.07,.12),((.09,.10),(.13,.24)),((-.06,.12),(-.11,.26))),   # bổ xuống (chạm)
 (.06,.05,(.08,.04),(.14,.10),(-.05,.06),(-.09,.10),((.10,.09),(.14,.23)),((-.07,.12),(-.13,.25))),    # kiếm hết đường, thấp trước
 (.04,.04,(.06,.06),(.09,.14),(-.04,.07),(-.07,.12),((.09,.10),(.13,.24)),((-.06,.12),(-.11,.26))),    # giữ thế
 (.01,.01,None,None,None,None,None,None)]                                                              # về gần tư thế đứng
B=[ # kéo kiếm thấp ra sau hông rồi chém ngang
 (-.02,.02,(-.04,.07),(-.09,.13),(.04,.07),(.07,.11),((.05,.12),(.07,.26)),((-.04,.13),(-.07,.27))),   # kéo kiếm ra sau hông
 (-.03,.03,(-.06,.06),(-.12,.10),(.05,.06),(.09,.09),((.06,.12),(.09,.26)),((-.05,.13),(-.08,.27))),   # xoay người lấy đà
 (.02,.03,(.03,.06),(.07,.09),(.00,.07),(-.03,.12),((.09,.11),(.13,.25)),((-.06,.12),(-.11,.26))),     # vung ngang
 (.05,.03,(.09,.04),(.18,.04),(-.05,.06),(-.09,.10),((.10,.10),(.14,.24)),((-.07,.12),(-.12,.26))),    # chém ngang duỗi thẳng (chạm)
 (.04,.02,(.09,.01),(.17,-.02),(-.04,.07),(-.07,.11),((.09,.10),(.13,.24)),((-.06,.12),(-.11,.26))),   # kiếm hất lên kết đòn
 (.01,.01,None,None,None,None,None,None)]
def frames(seq):
    out=[]
    for lean,sink,se,sw_,fe,fw,FL,BL in seq:
        kp=[]
        def add(l,x,y):kp.append({'x':round(min(.99,max(.01,x)),4),'y':round(min(.99,max(.01,y)),4),'label':l,'z_index':int(K[l]['z_index']//1)})
        for l in ['NOSE','NECK','LEFT EYE','RIGHT EYE','LEFT EAR','RIGHT EAR','LEFT SHOULDER','RIGHT SHOULDER']:
            x,y=P(l);add(l,x+lean,y+sink)
        for l in ['LEFT HIP','RIGHT HIP']:
            x,y=P(l);add(l,x+lean*.3,y+sink)
        hx,hy=hip[0]+lean*.3,hip[1]+sink
        for side,(e,w) in [(sw,(se,sw_)),(fr,(fe,fw))]:
            sx,sy=P(side+' SHOULDER');sx+=lean;sy+=sink
            if e is None:
                x,y=P(side+' ELBOW');add(side+' ELBOW',x+lean,y+sink);x,y=P(side+' ARM');add(side+' ARM',x+lean,y+sink)
            else:add(side+' ELBOW',sx+e[0],sy+e[1]);add(side+' ARM',sx+w[0],sy+w[1])
        for side,L in [(fl,FL),(bl,BL)]:
            if L is None:
                x,y=P(side+' KNEE');add(side+' KNEE',x,y+sink*.5);x,y=P(side+' LEG');add(side+' LEG',x,y)
            else:add(side+' KNEE',hx+L[0][0],hy+L[0][1]);add(side+' LEG',hx+L[1][0],hy+L[1][1])
        out.append(kp)
    return out
res={'first':[{'x':p['x'],'y':p['y'],'label':p['label'],'z_index':int(p['z_index']//1)} for p in K.values()],'A':frames(A),'B':frames(B),'sword_hand':sw}
json.dump(res,open(out,'w'))
EDG=[('NECK','NOSE'),('LEFT SHOULDER','LEFT ELBOW'),('LEFT ELBOW','LEFT ARM'),('RIGHT SHOULDER','RIGHT ELBOW'),('RIGHT ELBOW','RIGHT ARM'),('LEFT HIP','LEFT KNEE'),('LEFT KNEE','LEFT LEG'),('RIGHT HIP','RIGHT KNEE'),('RIGHT KNEE','RIGHT LEG'),('LEFT SHOULDER','RIGHT SHOULDER'),('LEFT HIP','RIGHT HIP'),('LEFT SHOULDER','LEFT HIP'),('RIGHT SHOULDER','RIGHT HIP')]
S=200;o=Image.new('RGB',(S*7,S*2),'#334');d=ImageDraw.Draw(o)
for r,key in enumerate(['A','B']):
    for f,kp in enumerate([res['first']]+res[key]):
        M={p['label']:(f*S+p['x']*S,r*S+p['y']*S) for p in kp}
        for a,c in EDG:d.line([M[a],M[c]],fill='#f84' if 'RIGHT' in a+c else '#4cf',width=3)
        w=M[sw+' ARM'];d.ellipse([w[0]-5,w[1]-5,w[0]+5,w[1]+5],outline='#ff0',width=2)
o.save(dbg);print('sword',sw,'front leg',fl)
