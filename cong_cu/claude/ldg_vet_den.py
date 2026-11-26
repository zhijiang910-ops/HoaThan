# Vệt mực đen (cọ khô) đặt sau tiêu đề màn chờ -> assets/ui/loading/vet_den.webp
import sys,numpy as np
from PIL import Image,ImageFilter
rng=np.random.default_rng(11)
W,H=1800,420
m=np.zeros((H,W),np.float32)
cx,cy=W/2,H/2
for y in range(H):
    t=(y-cy)/(H*0.42)
    if abs(t)>=1:continue
    prof=(1-t*t)**0.6                       # dày giữa, mỏng mép trên/dưới
    half=W*0.47*prof
    # đầu mút cọ khô: mỗi hàng dài ngắn khác nhau, theo sợi
    jl=rng.random()**2*W*0.10; jr=rng.random()**2*W*0.13
    x0=int(cx-half+jl+ (y-cy)*0.10); x1=int(cx+half-jr+(y-cy)*0.10)
    if x1>x0: m[y,max(0,x0):min(W,x1)]=1.0
# sợi cọ: khoét vài vệt mảnh ngang để lộ nền
for _ in range(60):
    y=rng.integers(20,H-20);x=rng.integers(0,W-300);l=rng.integers(120,520)
    m[y:y+rng.integers(1,3),x:x+l]*=rng.uniform(0.2,0.65)
# nhòe mép, mép mềm theo độ dày
m=np.array(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3)))/255.0
core=np.array(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(26)))/255.0
a=np.clip(m*0.86+core*0.25,0,0.92)
rgba=np.zeros((H,W,4),np.uint8);rgba[...,:3]=(5,6,10);rgba[...,3]=(a*255).astype(np.uint8)
Image.fromarray(rgba,'RGBA').save(sys.argv[1],quality=85,method=6);print('ok')
