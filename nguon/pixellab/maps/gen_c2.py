import json,base64,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Dark gloomy painterly pixel art like a Chinese wuxia action game environment, desaturated muted palette with soft shading, thin dark outline, front three-quarter view, single isolated object on a fully transparent background, no ground tile, no grass patch."
P=[('quanmon',"a huge ancient Chinese ghost gate (Quy Mon Quan): black stone gate with a curved dark tiled roof, red glowing lanterns, two stone demon guardian statues on both sides, chains hanging, dark open passage",(256,224),71),
('bienngan_hoa',"a dense patch of red spider lilies (higanbana) on dark ground, bright blood-red thin curling petals, no leaves",(96,72),72),
('bienngan_hoa2',"a wide field strip of red spider lilies mixed with dry grey reeds, blood-red petals",(128,80),73),
('vonghuong',"an ancient stone watchtower platform (Vong Huong Dai) with steps, a stone railing, small dark roofed pavilion on top, grey stone, white paper lanterns",(192,224),74),
('nghiepkinh',"a giant round bronze mirror on a tall black stone stand, ornate carved frame, the mirror surface glowing pale cyan-white, ancient Chinese underworld judgment mirror",(128,176),75),
('samla',"a grand dark underworld palace hall (Sam La Dien): black tiled double roof with upturned eaves, dark red wooden pillars, big closed doors, white paper lanterns, grey stone steps",(288,240),76),
('cotden',"a tall black stone pillar wrapped with a faded red ribbon and a small white lantern at the top, carved demon faces",(64,128),77),
('vacdong',"a large cold bronze cauldron (vac dong) on three thick legs, dark green patina, empty, soot, chains on the sides",(96,96),78),
('loncong',"a rusty iron hanging cage on a chain from a short wooden gallows post, dark, eerie",(80,112),79),
('tuongdo',"a short ruined grey stone wall section with broken top, cracks, a tattered white cloth hanging",(160,96),80),
('naiha',"an ancient arched stone bridge (Nai Ha bridge) seen from the side, grey stone, red-painted railing posts, white mist at the foot",(288,160),81),
('manhba',"a small roadside soup stall: a big iron pot on a fire with steaming pale soup, wooden table with stacked bowls, an old cloth awning, dim light",(128,112),82),
('ngai',"a grand black and gold throne of the underworld king on a stepped stone dais, high carved back with a red cloth, demon-face armrests",(160,176),83),
('cotdo',"a tall dark red lacquered palace pillar with gold dragon carving and a hanging yellow talisman, stone base",(64,160),84),
('banphan',"a judge's wooden desk with a big open ledger book, a brush, a red seal and a bronze incense burner, dark wood",(128,96),85),
('luanhoi',"a huge ancient stone wheel of reincarnation standing upright on a carved base, six sections with faint glowing carved symbols, pale blue-violet glow",(160,160),86),
('daitron',"a round stone altar platform seen at an angle, carved concentric rune rings with pale violet glowing lines, steps around the edge",(256,160),87)]
import os
for k,d,(w,h),s in P:
    if os.path.exists(f'c/{k}.png'):continue
    try:
        j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":s})
        im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
        open(f'c/{k}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,'ok',flush=True)
    except Exception as e:print(k,'ERR',e,flush=True)
