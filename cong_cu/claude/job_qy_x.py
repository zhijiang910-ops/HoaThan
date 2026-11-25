"""Tạo job PixelLab animate-with-skeleton-v3 cho Quyền X (giơ một tay lên trời rồi bổ chưởng xuống đất).
Dùng: job_qy_x.py <job_mẫu.json> <nam|nu> <thư mục có pose_X_<g>.json> <seed,seed>
Chạy skel_qy_x.py trước để có pose_X_<g>.json. Cách dựng job giống skel_qy.py (bỏ 3 khớp kiếm, ảnh gốc = khung đứng cắt canvas 128 lệch dx=16)."""
import json,sys,base64,io,os
from PIL import Image
src,tag,od,seeds=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4].split(',')
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
POS=json.load(open(f'{od}/pose_X_{tag}.json'))
ACT=('martial arts palm strike from the sky: raises the far arm straight up above the head with an open palm, '
     'arches the back, then slams the open palm down hard onto the ground in front to the right, then stands back up to guard; '
     'bare empty hands, no weapon, no gloves')
J=json.load(open(src));desc=J['description'].split(', holding')[0]+', bare empty hands, no weapon'
rig2=[j for j in J['rig'] if 'sword' not in j['name']]
F02=[p for p in J['first_frame_keypoints'] if 'sword' not in p['label']]
im=Image.open(f'{ROOT}/nguon/pixellab/quyen/in/{tag}_idle.png').convert('RGBA').crop((16,0,144,128))
b=io.BytesIO();im.save(b,'PNG');b64=base64.b64encode(b.getvalue()).decode()
for sd in seeds:
    nb=dict(J);nb.update(description=desc,rig=rig2,first_frame_keypoints=F02,keypoints=POS,action=ACT,seed=int(sd),
                         first_frame={'type':'base64','base64':b64,'format':'png'})
    json.dump(nb,open(f'{od}/job_{tag}_X_{sd}.json','w'))
print('ok',tag,len(POS),'khung, rig',len(rig2))
