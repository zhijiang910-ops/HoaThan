# Thử NGOẠI LỆ (chủ game cho phép 24/11): vẽ thêm chi tiết bằng code lên sprite có sẵn cho Mạnh Bà, Diêm Vương, Mã Diện.
# Chỉ ảnh tĩnh (khung idle đầu tiên), chưa vào game. Chạy: python3 boss_tu_ve_thu.py <thư mục ra>
import sys,json,re
import numpy as np
from PIL import Image,ImageDraw
exec(open('/tmp/claude-0/-home-user-HoaThan/a832d12c-e51d-5bff-8200-3e97690e9294/scratchpad/recolor_prev.py').read().split("items=")[0]) if False else None
R='/home/user/HoaThan/game/'
s=open(R+'index.html',encoding='utf-8').read()
CHMd=json.loads(re.search(r'const CHM=(\{.*?\});\n',s,re.S).group(1))
def frame(n):
    if n=='quytuong':return Image.open(R+'assets/quytuong.png').convert('RGBA').crop((0,0,145,149))
    v=CHMd[n];im=Image.open(R+f'assets/{n}.png').convert('RGBA');x,y=v['anims']['idle']['f'][0];return im.crop((x,y,x+v['w'],y+v['h']))
OUT=sys.argv[1] if len(sys.argv)>1 else '.'
def lum(a):return (0.3*a[...,0]+0.59*a[...,1]+0.11*a[...,2])/255
def hsv_shift(a,h=0,sm=1,vm=1):
    import colorsys
    o=a.copy()
    ys,xs=np.nonzero(a[...,3]>0)
    for y,x in zip(ys,xs):
        r,g,b=a[y,x,:3]/255;hh,ss,vv=colorsys.rgb_to_hsv(r,g,b);hh=(hh+h)%1;ss=min(1,ss*sm);vv=min(1,vv*vm)
        o[y,x,:3]=np.array(colorsys.hsv_to_rgb(hh,ss,vv))*255
    return o
# ---------- Mạnh Bà: tóc bạc, áo xám tối, thêm muôi ----------
def manhba():
    a=np.array(frame('bachhoa')).astype(float);L=lum(a);al=a[...,3]>0
    mx=a[...,:3].max(2);mn=a[...,:3].min(2);sat=(mx-mn)/np.maximum(mx,1)
    yy,xx=np.mgrid[0:a.shape[0],0:a.shape[1]]
    hair=al&(mx<150)&(mx>38)&(sat<0.55)&(yy<95)&(xx>=66)&(xx<=109)&~((a[...,0]>a[...,2]+25)&(mx>150))
    out=a.copy()
    g=np.clip(0.55+L*1.5,0,1)  # tóc bạc, giữ độ sáng tối để còn khối
    for c,k in enumerate([205,205,215]):out[...,c]=np.where(hair,k*g*0.95,out[...,c])
    skin=al&(xx>=86)&(yy>=26)&(yy<=66)&(a[...,0]>170)&(a[...,1]>110)&(a[...,2]<185)&(a[...,0]>a[...,2]+25)
    rest=al&~hair&(mx>48)&~skin
    rr=hsv_shift(out,h=0.58,sm=0.35,vm=0.75);out=np.where(rest[...,None],rr,out)
    for c,k in enumerate([226,214,200]):out[...,c]=np.where(skin,np.minimum(255,a[...,c]*0.55+k*0.45),out[...,c])
    im=Image.fromarray(np.clip(out,0,255).astype(np.uint8))
    d=ImageDraw.Draw(im)
    # muôi: cán gỗ chéo từ tay phải lên, gáo đồng ở đầu
    d.line([(98,74),(121,52)],fill=(20,12,8,255),width=4);d.line([(98,74),(121,52)],fill=(120,82,48,255),width=2)
    d.ellipse([117,46,129,56],fill=(20,12,8,255));d.ellipse([119,48,127,54],fill=(176,134,64,255));d.ellipse([121,49,125,52],fill=(230,200,120,255))
    return im
