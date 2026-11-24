import sys,json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Pixel art game weapon item sprite, dark gloomy Chinese wuxia style, muted desaturated palette, thin dark outline, flat soft shading, single isolated object, plain transparent background, no hand, no person, no text, no shadow."
P={
'dao':("a large single-edged curved Chinese broadsword (guibao dao), a demon-head shaped brass guard, long steel blade with a slightly curved back, hilt wrapped in dark red cloth, pommel with a red tassel, horizontal, blade pointing right, hilt on the left",(80,28)),
'truong':("a Buddhist monk staff (xi zhang, khakkhara), a long dark wooden shaft, at the top end a bronze ring-head with several loose jingling rings and a small lotus finial, plain grip area in the middle, horizontal, head pointing right",(112,28)),
'quyen':("a single iron fist gauntlet (fighting glove) seen from the side, white cloth bandage wrapped over the forearm with dark red stripes, a bronze knuckle plate with small studs across the knuckles, clenched fist shape, hollow grip, no hand inside, fist pointing right",(36,32)),
'quat':("an open folding war fan with iron ribs, silver edge, deep purple silk with a faint pattern, a short dark handle at the bottom left, seen from the side, fan spreading to the right",(52,44)),
'cung':("a recurve composite bow, dark green-black lacquered wood with bone tips and a gold wrapped grip at the center, a thin pale bowstring pulled straight, no arrow, vertical orientation, string on the left, bow arc bulging to the right",(32,80))}
for k,(d,(w,h)) in P.items():
    for seed in (3,11):
        try:
            j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"medium shading","seed":seed})
            im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
            open(f'/home/user/HoaThan/nguon/pixellab/vukhi/{k}_s{seed}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,seed,'ok',flush=True)
        except Exception as e:print(k,seed,'ERR',e,flush=True)
