"""(tham số 10 tùy chọn: ảnh master để khóa bảng màu)
Ghép sheet nhân vật chính: đứng/trúng/gục từ gói Wuxia + chạy/đòn A/đòn B tạo bằng PixelLab (khung 128, chân ở (64,118)).
ghep_anim.py <wuxia_sheet.png> <wuxia_meta.json> <thư_mục_frame_pixellab> <tag_run> <tag_A> <tag_B> <khung_B_bỏ,...> <ra.png> <ra.json>"""
import json,sys,glob
from PIL import Image
sh_p,meta_p,D,tr,ta,tb,drop,out_png,out_json=sys.argv[1:10]
master_p=sys.argv[10] if len(sys.argv)>10 else None
import numpy as np
PAL=None
if master_p:
    _m=np.array(Image.open(master_p).convert('RGBA'));PAL=np.unique(_m[_m[...,3]>128][:,:3],axis=0).astype(float)
def snap(im):
    """Khóa bảng màu: mỗi điểm ảnh đổi về màu master gần nhất."""
    if PAL is None:return im
    a=np.array(im);m=a[...,3]>40;px=a[m][:,:3].astype(float)
    idx=np.argmin(((px[:,None,:]-PAL[None,:,:])**2).sum(2),axis=1);a[...,:3][m]=PAL[idx].astype(np.uint8);a[...,3]=np.where(m,255,0)
    return Image.fromarray(a)
drop={int(x) for x in drop.split(',') if x}
m=json.load(open(meta_p));sh=Image.open(sh_p).convert('RGBA')
CW,CH,AX,AY=160,128,80,118          # ô mới, điểm chân
def pack_frame(an,i):
    x,y=m['anims'][an]['f'][i];c=sh.crop((x,y,x+m['w'],y+m['h']));cell=Image.new('RGBA',(CW,CH));cell.paste(c,(AX-m['ax'],AY-m['ay']),c);return cell
def gen(tag,skip=()):
    fs=sorted(glob.glob(f'{D}/{tag}_0*.png'));out=[]
    for i,f in enumerate(fs):
        if i in skip:continue
        im=snap(Image.open(f).convert('RGBA'));cell=Image.new('RGBA',(CW,CH));cell.paste(im,(AX-64,AY-118),im);out.append(cell)
    return out
A={'idle':[pack_frame('idle',i) for i in range(len(m['anims']['idle']['f']))],
   'run':gen(tr),'attack':gen(ta),'attack2':gen(tb,drop),
   'hit':[pack_frame('hit',i) for i in range(len(m['anims']['hit']['f']))],
   'death':[pack_frame('death',i) for i in range(len(m['anims']['death']['f']))]}
cells=[(k,c) for k,v in A.items() for c in v];COLS=16
S=Image.new('RGBA',(COLS*CW,((len(cells)+COLS-1)//COLS)*CH));anims={}
for i,(k,c) in enumerate(cells):
    px,py=(i%COLS)*CW,(i//COLS)*CH;S.paste(c,(px,py));anims.setdefault(k,{'fps':10,'f':[]})['f'].append([px,py])
S.save(out_png,optimize=True)
meta={'w':CW,'h':CH,'ax':AX,'ay':AY,'anims':anims,'src':m['src'],'realRun':True,'face':[m['face'][0]+AX-m['ax'],m['face'][1]+AY-m['ay']]}
json.dump(meta,open(out_json,'w'));print(out_png,S.size,{k:len(v['f']) for k,v in anims.items()})
