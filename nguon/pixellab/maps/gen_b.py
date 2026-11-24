import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Dark gloomy painterly pixel art like a Chinese wuxia action game environment, desaturated palette, thin dark outline, front three-quarter view, single isolated object on a fully transparent background, no ground tile."
P=[('lu_huong',"a large bronze Chinese incense burner (ding) on three legs, green patina, ash and burnt-out incense sticks, dusty and abandoned",(96,112),61),
('tuong_vo',"a broken stone Buddha statue sitting on a cracked pedestal, head missing, moss and cobwebs, abandoned temple, grey stone",(112,144),62),
('phuon_bua',"a tall wooden pole with a long faded yellow paper talisman banner with red Chinese characters, torn at the edges, hanging limp",(48,128),63),
('cot_da',"a broken weathered stone temple pillar with a cracked base and a faded red ribbon wrapped around it",(64,128),64),
('den_da',"a small stone temple lantern (toro) with a dim candle flame, mossy, leaning slightly",(64,96),65),
('cay_phong',"a gnarled bare autumn tree with only a few dark red withered leaves, thick trunk, leafless branches, gloomy",(176,208),66)]
for k,d,(w,h),s in P:
    try:
        j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":s})
        im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
        open(f'b/{k}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
