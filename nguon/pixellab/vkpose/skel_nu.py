# Tư thế nữ = khung xương nữ đứng + (khung xương nam tư thế i - khung xương nam đứng), rồi animate-with-skeleton-v3 từ khung đứng nữ.
import json,base64,sys,time,os,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
S=json.load(open('skel.json'));seed=int(sys.argv[1]);src=sys.argv[2] if len(sys.argv)>2 else 'idle_nu_ns'
kp=lambda f:{k['label']:k for k in S[f]['keypoints']}
base=kp('idle_nu_ns');m0=kp('nam_ms_0')
def tgt(i):
    mi=kp(f'nam_ms_{i}');o=[]
    for l,k in base.items():
        if l in mi and l in m0:o.append({'x':k['x']+mi[l]['x']-m0[l]['x'],'y':k['y']+mi[l]['y']-m0[l]['y'],'label':l,'z_index':mi[l]['z_index']})
        else:o.append(dict(k))
    return o
b=base64.b64encode(open(f'in/{src}.png','rb').read()).decode()
body={'description':os.environ.get('DESC','young wuxia swordswoman, long dark brown ponytail with red ribbon, red hanfu robe, dark boots, empty hands'),
 'action':os.environ.get('ACT','stands firm with fists at the waist, then points forward with the index finger and the arm fully extended, then lowers the arm. Plain character only: NO effects, NO fire, NO particles, NO smoke, NO magic. Hair and ribbon stay tidy and crisp, feet close together'),
 'direction':'east','view':'side','first_frame':{'type':'base64','base64':b},'first_frame_keypoints':S['idle_nu_ns']['keypoints'],
 'keypoints':[tgt(1),tgt(2),tgt(3)],'seed':seed,'no_background':True}
import urllib.error
try:
    j=pl.req('POST','/animate-with-skeleton-v3',body)
except urllib.error.HTTPError as e:
    print('ERR',e.read().decode()[:1500]);raise SystemExit(1)
jid=j['background_job_id'];t0=time.time();print('job',jid,flush=True)
while time.time()-t0<900:
    time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
ims=r['last_response'].get('images',[]);out=f'out/nu_skel_{src}_s{seed}'+os.environ.get('TAG','');os.makedirs(out,exist_ok=True)
for n,i in enumerate(ims):
    i=i.get('base64') if isinstance(i,dict) and 'base64' in i else i.get('image',{}).get('base64')
    open(f'{out}/{n}.png','wb').write(base64.b64decode(i.split(',')[-1]))
print('ok',out,len(ims),r['last_response'].get('usage'))
