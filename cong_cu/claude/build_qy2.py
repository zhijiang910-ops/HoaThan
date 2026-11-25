"""Ghép Quyền v2 (khung xương PixelLab) vào sheet thân không kiếm: game/assets/hero_{nam,nu}_qy.png (+ _qy_hand.png = lớp NẮM TAY tách riêng) và in bảng socket găng.
 - Hàng y=384/512/640 = A (tay xa đấm), B (tay gần đấm), C (quét chân); ô 160x128, canvas PixelLab 128 đặt lệch dx=16; mỗi hàng 7 khung (bỏ khung đứng đầu).
 - Mỗi khung kéo dọc để chân chạm đúng đường mặt đất của khung đứng (y=117).
 - Nắm tay = pixel màu da quanh khớp cổ tay (khung xương) → cắt khỏi thân, đưa sang lớp _qy_hand. Găng/vũ khí quyền là lớp RIÊNG vẽ tại socket (x,y,góc cẳng tay) đè lên thân; không có găng thì game vẽ lớp nắm tay.
Chạy: python3 cong_cu/claude/build_qy2.py   (nguồn: nguon/pixellab/quyen/skel/out, job_*.json)"""
import json,glob,math,sys
import numpy as np
from PIL import Image
ROOT='nguon/pixellab/quyen/skel'
PICK={'nam':{'A':47,'B':59,'C':47},'nu':{'A':47,'B':31,'C':31}}
FIX={('nam','B'):{5:6}}      # khung 5 của B nam nhòe ở mọi seed (tay gần lướt ngang thân): dùng lại khung 6 sạch, không vá pixel
ROWS={'A':384,'B':512,'C':640};GROUND=117;DX=16
LAB={'near':('near_wrist','right_wrist'),'far':('far_wrist','left_wrist')}
LAE={'near':('near_elbow','right_elbow'),'far':('far_elbow','left_elbow')}
def skin(a):
    R=a[...,0].astype(int);G=a[...,1].astype(int);B=a[...,2].astype(int)
    return (a[...,3]>40)&(R>140)&(G>0.50*R)&(G<0.80*R)&(B>0.30*R)&(B<G)&(R-B>45)
def comps8(mask):
    seen=np.zeros_like(mask);res=[]
    for y0,x0 in zip(*np.where(mask)):
        if seen[y0,x0]:continue
        st=[(y0,x0)];seen[y0,x0]=True;c=[]
        while st:
            y,x=st.pop();c.append((y,x))
            for dy in(-1,0,1):
                for dx in(-1,0,1):
                    yy,xx=y+dy,x+dx
                    if 0<=yy<mask.shape[0] and 0<=xx<mask.shape[1] and mask[yy,xx] and not seen[yy,xx]:seen[yy,xx]=True;st.append((yy,xx))
        res.append(c)
    return res
out={}
for g in('nam','nu'):
    ns=Image.open(f'game/assets/hero_{g}_ns.png').convert('RGBA');W,H=ns.size
    body=Image.new('RGBA',(W,H+3*128),(0,0,0,0));body.alpha_composite(ns,(0,0));hand=Image.new('RGBA',body.size,(0,0,0,0));sock={}
    for mv,y0 in ROWS.items():
        sd=PICK[g][mv];fs=sorted(glob.glob(f'{ROOT}/out/{g}_{mv}_{sd}_*.png'))
        kps=json.load(open(f'{ROOT}/job_{g}_{mv}_{sd}.json'))['keypoints']
        for ci in range(1,len(fs)):
            src=FIX.get((g,mv),{}).get(ci,ci)
            im=np.array(Image.open(fs[src]).convert('RGBA'));a=im[...,3]>40;ys=np.where(a.any(1))[0];sh=GROUND-int(ys.max())
            cell=np.zeros((128,160,4),np.uint8)
            y_lo,y_hi=max(0,sh),min(128,128+sh)       # dịch dọc sh px (dương = xuống)
            cell[y_lo:y_hi,DX:DX+128]=im[y_lo-sh:y_hi-sh]
            K={p['label']:(p['x']*128+DX,p['y']*128+sh) for p in kps[src]}
            hl=np.zeros_like(cell);sk=skin(cell);S=[];COMPS=comps8(sk);USED=set()
            for side in('far','near'):
                wk=next(K[l] for l in LAB[side] if l in K);el=next(K[l] for l in LAE[side] if l in K)
                yy,xx=np.mgrid[0:128,0:160]
                def fist(rad,maxn=32):   # nắm tay = cụm da NHỎ và RỜI (mảng da chân/mặt liền khối lớn bị loại)
                    comps=[c for c in COMPS if id(c) not in USED and len(c)<=maxn and min(math.hypot(x-wk[0],y-wk[1]) for y,x in c)<=rad]
                    if not comps:return np.zeros_like(sk)
                    best=min(comps,key=lambda c:min(math.hypot(x-wk[0],y-wk[1]) for y,x in c));m_=np.zeros_like(sk)
                    for y,x in best:m_[y,x]=True
                    return m_
                m=fist(7.5)
                if m.sum():USED.add(id(next(c for c in COMPS if (lambda t:all(m[y,x] for y,x in t[:1]))(c))))
                if m.sum()>=3:
                    cx,cy=float(xx[m].mean()),float(yy[m].mean());hl[m]=cell[m];cell[m]=0
                    ang=math.degrees(math.atan2(wk[1]-el[1],wk[0]-el[0]));S.append([round(cx,1),round(cy,1),round(ang,1)])
                # không thấy nắm tay (bị che) => không có socket, không vẽ găng ở tay đó
            x0=(ci-1)*160
            body.alpha_composite(Image.fromarray(cell,'RGBA'),(x0,H+(y0-384)));hand.alpha_composite(Image.fromarray(hl,'RGBA'),(x0,H+(y0-384)))
            sock[f'{x0},{y0}']=S
        print(g,mv,'seed',sd,len(fs)-1,'khung')
    body.save(f'game/assets/hero_{g}_qy.png',optimize=True);hand.save(f'game/assets/hero_{g}_qy_hand.png',optimize=True)
    out[g]=sock
json.dump(out,open('cong_cu/claude/qsock.json','w'),separators=(',',':'))
print('socket',{g:len(v) for g,v in out.items()});print(json.dumps(out)[:300])
