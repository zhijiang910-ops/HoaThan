import sys,json,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
M='/home/user/HoaThan/nguon/master_amgioi/'
KEEP="Redraw this exact character as a clean game sprite: KEEP THE DESIGN IDENTICAL (same face, same hat, same robe, same weapon, same colours, same ornaments, same pose and silhouette), do not redesign anything. Only convert it to a clean pixel grid with uniform pixels, hard edges, a thin 1 px dark outline, flat soft shading with few tones, muted palette, chibi proportions, side view facing right. "
J={
'hacvo':('chatgpt_hacvo_goc.png',KEEP+"Details to preserve: a tall black rectangular hat with three gold diamond ornaments; twisted copper-gold branch decorations on both sides of the hat with hanging black beads and white tassels; grey-white hair; dark grey face with red markings and glowing red eyes; a very long red tongue hanging down to the waist; a big necklace of black prayer beads with red dots; black robe with gold cloud-pattern trim and a tattered purple-grey cloak; ornate gold belt buckle; white gloved hands; the front hand holds a staff topped with a curved crescent glaive blade with an iron chain looping down; the other hand holds a coil of iron chain. Transparent background."),
'bachvo':('chatgpt_bachvo_goc.png',KEEP+"Details to preserve: a tall white curved hat with gold cloud ornaments and a red stripe; twisted copper-gold branch decorations on both sides of the hat with hanging black beads and white tassels; very long flowing white hair; pale white face with red markings and red eyes; a very long red tongue hanging down to the chest; a necklace of black prayer beads; white robe with gold cloud-pattern trim and tattered white cloth strips, gold diamond ornaments hanging at the waist; white gloved hands; holding a long wooden staff topped with gold orbs and a white funeral banner with a black and white Taiji (yin-yang) symbol and tattered tassels. Transparent background.")}
k=sys.argv[1];f,d=J[k];S=192
im=Image.open(M+f).convert('RGBA');bb=im.getbbox();im=im.crop(bb)
sc=(S-8)/max(im.width,im.height);c=im.resize((round(im.width*sc),round(im.height*sc)),Image.BOX)
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(c,((S-c.width)//2,S-c.height-3));cv.save(f'vt/in_{k}.png')
b64=base64.b64encode(open(f'vt/in_{k}.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":S,"height":S}],"image_size":{"width":S,"height":S},"description":d,"seed":int(sys.argv[2]) if len(sys.argv)>2 else 7,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(f'vt/{k}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print('ok')
