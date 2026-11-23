#!/bin/bash
# run5.sh <move A5|B5|C5> <seedlist> [first_nam.png first_nu.png]
S=/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad; cd $S/combo5
MV=$1; SEEDS=$2; FN=$3; FU=$4
python3 -I - "$MV" "$SEEDS" "$FN" "$FU" <<'PY'
import json,sys,base64
mv,seeds,fn,fu=sys.argv[1],sys.argv[2].split(','),sys.argv[3],sys.argv[4]
ACT={'A5':'sword combo opener: raises the sword diagonally in front, steps forward into a lunge and cuts horizontally forward with the arm extended, then lowers the sword in front; one sword held in one hand only, full length',
 'B5':'reverse upward slash: from a low sword, swings the sword upward in a big rising arc in front of the body, holds it high in front, then brings it level at chest height; one sword held in one hand only, full length',
 'C5':'spinning sweep finisher in a wide stance: sweeps the sword horizontally forward, raises it, sweeps forward again, pulls it to the hip and does a final powerful horizontal sweep, then returns to stance; facing the same direction the whole time; one sword held in one hand only, full length'}
for g,src,ff in [('nam','../pl/xt_nam_rigB_body.json',fn),('nu','../pl/xd_nu_rigB_body.json',fu)]:
    b=json.load(open(src));kp=json.load(open(f'{g}_pose_{mv}.json'))
    for sd in seeds:
        nb=dict(b);nb['action']=ACT[mv];nb['seed']=int(sd);nb['keypoints']=kp;nb['first_frame_keypoints']=kp[0]
        if ff and ff!='-':nb['first_frame']={'type':'base64','base64':base64.b64encode(open(ff,'rb').read()).decode(),'format':'png'}
        json.dump(nb,open(f'job_{g}_{mv}_{sd}.json','w'))
PY
cd $S
for g in ${GS:-nam nu}; do for sd in ${SEEDS//,/ }; do t=${g}_${MV}_$sd; (timeout 900 python3 -I tools/pl.py /animate-with-skeleton-v3 combo5/job_$t.json combo5/out $t > combo5/log_$t.txt 2>&1 &); sleep 25; done; done
sleep 60; n=$(( $(echo $SEEDS | tr ',' ' ' | wc -w) * $(echo ${GS:-nam nu} | wc -w) ))
until [ $(ls combo5/log_*_${MV}_*.txt | xargs -n1 sh -c 'grep -q "^done\|FAIL\|rror\|timeout" "$0" && echo y' | wc -l) -ge $n ]; do sleep 6; done
grep -L "^done" combo5/log_*_${MV}_*.txt
sed -e "s#combo3#combo5#g; s#_pose_A3.json#_pose_A5.json#" tools/qcrun.py > tools/qcrun5.py
cd $S && python3 -I tools/qcrun5.py $MV $(for g in ${GS:-nam nu}; do for sd in ${SEEDS//,/ }; do echo -n "${g}_${MV}_$sd "; done; done)
cd combo5 && python3 -I - "$MV" "$SEEDS" "${GS:-nam nu}" <<'PY'
import sys,json
from PIL import Image,ImageDraw
mv,seeds=sys.argv[1],sys.argv[2].split(',')
rows=[f'{g}_{mv}_{s}' for g in sys.argv[3].split() for s in seeds]
n=len(json.load(open(f'nam_pose_{mv}.json')))
o=Image.new('RGBA',(n*150,len(rows)*150),(40,44,52,255));d=ImageDraw.Draw(o)
for r,t in enumerate(rows):
    for i in range(n):
        o.alpha_composite(Image.open(f'out/{t}_{i:02d}.png').convert('RGBA').crop((10,0,138,128)).resize((148,148),Image.NEAREST),(i*150,r*150));d.text((2+i*150,r*150+2),f'{t} {i}',fill='yellow')
o.save(f'eye_{mv}_'+sys.argv[3].replace(' ','')+'.png')
PY
