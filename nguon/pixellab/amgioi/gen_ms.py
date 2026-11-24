import json,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
KEEP="Same character, same chibi proportions, same pixel art style, same thin dark outline, same muted palette and flat soft shading, same size and pose, side view facing right. "
J=[('vonghon','daulap',133,122,"Turn this farmer into a pale ghost (Vong Hon): the body becomes semi-transparent pale blue-grey spirit, replace the straw hat with long tangled black hair covering the face, hollow dark eyes, tattered white burial shroud, and replace the legs with a tapering wispy mist tail floating just above the ground."),
('ambinh','hacphong',187,146,"Turn this swordsman into an undead underworld soldier (Am Binh): grey-blue pale skin, rusted dark green-black ancient Chinese armor and a dented helmet, dim glowing red eyes, replace the sword with a long spear, a tattered small banner on the back."),
('oanhonxa','bachhoa',198,117,"Turn this girl into a ghost archer (Oan Hon Xa): translucent pale blue-grey body, tattered grey-white robe, long loose black hair, hollow eyes, holding a wooden bow with a faint glowing spirit arrow."),
('khuyen','ho',175,121,"Turn this tiger-man into a hellhound beast-man (Dia Nguc Khuyen): a skeletal black dog head with red glowing eyes and sharp teeth, exposed ribs, dark grey-black fur, thin grey-green ghost flames licking along the shoulders and tail, keep the same upright stance and the same clothes shape but dark and ragged.")]
for k,base,w,h,d in J:
    im=Image.open(f'/home/user/HoaThan/game/assets/{base}.png').convert('RGBA').crop((0,0,w,h));im.save(f'ms/in_{base}.png')
    b64=base64.b64encode(open(f'ms/in_{base}.png','rb').read()).decode()
    try:
        j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":w,"height":h}],"image_size":{"width":w,"height":h},"description":KEEP+d+" Transparent background.","seed":7,"no_background":True})
        jid=j.get('background_job_id');t0=time.time()
        while jid and time.time()-t0<400:
            time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
            if r['status']=='completed':break
            if r['status']=='failed':raise Exception(str(r)[:300])
        imgs=r['last_response'].get('images',[])
        x=imgs[0];x=x.get('base64') if isinstance(x,dict) else x
        open(f'ms/{k}.png','wb').write(base64.b64decode(x.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
# Ma Trơi: không có sprite nền, tạo riêng theo phong cách master (muted)
try:
    j=pl.req('POST','/create-image-pixflux',{"description":"Ma Troi: a small floating ghost fire spirit, pale blue-white flame with a tiny skull face inside, trailing flame tail, muted dark palette, soft shading, thin dark outline, chibi style, side view facing right, single object. Same pixel art style as a cute dark Chinese wuxia game.","image_size":{"width":96,"height":96},"no_background":True,"detail":"medium detail","outline":"single color black outline","shading":"basic shading","seed":9})
    x=j['image'];x=x.get('base64') if isinstance(x,dict) else x
    open('ms/matroi.png','wb').write(base64.b64decode(x.split(',')[-1]));print('matroi ok',flush=True)
except Exception as e:print('matroi ERR',e,flush=True)
