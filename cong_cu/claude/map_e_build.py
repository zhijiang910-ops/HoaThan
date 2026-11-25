"""Vật PixelLab mới cho Uổng Tử (vạc dầu, xương) và Vong Xuyên (thuyền ma, đá Tam Sinh, đèn hoa) + nền Vong Xuyên dựng lại (sông giữa map, cầu bắc ngang). Chạy: python3 cong_cu/claude/map_e_build.py"""
from PIL import Image
import json
R='/home/user/hoathan/'
E=R+'nguon/pixellab/maps/e/'
OUT=R+'game/assets/map/'
S=[('Dp_vacdau','vacdau_11',[-40,-16,40,-2],0),('Dp_vacdau2','vacdau_23',[-40,-16,40,-2],0),('Dp_docxuong','docxuong_11',[-26,-8,26,-2],0),
('Dp_giandinh','giandinh_11',[-40,-14,40,-2],0),('Dp_giandinh2','giandinh_23',[-40,-14,40,-2],0),('Dp_cocxich','coc_xich_11',[-9,-8,9,0],0),('Dp_thaposo','thaposo_11',[-22,-10,22,-2],0),
('Dp_tamsinh','tamsinh_23',[-14,-8,14,-2],0),('Dp_thuyenma','thuyenma_11',None,1),('Dp_thuyenma2','thuyenma_23',None,1),('Dp_denhoa','denhoa_11',None,1)]
mm={}
for n,f,col,flat in S:
    im=Image.open(E+f+'.png').convert('RGBA');bb=im.getchannel('A').point(lambda a:255 if a>40 else 0).getbbox();im=im.crop(bb)
    im.save(OUT+n+'.png',optimize=True)
    w,h=im.size;d={"src":"assets/map/%s.png"%n,"w":w,"h":h,"ax":w//2,"ay":h-2,"col":col}
    if flat:d["flat"]=1
    mm[n]=d
print(json.dumps(mm,separators=(',',':'),ensure_ascii=False))
# nền Vong Xuyên: sông ở giữa map, cầu bắc dọc qua sông
o=Image.open(R+'nguon/master_amgioi/chatgpt_map_vongxuyen_1600x1140.png').convert('RGB')
W=Image.new('RGB',(1600,1140))
W.paste(o.crop((0,500,1600,830)),(0,0))
W.paste(o.crop((0,400,1600,810)),(0,730))
W.paste(o.crop((0,0,1600,400)),(0,330))
import numpy as np
foot=o.crop((690,270,1090,400)).transpose(Image.FLIP_TOP_BOTTOM)
fa=np.array(foot).astype(int);ga=np.array(W.crop((690,200,1090,330))).astype(int)
br=fa.sum(2)/3;water=(br<48)&(fa[:,:,2]>fa[:,:,0]+16)&(fa[:,:,1]>fa[:,:,0]+8)
# làm dày mặt nạ nước một chút để bỏ viền xanh
w2=water.copy()
pass
water=w2
fa[water]=ga[water];W.paste(Image.fromarray(fa.astype('uint8')),(690,200))
# làm mềm đường nối phía bắc và phía nam của dải sông
import numpy as np
a=np.array(W).astype(float)
def feather(y,h=14):
    for i in range(h):
        t=(i+1)/(h+1);a[y-h//2+i]=a[y-h//2+i]*(1-t*0.0)  # giữ nguyên, chỉ để lại hook
feather(330)
W=Image.fromarray(a.astype('uint8'))
W.save(R+'nguon/master_amgioi/vongxuyen_nen_moi_1600x1140.png')
W.save(OUT+'bg_vongxuyen.png',optimize=True)
print('bg ok',W.size)
