import sys,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
A='/home/user/HoaThan/game/assets/';OUT='/home/user/HoaThan/nguon/pixellab/amgioi/sy3/'
STYLE=("Redraw this sprite as a DIFFERENT character, keeping EXACTLY the same pixel art style, same rendering, same fine 1 px grid, same thin dark outline, same shading, same muted dark palette, same proportions and scale, same side view facing right, same level of detail as the input (it is a boss of the same game). ")
J={'phanquan':('hacvo',STYLE+"New character: Pan Guan, the Underworld Judge. Black official hat with two wing-shaped side ornaments, red face with black beard and moustache, crimson robe with gold trim and wide sleeves, holding a large judge brush pen with a white fur tip, a small book at the waist. No axe, no chain, no tall hat. Transparent background."),
'manhba':('bachvo',STYLE+"New character: Meng Po, the old hunched woman of the Underworld. Grey-white hair in a bun with gold hairpins and a white flower, grey-green robe with gold ornaments and tattered strips, holding a wooden ladle dripping green soup, a black iron cauldron with a white skull emblem and green steam at her feet. No tall hat, no axe. Transparent background.")}
k=sys.argv[1];base,D=J[k];S=192;seed=int(sys.argv[2]) if len(sys.argv)>2 else 7
im=Image.open(A+base+'_am.png').convert('RGBA');im=im.crop(im.getbbox())
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(im,((S-im.width)//2,S-im.height-6));cv.save(OUT+f'in_{k}.png')
b64=base64.b64encode(open(OUT+f'in_{k}.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":S,"height":S}],"image_size":{"width":S,"height":S},"description":D,"seed":seed,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(OUT+f'{k}_s{seed}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print(k,'ok')
