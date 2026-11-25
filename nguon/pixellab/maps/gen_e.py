import json,base64,importlib.util,sys
spec=importlib.util.spec_from_file_location('pl','/home/user/hoathan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
ST=" Dark gloomy painterly pixel art like a Chinese wuxia action game environment, desaturated muted palette with soft shading, thin dark outline, front 3/4 top-down view, single isolated object on a fully transparent background, no ground, no shadow."
P=[('vacdau',"a huge black iron cauldron on a stone base, boiling black oil with bubbles, orange fire flames licking under it, human skulls on the rim, thin dark steam, hell oil pot",(128,128)),
('docxuong',"a heap of human skulls and scattered bones, ribcages and femurs piled up",(112,80)),
('giandinh',"an iron torture rack of sharp rusty spikes and blades planted in the ground with impaled bones and skulls, knife mountain of hell",(128,96)),
('coc_xich',"a black iron post with hanging rusty chains and meat hooks, a skull at the foot, torture post of hell",(64,128)),
('thaposo',"a tall tower of stacked human skulls with a dim red glow in the eye sockets",(96,128)),
('tamsinh',"the Three-Life Stone of Naihe bridge, a tall dark standing stone with glowing pale blue carved runes and a faint spirit glow",(64,128)),
('thuyenma',"a large old wooden ferry boat of the underworld river, tattered sail, two hanging lanterns with pale blue ghost fire, a hooded ferryman silhouette",(160,96)),
('denhoa',"a floating river lantern shaped like a lotus with pale blue ghost fire flame",(32,32)),
('bia_naihe',"a stone tablet beside a bridge carved with Chinese characters, mossy, pale blue glow, small ghost fire brazier",(64,96))]
for k,d,(w,h) in P:
  for s in (11,23):
    import os,time
    if os.path.exists(f'e/{k}_{s}.png'):continue
    j=None
    for _t in range(4):
      try:
        j=pl.req('POST','/create-image-pixflux',{"description":d+ST,"image_size":{"width":w,"height":h},"no_background":True,"detail":"highly detailed","outline":"single color black outline","shading":"detailed shading","seed":s});break
      except Exception as ex:
        print('retry',k,s,ex,flush=True);time.sleep(5)
    if not j:continue
    im=j['image'];im=im.get('base64') if isinstance(im,dict) else im
    open(f'e/{k}_{s}.png','wb').write(base64.b64decode(im.split(',')[-1]));print(k,s,'ok',flush=True)
