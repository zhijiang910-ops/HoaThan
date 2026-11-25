import json,base64,time,os,sys,threading,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
src=open('trangphuc/gen_tp.py').read();INS=eval(src[src.index("INS=")+4:src.index("\nsz=")])
sect,g=sys.argv[1],sys.argv[2];F=[tuple(x) for x in json.load(open('trangphuc/frames.json'))]
key=f'{sect}_{g}';os.makedirs(f'trangphuc/full/{key}',exist_ok=True);os.makedirs('trangphuc/cells',exist_ok=True)
sh=Image.open(f'/home/user/HoaThan/game/assets/hero_{g}_ns.png').convert('RGBA')
for (x,y) in F:
    p=f'trangphuc/cells/{g}_{x}_{y}.png'
    if not os.path.exists(p):
        c=Image.new('RGBA',(128,128),(0,0,0,0));c.alpha_composite(sh.crop((x,y,x+160,y+128)),(-16,0));c.save(p)
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
rb=b(f'trangphuc/in/ref_{key}.png');rw,rh=Image.open(f'trangphuc/in/ref_{key}.png').size;sz={'width':128,'height':128}
todo=[f'{x}_{y}' for x,y in F if not os.path.exists(f'trangphuc/full/{key}/{x}_{y}.png')]
groups=[todo[i:i+3] for i in range(0,len(todo),3)]
if groups and len(groups[-1])<2:groups[-1]=[f'{F[0][0]}_{F[0][1]}']+groups[-1]
def job(grp):
    body={'reference_image':{'image':{'type':'base64','base64':rb},'size':{'width':rw,'height':rh}},'frames':[{'image':{'type':'base64','base64':b(f'trangphuc/cells/{g}_{k}.png')},'size':sz} for k in grp],'image_size':sz,'no_background':True,'additional_instructions':INS[sect],'seed':5}
    for a in range(3):
        try:
            j=pl.req('POST','/transfer-outfit-v2',body);jid=j['background_job_id'];t0=time.time()
            while time.time()-t0<600:
                time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
                if r['status']=='completed':break
                if r['status']=='failed':raise Exception(str(r)[:200])
            ims=r['last_response'].get('images',[])
            for k,x in zip(grp,ims):
                x=x.get('base64') if isinstance(x,dict) and 'base64' in x else x.get('image',{}).get('base64')
                open(f'trangphuc/full/{key}/{k}.png','wb').write(base64.b64decode(x.split(',')[-1]))
            print('ok',grp,flush=True);return
        except Exception as e:print('retry',grp,e,flush=True);time.sleep(20)
th=[]
for grp in groups:
    t=threading.Thread(target=job,args=(grp,));t.start();th.append(t);time.sleep(12)
    while sum(x.is_alive() for x in th)>=3:time.sleep(4)
for t in th:t.join()
print('done',key,len(os.listdir(f'trangphuc/full/{key}')),'/',len(F),flush=True)
