import sys,base64,time,importlib.util
from PIL import Image
import numpy as np
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
M='/home/user/HoaThan/nguon/master_amgioi/'
OUT='/home/user/HoaThan/nguon/pixellab/amgioi/sy2/'
STYLE=("Match the exact rendering style of the other bosses of this game: ultra-fine 1 px pixel grid with NO 2x2 blocks, crisp hard edges, a thin 1 px near-black outline, rich shading with 4 to 5 tones per material, fabric folds and fine texture, small ornate details, muted dark palette. "
       "KEEP THE CHARACTER DESIGN IDENTICAL to the input (same face, hat, props, silhouette, pose), side view facing right. ")
J={
'phanquan':STYLE+"Details: a black official hat with two wing-shaped side ornaments (guan cap) and a small feather; red face with black beard and moustache; crimson robe with gold trim and wide sleeves; a golden decorative panel; holding a large brush pen with a white fur tip, a small book at the waist. Transparent background.",
'manhba':STYLE+"Details: a hunched old woman with grey-white hair in a bun held by gold hairpins and a white flower; grey-green robe with gold ornaments and tattered strips; holding a wooden ladle that drips green soup; at her feet a black iron cauldron with a white skull emblem and curling green steam. Transparent background."}
TGT={'phanquan':156,'manhba':152}
k=sys.argv[1];S=192;seed=int(sys.argv[2]) if len(sys.argv)>2 else 7
im=Image.open(M+f'chatgpt_{k}_goc.png').convert('RGBA');im=im.crop(im.getbbox())
nat=im.resize((im.width//2,im.height//2),Image.NEAREST)
f=TGT[k]/nat.height
sm=nat.resize((round(nat.width*f),TGT[k]),Image.LANCZOS)
a=np.array(sm);a[:,:,3]=np.where(a[:,:,3]>110,255,0);sm=Image.fromarray(a)
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(sm,((S-sm.width)//2,S-sm.height-6));cv.save(OUT+f'in_{k}.png')
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
