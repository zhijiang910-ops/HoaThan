import json,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
KEEP="Same character, same chibi proportions, same pixel art style, same thin dark outline, same muted palette and flat soft shading, same size and pose, side view facing right. "
D=KEEP+"Turn this swordsman into Hac Vo Thuong (Black Impermanence), a Chinese underworld guardian: a tall cylindrical black hat with a flat top and a white Chinese character on the front, pale white face with dark hollow eyes, a long red tongue hanging down to the chest, a long black robe, a white sash tied around the waist, holding a black mourning staff (khoc tang bang) in the front hand instead of the sword. Transparent background."
w,h=187,146
im=Image.open('/home/user/HoaThan/game/assets/hacphong.png').convert('RGBA').crop((0,0,w,h));im.save('hv/in_hacphong.png')
b64=base64.b64encode(open('hv/in_hacphong.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":w,"height":h}],"image_size":{"width":w,"height":h},"description":D,"seed":7,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
imgs=r['last_response'].get('images',[]);print(len(imgs),'ảnh')
for i,x in enumerate(imgs):
    x=x.get('base64') if isinstance(x,dict) else x
    open(f'hv/hacvo_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print('ok')
