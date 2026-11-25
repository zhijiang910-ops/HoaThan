"""Quyền (25/11): nhuộm VFX gói Wuxia sang tím-lam: bàn tay Như Lai -> bàn tay quỷ (qy_hand), vết chưởng, bụi, đá, chuông Kim Cương.
Giữ nguyên alpha và hình, chỉ ánh xạ độ sáng -> bảng màu. Chạy: python3 cong_cu/claude/qy_tim.py"""
from PIL import Image
import numpy as np
R='/home/user/hoathan/game/assets/vfx/'
def tint(src,dst,stops,gain=1.15):
    a=np.array(Image.open(R+src).convert('RGBA')).astype(float)
    lum=(a[:,:,0]*0.3+a[:,:,1]*0.59+a[:,:,2]*0.11)/255
    o=np.zeros_like(a)
    for ch in range(3):
        o[:,:,ch]=np.interp(np.clip(lum*gain,0,1),[s[0] for s in stops],[s[1][ch] for s in stops])
    o[:,:,3]=a[:,:,3]
    Image.fromarray(o.astype('uint8')).save(R+dst,optimize=True);print(dst)
HAND=[(0,(8,4,26)),(0.25,(46,22,110)),(0.5,(104,56,214)),(0.72,(168,120,255)),(0.88,(218,196,255)),(1,(250,244,255))]
tint('rulai_hand.png','qy_hand.png',HAND)
tint('rulai_crater.png','qy_crater.png',HAND,1.0)
tint('rulai_dust.png','qy_dust.png',[(0,(30,16,70)),(0.5,(96,70,170)),(1,(200,184,255))])
tint('rulai_rock.png','qy_rock.png',[(0,(10,6,28)),(0.5,(60,40,120)),(1,(150,124,230))])
tint('pm_bell.png','qy_bell.png',HAND)
tint('van_vang.png','qy_van.png',[(0,(20,8,60)),(0.5,(120,80,230)),(1,(236,224,255))],1.0)
