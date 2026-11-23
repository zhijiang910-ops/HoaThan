"""Nối dài lưỡi kiếm trong 1 frame về đúng độ dài master (dời mũi + lặp thân kiếm).
noikiem.py <tools_dir> <in.png> <out.png> <wx> <wy> <angle> <L>"""
import sys,math;sys.path.insert(0,sys.argv[1]);import qc,numpy as np
from PIL import Image
src,dst=sys.argv[2],sys.argv[3];w=(float(sys.argv[4]),float(sys.argv[5]));ang=float(sys.argv[6]);L=float(sys.argv[7])
A=qc.load(src);bm=qc.blade_px(A);c,ww,aa=qc.best_line(bm,w,ang,L)
a=math.radians(aa);ux,uy=math.cos(a),math.sin(a)
# chiều dài hiện tại: điểm xa nhất có điểm ảnh lưỡi kiếm sát trục
H,W=bm.shape;Lc=0
for i in range(int(L*1.3)):
    x,y=ww[0]+ux*i,ww[1]+uy*i
    xi,yi=int(round(x)),int(round(y))
    if 0<=xi<W and 0<=yi<H and bm[max(0,yi-1):yi+2,max(0,xi-1):xi+2].any():Lc=i
d=int(round(L-Lc))
print('góc',aa,'dài hiện tại',Lc,'cần',round(L),'nối thêm',d)
if d<=1:Image.fromarray(A.astype(np.uint8)).save(dst);sys.exit()
vx,vy=int(round(ux*d)),int(round(uy*d))
yy,xx=np.mgrid[0:H,0:W];px,py=xx-ww[0],yy-ww[1];t=px*ux+py*uy;dist=np.abs(-px*uy+py*ux)
op=A[...,3]>40
tipm=op&(dist<=2.6)&(t>=Lc-5)&(t<=Lc+2)
bodym=op&(dist<=2.6)&(t>=Lc-5-d)&(t<Lc-5)
out=A.copy()
def paste(mask,src_arr):
    ys,xs=np.nonzero(mask);ty,tx=ys+vy,xs+vx;ok=(ty>=0)&(ty<H)&(tx>=0)&(tx<W)
    out[ty[ok],tx[ok]]=src_arr[ys[ok],xs[ok]]
paste(bodym,A)   # thân kiếm lấp khoảng nối
paste(tipm,A)    # mũi kiếm ra vị trí mới
Image.fromarray(out.astype(np.uint8)).save(dst)
