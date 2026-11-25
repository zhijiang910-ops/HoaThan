"""Khung xương ULTIMATE X Quyền: giơ MỘT tay (tay xa) thẳng lên trời, rồi bổ chưởng mạnh xuống đất trước mặt.
Dùng: skel_qy_x.py <job_mẫu.json> <nam|nu> <outdir> [seed,seed]  (chỉ dựng tư thế + ảnh phác thảo; gọi PixelLab bằng pl.py /animate-with-skeleton-v3 job.json)"""
import json,sys,base64,os,io
src,tag,od=sys.argv[1],sys.argv[2],sys.argv[3];seeds=(sys.argv[4] if len(sys.argv)>4 else '').split(',') if len(sys.argv)>4 else []
P1=os.path.join(os.path.dirname(os.path.abspath(__file__)),'combopose.py');code=open(P1).read();code=code[:code.index('# chân: bước dài')]
sys.argv=['combopose.py',src,od,tag];os.makedirs(od,exist_ok=True);exec(code)
GN=((3,8),(8,4));STEP=(((3,14),(5,30)),((-3,15),(-6,31)))
WIDE=(((7,13),(12,29)),((-7,15),(-13,30)))
def kp(**k):
    out=pose(**k);return [p for p in out if 'sword' not in p['label']]
D=[kp(),
 kp(dx=-1,dy=2,lean=-3,farm=((3,6),(7,0)),narm=GN,nleg=STEP[0],fleg=STEP[1],hair=1),                 # 1 lấy đà, hạ trọng tâm
 kp(dx=-1,dy=0,lean=-4,farm=((2,-9),(3,-18)),narm=GN,nleg=STEP[0],fleg=STEP[1],hair=2),              # 2 tay xa giơ thẳng lên trời
 kp(dx=-2,dy=-1,lean=-6,farm=((1,-10),(1,-21)),narm=((3,9),(8,5)),nleg=STEP[0],fleg=STEP[1],hair=3),  # 3 giữ trên đỉnh, ưỡn người ra sau
 kp(dx=2,dy=3,lean=3,farm=((8,-2),(14,6)),narm=((4,9),(9,7)),nleg=WIDE[0],fleg=WIDE[1],hair=4),      # 4 bổ giữa chừng, dồn người tới
 kp(dx=4,dy=6,lean=8,farm=((9,6),(15,19)),narm=((5,10),(10,12)),nleg=WIDE[0],fleg=WIDE[1],hair=5),   # 5 CHẠM: chưởng đập xuống đất
 kp(dx=1,dy=2,lean=2,farm=GN if False else ((4,6),(8,4)),narm=GN,nleg=STEP[0],fleg=STEP[1],hair=1),   # 7 thu về
 kp()]
json.dump(D,open(f'{od}/pose_X_{tag}.json','w'))
from PIL import Image,ImageDraw
img=Image.open(f'/home/user/hoathan/nguon/pixellab/quyen/in/{tag}_idle.png').convert('RGBA').crop((16,0,144,128))
o=Image.new('RGBA',(len(D)*N*2,N*2),(40,44,52,255));d=ImageDraw.Draw(o)
for i,fr in enumerate(D):
    bg=img.resize((N*2,N*2),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*N*2,0))
    Pp={MAP.get(p['label'],p['label']):(p['x']*N*2+i*N*2,p['y']*N*2) for p in fr}
    for n in names:
        if par[n] and n in Pp and par[n] in Pp:d.line([Pp[par[n]],Pp[n]],fill=(0,255,255) if n.startswith('far') else (255,80,200) if n.startswith('near') else (220,220,220),width=3)
    d.text((i*N*2+4,4),str(i),fill=(255,255,0))
o.save(f'{od}/sketch_X_{tag}.png');print('ok',len(D))
