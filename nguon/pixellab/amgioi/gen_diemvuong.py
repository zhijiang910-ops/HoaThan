import sys,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
M='/home/user/HoaThan/nguon/master_amgioi/'
OUT='/home/user/HoaThan/nguon/pixellab/amgioi/dv/'
S=256
D=("Redraw this exact character as the FINAL BOSS game sprite. KEEP THE DESIGN: same flat black imperial crown board with gold bead strings, same red face with bold black eyebrows and long black beard, same black and gold dragon-pattern robe, same wide sleeves, same cream tablet in the front hand, same pose, side view facing right. "
   "The source is blocky with big 2x2 pixels, so redraw it with a much finer pixel grid, 1 px detail, crisp hard edges, thin 1 px dark outline, flat soft shading, muted palette. "
   "Make him look far more imposing, regal and terrifying: broader shoulders, larger robe, glowing red eyes, and a menacing AURA around the whole body made of swirling dark crimson and black flames and smoke with a few golden sparks rising from the ground and the shoulders, a faint dark red glow behind him. Keep the aura as part of the sprite, flames rising upward around the figure. Transparent background.")
im=Image.open(M+'chatgpt_diemvuong_goc.png').convert('RGBA');im=im.crop(im.getbbox())
f=1.25;im=im.resize((round(im.width*f),round(im.height*f)),Image.NEAREST)
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(im,((S-im.width)//2,S-im.height-14));cv.save(OUT+'in_diemvuong.png')
b64=base64.b64encode(open(OUT+'in_diemvuong.png','rb').read()).decode()
seed=int(sys.argv[1]) if len(sys.argv)>1 else 7
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
