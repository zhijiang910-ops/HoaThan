"""Ghép kết quả transfer-outfit (nguon/pixellab/trangphuc/full/<phai>_<gioi>/x_y.png, 128x128) vào bản sao sheet thân không kiếm:
game/assets/hero_<gioi>_<hauto>.png (3840x384). Ô gốc 160x128 tại (x,y); cell đã lệch -16 nên dán lại ở (x+16,y). Khung thiếu giữ nguyên bản gốc.
Dùng: python3 cong_cu/claude/build_outfit.py maoson ms nam nu"""
import sys,os
from PIL import Image
sect,sfx=sys.argv[1],sys.argv[2]
for g in sys.argv[3:]:
    ns=Image.open(f'game/assets/hero_{g}_ns.png').convert('RGBA');out=ns.copy();n=0
    d=f'nguon/pixellab/trangphuc/full/{sect}_{g}'
    for f in sorted(os.listdir(d)):
        x,y=map(int,f[:-4].split('_'));cell=Image.open(f'{d}/{f}').convert('RGBA')
        # xóa ô gốc rồi dán bản mới
        blank=Image.new('RGBA',(160,128),(0,0,0,0));out.paste(blank,(x,y));out.alpha_composite(cell,(x+16,y));n+=1
    out.save(f'game/assets/hero_{g}_{sfx}.png',optimize=True)
    # lớp tay: dùng lại lớp tay gốc (tay da giữ nguyên)
    import shutil;shutil.copy(f'game/assets/hero_{g}_hand.png',f'game/assets/hero_{g}_{sfx}_hand.png')
    print(g,n,'khung',out.size)
