"""Kiểm combo chốt: kiếm (độ phủ, đầu kiếm, không dài/ngắn hơn master, không dư kiếm), bàn tay 2 bên, chân chạm đất,
điểm ảnh rác, màu trang phục (sai số 12) so với master, chiều cao người. qc3.py <tools> <combo3_dir> <move> <tags...>"""
import sys,json,math
sys.path.insert(0,sys.argv[1]);import qc
import numpy as np
C=sys.argv[2];mv=sys.argv[3];tags=sys.argv[4:];N=128
MAST={'nam':C+'/../pl/xt_nam_first.png','nu':C+'/../pl/xd_nu_first.png'}
K={'nam':dict(w='far_wrist',t='sword_tip',nw='near_wrist',an=('near_ankle','far_ankle')),'nu':dict(w='left_wrist',t='sword_tip',nw='right_wrist',an=('right_ankle','left_ankle'))}
res={}
for tag in tags:
    g=tag.split('_')[0];k=K[g];kp=json.load(open(f'{C}/{g}_pose_{mv}.json'))
    M=qc.load(MAST[g]);pal=qc.palette_set(M).astype(float);mh=np.nonzero(M[...,3].max(1)>40)[0];mH=mh[-1]-mh[0]
    f0={p['label']:(p['x']*N,p['y']*N) for p in json.load(open(f'{C}/{g}_pose_A3.json'))[0]};L=math.dist(f0[k['w']],f0[k['t']])
    mang=math.degrees(math.atan2(f0[k['t']][1]-f0[k['w']][1],f0[k['t']][0]-f0[k['w']][0]))
    fr=[]
    for i,fk in enumerate(kp):
        P={p['label']:(p['x']*N,p['y']*N) for p in fk};a=math.degrees(math.atan2(P[k['t']][1]-P[k['w']][1],P[k['t']][0]-P[k['w']][0]))
        fr.append((f'{C}/out/{tag}_{i:02d}.png',P[k['w']],a))
    r=qc.check(MAST[g],f0[k['w']],mang,L,fr)[1:]
    rows=[]
    for i,(x,fk) in enumerate(zip(r,kp)):
        P={p['label']:(p['x']*N,p['y']*N) for p in fk};A=qc.load(fr[i][0])
        hand=qc.hand_ok(A,P[k['w']]) ;off=qc.hand_ok(A,P[k['nw']])
        al=A[...,3]>40;foot=all(al[int(P[a][1])-4:int(P[a][1])+6,int(P[a][0])-6:int(P[a][0])+7].any() for a in k['an'])
        st=qc.stray(A);c12=qc.costume12(A,pal)
        ys=np.nonzero(A[...,3].max(1)>40)[0];h=ys[-1]-ys[0]
        bad=[]
        if not x['pass']:bad.append(f"kiếm(phủ {x['sword_cov']},đầu {x['tip']},thừa {x['over']})")
        if x['extra']:bad.append(f"dư kiếm {x['extra']}")
        if not hand:bad.append('mất tay cầm kiếm')
        if not off:bad.append('mất tay kia')
        if not foot:bad.append('mất chân')
        if st:bad.append(f'điểm rác {st}')
        if c12<0.98:bad.append(f'trang phục {c12*100:.1f}%')
        rows.append({'f':i,'ok':not bad,'loi':bad,'phu':x['sword_cov'],'dau':x['tip'],'tp':round(c12*100,1),'cao%':round(100*h/mH)})
    res[tag]=rows
    print(tag,'ĐẠT' if all(z['ok'] for z in rows) else 'LỖI',[(z['f'],z['loi']) for z in rows if not z['ok']])
json.dump(res,open(f'{C}/qc_{mv}.json','w'),ensure_ascii=False,indent=0)
