import sys,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
M='/home/user/HoaThan/nguon/master_amgioi/';OUT='/home/user/HoaThan/nguon/pixellab/amgioi/sy6/'
D=("Convert this whole scene into the exact pixel art style of the other bosses of this game: ultra-fine 1 px pixel grid, NO big blocky pixels, thin 1 px dark outline, rich shading 4 to 5 tones per material, fabric folds and fine texture, muted dark palette, crisp hard edges. "
   "KEEP THE WHOLE COMPOSITION AND DESIGN IDENTICAL: the central king Yan Wang with black crown board with long hanging gold bead curtains and red tassels, glowing red eyes, long black wavy hair and beard, green-black robe with gold cloud embroidery, gold dragon-head shoulders, glowing red demon-skull chest plate, one hand holding a big brush writing on a long scroll lying on an ornate black-and-gold desk (throne) with a skull emblem at left front, the other hand reaching out; BEHIND HIM two translucent grey ghost officials (left one with tall hat holding a staff with grey smoke, right one with horned crown), grey swirling smoke; at right front an ornate black-gold brazier with a skull emblem and red flames. Transparent background, remove the dark vignette.")
W,H=384,256;seed=7
im=Image.open(M+'chatgpt_diemvuong_v4_goc.png').convert('RGBA').resize((W,H),Image.LANCZOS)
im.save(OUT+'in_dvscene.png')
b64=base64.b64encode(open(OUT+'in_dvscene.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":W,"height":H}],"image_size":{"width":W,"height":H},"description":D,"seed":seed,"no_background":True})
print(str(j)[:200])
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<500:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(OUT+f'dvscene_s{seed}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print('ok')
