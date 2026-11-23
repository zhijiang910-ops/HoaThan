"""Kiểm toàn bộ animation nhân vật chính, xuất bảng kết quả + ảnh soát (đánh dấu đỏ frame lỗi).
qc_all.py <tools_dir> <out_png>"""
import sys,json,glob,math
sys.path.insert(0,sys.argv[1]);import qc
from PIL import Image,ImageDraw
P='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/pl/'
import os
SETS=[tuple(x) for x in json.loads(os.environ['QCSETS'])] if os.environ.get('QCSETS') else [('xt_nam','Nam · chạy','nam_run_sk','run',()),('xt_nam','Nam · đòn A','xt_nam_rigA2','A',()),('xt_nam','Nam · đòn B','xt_nam_rigB3','B',(4,)),
      ('xd_nu','Nữ · chạy','nu_run_sk','run',()),('xd_nu','Nữ · đòn A','xd_nu_rigA2','A',()),('xd_nu','Nữ · đòn B','xd_nu_rigB2','B',(4,))]
# Frame tay cầm kiếm bị đầu che theo thiết kế (giơ kiếm ra sau đầu): không đòi thấy kiếm đủ dài
HIDE_SWORD={('A',0),('A',1)}
rows=[];report=[]
for k,name,tag,key,skip in SETS:
    C=json.load(open(P+f'out/{k}_cust_meta.json'));F0={p['label']:p for p in C['frames'][0]}
    names=[j['name'] for j in C['rig']];par={j['name']:j['parent'] for j in C['rig']}
    sw=[n for n in names if n.startswith('sword')];wr=par[sw[0]]
    near=[n for n in names if ('near' in n or 'right' in n) and 'wrist' in n][0]
    S=128;w0=(F0[wr]['x']*S,F0[wr]['y']*S);t0=(F0[sw[-1]]['x']*S,F0[sw[-1]]['y']*S);L=math.dist(w0,t0);mang=math.degrees(math.atan2(t0[1]-w0[1],t0[0]-w0[0]))
    M=qc.load(P+f'{k}_first.png');pal=qc.palette_set(M).astype(float)
    fs=sorted(glob.glob(P+f'out/{tag}_0*.png'))
    if key=='run':
        R=json.load(open(P+f'{k}_runskel.json'));exp=[]
        for kp in R['frames']:
            d={q['label']:q for q in kp};exp.append(((d['LEFT ARM']['x']*S,d['LEFT ARM']['y']*S),mang,(d['RIGHT ARM']['x']*S,d['RIGHT ARM']['y']*S)))
    else:
        R=json.load(open(P+f'{k}_rigatk.json'));exp=[]
        for kp in R[key]:
            d={q['label']:q for q in kp};w=(d[wr]['x']*S,d[wr]['y']*S);t=(d[sw[-1]]['x']*S,d[sw[-1]]['y']*S)
            exp.append((w,math.degrees(math.atan2(t[1]-w[1],t[0]-w[0])),(d[near]['x']*S,d[near]['y']*S)))
    row=[]
    for i,(f,(w,ang,nw)) in enumerate(zip(fs,exp)):
        if i in skip:continue
        A=qc.load(f);bm=qc.blade_px(A);c,ww,aa=qc.best_line(bm,w,ang,L)
        tip=qc.cover(bm,ww,aa,L,0.85,1.0);over=qc.cover(bm,ww,aa,L,1.12,1.3)
        cs=qc.costume12(A,pal);hand=qc.hand_ok(A,nw);st=qc.stray(A)
        errs=[]
        if (key,i) not in HIDE_SWORD:
            if c<0.9:errs.append('thiếu kiếm')
            else:
                if qc.cover(bm,ww,aa,L,0.95,1.0)<0.5:errs.append('kiếm ngắn')
            if qc.cover(bm,ww,aa,L,1.06,1.25)>0.5:errs.append('kiếm dài')
        if cs<0.97:errs.append(f'trang phục {cs*100:.1f}%')
        if not hand:errs.append('mất bàn tay')
        if st:errs.append(f'điểm rác x{len(st)}')
        row.append((f,errs));report.append((name,i,errs))
    rows.append((name,P+f'{k}_first.png',row))
# ảnh soát
Z=2;CW=128*Z;o=Image.new('RGB',(CW*9,(CW+24)*len(rows)),'#2a2f38');from PIL import ImageFont
FT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',12);d=ImageDraw.Draw(o)
for r,(name,master,row) in enumerate(rows):
    y=r*(CW+24);d.text((6,y+4),name,fill='#ffd987',font=FT)
    ims=[(master,None)]+row
    for c,(f,errs) in enumerate(ims):
        im=Image.open(f).convert('RGBA').resize((CW,CW),Image.NEAREST);x=c*CW
        bg=Image.new('RGBA',(CW,CW),(70,78,90,255));bg.alpha_composite(im);o.paste(bg.convert('RGB'),(x,y+20))
        lab='MASTER' if errs is None else (('LỖI: '+', '.join(errs)) if errs else 'ĐẠT')
        col='#9cc4ff' if errs is None else ('#ff6a5a' if errs else '#8fe0a8')
        d.text((x+4,y+22),lab[:40],fill=col,font=FT)
        if errs:d.rectangle((x,y+20,x+CW-1,y+20+CW-1),outline='#ff4030',width=3)
o.save(sys.argv[2])
bad=[r for r in report if r[2]]
print('Tổng',len(report),'frame · lỗi',len(bad))
for n,i,e in bad:print('  ',n,'frame',i,e)
