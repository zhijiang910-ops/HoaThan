import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/hoathan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Pixel art game weapon sprite, dark gloomy Chinese wuxia style, muted palette, thick black outline, rich pixel shading, single isolated object, transparent background, no hand, no person, no text."
D="a giant ancient Chinese jian greatsword pointing straight DOWN, long wide dark blue-black steel blade with a bright pale-blue central fuse line and etched talisman runes, sharp pointed tip at the bottom, ornate gold-bronze cross guard, leather wrapped long grip, jade pommel at the top, perfectly vertical symmetric"
for seed in (3,17,41):
    j=pl.req('POST','/create-image-pixflux',{"description":D+ST,"image_size":{"width":80,"height":288},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":seed})
    im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
    open(f'/home/user/hoathan/nguon/pixellab/cukiem2/s{seed}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(seed,'ok',flush=True)
