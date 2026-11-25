import json,base64,time,importlib.util,sys,os
spec=importlib.util.spec_from_file_location('pl','/home/user/hoathan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
K="A young martial artist with bare empty hands (no weapon, no gloves), side view facing right, same character, same colors, outfit, body proportions and size, same pixel art style, the head stays at the same height. "
P={'b':K+"Cross punch with the arm CLOSEST to the camera: that near arm, drawn in front of the torso, swings across and punches straight forward to the right at shoulder height with the fist, the shoulders and hips rotate toward the right, the far arm is pulled back behind the body, feet stay planted, then returns to the guard.",
'c':K+"Ground leg sweep: crouches low with the body leaning back and one hand pushed on the floor, the other leg stays bent, one leg is fully extended straight and sweeps forward to the right sliding along the floor with the foot at ankle height touching the ground, a flat low sweeping kick below the knee line, never raised above the knee, then stands back up."}
clip=sys.argv[1];seed=int(sys.argv[2]);gs=sys.argv[3:]
for g in gs:
    b64=base64.b64encode(open(f'in/{g}_idle.png','rb').read()).decode()
    tag=f'{g}_{clip}_s{seed}'
    if os.path.exists(f'raw3/{tag}_00.png'):continue
    try:
        j=pl.req('POST','/animate-with-text-v3',{"first_frame":{"type":"base64","base64":b64},"last_frame":{"type":"base64","base64":b64},"action":P[clip],"frame_count":8,"seed":seed,"no_background":True,"enhance_prompt":False})
        jid=j.get('background_job_id');t0=time.time()
        while jid and time.time()-t0<500:
            time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
            if r['status']=='completed':break
            if r['status']=='failed':raise Exception(str(r)[:300])
        for i,x in enumerate(r['last_response'].get('images',[])):
            x=x.get('base64') if isinstance(x,dict) else x
            open(f'raw3/{tag}_{i:02d}.png','wb').write(base64.b64decode(x.split(',')[-1]))
        print(tag,'ok',flush=True)
    except Exception as e:print(tag,'ERR',e,flush=True)
