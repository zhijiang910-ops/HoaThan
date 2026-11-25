import json,base64,time,os,sys,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
INS={'thiencuong':"Side view facing right. Keep the exact pose, limbs, hair, ponytail and face of each frame, the same chibi proportions, thin dark outline, muted palette. Replace only the clothing with the reference martial-monk fighter outfit: white short-sleeve robe with red dragon patterns, dark scaled armored forearm bracers with red wraps, wooden prayer beads necklace, red and gold sash with a fist emblem, dark baggy trousers, armored boots. Hands are bare empty fists.",
 'tramyeu':"Side view facing right. Keep the exact pose, limbs, hair, ponytail and face of each frame, the same chibi proportions, thin dark outline, muted palette. Replace only the clothing with the reference demon-slayer outfit: black scaled armor with gold trim and a gold beast-head pauldron, red scarf and red headband, red and black layered skirt/coat with flame patterns, dark armored boots. Hands empty (a weapon layer is added separately).",
 'maoson':"Side view facing right. Keep the exact pose, limbs, hair, ponytail and face of each frame, the same chibi proportions, thin dark outline, muted palette. Replace only the clothing with the reference Mao Son taoist outfit: deep navy-blue wide-sleeve robe with gold cloud trim, white inner layers, yellow talisman strips hanging, a bagua yin-yang emblem on the shoulder, gold belt, dark boots. Hands empty (a sword layer is added separately)."}
sz={'width':128,'height':128}
for key in sys.argv[1:]:
    s,g=key.split('_');
    if os.path.exists(f'trangphuc/out/{key}_0.png'):continue
    rb=b(f'trangphuc/in/ref_{key}.png');from PIL import Image;rw,rh=Image.open(f'trangphuc/in/ref_{key}.png').size
    body={'reference_image':{'image':{'type':'base64','base64':rb},'size':{'width':rw,'height':rh}},'frames':[{'image':{'type':'base64','base64':b(f'trangphuc/in/{g}_{i}.png')},'size':sz} for i in (0,1)],'image_size':sz,'no_background':True,'additional_instructions':INS[s],'seed':5}
    try:
        j=pl.req('POST','/transfer-outfit-v2',body);jid=j.get('background_job_id');t0=time.time()
        while jid and time.time()-t0<500:
            time.sleep(8);r=pl.req('GET','/background-jobs/'+jid)
            if r['status']=='completed':break
            if r['status']=='failed':raise Exception(str(r)[:300])
        lr=r['last_response'];ims=lr.get('images') or lr.get('frames') or []
        for i,x in enumerate(ims):
            x=x.get('base64') if isinstance(x,dict) and 'base64' in x else (x.get('image',{}).get('base64') if isinstance(x,dict) else x)
            open(f'trangphuc/out/{key}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
        print(key,len(ims),lr.get('usage') or j.get('usage'),flush=True)
    except Exception as e:print(key,'ERR',e,flush=True)
