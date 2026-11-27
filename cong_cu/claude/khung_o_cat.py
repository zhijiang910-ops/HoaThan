# Cắt tấm 6 khung ô (chủ game gửi 27/11) thành 6 sprite sát mép ngoài, nền ngoài khung trong suốt.
# Mép = viền đen ngoài cùng (tổng RGB < 70) theo từng hàng và từng cột (xử lý được góc vát).
# Chạy: python3 cong_cu/claude/khung_o_cat.py  -> game/assets/ui/popup/o_{cao,cao_chon,nho,tui_trong,tui_do,tui_chon}.png
from PIL import Image
import numpy as np, os
SRC='nguon/master_amgioi/popup/khung_o_goc.png'; OUT='game/assets/ui/popup'
A=np.array(Image.open(SRC).convert('RGBA'))
BOX={'o_cao':(148,45,418,528),'o_cao_chon':(627,45,893,528),'o_nho':(1087,160,1398,522),
     'o_tui_trong':(120,615,457,945),'o_tui_do':(600,615,937,945),'o_tui_chon':(1077,615,1417,945)}
from collections import deque
def bgmask(C,th=16):
    P=C[...,:3].astype(int); H,W=P.shape[:2]; bg=np.zeros((H,W),bool); q=deque()
    for x in range(W):
        for y in (0,H-1): bg[y,x]=1; q.append((y,x))
    for y in range(H):
        for x in (0,W-1): bg[y,x]=1; q.append((y,x))
    while q:
        y,x=q.popleft()
        for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
            v,u=y+dy,x+dx
            if 0<=v<H and 0<=u<W and not bg[v,u] and np.abs(P[v,u]-P[y,x]).sum()<th:
                bg[v,u]=1; q.append((v,u))
    return bg
for k,(x0,y0,x1,y1) in BOX.items():
    m=26; C=A[y0-m:y1+m,x0-m:x1+m].copy(); bg=bgmask(C)
    C[bg,3]=0
    keep=~bg
    # bỏ đốm lẻ ngoài khung: chỉ lấy hàng/cột có ít nhất 30% điểm thuộc khung
    r=keep.mean(1)>.3; c=keep.mean(0)>.3; ys=np.where(r)[0]; xs=np.where(c)[0]
    keep[:ys.min()]=0; keep[ys.max()+1:]=0; keep[:,:xs.min()]=0; keep[:,xs.max()+1:]=0; C[~keep,3]=0
    C=C[ys.min():ys.max()+1,xs.min():xs.max()+1]
    Image.fromarray(C).save(f'{OUT}/{k}.png'); print(k,C.shape[1],C.shape[0])
# Thu về cỡ dùng trong game (đủ nét ở màn 1280×720 DPR2), lưu webp có alpha
SZ={'o_cao':300,'o_cao_chon':300,'o_nho':200,'o_tui_trong':150,'o_tui_do':150,'o_tui_chon':150}
for k,h in SZ.items():
    im=Image.open(f'{OUT}/{k}.png'); im=im.resize((round(im.width*h/im.height),h),Image.LANCZOS)
    im.save(f'{OUT}/{k}.webp',quality=88,method=6); os.remove(f'{OUT}/{k}.png')
b=Image.open('nguon/master_amgioi/popup/banhu_goc.png').convert('RGBA'); b=b.crop((89,113,1195,1118))
b.resize((480,round(480*b.height/b.width)),Image.LANCZOS).save(f'{OUT}/banhu.webp',quality=90,method=6)
print('ok')
