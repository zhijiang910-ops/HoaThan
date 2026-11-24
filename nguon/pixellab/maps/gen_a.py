import json,base64,importlib.util,sys
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Pixel art environment prop for a dark Chinese wuxia action game, painterly muted palette, soft shading, thin dark outline, three-quarter top-down view, single object, transparent background, no ground shadow platform."
P=[('quantai_do',"a closed Chinese coffin painted deep red with black trim and a worn lid, lying on the ground, slightly weathered, a white paper talisman strip stuck on the lid",(112,72)),
('quantai_do2',"a red Chinese coffin standing at a tilt, half open lid, dark weathered wood, red lacquer peeling, cobwebs",(96,112)),
('denlong_trang',"a tall wooden pole with a hanging white paper lantern, glowing soft pale light, thin black Chinese characters on the lantern, weathered wood",(48,112)),
('denlong_trang2',"a rope with three small white paper lanterns hanging from two crooked wooden posts, pale glow, ghostly",(120,96)),
('bia_mo',"an old stone tombstone with carved Chinese characters, mossy and cracked, small grave mound of earth at the base, withered grass",(64,88)),
('bia_mo2',"two weathered stone tombstones leaning, one broken, grave mounds, dry weeds, a small bowl of incense ash",(100,84)),
('nha_hoang',"an abandoned ruined Chinese village house, collapsed tiled roof, broken wooden walls, dark empty doorway, overgrown dead weeds, cobwebs, dim and gloomy",(220,200)),
('cay_kho',"a dead twisted leafless tree with gnarled black branches, dry thin roots on dark earth, eerie",(150,190))]
for k,d,(w,h) in P:
    try:
        j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"view":"high top-down","detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":11})
        im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
        open(f'a/{k}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
