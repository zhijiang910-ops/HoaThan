import sys,json,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
KEEP="Same chibi proportions, same pixel art style, same thin dark outline, same muted palette and flat soft shading, side view facing right. This is a BOSS: make it look imposing, ornate and richly detailed, larger and more elaborate than a normal enemy, with layered armor plates, ornaments, cloth and chains, a strong confident stance. "
J={
'nguudau':('quytuong',145,149,KEEP+"Turn this ogre into Nguu Dau (Ox-Head), the bull-headed underworld guardian general: a huge black bull head with two massive curved ivory horns tipped with iron caps, a heavy bronze nose ring, glowing red eyes and flared nostrils; broad muscular bluish-grey body; heavy dark iron and bone shoulder pauldrons with spikes; layered black leather and iron plate armor with a skull belt buckle; a long tattered crimson cape and waist sash; iron chains wrapped around the arms; holding a huge black iron trident (three-pronged fork) in the front hand instead of the axe. Keep a clearly readable bull head silhouette. Transparent background."),
'madien':('ho',175,121,KEEP+"Turn this tiger-man into Ma Dien (Horse-Face), the horse-headed underworld guardian general, the partner of the bull-headed Nguu Dau: a long chestnut-brown horse head with a flowing black mane, flared nostrils, bared teeth, pointed upright ears, glowing red eyes; upright muscular body; spiked bronze and dark iron shoulder pauldrons; layered dark leather and bronze plate armor with a horse-skull belt buckle; long tattered crimson scarf and sash; iron chains wrapped around the forearms; holding a long spiked iron mace-halberd in the front hand. Keep a clearly readable horse head silhouette, the tail becomes a long flowing black horse tail. Transparent background.")}
k=sys.argv[1];base,w,h,d=J[k];S=192
src=Image.open(f'/home/user/HoaThan/game/assets/{base}.png').convert('RGBA').crop((0,0,w,h))
bb=src.getbbox();src=src.crop(bb)
cv=Image.new('RGBA',(S,S),(0,0,0,0));cv.alpha_composite(src,((S-src.width)//2,S-src.height-6));cv.save(f'bo/in_{k}.png')
b64=base64.b64encode(open(f'bo/in_{k}.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":S,"height":S}],"image_size":{"width":S,"height":S},"description":d,"seed":int(sys.argv[2]) if len(sys.argv)>2 else 7,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(f'bo/{k}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print('ok')
