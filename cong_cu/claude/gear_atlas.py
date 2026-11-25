"""Ghép icon trang bị âm giới (zip chủ game 25/11) thành 5 atlas màu phẩm: game/assets/gear/<màu>.png (448x448, 64 px/ô).
Cột = ô trang bị (SLOT_ORDER), hàng = bộ (SET_ORDER). Nguồn: thư mục giải nén zip (mau-thu-kho/<màu>/<bộ>/<ô>.png). Dùng: gear_atlas.py <thư mục zip>"""
import sys,os
from PIL import Image
Z=sys.argv[1];OUT=os.path.join(os.path.dirname(__file__),'..','..','game','assets','gear');os.makedirs(OUT,exist_ok=True)
SET_ORDER=['hanh-gia','huyet-sa','han-thiet','hac-vu','vong-xuyen','bach-cot','diem-la']
SLOT_ORDER=['y-phuc','hai','dai-lung','ho-phu','nhan','ngoc-boi','non']
for col in ['bach','luc','lam','hoang','tu']:
    a=Image.new('RGBA',(64*len(SLOT_ORDER),64*len(SET_ORDER)),(0,0,0,0))
    for r,s in enumerate(SET_ORDER):
        for c,sl in enumerate(SLOT_ORDER):
            f=os.path.join(Z,'mau-thu-kho',col,s,sl+'.png')
            im=Image.open(f).convert('RGBA');assert im.size==(64,64),(f,im.size)
            a.paste(im,(c*64,r*64))
    a.save(os.path.join(OUT,col+'.png'),optimize=True);print(col,a.size)