# ---------- Diêm Vương: áo đỏ đen + mũ miện (mão có dải châu) ----------
def diemvuong():
    a=np.array(frame('quytuong')).astype(float);al=a[...,3]>0
    o=hsv_shift(a,h=-0.05,sm=1.6,vm=0.72)
    t=np.array([150,12,16])/255;m=0.42
    v=o[...,:3]/255;v=v*(1-m)+t*m*(0.35+0.65*v.max(2,keepdims=True))
    o[...,:3]=np.where(al[...,None],np.clip(v,0,1)*255,o[...,:3])
    im=Image.fromarray(o.astype(np.uint8));d=ImageDraw.Draw(im)
    K=(18,10,10,255);G=(222,176,52,255);G2=(160,118,34,255);B=(236,206,98,255)
    d.rectangle([33,34,68,40],fill=K);d.rectangle([34,35,67,39],fill=G);d.rectangle([34,38,67,39],fill=G2)   # tấm miện
    d.rectangle([40,40,62,44],fill=K);d.rectangle([41,40,61,43],fill=(60,10,14,255))                          # mũ đội
    for x in (35,40,45):d.line([(x,40),(x,50)],fill=K);d.point([(x,50)],fill=B)                                # dải châu trước
    for x in (57,62,67):d.line([(x,40),(x,50)],fill=K);d.point([(x,50)],fill=B)
    d.line([(36,36),(66,36)],fill=B)
    return im
# ---------- Mã Diện: đầu ngựa thay đầu hổ, lông nâu ----------
def madien():
    a=np.array(frame('ho')).astype(float);al=a[...,3]>0
    L=lum(a);brown=np.array([[150,102,62]],float)
    tone=np.clip(0.38+L*0.75,0,1)
    out=a.copy()
    mx=a[...,:3].max(2);mn=a[...,:3].min(2);sat=(mx-mn)/np.maximum(mx,1)
    fur=al&(sat>0.45)&(a[...,0]>a[...,2]+30)   # lông cam/đen sọc của hổ
    for c in range(3):out[...,c]=np.where(fur,brown[0,c]*tone*1.25,out[...,c])
    im=Image.fromarray(np.clip(out,0,255).astype(np.uint8))
    px=np.array(im)
    px[5:38,90:127,3]=0           # xoá đầu hổ
    im=Image.fromarray(px);d=ImageDraw.Draw(im)
    K=(24,14,10,255);F=(158,108,66,255);S=(122,80,48,255);H=(210,164,120,255);M=(44,26,18,255);M2=(70,42,26,255)
    head=[(92,16),(99,13),(112,17),(122,25),(127,31),(127,36),(120,40),(110,37),(100,36),(93,34)]
    d.polygon([(x-0,y-0) for x,y in head],fill=K)
    inner=[(93,17),(99,14),(111,18),(121,26),(125,31),(125,35),(120,38),(110,35),(101,34),(94,33)]
    d.polygon(inner,fill=F)
    d.polygon([(100,30),(110,32),(121,35),(120,38),(110,35),(101,34)],fill=S)      # bóng dưới hàm
    d.polygon([(110,19),(121,26),(124,30),(116,26)],fill=H)                          # sống mũi sáng
    d.polygon([(94,8),(99,3),(101,13),(96,14)],fill=K);d.polygon([(95,9),(99,5),(100,12)],fill=F)  # tai
    d.ellipse([105,21,109,25],fill=K);d.point([(107,22),(108,22)],fill=(240,230,200,255))          # mắt
    d.rectangle([122,29,123,31],fill=K)                                                              # lỗ mũi
    for i,(x,y) in enumerate([(90,10),(88,14),(87,19),(87,24),(88,29),(90,33)]):d.polygon([(x,y),(x+7,y-2),(x+9,y+4),(x+2,y+6)],fill=M if i%2 else M2)  # bờm
    d.polygon([(88,34),(98,33),(100,39),(90,40)],fill=F)
    return im
items=[('Mạnh Bà',frame('bachhoa'),manhba()),('Diêm Vương',frame('quytuong'),diemvuong()),('Mã Diện',frame('ho'),madien())]
Z=3;CW=190*Z//1;W=Image.new('RGBA',(6*0+len(items)*2*160,0),(0,0,0,0))
cellw,cellh=170,160;W=Image.new('RGBA',(len(items)*2*cellw,cellh*1),(54,48,52,255));dd=ImageDraw.Draw(W)
for k,(nm,b,a) in enumerate(items):
    for j,im in enumerate((b,a)):
        bb=a.getbbox() if a.getbbox() else (0,0,10,10);bb=(max(0,min(b.getbbox()[0],a.getbbox()[0])-4),max(0,min(b.getbbox()[1],a.getbbox()[1])-4),min(im.width,max(b.getbbox()[2],a.getbbox()[2])+4),min(im.height,max(b.getbbox()[3],a.getbbox()[3])+4))
        c=im.crop(bb);c=c.resize((int(c.width*1.35),int(c.height*1.35)),Image.NEAREST)
        W.alpha_composite(c,((k*2+j)*cellw+(cellw-c.width)//2,(cellh-c.height)//2))
W.convert('RGB').save(OUT+'/boss_tu_ve_thu.png')
for nm,b,a in items:a.save(OUT+'/'+nm.replace(' ','_')+'_tu_ve.png')
print('ok')
