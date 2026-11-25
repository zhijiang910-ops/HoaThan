import json,base64,time,importlib.util,sys
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
A='/home/user/HoaThan/game/assets/'
KEEP="Same chibi proportions, same pixel art style, same thin dark outline, same muted desaturated palette and flat soft shading with 4-5 tones, no glow, same size, side view facing right, standing on the ground. "
J=[('daxoa',A+'quysai_am.png',None,"Redraw this guard as a Yaksha (Da Xoa), an underworld demon guard: dull grey-green skin, spiky dark-red hair standing up, two small tusks pointing up from the lower jaw, pointed ears, dull yellow eyes, bare muscular torso wrapped in rusty chains and ragged cloth strips, a ragged beast-hide skirt, holding a small rusty iron trident (three-pronged fork) instead of the club. Hunched aggressive stance."),
('cuongthi',A+'hacphong.png',(0,0,187,146),"Redraw this swordsman as a Jiangshi (Chinese hopping vampire corpse): faded blue-black Qing dynasty official robe and official hat, pale grey-blue skin, a yellow paper talisman with red writing stuck on the forehead, both arms stretched straight out in front, long dark nails, closed eyes, stiff upright posture, no sword."),
('chitrat',A+'bachhoa.png',(0,0,198,117),"Redraw this girl as a paper effigy (Chi Trat Nhan) offered to the dead: body made of crumpled ivory-white paper, round red cheek dots, simple black dot eyes, a stiff awkward smile, red and yellow paper clothes, a few torn spots showing bamboo frame inside, holding a small paper lantern in one hand, no bow."),
('thuyquy',A+'daulap.png',(0,0,133,122),"Redraw this farmer as a Shui Gui (drowned water ghost): bloated pale blue-green waterlogged skin, wet black hair plastered on the face with green river weed, tattered wet cloth and weeds wrapped around the body, dark empty eye sockets, dragging steps, water drips falling from the body and hands, no straw hat."),
('dieutu',A+'vonghon_am.png',None,"Redraw this ghost as a hanged ghost (Dieu Tu Quy): tall thin pale grey body slightly floating, a very long red tongue hanging out of the mouth down to the chest, long black hair hanging to cover half the face, tattered white mourning robe, a broken rope loop around the neck with the cut rope hanging down.")]
only=sys.argv[1:]
for k,src,box,d in J:
    if only and k not in only:continue
    im=Image.open(src).convert('RGBA')
    if box:im=im.crop(box)
    w,h=im.size;im.save(f'qt/in_{k}.png')
    b64=base64.b64encode(open(f'qt/in_{k}.png','rb').read()).decode()
    try:
        j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":w,"height":h}],"image_size":{"width":w,"height":h},"description":KEEP+d+" Transparent background.","seed":7,"no_background":True})
        jid=j.get('background_job_id');t0=time.time()
        while jid and time.time()-t0<400:
            time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
            if r['status']=='completed':break
            if r['status']=='failed':raise Exception(str(r)[:300])
        x=r['last_response']['images'][0];x=x.get('base64') if isinstance(x,dict) else x
        open(f'qt/{k}.png','wb').write(base64.b64decode(x.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
