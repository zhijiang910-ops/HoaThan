import sys,base64,time,importlib.util
from PIL import Image
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
D='/home/user/HoaThan/nguon/pixellab/amgioi/dv/'
S=256
BASE=("Redraw this exact character, the FINAL BOSS Yan Wang (King of the Underworld), keeping the same face (red face, bold black eyebrows, long black beard), the same flat black imperial crown board with gold bead strings, the same tablet in the front hand, the same pose, side view facing right, fine 1 px pixel detail, crisp hard edges, thin dark outline, flat soft shading. "
      "CHANGE: he now wears a deep JET-BLACK imperial dragon robe (hei pao), the whole robe and sleeves clearly black, only fine thin dark-gold dragon embroidery and trim, broad shoulders, wide black sleeves, a long black cape. ")
V={
'a':BASE+"Make him even more imposing and cool: a larger, more elaborate crown with longer gold bead curtains, intense glowing red eyes, and a menacing aura of swirling dark crimson and black flames with ghostly dark-purple smoke rising around the whole body, a faint red glow behind him. Transparent background.",
'b':BASE+"Make him even more imposing and cool: dragon-head shoulder pauldrons in black and dark gold, a black cape with a crimson inner lining flowing behind him, a taller crown, glowing red eyes, and an aura of dark crimson flames rising from the ground with floating dark red ghost-fire wisps and golden sparks. Transparent background."}
k=sys.argv[1];seed={'a':7,'b':19}[k]
im=Image.open(D+'diemvuong_s7_0.png').convert('RGBA');im.save(D+f'in2_{k}.png')
b64=base64.b64encode(open(D+f'in2_{k}.png','rb').read()).decode()
j=pl.req('POST','/edit-images-v2',{"method":"edit_with_text","edit_images":[{"image":{"type":"base64","base64":b64},"width":S,"height":S}],"image_size":{"width":S,"height":S},"description":V[k],"seed":seed,"no_background":True})
jid=j.get('background_job_id');t0=time.time();r=j
while jid and time.time()-t0<400:
    time.sleep(6);r=pl.req('GET','/background-jobs/'+jid)
    if r['status']=='completed':break
    if r['status']=='failed':raise Exception(str(r)[:300])
for i,x in enumerate(r['last_response'].get('images',[])):
    x=x.get('base64') if isinstance(x,dict) else x
    open(D+f'diemvuong_v2{k}_{i}.png','wb').write(base64.b64decode(x.split(',')[-1]))
print(k,'ok')
