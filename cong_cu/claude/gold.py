import sys,glob,colorsys,json
from PIL import Image
R,out,mode=sys.argv[1],sys.argv[2],sys.argv[3]   # mode: gold | keep
RAMP=[(71,28,21),(129,67,28),(181,76,28),(212,127,26),(242,156,45),(249,179,34),(253,204,66),(255,236,160)]
def g(p):
    r,gg,b,a=p
    if a==0 or mode=='keep':return p
    h,l,s=colorsys.rgb_to_hls(r/255,gg/255,b/255)
    hue=h*360
    eff=(s>0.35 and (hue<14 or hue>335)) or (s>0.08 and 230<hue<335) or (l>0.86 and s<0.5)   # đỏ, tím, trắng của hiệu ứng; giữ bụi nâu
    if not eff:return p
    lum=(0.3*r+0.59*gg+0.11*b)/255
    i=min(len(RAMP)-1,int(lum*1.35*len(RAMP)))
    c=RAMP[i];return (c[0],c[1],c[2],a)
fs=sorted(glob.glob(R+'/frames/*.png'));ims=[Image.open(f).convert('RGBA') for f in fs]
bb=None
for im in ims:
    b=im.getbbox()
    if b:bb=b if bb is None else (min(bb[0],b[0]),min(bb[1],b[1]),max(bb[2],b[2]),max(bb[3],b[3]))
bb=(bb[0]-1,bb[1]-1,bb[2]+1,bb[3]+1);w,h=bb[2]-bb[0],bb[3]-bb[1]
sh=Image.new('RGBA',(w*len(ims),h))
for i,im in enumerate(ims):
    c=im.crop(bb);c.putdata([g(p) for p in c.getdata()]);sh.paste(c,(i*w,0))
sh.save(out);print(json.dumps({'w':w,'h':h,'c':len(ims),'n':len(ims),'px':160-bb[0],'py':160-bb[1]}))
