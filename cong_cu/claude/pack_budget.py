#!/usr/bin/env python3
"""Kiểm ngân sách dung lượng theo gói. Dùng: python3 cong_cu/claude/pack_budget.py <json từ pack_dump.js>
Thoát mã 1 nếu có gói vượt ngưỡng. Ngưỡng nằm ở BUD (MB): disk = dung lượng tải, dec = ước lượng bộ nhớ sau giải nén (rộng x cao x 4)."""
import json,os,sys
from PIL import Image
G=os.path.join(os.path.dirname(__file__),'..','..','game')
BUD={'boot':(5.0,None),'map':(3.0,45),'vfx':(3.5,80),'mons_floor':(2.5,40),'mons_route':(3.5,55),'sheet':(1.5,40),'god':(1.0,25)}
cache={}
def info(src):
    if src in cache:return cache[src]
    f=os.path.join(G,src);d=0;dec=0
    if os.path.exists(f):
        d=os.path.getsize(f)
        try:
            w,h=Image.open(f).size;dec=w*h*4
        except Exception:pass
    cache[src]=(d,dec);return cache[src]
def tot(srcs):
    s=set(srcs);return sum(info(x)[0] for x in s)/1048576,sum(info(x)[1] for x in s)/1048576,len(s)
P=json.load(open(sys.argv[1]));bad=[];rows=[]
def add(kind,name,srcs):
    d,dec,n=tot(srcs);bd,bm=BUD[kind];ok=d<=bd and (bm is None or dec<=bm)
    rows.append((kind,name,n,d,dec,bd,bm,ok))
    if not ok:bad.append(f'{kind}:{name}')
boot=[x[0] for x in P.get('boot',[])];bd=sum(x[1] for x in P.get('boot',[]))/1048576
rows.append(('boot','mở game (đo mạng)',len(boot),bd,sum(info(x)[1] for x in set(boot))/1048576,BUD['boot'][0],None,bd<=BUD['boot'][0]))
if bd>BUD['boot'][0]:bad.append('boot')
for k,v in P['maps'].items():add('map',k,v)
for k,v in P['vfx'].items():add('vfx',k,v)
for k,v in P['mons']['floors'].items():add('mons_floor','tầng '+k,v)
for k,v in P['mons']['route'].items():add('mons_route','Vượt Ải '+k,v)
for k,v in P['gods'].items():add('god',k,v)
for k,v in P['sheets'].items():
    if k.startswith('hero_'):add('sheet',k,v)
print(f'{"gói":<12}{"tên":<24}{"file":>5}{"tải MB":>9}{"giải nén MB":>13}  ngưỡng       kết quả')
for kind,name,n,d,dec,bd_,bm,ok in rows:
    print(f'{kind:<12}{name:<24}{n:>5}{d:>9.2f}{dec:>13.1f}  {bd_}MB/{bm if bm else "-"}MB  {"đạt" if ok else "VƯỢT"}')
print('\nVƯỢT NGÂN SÁCH:',', '.join(bad) if bad else 'không có');sys.exit(1 if bad else 0)
