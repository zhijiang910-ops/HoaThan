import sys,json,math
sys.path.insert(0,'tools');import qc
N=128;MAST={'nam':'pl/xt_nam_first.png','nu':'pl/xd_nu_first.png'};K={'nam':('far_wrist','sword_tip'),'nu':('left_wrist','sword_tip')}
mv=sys.argv[1]
for tag in sys.argv[2:]:
    g=tag.split('_')[0];w,t=K[g];kp=json.load(open(f'combo3/{g}_pose_{mv}.json'))
    M=qc.load(MAST[g]);pal=qc.palette_set(M).astype(float)
    f0={p['label']:(p['x']*N,p['y']*N) for p in json.load(open(f'combo3/{g}_pose_A3.json'))[0]};L=math.dist(f0[w],f0[t]);mang=math.degrees(math.atan2(f0[t][1]-f0[w][1],f0[t][0]-f0[w][0]))
    fr=[]
    for i,fk in enumerate(kp):
        P={p['label']:(p['x']*N,p['y']*N) for p in fk};fr.append((f'combo3/out/{tag}_{i:02d}.png',P[w],math.degrees(math.atan2(P[t][1]-P[w][1],P[t][0]-P[w][0]))))
    r=qc.check(MAST[g],f0[w],mang,L,fr)[1:]
    bad=[(i,x['sword_cov'],x['tip'],x['over']) for i,x in enumerate(r) if not x['pass']]
    tp=[round(qc.costume12(qc.load(f[0]),pal)*100,1) for f in fr];st=[i for i,f in enumerate(fr) if qc.stray(qc.load(f[0]))]
    print(tag,'kiếm lỗi:',bad,'| trang phục min',min(tp),'| rác ở khung',st)
