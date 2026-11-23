"""Tạo VFX PixelLab: plvfx.py <name> <out_dir> <desc> [sprite.png]"""
import json,sys,time,base64,urllib.request,os
API='https://api.pixellab.ai/v2'
def req(m,p,b=None):
    r=urllib.request.Request(API+p,method=m,data=json.dumps(b).encode() if b is not None else None,headers={'Authorization':'Bearer proxy-injected','Content-Type':'application/json'})
    with urllib.request.urlopen(r,timeout=120) as f:return json.loads(f.read())
name,out,desc=sys.argv[1:4];os.makedirs(out,exist_ok=True)
b={'description':desc,'artist':os.environ.get('ARTIST','lite'),'name':name}
if len(sys.argv)>4:b['sprite']={'type':'base64','base64':base64.b64encode(open(sys.argv[4],'rb').read()).decode(),'format':'png'}
if os.environ.get('GAMEPACK'):b['game_pack']=True
if os.environ.get('EFFECT'):
    m=json.load(open(os.environ['EFFECT']+'_meta.json'));b['effect_id']=m['effect_id'];b['conversation']=json.load(open(os.environ['EFFECT']+'_conv.json'));b.pop('sprite',None)
try:j=req('POST','/vfx',b)
except urllib.error.HTTPError as e:print('ERR',e.code,e.read()[:600]);sys.exit(1)
jid=j.get('background_job_id');print(name,'quote',j.get('quoted_generations'))
t0=time.time()
while True:
    time.sleep(8);r=req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':print('FAILED',json.dumps(r)[:600]);sys.exit(1)
    if time.time()-t0>600:print('timeout');sys.exit(1)
lr=r['last_response'];json.dump({k:v for k,v in lr.items() if k!='conversation'},open(f'{out}/{name}_meta.json','w'))
json.dump(lr.get('conversation'),open(f'{out}/{name}_conv.json','w'))
F=lr.get('files',{});F=F.items() if isinstance(F,dict) else [(x.get('name'),x.get('url')) for x in F]
for fn,u in F:
    if fn.endswith(('.png','.json','.gif','.zip')):
        with urllib.request.urlopen(u,timeout=120) as g:open(f'{out}/{fn}','wb').write(g.read())
print(name,'done',int(time.time()-t0),'s',lr.get('canvas'),lr.get('frames'),lr.get('fps'),'|',(lr.get('message') or '')[:160])
