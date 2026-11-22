"""Dựng gear.png mới (10 cột x 4 hàng, ô 64px) từ icon Items_64 của Wuxia; phẩm cao thêm viền sáng màu phẩm."""
import sys,numpy as np
from PIL import Image,ImageFilter
I=sys.argv[1].rstrip('/')+'/';OUT=sys.argv[2]
def icon(n):return Image.open(I+n+'.png').convert('RGBA').resize((64,64),Image.NEAREST) if Image.open(I+n+'.png').size!=(64,64) else Image.open(I+n+'.png').convert('RGBA')
TC=[None,(122,214,122),(111,178,255),(200,140,255),(255,207,90),(255,138,58),(255,244,200)]
def glow(im,t):
    if not t or not TC[t]:return im
    a=np.array(im.getchannel('A'))>0
    m=Image.fromarray((a*255).astype('uint8')).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.4))
    g=Image.new('RGBA',im.size,TC[t]+(0,));g.putalpha(m.point(lambda v:int(v*(0.55+0.07*t))))
    out=Image.alpha_composite(g,im)
    if t>=5:  # ánh kim nhẹ lên thân
        tint=Image.new('RGBA',im.size,TC[t]+(0,));tint.putalpha(im.getchannel('A').point(lambda v:int(v*0.18)));out=Image.alpha_composite(out,tint)
    return out
# Giữ nguyên 30 ô cũ (phẩm Tiên trở lên, hộ phù); thêm 2 hàng icon Wuxia cho đồ phẩm thấp + Đai/Găng
OLD=Image.open(sys.argv[3]).convert('RGBA')
CELLS={30:('I01_wood_sword',0),31:('I01_short_sword',1),32:('I01_iron_sword',2),
 34:('I02_cloth_tunic',0),35:('I02_leather_armor',1),36:('I02_swordswoman_outfit',2),
 37:('I02_cloth_shoes',0),38:('I02_leather_boots',1),39:('I02_shin_guards',2),
 40:('I06b_broken_jade',0),41:('I06b_jade_pendant',1),42:('I06b_jade_pendant',2),
 43:('I02_belt',0),44:('I02_wrist_guards',1),45:('I01_gauntlets',2),46:('I01_gauntlets',3),47:('I02_belt',4),48:('I01_gauntlets',5),49:('I01_gauntlets',6)}
sheet=Image.new('RGBA',(640,320));sheet.alpha_composite(OLD,(0,0))
for c,(n,t) in CELLS.items():
    sheet.alpha_composite(glow(icon(n),t),((c%10)*64,(c//10)*64))
sheet.save(OUT);print('ok',OUT)
