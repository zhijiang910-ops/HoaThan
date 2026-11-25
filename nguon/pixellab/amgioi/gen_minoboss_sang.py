import json,base64,time,importlib.util,sys,shutil
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
D=("Exactly the same character, same pose, same weapon, same silhouette, same design details and same pixel size. Only improve readability on a dark background: "
"lift the overall brightness by about 20 percent, raise contrast, add lighter highlights on armor edges, horns, weapon and skin (subtle rim light), keep the thin 1 px dark outline, "
"use richer shading with 5-6 distinct tones per material, crisp clean pixels, no blur, no glow, no 2x2 blocks, keep the muted dark underworld palette and the same hue of each part. Transparent background.")
J=sys.argv[1:] or ['nghiethoa','thietlao','vongxuyenqt']
for k in J:
    src=f'/home/user/HoaThan/game/assets/{k}_am.png'
    im=Image.open(src).convert('RGBA');w,h=im.size;im.save(f'mb/in_{k}.png')
    b64=base64.b64encode(open(f'mb/in_{k}.png','rb').read()).decode()
    try:
        j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":w,"height":h}],"image_size":{"width":w,"height":h},"description":D,"seed":7,"no_background":True})
        jid=j.get('background_job_id');t0=time.time()
        while jid and time.time()-t0<400:
            time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
            if r['status']=='completed':break
            if r['status']=='failed':raise Exception(str(r)[:300])
        x=r['last_response']['images'][0];x=x.get('base64') if isinstance(x,dict) else x
        open(f'mb/{k}.png','wb').write(base64.b64decode(x.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
