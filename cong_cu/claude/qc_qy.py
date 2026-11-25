"""Kiểm lệch khung clip Quyền: so từng khung với khung đứng gốc (in/{g}_idle.png): đỉnh đầu, đáy chân, tâm thân (cột trung vị), bề cao, số pixel. In cảnh báo khi lệch quá ngưỡng.
Dùng: python3 qc_qy.py <thư mục raw> [nam nu]"""
import sys,glob
import numpy as np
from PIL import Image
R=sys.argv[1];gs=sys.argv[2:] or ['nam','nu']
def stat(p):
    a=np.array(Image.open(p).convert('RGBA'));m=a[...,3]>40
    ys,xs=np.where(m)
    if not len(ys):return None
    # tâm thân: trung vị cột của phần thân (từ 30% đến 80% chiều cao của bbox)
    y0,y1=ys.min(),ys.max();sel=(ys>y0+0.3*(y1-y0))&(ys<y0+0.8*(y1-y0))
    return dict(top=int(y0),bot=int(y1),h=int(y1-y0+1),cx=float(np.median(xs[sel])) if sel.any() else float(np.median(xs)),n=int(m.sum()),l=int(xs.min()),r=int(xs.max()))
for g in gs:
    base=stat(f'nguon/pixellab/quyen/in/{g}_idle.png');print(g,'GỐC',base)
    for k in 'abc':
        fs=sorted(glob.glob(f'{R}/{g}_{k}_*.png'))
        if not fs:continue
        print(' clip',k,len(fs))
        for i,f in enumerate(fs):
            s=stat(f);flag=[]
            if s is None:print('  ',i,'TRỐNG');continue
            if abs(s['top']-base['top'])>6 and k!='c':flag.append('đầu lệch %+d'%(s['top']-base['top']))
            if abs(s['bot']-base['bot'])>4:flag.append('chân lệch %+d'%(s['bot']-base['bot']))
            if abs(s['cx']-base['cx'])>10:flag.append('thân trôi %+.0f'%(s['cx']-base['cx']))
            if s['n']<0.75*base['n'] or s['n']>1.35*base['n']:flag.append('cỡ lạ n=%d'%s['n'])
            print('  ',i,'top',s['top'],'bot',s['bot'],'cx %.0f'%s['cx'],'n',s['n'],'x',s['l'],'-',s['r'],' '.join('⚠'+x for x in flag))
