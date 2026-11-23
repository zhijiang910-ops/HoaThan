"""Gọi PixelLab API (key do proxy gắn). Dùng: pl.py <endpoint> <json_body_file> <out_dir>"""
import json,sys,time,base64,io,urllib.request,os
API='https://api.pixellab.ai/v2'
def req(method,path,body=None):
    r=urllib.request.Request(API+path,method=method,data=json.dumps(body).encode() if body is not None else None,
        headers={'Authorization':'Bearer proxy-injected','Content-Type':'application/json'})
    with urllib.request.urlopen(r,timeout=120) as f:return json.loads(f.read())
def run(path,body,out,tag):
    os.makedirs(out,exist_ok=True)
    j=req('POST',path,body);jid=j.get('background_job_id') or j.get('id');print('job',jid,{k:v for k,v in j.items() if k!='images'})
    t0=time.time()
    while True:
        time.sleep(6);r=req('GET','/background-jobs/'+jid);st=r.get('status')
        if st=='completed':break
        if st=='failed':print('FAILED',json.dumps(r)[:800]);sys.exit(1)
        if time.time()-t0>600:print('timeout');sys.exit(1)
    lr=r['last_response'];imgs=lr.get('images',[])
    for i,im in enumerate(imgs):
        b=im.get('base64') if isinstance(im,dict) else im
        open(f'{out}/{tag}_{i:02d}.png','wb').write(base64.b64decode(b.split(',')[-1]))
    print('done',len(imgs),'in',int(time.time()-t0),'s', {k:v for k,v in lr.items() if k not in('images','keypoints')})
    json.dump({k:v for k,v in lr.items() if k!='images'},open(f'{out}/{tag}_meta.json','w'))
if __name__=='__main__':
    run(sys.argv[1],json.load(open(sys.argv[2])),sys.argv[3],sys.argv[4])
