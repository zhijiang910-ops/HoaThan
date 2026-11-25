"""Khung xương 3 động tác Quyền (bỏ 3 khớp kiếm): A = tay xa đấm thẳng, B = tay gần đấm xoay hông, C = hạ thấp quét chân sát đất.
Dùng: skel_qy.py <job_mẫu.json (có rig, first_frame_keypoints)> <nam|nu> <outdir> <seed,seed>"""
import json,sys,base64,os
src,tag,od,seeds=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4].split(',')
P1=os.path.join(os.path.dirname(os.path.abspath(__file__)),'combopose.py');code=open(P1).read();code=code[:code.index('# chân: bước dài')]
sys.argv=['combopose.py',src,od,tag];exec(code)
N=128
GUARD_F=((3,7),(8,2));GUARD_N=((3,8),(8,4))   # thế thủ (tay co trước ngực)
STEP=(((3,14),(5,30)),((-3,15),(-6,31)))        # chân hơi mở, KHÔNG xòe rộng (tránh lộ quần)
def kp(**k):
    out=pose(**k);return [p for p in out if 'sword' not in p['label']]
# A: tay xa đấm thẳng
A=[kp(),
 kp(dx=-1,lean=-2,farm=GUARD_F,narm=GUARD_N,nleg=STEP[0],fleg=STEP[1],hair=1),
 kp(dx=1,lean=1,farm=((6,2),(12,1)),narm=GUARD_N,nleg=STEP[0],fleg=STEP[1],hair=2),
 kp(dx=3,lean=4,farm=((9,0),(20,0)),narm=GUARD_N,nleg=STEP[0],fleg=STEP[1],hair=3),
 kp(dx=3,lean=4,farm=((9,0),(21,0)),narm=GUARD_N,nleg=STEP[0],fleg=STEP[1],hair=3),
 kp(dx=2,lean=2,farm=((7,3),(13,2)),narm=GUARD_N,nleg=STEP[0],fleg=STEP[1],hair=2),
 kp(dx=1,lean=0,farm=GUARD_F,narm=GUARD_N,hair=1),
 kp()]
# B: tay gần đấm thẳng, xoay hông (người nghiêng nhiều hơn)
B=[kp(),
 kp(dx=-1,lean=-3,farm=GUARD_F,narm=((2,9),(6,5)),nleg=STEP[0],fleg=STEP[1],hair=1),
 kp(dx=2,lean=2,farm=GUARD_F,narm=((6,2),(12,1)),nleg=STEP[0],fleg=STEP[1],hair=2),
 kp(dx=4,lean=6,farm=((2,8),(5,6)),narm=((9,0),(20,0)),nleg=STEP[0],fleg=STEP[1],hair=4),
 kp(dx=4,lean=6,farm=((2,8),(5,6)),narm=((9,0),(21,0)),nleg=STEP[0],fleg=STEP[1],hair=4),
 kp(dx=2,lean=3,farm=GUARD_F,narm=((7,3),(13,2)),nleg=STEP[0],fleg=STEP[1],hair=2),
 kp(dx=1,lean=0,farm=GUARD_F,narm=GUARD_N,hair=1),
 kp()]
# C: hạ thấp, hai tay chống xuống đất, một chân duỗi quét sát đất (mắt cá cách đất ~2px), rồi đứng lên
DN=((6,6),(10,24))
C=[kp(),
 kp(dx=0,dy=10,lean=2,farm=((5,9),(9,18)),narm=((4,9),(8,19)),nleg=((9,9),(14,26)),fleg=((7,9),(3,26))),
 kp(dx=-2,dy=22,lean=1,farm=((6,14),(11,29)),narm=((3,14),(6,30)),nleg=((11,5),(17,19)),fleg=((6,7),(-4,19))),
 kp(dx=-3,dy=22,lean=-3,farm=((6,14),(11,29)),narm=((3,14),(6,30)),nleg=((16,5),(27,19)),fleg=((6,7),(-4,19))),
 kp(dx=-3,dy=22,lean=-4,farm=((6,14),(11,29)),narm=((3,14),(6,30)),nleg=((20,4),(35,20)),fleg=((6,7),(-4,19)),hair=2),
 kp(dx=-2,dy=22,lean=-3,farm=((6,14),(11,29)),narm=((3,14),(6,30)),nleg=((17,5),(30,20)),fleg=((6,7),(-4,19)),hair=1),
 kp(dx=0,dy=10,lean=0,farm=((5,9),(9,18)),narm=((4,9),(8,19)),nleg=((9,9),(14,26)),fleg=((7,9),(3,26))),
 kp()]
POS={'A':A,'B':B,'C':C}
ACT={'A':'martial arts jab: throws a fast straight punch forward to the right with the far arm, then pulls it back to guard; bare empty hands, no weapon, no gloves',
 'B':'martial arts cross punch: twists the hips and throws a straight punch forward to the right with the near arm, then returns to guard; bare empty hands, no weapon, no gloves',
 'C':'low ground leg sweep: drops into a crouch with both hands on the floor and sweeps one fully extended leg forward to the right along the ground, then stands back up; bare empty hands, no weapon, no gloves'}
J=json.load(open(src));desc=J['description'].split(', holding')[0]+', bare empty hands, no weapon'
rig2=[j for j in J['rig'] if 'sword' not in j['name']]
F02=[p for p in J['first_frame_keypoints'] if 'sword' not in p['label']]
import io
from PIL import Image
_im=Image.open(f'/home/user/hoathan/nguon/pixellab/quyen/in/{tag}_idle.png').convert('RGBA').crop((16,0,144,128));_b=io.BytesIO();_im.save(_b,'PNG');b64=base64.b64encode(_b.getvalue()).decode()  # canvas 128, ô 160 lệch dx=16
os.makedirs(od,exist_ok=True)
for mv in 'ABC':
    for sd in seeds:
        nb=dict(J);nb.update(description=desc,rig=rig2,first_frame_keypoints=F02,keypoints=POS[mv],action=ACT[mv],seed=int(sd),first_frame={'type':'base64','base64':b64,'format':'png'})
        json.dump(nb,open(f'{od}/job_{tag}_{mv}_{sd}.json','w'))
print('ok',tag,[len(POS[m]) for m in 'ABC'],'rig',len(rig2),'kp',len(POS['A'][0]))
