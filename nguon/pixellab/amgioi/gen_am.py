import json,base64,time,importlib.util,sys
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
b64=base64.b64encode(open('ms/ambinh.png','rb').read()).decode()
K="An undead underworld soldier in rusted armor holding a long spear with a tattered banner, side view facing right, same character, same colors and size, same pixel art style. "
A=[('idle',6,K+"Standing in place breathing slowly, the spear held upright, the banner swaying slightly, a subtle body bob, feet stay planted."),
('run',8,K+"Marching forward to the right with a heavy steady stride, legs alternating, the spear carried forward, the banner fluttering."),
('attack',8,K+"Winds back and then thrusts the spear forward to the right with a quick stab, holds for a moment, then pulls the spear back."),
('hit',4,K+"Flinches backward when struck, the head and body jerking back, then starts to recover."),
('death',8,K+"Collapses and falls to the ground, the armor falling apart, ending lying on the ground and staying down.")]
for k,n,d in A:
    try:
        j=pl.req('POST','/animate-with-text-v3',{"first_frame":{"type":"base64","base64":b64},"action":d,"frame_count":n,"seed":11,"no_background":True,"enhance_prompt":False})
        jid=j.get('background_job_id');t0=time.time()
        while jid and time.time()-t0<500:
            time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
            if r['status']=='completed':break
            if r['status']=='failed':raise Exception(str(r)[:300])
        imgs=r['last_response'].get('images',[])
        for i,x in enumerate(imgs):
            x=x.get('base64') if isinstance(x,dict) else x
            open(f'am/{k}_{i:02d}.png','wb').write(base64.b64decode(x.split(',')[-1]))
        print(k,len(imgs),'ok',r['last_response'].get('usage') or j.get('usage'),flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
