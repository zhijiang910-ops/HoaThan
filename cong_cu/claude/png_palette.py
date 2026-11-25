#!/usr/bin/env python3
"""Nén PNG KHÔNG MẤT NÉT: ảnh <=256 màu (kể cả alpha) đổi sang PNG bảng màu; chỉ ghi khi từng pixel RGBA giống hệt bản gốc.
Dùng: python3 cong_cu/claude/png_palette.py [thư mục=game/assets] [--dry]"""
import os,io,sys
import numpy as np
from PIL import Image
root=next((a for a in sys.argv[1:] if not a.startswith('--')),'game/assets');dry='--dry' in sys.argv
before=after=0;done=[];bad=[]
for d,_,fs in os.walk(root):
    for f in fs:
        if not f.lower().endswith('.png'):continue
        p=os.path.join(d,f);sz=os.path.getsize(p)
        try:im=Image.open(p);im.load()
        except Exception:continue
        if im.mode=='P':before+=sz;after+=sz;continue
        rgba=im.convert('RGBA');a=np.array(rgba)
        u=np.unique(a.reshape(-1,4).view(np.uint32))
        if len(u)>256:before+=sz;after+=sz;continue
        pal=rgba.quantize(colors=256,method=Image.Quantize.FASTOCTREE,dither=Image.Dither.NONE) if False else None
        # bảng màu CHÍNH XÁC: dựng thẳng từ các màu duy nhất
        cols=np.array(u,dtype=np.uint32).view(np.uint8).reshape(-1,4)
        lut={tuple(c):i for i,c in enumerate(cols)}
        idx=np.array([lut[tuple(px)] for px in a.reshape(-1,4)],dtype=np.uint8).reshape(a.shape[:2]) if a.shape[0]*a.shape[1]<400000 else None
        if idx is None:
            key=(a[...,0].astype(np.uint32)<<24)|(a[...,1].astype(np.uint32)<<16)|(a[...,2].astype(np.uint32)<<8)|a[...,3].astype(np.uint32)
            ukeys=((cols[:,0].astype(np.uint32)<<24)|(cols[:,1].astype(np.uint32)<<16)|(cols[:,2].astype(np.uint32)<<8)|cols[:,3].astype(np.uint32))
            order=np.argsort(ukeys);idx=order[np.searchsorted(ukeys[order],key)].astype(np.uint8)
        out=Image.fromarray(idx,'P')
        pal=[];tr=[]
        for c in cols:pal+= [int(c[0]),int(c[1]),int(c[2])];tr.append(int(c[3]))
        out.putpalette(pal+[0]*(768-len(pal)))
        buf=io.BytesIO();kw=dict(optimize=True)
        if any(t<255 for t in tr):kw['transparency']=bytes(tr)
        out.save(buf,'PNG',**kw);nb=buf.getvalue()
        chk=np.array(Image.open(io.BytesIO(nb)).convert('RGBA'))
        if not np.array_equal(chk,a):bad.append(p);before+=sz;after+=sz;continue
        before+=sz
        if len(nb)<sz*0.97:
            after+=len(nb);done.append((sz-len(nb),p))
            if not dry:open(p,'wb').write(nb)
        else:after+=sz
done.sort(reverse=True)
print(f'{"(thử, chưa ghi) " if dry else ""}đã nén {len(done)} file, {before/1048576:.1f} MB -> {after/1048576:.1f} MB (giảm {(before-after)/1048576:.1f} MB); lệch pixel (bỏ qua): {len(bad)}')
for s,p in done[:10]:print(f'  -{s//1024} KB {p}')
for p in bad:print('  LỆCH',p)
