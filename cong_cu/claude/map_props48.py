"""48 vật trang trí ChatGPT (6 tấm x 8 vật, 1024x512 nền trong suốt, pixel 1:1) -> cắt từng vật, lưu game/assets/map/Dp_<mã>.png,
in JSON dòng MM. Chạy: python3 cong_cu/claude/map_props48.py  (đọc nguon/master_amgioi/chatgpt_vat48/sheet1..6.png)"""
import json
import numpy as np
from PIL import Image,ImageFilter
SRC='nguon/master_amgioi/chatgpt_vat48/';DST='game/assets/map/'
# thứ tự đọc: hàng trên trái->phải, hàng dưới trái->phải. (mã, col(tỉ lệ nửa rộng,cao) hoặc None, flat)
N={1:[('dl_ngai',(.3,.1),0),('dl_ban',(.42,.14),0),('dl_sutu',(.3,.1),0),('dl_lu',(.28,.1),0),('dl_cot',(.18,.06),0),('dl_trong',(.3,.1),0),('dl_phongbinh',(.42,.08),0),('dl_ruong',(.38,.12),0)],
2:[('ut_vac',(.34,.12),0),('ut_cuangoc',(.38,.1),0),('ut_xich',None,1),('ut_cotden',(.16,.06),0),('ut_tuongvo',(.36,.1),0),('ut_lo',(.34,.12),0),('ut_ghe',(.3,.1),0),('ut_tro',None,1)],
3:[('nk_guong',(.3,.06),0),('nk_guongvo',None,0),('nk_dai',None,1),('nk_den',(.2,.06),0),('nk_lu',(.3,.1),0),('nk_sutuvo',(.38,.12),0),('nk_gia',(.4,.08),0),('nk_cay',(.2,.05),0)],
4:[('bn_hoa',None,0),('bn_hang',(.4,.1),0),('bn_den',(.18,.06),0),('bn_dai',None,1),('bn_cay',(.18,.05),0),('bn_gia',(.4,.08),0),('bn_lu',(.3,.1),0),('bn_chau',(.4,.14),0)],
5:[('ht_den',(.14,.05),0),('ht_bia',(.3,.08),0),('ht_tre',None,0),('ht_hu',(.34,.1),0),('ht_mieu',(.38,.1),0),('ht_xe',(.34,.1),0),('ht_gia',(.4,.08),0),('ht_da',(.38,.12),0)],
6:[('lh_sutu',(.32,.1),0),('lh_den',(.3,.1),0),('lh_tru',(.3,.08),0),('lh_lu',(.3,.1),0),('lh_tuong',(.4,.1),0),('lh_chuong',(.38,.06),0),('lh_cay',(.16,.05),0),('lh_long',(.2,.04),0)]}
def comps(al):
    h,w=al.shape;m=np.array(Image.fromarray((al*255).astype('uint8')).filter(ImageFilter.MaxFilter(15)))>0
    lab=np.zeros((h,w),int);n=0
    for y in range(h):
        for x in range(w):
            if m[y,x] and not lab[y,x]:
                n+=1;st=[(y,x)];lab[y,x]=n
                while st:
                    cy,cx=st.pop()
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=cy+dy,cx+dx
                        if 0<=ny<h and 0<=nx<w and m[ny,nx] and not lab[ny,nx]:lab[ny,nx]=n;st.append((ny,nx))
    return lab,n
MM={}
for k,names in N.items():
    im=Image.open(SRC+f'sheet{k}.png').convert('RGBA');a=np.array(im)
    lab,n=comps(a[:,:,3]>10)
    if n!=8:print('CẢNH BÁO sheet',k,'có',n,'vật')
    objs=[]
    for i in range(1,n+1):
        ys,xs=np.where((lab==i)&(a[:,:,3]>10));objs.append((ys.mean(),xs.mean(),i))
    objs.sort(key=lambda o:(o[0]>256,o[1]))
    for (cy,cx,i),(nm,col,flat) in zip(objs,names):
        sel=(lab==i)&(a[:,:,3]>10);ys,xs=np.where(sel);y0,y1,x0,x1=ys.min(),ys.max()+1,xs.min(),xs.max()+1
        sub=a[y0:y1,x0:x1].copy();sub[~sel[y0:y1,x0:x1]]=0
        sp=Image.fromarray(sub);sp.save(DST+f'Dp_{nm}.png');w,h=sp.size
        e={'src':f'assets/map/Dp_{nm}.png','w':w,'h':h,'ax':w//2,'ay':h-2,'col':[-round(w*col[0]),-round(h*col[1]),round(w*col[0]),-2] if col else None}
        if flat:e['flat']=1
        MM['Dp_'+nm]=e;print(nm,w,h)
open('/tmp/mm_dp48.json','w').write(json.dumps(MM,ensure_ascii=False))
