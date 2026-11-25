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
GF=((3,7),(8,2))
D=[kp(),
 kp(dx=-1,dy=2,lean=-3,narm=((4,6),(8,0)),farm=GF,nleg=STEP[0],fleg=STEP[1],hair=1),                  # 1 lấy đà
 kp(dx=-1,dy=0,lean=-3,narm=((6,-8),(8,-19)),farm=GF,nleg=STEP[0],fleg=STEP[1],hair=2),               # 2 tay GẦN giơ thẳng lên trời, lệch trước mặt
 kp(dx=-2,dy=-1,lean=-5,narm=((6,-10),(7,-23)),farm=GF,nleg=STEP[0],fleg=STEP[1],hair=3),             # 3 giữ trên đỉnh, ưỡn người
 kp(dx=2,dy=3,lean=3,narm=((9,-3),(15,6)),farm=GF,nleg=WIDE[0],fleg=WIDE[1],hair=4),                  # 4 bổ giữa chừng
 kp(dx=4,dy=6,lean=8,narm=((9,6),(15,19)),farm=GF,nleg=WIDE[0],fleg=WIDE[1],hair=5),                  # 5 CHẠM: chưởng đập xuống đất
 kp(dx=1,dy=2,lean=2,narm=((5,6),(9,3)),farm=GF,nleg=STEP[0],fleg=STEP[1],hair=1),                    # 6 thu về
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
# ---- job PixelLab (chỉ khi truyền seed) ----
if seeds and seeds[0]:
    J=json.load(open(src));desc=J['description'].split(', holding')[0]+', bare empty hands, no weapon'
    rig2=[j for j in J['rig'] if 'sword' not in j['name']];F02=[p for p in J['first_frame_keypoints'] if 'sword' not in p['label']]
    _b=io.BytesIO();img.save(_b,'PNG');b64=base64.b64encode(_b.getvalue()).decode()
    ACT='martial arts palm strike: raises the near arm straight up to the sky, leaning back slightly, then slams the open palm down hard to the ground in front with the whole body weight, feet planted wide, then recovers to standing; bare empty hands, no weapon, no gloves'
    for sd in seeds:
        nb=dict(J);nb.update(description=desc,rig=rig2,first_frame_keypoints=F02,keypoints=D,action=ACT,seed=int(sd),first_frame={'type':'base64','base64':b64,'format':'png'})
        json.dump(nb,open(f'{od}/job_{tag}_X_{sd}.json','w'))
    print('jobs',seeds)
