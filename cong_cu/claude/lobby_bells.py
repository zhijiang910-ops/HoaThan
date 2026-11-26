# Tách 3 quả chuông khỏi ảnh nền sảnh (GrabCut) -> sprite RGBA + nền đã lấp chỗ chuông (inpaint). Gốc 1672x941.
import cv2,numpy as np,sys
SRC='/home/user/hoathan/nguon/master_amgioi/sanh_cau_go_cong_bat_quai_goc.png';OUT='/home/user/hoathan/nguon/lobby_anim/'
im=cv2.imread(SRC)
Z=lambda pts:[(120+x/4,380+y/4) for x,y in pts]
# viền vẽ tay trên ảnh phóng 4x (gốc cắt tại 120,380): thân chuông + tua đỏ
P={'l':(Z([(206,58),(264,58),(266,100),(300,125),(315,160),(322,250),(336,292),(348,318),(344,338),(250,344),(150,342),(114,330),(120,308),(140,270),(145,200),(158,140),(190,112),(206,98)]),
      Z([(220,326),(250,326),(252,375),(262,470),(240,535),(214,490),(220,430),(226,380)]),(179,396)),
   'c':(Z([(505,140),(565,140),(572,185),(615,210),(632,260),(640,330),(655,400),(672,425),(668,445),(560,455),(430,452),(400,432),(410,410),(425,380),(432,320),(440,250),(460,215),(500,195),(506,170)]),
      Z([(520,445),(560,445),(562,520),(575,580),(552,655),(522,612),(528,540),(525,500)]),(254,416)),
   'r':(Z([(742,205),(782,205),(784,235),(810,262),(815,300),(822,345),(825,365),(745,378),(698,368),(702,345),(710,290),(722,262),(742,240)]),
      Z([(752,372),(778,372),(776,420),(785,470),(768,490),(752,455),(758,420)]),(310,433))}
full=np.zeros(im.shape[:2],np.uint8);meta={}
for k,(body,tas,piv) in P.items():
    mk=np.zeros(im.shape[:2],np.uint8)
    for poly in (body,tas):cv2.fillPoly(mk,[np.round(np.array(poly)).astype(np.int32)],1)
    full|=mk
    a=cv2.GaussianBlur(mk.astype(np.float32),(0,0),0.8)
    ys,xs=np.where(mk>0);pad=3;X0,Y0,X1,Y1=xs.min()-pad,ys.min()-pad,xs.max()+pad+1,ys.max()+pad+1
    rgba=np.dstack([im[Y0:Y1,X0:X1],(a[Y0:Y1,X0:X1]*255).astype(np.uint8)])
    cv2.imwrite(OUT+f'chuong_{k}.png',rgba);meta[k]=dict(x=int(X0),y=int(Y0),w=int(X1-X0),h=int(Y1-Y0),px=int(piv[0]-X0),py=int(piv[1]-Y0))
    print(k,meta[k])
# nền không chuông: nở mặt nạ 3 px rồi inpaint
dil=cv2.dilate(full,np.ones((5,5),np.uint8))
bgi=cv2.inpaint(im,dil*255,5,cv2.INPAINT_TELEA);cv2.imwrite(OUT+'nen_khong_chuong.png',bgi)
# xem thử
prev=np.full(im.shape,90,np.uint8)
for k in P:
    s=cv2.imread(OUT+f'chuong_{k}.png',cv2.IMREAD_UNCHANGED);m=meta[k];a=s[...,3:4]/255.0
    prev[m['y']:m['y']+m['h'],m['x']:m['x']+m['w']]=(s[...,:3]*a+prev[m['y']:m['y']+m['h'],m['x']:m['x']+m['w']]*(1-a)).astype(np.uint8)
cv2.imwrite('/tmp/claude-0/-home-user-hoathan/5b1798db-21c6-5052-8b46-d0f605bb00ba/scratchpad/bells_mask.png',cv2.resize(prev[380:570,120:350],None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC))
cv2.imwrite('/tmp/claude-0/-home-user-hoathan/5b1798db-21c6-5052-8b46-d0f605bb00ba/scratchpad/bells_bg.png',cv2.resize(bgi[380:570,120:350],None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC))
import json;json.dump(meta,open(OUT+'meta.json','w'))
