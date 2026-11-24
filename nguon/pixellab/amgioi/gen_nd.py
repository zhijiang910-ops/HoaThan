import base64,time,importlib.util
from PIL import Image
import numpy as np
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
A='/home/user/HoaThan/game/assets/nguudau_am.png';OUT='/home/user/HoaThan/nguon/pixellab/amgioi/sy7/'
D=("Redraw this exact character at a larger size with the same rendering as the other bosses of this game (like the horse-headed general Ma Mian): ultra-fine 1 px pixel grid, NO big blocky pixels, thin 1 px dark outline, rich shading 4 to 5 tones per material, fine texture on fur, armor and cloth, muted dark palette. "
   "KEEP THE DESIGN IDENTICAL: black bull head with big curved pale horns and glowing red eyes and nose ring, spiked dark iron pauldrons, blue-grey muscular body, red sash belt with a skull, dark red cape, black trident with sharp prongs, same pose, side view facing right. The character should look big, powerful and detailed like a boss. Transparent background.")
S=192;T=160;seed=7
im=Image.open(A).convert('RGBA');im=im.crop(im.getbbox())
f=T/im.height;w=min(S-6,round(im.width*f));f=w/im.width
sm=im.resize((w,round(im.height*f)),Image.LANCZOS)
a=np.array(sm);a[:,:,3]=np.where(a[:,:,3]>110,255,0);sm=Image.fromarray(a)
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(sm,((S-sm.width)//2,S-sm.height-4));cv.save(OUT+'in_nd.png')
b64=base64.b64encode(open(OUT+'in_nd.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":S,"height":S}],"image_size":{"width":S,"height":S},"description":D,"seed":seed,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(OUT+f'nguudau_s{seed}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print('ok')
