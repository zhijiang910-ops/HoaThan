# Sửa dải buộc tóc của hero_{g}_ms.png theo Master (hero_{g}_ns.png): chạy SAU build_outfit.py
import json,numpy as np
from PIL import Image
F=[tuple(x) for x in json.load(open('nguon/pixellab/trangphuc/frames.json'))]
def rib(a,g):
    r,gg,b,al=[a[...,i].astype(int) for i in range(4)]
    if g=='nu': return (al>100)&(r>120)&(gg<75)&(b<75)
    mx=np.maximum(np.maximum(r,gg),b);mn=np.minimum(np.minimum(r,gg),b)
    return (al>100)&(mx>130)&((mx-mn)<45)
def wrong(a,g):
    r,gg,b,al=[a[...,i].astype(int) for i in range(4)]
    if g=='nu': return (al>100)&(b>r+25)
    return (al>100)&(r>150)&(gg>110)&(b<90)
for g in('nam','nu'):
    ns=np.array(Image.open(f'game/assets/hero_{g}_ns.png').convert('RGBA'));ms=np.array(Image.open(f'game/assets/hero_{g}_ms.png').convert('RGBA'));n=0
    for x,y in F:
        a=ns[y:y+128,x:x+160];b=ms[y:y+128,x:x+160]
        ys=np.where(a[...,3]>40)[0]
        if not len(ys):continue
        t=ys.min();m=np.zeros(a.shape[:2],bool);m[t:t+30]=True
        rs=rib(a,g)&m
        sel=(rs&~rib(b,g))|(wrong(b,g)&m&~rs)
        b[sel]=np.where(rs[sel][:,None],a[sel],np.array([0,0,0,0]))
        n+=int(sel.sum())
    Image.fromarray(ms).save(f'game/assets/hero_{g}_ms.png');print(g,'pixel sửa',n)
