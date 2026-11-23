import json,urllib.request,base64,time
API='https://api.pixellab.ai/v2'
def req(m,p,b=None):
  r=urllib.request.Request(API+p,method=m,data=json.dumps(b).encode() if b is not None else None,headers={'Authorization':'Bearer proxy-injected','Content-Type':'application/json'})
  try:
    with urllib.request.urlopen(r,timeout=180) as f:return json.loads(f.read())
  except urllib.error.HTTPError as e:print('ERR',e.code,e.read()[:600]);raise
def wait(j):
  if 'background_job_id' not in j:return j
  jid=j['background_job_id']
  while True:
    time.sleep(6);r=req('GET','/background-jobs/'+jid)
    if r['status'] in('completed','failed'):print(r['status']);return r.get('last_response') or r
b64=lambda f:base64.b64encode(open(f,'rb').read()).decode()
def save(img,f):open(f,'wb').write(base64.b64decode(img['base64'].split(',')[-1]))
