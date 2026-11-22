"""Chạy QC cho một bộ: qc_run.py <k> <tag> <keyset: run|A|B>"""
import sys,json,glob,math
sys.path.insert(0,sys.argv[4]);import qc
k,tag,key=sys.argv[1:4]
P='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/pl/'
C=json.load(open(P+f'out/{k}_cust_meta.json'));F={p['label']:p for p in C['frames'][0]}
names=[j['name'] for j in C['rig']];sw=[n for n in names if n.startswith('sword')];par={j['name']:j['parent'] for j in C['rig']}
wr=par[sw[0]];S=128
w0=(F[wr]['x']*S,F[wr]['y']*S);t0=(F[sw[-1]]['x']*S,F[sw[-1]]['y']*S)
L=math.dist(w0,t0);mang=math.degrees(math.atan2(t0[1]-w0[1],t0[0]-w0[0]))
fs=sorted(glob.glob(P+f'out/{tag}_0*.png'))
frames=[]
if key=='run':
    R=json.load(open(P+f'{k}_runskel.json'));lab='LEFT ARM' if R['sword_hand']=='LEFT' else 'RIGHT ARM'
    for f,kp in zip(fs,R['frames']):
        p={q['label']:q for q in kp}[lab];frames.append((f,(p['x']*S,p['y']*S),mang))
else:
    R=json.load(open(P+f'{k}_rigatk.json'))
    for f,kp in zip(fs,R[key]):
        p={q['label']:q for q in kp};w=(p[wr]['x']*S,p[wr]['y']*S);t=(p[sw[-1]]['x']*S,p[sw[-1]]['y']*S)
        frames.append((f,w,math.degrees(math.atan2(t[1]-w[1],t[0]-w[0]))))
res=qc.check(P+f'{k}_first.png',w0,mang,L,frames)
print(tag,'L=%.1f'%L)
for r in res:print('  ',('ĐẠT' if r.get('pass') else ('---' if 'pass' not in r else 'LỖI')),r)
