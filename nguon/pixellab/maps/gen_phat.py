import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Dark gloomy painterly pixel art like a Chinese wuxia action game environment, desaturated palette, thin dark outline, front view, single isolated object on a fully transparent background, no ground tile."
D="a huge seated stone Buddha statue in meditation pose on a tall carved lotus pedestal, calm face, robes, moss and cracks, weathered grey stone, abandoned ancient temple"
j=pl.req('POST','/create-image-pixflux',{"description":D+ST,"image_size":{"width":320,"height":400},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":71})
im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
open('b2/tuongphat_lon.png','wb').write(base64.b64decode(im.split(',')[-1]));print('ok')
