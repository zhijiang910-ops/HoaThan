import json,base64,time,importlib.util,sys
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
W=H=96
src=Image.open('/home/user/HoaThan/game/assets/matroi_am.png').convert('RGBA');bb=src.getbbox();src=src.crop(bb)
s=min(80/src.width,80/src.height);src=src.resize((round(src.width*s),round(src.height*s)),Image.LANCZOS)
c=Image.new('RGBA',(W,H),(0,0,0,0));c.alpha_composite(src,((W-src.width)//2,(H-src.height)//2));c.save('mt/in.png')
b64=base64.b64encode(open('mt/in.png','rb').read()).decode()
D=("Same chibi proportions, same pixel art style as a dark muted Chinese wuxia underworld game: thin dark outline, muted desaturated palette, soft flat shading with 4-5 tones, NO glow, NO bright cyan. "
"Redraw this will-o-wisp (Ma Troi) as an eerie ghost fire: dull grey-teal and pale blue-grey flame body with darker blue-grey shading, a small hollow-eyed skull face inside the flame with dark sockets, a ragged flame tail trailing behind, a few tiny drifting embers. Keep the same size and pose. Transparent background.")
for seed in (7,21):
    try:
        j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":W,"height":H}],"image_size":{"width":W,"height":H},"description":D,"seed":seed,"no_background":True})
        jid=j.get('background_job_id');t0=time.time()
        while jid and time.time()-t0<400:
            time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
            if r['status']=='completed':break
            if r['status']=='failed':raise Exception(str(r)[:300])
        x=r['last_response']['images'][0];x=x.get('base64') if isinstance(x,dict) else x
        open(f'mt/s{seed}.png','wb').write(base64.b64decode(x.split(',')[-1]));print(seed,'ok',flush=True)
    except Exception as e:print(seed,'ERR',e,flush=True)
