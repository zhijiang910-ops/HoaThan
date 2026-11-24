import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Dark gloomy painterly pixel art like a Chinese wuxia action game environment, desaturated brown and grey palette, thin dark outline, front three-quarter view, single isolated building on a fully transparent background, no ground tile, no grass patch."
P=[('nha_c',"a ruined abandoned Chinese village house with sagging dark tiled roof full of holes, rotten wooden pillars, cracked grey plaster walls, broken lattice windows, dark empty doorway, torn white mourning cloth hanging from the eaves",(224,208),51),
('nha_d',"a derelict Chinese farmhouse, collapsed thatched roof, leaning wooden wall, broken door, grey ash and cobwebs, a faded white lantern hanging crooked by the door",(208,192),52)]
for k,d,(w,h),s in P:
    try:
        j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":s})
        im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
        open(f'a/{k}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
