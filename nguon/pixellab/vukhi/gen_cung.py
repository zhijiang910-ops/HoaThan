import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Pixel art game weapon item sprite, dark gloomy Chinese wuxia style, muted desaturated palette, thick bold black outline, flat soft shading, single isolated object, plain transparent background, no hand, no person, no text, no shadow."
D="a chunky recurve bow, thick dark green-black lacquered limbs, wide and bold, curved tips with pale bone caps, a wide gold-wrapped grip at the exact center, a clearly visible taut pale bowstring on the left side, no arrow, vertical orientation, bow arc bulging to the right"
for seed in (5,23):
    j=pl.req('POST','/create-image-pixflux',{"description":D+ST,"image_size":{"width":56,"height":96},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"medium shading","seed":seed})
    im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
    open(f'/home/user/HoaThan/nguon/pixellab/vukhi/cung2_s{seed}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(seed,'ok',flush=True)
