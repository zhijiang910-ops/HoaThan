# Ghép sheet tư thế Vạn Kiếm 4 khung (160x128): khung 0 = khung đứng gốc của sheet đích, khung 1-3 = khung PixelLab (canvas 128, đặt lệch dx=16), kéo dọc cho chân chạm y=117 như khung gốc.
# python3 cong_cu/claude/build_vk.py <sheet đích, vd nam_ns> <ra, vd hero_nam_vk> <khung1.png> <khung2.png> <khung3.png>
import sys,numpy as np
from PIL import Image
A='/home/user/HoaThan/game/assets/'
tgt,outn,fs=sys.argv[1],sys.argv[2],sys.argv[3:6]
sh=Image.open(A+'hero_'+tgt+'.png').convert('RGBA')
out=Image.new('RGBA',(640,128));out.alpha_composite(sh.crop((0,0,160,128)),(0,0))
for i,f in enumerate(fs):
    im=Image.open(f).convert('RGBA');a=np.array(im)[:,:,3];bot=np.where(a.max(1)>0)[0].max()
    out.alpha_composite(im,(160*(i+1)+16,int(117-bot)))
out.save(A+outn+'.png');print('ok',outn)
