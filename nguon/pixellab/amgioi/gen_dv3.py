import sys,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
M='/home/user/HoaThan/nguon/master_amgioi/';OUT='/home/user/HoaThan/nguon/pixellab/amgioi/sy6/'
D=("Convert ONLY the central king (Yan Wang, King of the Underworld, the FINAL BOSS) into the exact pixel art style of the other bosses of this game: ultra-fine 1 px pixel grid, NO big blocky pixels, thin 1 px dark outline, rich shading 4 to 5 tones per material, fabric folds and fine texture, muted dark palette, crisp hard edges. "
   "KEEP THE DESIGN IDENTICAL: black imperial crown board with long hanging gold bead curtains and red tassels, glowing red eyes, long black wavy hair and long black beard, open shouting mouth, green-black robe with wide sleeves and gold cloud-swirl embroidery, gold dragon-head shoulder ornaments, glowing red demon-skull chest plate, jewelled belt, black and gold front panel, one hand holding a large brush pen, the other hand reaching out, same pose. "
   "REMOVE completely: the two grey ghost officials behind, the desk with scroll, the brazier with flames, the dark vignette background and glow. Only the king, transparent background, subtle dark red aura around him is allowed.")
S=256;seed=7
im=Image.open(M+'chatgpt_diemvuong_v4_goc.png').convert('RGBA');print(im.size)
c=im.crop((380,0,1360,1024))
f=236/c.height;w=min(S-6,round(c.width*f));f=w/c.width
sm=c.resize((w,round(c.height*f)),Image.LANCZOS)
cv=Image.new('RGBA',(S,S),(0,0,0,255));cv.alpha_composite(sm,((S-sm.width)//2,S-sm.height-2));cv.save(OUT+'in_dv.png')
b64=base64.b64encode(open(OUT+'in_dv.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":S,"height":S}],"image_size":{"width":S,"height":S},"description":D,"seed":seed,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(OUT+f'diemvuong_s{seed}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print('ok')
