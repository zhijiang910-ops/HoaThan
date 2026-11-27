# Tư thế Vạn Kiếm cho bộ áo khác: transfer-outfit-v2 từ khung tư thế (128 canvas) + ảnh mẫu = khung đứng của bộ đích; bảng màu lấy từ hàng 0 của sheet đích.
# python3 gen_vk.py <sheet đích vd nam_ns> <seed> <tag> <khung vào 1> [<khung 2> <khung 3>]
import json,base64,time,os,sys,importlib.util
from PIL import Image
import numpy as np
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
D='/home/user/HoaThan/nguon/pixellab/vkpose/';A='/home/user/HoaThan/game/assets/'
tgt,seed,tag=sys.argv[1],int(sys.argv[2]),sys.argv[3];ins=sys.argv[4:]
sh=Image.open(A+'hero_'+tgt+'.png').convert('RGBA')
px=[]
for c in range(12):
    a=np.array(sh.crop((c*160,0,c*160+160,128)));px.append(a[a[:,:,3]>0][:,:3])
px=np.concatenate(px);im=Image.fromarray(px.reshape(-1,1,3).astype('uint8')).quantize(40,method=Image.MEDIANCUT)
pal=np.array(im.getpalette()[:120]).reshape(-1,3);cols=['#%02x%02x%02x'%tuple(c) for c in pal]
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
fr=[{'image':{'type':'base64','base64':b(D+'in/'+f+'.png')},'size':{'width':128,'height':128}} for f in ins]
INS=os.environ.get('INS',"Dress the character in EXACTLY the outfit of the reference image (same robe/armor, colors, trim, sash, boots). Keep the exact pose, arm positions, hands, hair, face, proportions and pixel art style of each input frame. Same outfit in every frame.")
body={'reference_image':{'image':{'type':'base64','base64':b(D+'in/idle_'+tgt+'.png')},'size':{'width':128,'height':128}},'frames':fr,'image_size':{'width':128,'height':128},'seed':seed,'no_background':True,'additional_instructions':INS,'target_palette':{'colors':cols,'name':tgt,'max_colors':40}}
j=pl.req('POST','/transfer-outfit-v2',body);jid=j['background_job_id'];t0=time.time()
while time.time()-t0<900:
    time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
ims=r['last_response'].get('images',[]);out=D+'out/'+tag;os.makedirs(out,exist_ok=True)
for f,i in zip(ins,ims):
    i=i.get('base64') if isinstance(i,dict) and 'base64' in i else i.get('image',{}).get('base64')
    open(f'{out}/{f}.png','wb').write(base64.b64decode(i.split(',')[-1]))
print('ok',out,len(ims))
