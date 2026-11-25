# Tạo lại khung Mao Sơn nam: NHIỀU khung một lần + bảng màu cố định (target_palette) + mô tả cố định => đồng nhất. 
import json,base64,time,os,sys,importlib.util
from PIL import Image
import numpy as np
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
g,tag,seed=sys.argv[1],sys.argv[2],int(sys.argv[3]);cells=[tuple(map(int,c.split(','))) for c in sys.argv[4:]]
A='/home/user/HoaThan/game/assets/';T='trangphuc/'
os.makedirs(f'{T}cells',exist_ok=True);out=f'{T}full/maoson_{g}_{tag}';os.makedirs(out,exist_ok=True)
ns=Image.open(A+f'hero_{g}_ns.png').convert('RGBA');ms=Image.open(A+f'hero_{g}_ms.png').convert('RGBA')
# bảng màu: lấy từ các khung đứng + chạy đã đạt (hàng 0, ô 0-11) của chính bộ Mao Sơn
px=[]
for c in range(12):
    a=np.array(ms.crop((c*160,0,c*160+160,128)));px.append(a[a[:,:,3]>0][:,:3])
px=np.concatenate(px);im=Image.fromarray(px.reshape(-1,1,3).astype('uint8')).quantize(40,method=Image.MEDIANCUT)
pal=np.array(im.getpalette()[:120]).reshape(-1,3);cols=['#%02x%02x%02x'%tuple(c) for c in pal]
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
fr=[]
for (x,y) in cells:
    p=f'{T}cells/{g}_{x}_{y}.png'
    if not os.path.exists(p):
        c=Image.new('RGBA',(128,128),(0,0,0,0));c.alpha_composite(ns.crop((x,y,x+160,y+128)),(-16,0));c.save(p)
    fr.append({'image':{'type':'base64','base64':b(p)},'size':{'width':128,'height':128}})
rf=f'{T}in/ref_maoson_{g}.png';rw,rh=Image.open(rf).size
INS=("The SAME outfit in every frame, never change it between frames: a long deep navy-blue robe with fine gold cloud-pattern trim along the hem and cuffs, narrow sleeves with thin white cuffs, one single yellow-gold sash at the waist with one tail hanging at the hip, a thin white inner layer only at the very bottom hem, dark navy-grey trousers and black boots. "
     "Boots are plain black with NO gold trim. The navy robe is a medium deep navy, not black. Keep the exact same pixel art style, same line weight, same character proportions and pose as each input frame.")
body={'reference_image':{'image':{'type':'base64','base64':b(rf)},'size':{'width':rw,'height':rh}},'frames':fr,'image_size':{'width':128,'height':128},'seed':seed,'no_background':True,'additional_instructions':INS,'target_palette':{'colors':cols,'name':'maoson','max_colors':40}}
import urllib.request,urllib.error
try:
    j=pl.req('POST','/transfer-outfit-v2',body)
except urllib.error.HTTPError as e:
    print('ERR',e.read().decode()[:600]);raise SystemExit(1)
print(str(j)[:200]);jid=j['background_job_id'];t0=time.time()
while time.time()-t0<900:
    time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
ims=r['last_response'].get('images',[]);print('frames',len(ims))
for (x,y),i in zip(cells,ims):
    i=i.get('base64') if isinstance(i,dict) and 'base64' in i else i.get('image',{}).get('base64')
    open(f'{out}/{x}_{y}.png','wb').write(base64.b64decode(i.split(',')[-1]))
print('ok',out)
