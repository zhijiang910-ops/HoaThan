import sys,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
M='/home/user/HoaThan/nguon/master_amgioi/'
OUT='/home/user/HoaThan/nguon/pixellab/amgioi/vt2/'
KEEP=("Redraw this exact character as a clean high-detail game sprite: KEEP THE DESIGN IDENTICAL (same face, same hat, same robe, same props, same colours, same ornaments, same pose and silhouette), do not redesign anything. "
      "The source is blocky with big 2x2 pixels, so redraw it with a much finer pixel grid, 1 px detail, crisp hard edges, a thin 1 px dark outline, flat soft shading with few tones, muted palette, chibi proportions, side view facing right. ")
J={
'phanquan':KEEP+"Details to preserve: a black official hat with two wing-shaped side ornaments (guan cap) and a small feather; red face with black beard and moustache; a crimson robe with gold trim and wide sleeves; a golden decorative panel at the front; holding a large brush pen (judge pen) with a white fur tip in the front hand, a small book at the waist. Transparent background.",
'manhba':KEEP+"Details to preserve: a hunched old woman with grey-white hair in a bun held by gold hairpins and a white flower; a grey-green robe with gold ornaments and tattered strips; holding a wooden ladle that drips green soup in the front hand; beside her feet a black iron cauldron with a white skull emblem and curling green steam. Transparent background."}
k=sys.argv[1];S=224;seed=int(sys.argv[2]) if len(sys.argv)>2 else 7
im=Image.open(M+f'chatgpt_{k}_goc.png').convert('RGBA');im=im.crop(im.getbbox())
f=1.2;im=im.resize((round(im.width*f),round(im.height*f)),Image.NEAREST)
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(im,((S-im.width)//2,S-im.height-6));cv.save(OUT+f'in_{k}.png')
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
