#!/usr/bin/env python3
"""Kiểm cỡ quái so với nhân vật chính (chủ game 25/11: QUÁI THƯỜNG VÀ TINH ANH PHẢI NHỎ HƠN MAIN).
Main cao 106 px sprite x 0,98 (HERO.SC gốc) = ~104 px thế giới. Mini-boss và trùm được to hơn.
Chạy: python3 cong_cu/claude/size_check.py  (thoát mã 1 nếu có quái thường/Tinh Anh >= main)"""
import re,sys
from PIL import Image
S=open('game/index.html',encoding='utf-8').read()
HERO=106*0.98
esp={}
m=re.search(r"const ESPR=\{(.*?)\};",S,re.S)
for k,n,v in re.findall(r"(\w+):\['(\w+)',([0-9.]+)\]",m.group(1)):esp[k]=(n,float(v))
for k,n,v in re.findall(r"ESPR\.(\w+)=\['(\w+)',([0-9.]+)\]",S):esp[k]=(n,float(v))
for k,n,v in re.findall(r"ESPR\[k\]=\[k,([0-9.]+)\]",S):pass
et={}
for k,body in re.findall(r"\n\s*(\w+):\{(name:'[^}]*)\}",S[S.index('const ET={'):S.index('const ET={')+3000]):et[k]=body
for k,body in re.findall(r"ET\.(\w+)=\{(name:[^}]*)\}",S):et[k]=body
box={'ambinh':(0,0,187,146)}
def vh(sp):
    im=Image.open(f'game/assets/{sp}_am.png' if sp!='ambinh' else 'game/assets/ambinh.png').convert('RGBA')
    if sp in box:im=im.crop(box[sp])
    b=im.getbbox();return b[3]-b[1]
bad=0
THULINH={'tacvuong','langvuong'}  # thủ lĩnh sự kiện chặn đường (Quỷ Tướng, Ma Khuyển Vương): được to hơn main như mini-boss
print(f'main = {HERO:.0f} px')
for k,body in sorted(et.items()):
    if k not in esp:continue
    sp,sc=esp[k]
    if 'boss:1' in body or 'mini:1' in body or k in THULINH:continue
    try:h=vh(sp)*sc
    except Exception as e:continue
    ok=h<HERO
    if not ok:bad+=1
    print(f'{"OK " if ok else "LON"} {k:12s} {sp:12s} {h:5.0f} px')
sys.exit(1 if bad else 0)
