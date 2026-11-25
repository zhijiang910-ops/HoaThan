import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Dark gloomy painterly pixel art like a Chinese wuxia action game environment, desaturated muted palette with soft shading, thin dark outline, side view, single isolated object on a fully transparent background, no water, no ground, no shadow."
P=[('thuyen1',"a small old wooden ferry boat of the Wang Chuan underworld river, curved prow, a hanging white paper lantern with a pale blue glow on a pole, tattered cloth canopy, dark weathered wood",(128,80),91),
('thuyen2',"a narrow wooden punt boat with a hooded ferryman in a straw cape standing at the back holding a long pole, a small red lantern at the front, dark weathered wood",(128,96),92)]
for k,d,(w,h),s in P:
    j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":s})
    im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
    open(f'd/{k}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,'ok',flush=True)
