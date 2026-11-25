import json,base64,time,importlib.util,sys,os
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
K="A young martial artist with bare empty hands (no weapon), side view facing right, same character, same colors, outfit and size, same pixel art style, feet stay planted. "
A=[('a',8,K+"Throws a quick straight right-hand punch forward to the right, the fist extends fully with the arm straight, then pulls the arm back to the guard pose."),
('b',8,K+"Twists the hips and throws a strong hook with the other fist sweeping across forward to the right, then returns to the guard pose."),
('c',8,K+"Crouches slightly then drives a heavy rising uppercut with the fist forward and upward to the right while stepping forward, finishing standing with the fist raised, then lowers it.")]
gs=sys.argv[1:] or ['nam','nu']
for g in gs:
    b64=base64.b64encode(open(f'quyen/in/{g}_idle.png','rb').read()).decode()
    for k,n,d in A:
        if os.path.exists(f'quyen/raw/{g}_{k}_00.png'):continue
        try:
            j=pl.req('POST','/animate-with-text-v3',{"first_frame":{"type":"base64","base64":b64},"last_frame":{"type":"base64","base64":b64},"action":d,"frame_count":n,"seed":21,"no_background":True,"enhance_prompt":False})
            jid=j.get('background_job_id');t0=time.time()
            while jid and time.time()-t0<500:
                time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
                if r['status']=='completed':break
                if r['status']=='failed':raise Exception(str(r)[:300])
            imgs=r['last_response'].get('images',[])
            for i,x in enumerate(imgs):
                x=x.get('base64') if isinstance(x,dict) else x
                open(f'quyen/raw/{g}_{k}_{i:02d}.png','wb').write(base64.b64decode(x.split(',')[-1]))
            print(g,k,len(imgs),r['last_response'].get('usage') or j.get('usage'),flush=True)
        except Exception as e:print(g,k,'ERR',e,flush=True)
