"""Chuẩn hóa 5 kiếm của gói trang bị 26/11: xoay ngang (mũi sang phải), thu BOX về cỡ game, alpha cứng, lượng tử màu.
Chạy: python3 cong_cu/claude/kiem_goi_build.py  -> game/assets/wpn/kiem*.png + in số WPN."""
import numpy as np, math, json
from PIL import Image
SRC='nguon/trang_bi_goi_26_11/weapon-sources/'; OUT='game/assets/wpn/'
# tên -> (file, chiều dài thân ~px game, vị trí nắm = tỉ lệ dọc trục từ đầu chuôi)
J={'kiem01':('kiem-01.png',62,.20),'kiem02':('kiem-02.png',62,.22),'kiem03':('kiem-03.png',64,.20),
   'kiem04b':('kiem-04-B.png',64,.18),'kiem04d':('kiem-04-D.png',64,.18),'kiem05':('kiem-05.png',64,.20)}
res={}
for k,(f,L,gr) in J.items():
    im=Image.open(SRC+f).convert('RGBA'); a=np.array(im)[:,:,3]>40
    ys,xs=np.nonzero(a); c=np.array([xs.mean(),ys.mean()]); P=np.stack([xs,ys],1)-c
    w,v=np.linalg.eigh(np.cov(P.T)); ax=v[:,1]
    if k in('kiem04b','kiem04d'): ax=np.array([1.,0.])   # đã nằm ngang, chuôi trái
    elif ax[0]<0: ax=-ax
    if k not in('kiem04b','kiem04d'):
        # mũi ở phía có ít khối (mũi nhọn): chọn chiều đầu mút nào mảnh hơn
        pr=P@ax; lo=pr<np.percentile(pr,12); hi=pr>np.percentile(pr,88)
        wlo=np.ptp(P[lo]@np.array([-ax[1],ax[0]])); whi=np.ptp(P[hi]@np.array([-ax[1],ax[0]]))
        if whi>wlo: ax=-ax            # đầu rộng hơn = chuôi, phải ở trái
    ang=math.degrees(math.atan2(ax[1],ax[0]))
    r=im.rotate(ang,resample=Image.BICUBIC,expand=True)   # PIL: dương = ngược chiều kim đồng hồ; trục ax (y xuống) -> ngang
    bb=r.getbbox(); r=r.crop(bb)
    HR=3                                   # ảnh nét gấp 3 lần cỡ game; game tự thu về đúng pixel màn hình (wImgFor)
    nw=round(L*HR); nh=max(1,round(r.height*nw/r.width))
    # LANCZOS trên ảnh nhân alpha (không viền đen), giữ alpha mềm, KHÔNG giảm màu
    arr=np.array(r).astype(np.float64); al=arr[:,:,3:4]/255.0
    pm=np.concatenate([arr[:,:,:3]*al,arr[:,:,3:4]],2)
    ch=[np.array(Image.fromarray(pm[:,:,i].astype(np.float32),'F').resize((nw,nh),Image.LANCZOS)) for i in range(4)]
    o=np.stack(ch,2); A=np.clip(o[:,:,3],0,255)
    rgb=np.where(A[:,:,None]>1.0,o[:,:,:3]/np.maximum(A[:,:,None]/255.0,1e-3),0)
    out=np.dstack([np.clip(rgb,0,255),A]).astype(np.uint8)
    out[:,:,3]=np.where(out[:,:,3]<12,0,out[:,:,3])
    img=Image.fromarray(out,'RGBA'); img=img.crop(img.getbbox()); img.save(OUT+k+'.png',optimize=True)
    W,H=img.size; m=np.array(img)[:,:,3]>128
    gx=round(W*gr); col=np.nonzero(m[:,gx])[0]; gy=round(col.mean()) if len(col) else H//2
    # WPN dùng ĐƠN VỊ GAME (ảnh/HR): [dài,cao,gripX,gripY,dài lưỡi]
    res[k]=[round(W/HR,1),round(H/HR,1),round(gx/HR,1),round(gy/HR,1),round(W/HR*0.8)]; print(k,round(ang,1),(W,H),'grip',gx,gy)
print(json.dumps(res))
