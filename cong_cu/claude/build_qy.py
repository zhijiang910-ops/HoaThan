"""Ghép động tác đấm Song Quyền (PixelLab, nguon/pixellab/quyen/raw) vào bản sao sheet thân không kiếm: game/assets/hero_{nam,nu}_qy.png
Hàng y=384 (A, đấm thẳng), 512 (B, móc), 640 (C, móc ngược), ô 160x128; bỏ khung 0 (khung gốc). Kèm hero_{g}_qy_hand.png trong suốt (game vẽ lớp tay nếu có socket)."""
import sys,glob
from PIL import Image
import numpy as np
for g in sys.argv[1:] or ['nam','nu']:
    ns=Image.open(f'game/assets/hero_{g}_ns.png').convert('RGBA');W,H=ns.size
    sh=Image.new('RGBA',(W,H+3*128),(0,0,0,0));sh.alpha_composite(ns,(0,0));cnt={}
    for r,k in enumerate('abc'):
        fs=sorted(glob.glob(f'nguon/pixellab/quyen/raw/{g}_{k}_*.png'))[1:]
        for i,f in enumerate(fs):
            im=Image.open(f).convert('RGBA');a=np.array(im);a[a[...,3]<40]=0
            if g=='nu' and k=='b':  # vòng trắng rác của PixelLab quanh nắm tay
                rgb=a[...,:3].astype(int);w=(rgb.min(-1)>195)&((rgb.max(-1)-rgb.min(-1))<35);w[:,:105]=False;a[w,3]=0
            sh.alpha_composite(Image.fromarray(a,'RGBA'),(i*160,H+r*128))
        cnt[k]=len(fs)
    sh.save(f'game/assets/hero_{g}_qy.png',optimize=True)
    Image.new('RGBA',(W,H+3*128),(0,0,0,0)).save(f'game/assets/hero_{g}_qy_hand.png',optimize=True)
    print(g,cnt,sh.size)
