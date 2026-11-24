import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Pixel art environment prop for a dark Chinese wuxia action game, painterly muted palette, soft shading, thin dark outline, three-quarter top-down view, single isolated object on a fully transparent background, no ground tile, no platform."
P=[('quantai_a',"a Chinese traditional coffin (guan cai) seen from above at an angle: elongated hexagonal shape, wider at the head end and narrower at the foot end, thick rounded domed lid, deep red lacquer with black edge trim and two small brass handles, a yellow paper talisman strip pasted across the lid",(120,76),21),
('quantai_b',"a Chinese traditional coffin (guan cai) on two wooden stools, elongated tapered hexagonal shape, thick rounded domed lid, dark red lacquer with chipped paint, black end caps, white paper strips hanging",(120,84),22),
('quantai_c',"a Chinese traditional coffin leaning upright against the ground at an angle, tapered shape, red lacquer, lid slightly ajar showing darkness inside",(88,120),23),
('nha_a',"a ruined abandoned Chinese village house: roof half collapsed with a big hole and broken tiles, leaning cracked plaster walls, broken wooden door hanging, dark interior, dead weeds growing on the roof",(224,200),31),
('nha_b',"a burnt-out collapsed Chinese peasant hut, charred wooden beams sticking out, broken clay wall, a torn white cloth hanging, grey ash",(200,170),32),
('cay_kho_a',"a dead twisted leafless tree, gnarled black bare branches, thick trunk, a few hanging white paper strips, no leaves",(160,192),41),
('cay_kho_b',"a dead bare tree stump with a few crooked branches and a crow perched, dark wood",(128,160),42)]
for k,d,(w,h),s in P:
    try:
        j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"view":"high top-down","detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":s})
        im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
        open(f'a/{k}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
