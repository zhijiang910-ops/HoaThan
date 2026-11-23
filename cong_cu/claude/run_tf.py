import sys,json,os,time,threading
sys.path.insert(0,'/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/outfit')
from pl2 import *
S='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/'
g=sys.argv[1];ref=sys.argv[2]
used=json.load(open(S+'wl/frames_used.json'))['hero_'+g];order=[]
for an in ['idle','run','attack','attack2','attack3','hit','death','cutC','dash','brake']:
  for f in used.get(an,[]):
    k='%d_%d'%(f[0],f[1])
    if k not in order:order.append(k)
os.makedirs('out_'+g,exist_ok=True)
todo=[k for k in order if not os.path.exists('out_%s/%s.png'%(g,k))]
groups=[todo[i:i+3] for i in range(0,len(todo),3)]
if groups and len(groups[-1])<2:groups[-1]=[order[0]]+groups[-1]   # cần tối thiểu 2 khung
sz={'width':128,'height':128}
def job(grp):
  body={'reference_image':{'image':{'type':'base64','base64':b64(ref)},'size':sz},'frames':[{'image':{'type':'base64','base64':b64('cells/%s_%s.png'%(g,k))},'size':sz} for k in grp],'image_size':sz,'no_background':True,
    'additional_instructions':'Side view facing right. Keep the exact pose, limbs, hair, ponytail, hair ribbon and face of every frame; only replace the clothing with the reference black lacquered armor (gold trim, red sash). Hands stay empty.'}
  for a in range(4):
    try:
      j=wait(req('POST','/transfer-outfit-v2',body));ims=j.get('images') or j.get('frames') or []
      for k,im in zip(grp,ims):save(im if 'base64' in im else im.get('image'),'out_%s/%s.png'%(g,k))
      print('ok',grp,flush=True);return
    except Exception as e:print('retry',grp,e,flush=True);time.sleep(30)
th=[]
for i,grp in enumerate(groups):
  t=threading.Thread(target=job,args=(grp,));t.start();th.append(t);time.sleep(20)
  while sum(x.is_alive() for x in th)>=3:time.sleep(5)
for t in th:t.join()
print('done',len(os.listdir('out_'+g)),'/',len(order))
