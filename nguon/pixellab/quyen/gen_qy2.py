import json,base64,time,importlib.util,sys,os
spec=importlib.util.spec_from_file_location('pl','/home/user/hoathan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
K="A young martial artist with bare empty hands (no weapon, no gloves), side view facing right, same character, same colors, outfit, body proportions and size, same pixel art style, the head stays at the same height. "
A=[('a',8,K+"Fast jab: throws a quick straight punch forward to the right with the leading arm, arm fully straight at shoulder height, the other fist stays guarding near the chest, feet stay planted, then pulls the arm back to the guard."),
('b',8,K+"Cross punch with the OTHER arm: twists the hips and shoulders and throws a straight punch forward to the right with the rear arm, arm fully straight at shoulder height, the first arm pulls back to the chest, feet stay planted, then returns to guard."),
('c',8,K+"Low leg sweep: drops into a deep crouch with both hands on the ground, spins and sweeps one fully extended leg in a wide low arc along the ground forward to the right at ankle height, then rises back to standing.")]
gs=sys.argv[1:] or ['nam','nu']
for g in gs:
    b64=base64.b64encode(open(f'in/{g}_idle.png','rb').read()).decode()
    for k,n,d in A:
        if os.path.exists(f'raw2/{g}_{k}_00.png'):continue
        try:
            j=pl.req('POST','/animate-with-text-v3',{"first_frame":{"type":"base64","base64":b64},"last_frame":{"type":"base64","base64":b64},"action":d,"frame_count":n,"seed":33,"no_background":True,"enhance_prompt":False})
            jid=j.get('background_job_id');t0=time.time()
            while jid and time.time()-t0<500:
                time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
                if r['status']=='completed':break
                if r['status']=='failed':raise Exception(str(r)[:300])
            imgs=r['last_response'].get('images',[])
            for i,x in enumerate(imgs):
                x=x.get('base64') if isinstance(x,dict) else x
                open(f'raw2/{g}_{k}_{i:02d}.png','wb').write(base64.b64decode(x.split(',')[-1]))
            print(g,k,len(imgs),r['last_response'].get('usage') or j.get('usage'),flush=True)
        except Exception as e:print(g,k,'ERR',e,flush=True)
