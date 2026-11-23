import sys,json,math
sys.path.insert(0,sys.argv[1]);import qc
C=sys.argv[2];N=128
MAST={'nam':'../pl/xt_nam_first.png','nu':'../pl/xd_nu_first.png'}
GRIP={'nam':('far_wrist','sword_tip'),'nu':('left_wrist','sword_tip')}
res={}
for g in ('nam','nu'):
    for k in 'CL':
        kp=json.load(open(f'{C}/{g}_pose_{k}.json'))
        f0={p['label']:(p['x']*N,p['y']*N) for p in kp[0]};w,t=GRIP[g];L=math.dist(f0[w],f0[t])
        mang=math.degrees(math.atan2(f0[t][1]-f0[w][1],f0[t][0]-f0[w][0]))
        for seed in (31,47):
            fr=[]
            for i,fk in enumerate(kp):
                P={p['label']:(p['x']*N,p['y']*N) for p in fk}
                a=math.degrees(math.atan2(P[t][1]-P[w][1],P[t][0]-P[w][0]))
                fr.append((f'{C}/out/{g}_{k}{seed}_{i:02d}.png',P[w],None if (k=='C' and i==1) else a))
            r=qc.check(MAST[g],f0[w],mang,L,fr)
            bad=[(i,x) for i,x in enumerate(r[1:]) if x.get('pass') is False]
            res[f'{g}_{k}{seed}']=bad
            print(f'{g}_{k}{seed}: FAIL',[(i,x['sword_cov'],x['tip'],x['costume%']) for i,x in bad])
