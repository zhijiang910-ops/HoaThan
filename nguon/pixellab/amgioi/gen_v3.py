import sys,base64,time,importlib.util
from PIL import Image
import numpy as np
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
M='/home/user/HoaThan/nguon/master_amgioi/';OUT='/home/user/HoaThan/nguon/pixellab/amgioi/sy4/'
STYLE=("Convert this character into the exact pixel art style of the other bosses of this game: ultra-fine 1 px pixel grid, NO big blocky pixels, thin 1 px dark outline (not thick), rich shading with 4 to 5 tones per material, fabric folds and fine texture, muted dark palette, crisp hard edges. "
       "KEEP THE DESIGN IDENTICAL: same face, hair, hat, robe, props, colours, chibi proportions and pose, side view facing right. ")
J={'manhba':STYLE+"Details: old woman with silver-grey hair in a bun with gold hairpins and a white flower and green ribbon with jade tassel, angry red glowing eyes with a small red mark on the forehead, gold earring, teal-grey layered robe with cloud swirl patterns and gold tassel, holding a wooden ladle dripping green soup; a LARGE black iron cauldron with gold ring handle and white skull, green soup and curling green steam, standing next to her. Transparent background.",
'phanquan':STYLE+"Details: black official hat with wide gold-trimmed wing ornaments and a red gem, red face with angry eyes, long black beard, flowing red ribbons, dark crimson robe with gold cloud-swirl trim and a red tassel, holding a large judge brush pen with white fur tip in one hand and a black book with a skull in the other. Transparent background."}
TGT={'manhba':152,'phanquan':160}
k=sys.argv[1];S=192;seed=int(sys.argv[2]) if len(sys.argv)>2 else 7
im=Image.open(M+f'chatgpt_{k}_v3_goc.png').convert('RGBA');im=im.crop(im.getbbox())
f=TGT[k]/im.height
w=round(im.width*f)
if w>S-8:f=(S-8)/im.width;w=S-8
sm=im.resize((w,round(im.height*f)),Image.LANCZOS)
a=np.array(sm);a[:,:,3]=np.where(a[:,:,3]>110,255,0);sm=Image.fromarray(a)
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(sm,((S-sm.width)//2,S-sm.height-4));cv.save(OUT+f'in_{k}.png')
b64=base64.b64encode(open(OUT+f'in_{k}.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":S,"height":S}],"image_size":{"width":S,"height":S},"description":J[k],"seed":seed,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(OUT+f'{k}_s{seed}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print(k,'ok')
