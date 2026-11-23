"""Phác thảo combo Song Quyền: khung xương (không kiếm) đè lên nhân vật thật. quyen_sketch.py <rig_body.json> <outdir> <tag>"""
import sys,math
P1=sys.argv[0].replace('quyen_sketch','combopose');src=open(P1).read();src=src[:src.index('# chân: bước dài')]
exec(src)
from PIL import ImageFont
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13);Fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',17)
GUARD_N=((5,7),(10,1));GUARD_F=((4,8),(8,3))          # thủ quyền: 2 nắm tay trước ngực
PUNCH_N=((8,2),(17,1));PUNCH_F=((9,1),(19,0))         # đấm thẳng
BACKF=((-4,8),(-6,11))                                 # tay kéo về hông
STANCE=(((5,13),(9,28)),((-6,14),(-11,29)))            # tấn trước-sau
LUNGE=(((11,10),(18,27)),((-11,14),(-21,26)))
KICK=(((12,2),(26,-2)),((-5,15),(-9,30)))              # đá ngang chân gần, chân xa trụ
KNEE=(((10,1),(9,12)),((-4,15),(-8,30)))               # co gối chuẩn bị đá
UPPER_N=((7,-2),(9,-14));CROUCH=(((5,13),(10,27)),((-5,14),(-9,28)))
D=[('A · LIÊN QUYỀN (2 đấm thẳng nhanh)',[
  ('thủ quyền',pose(narm=GUARD_N,farm=GUARD_F,nleg=STANCE[0],fleg=STANCE[1])),
  ('đấm tay gần (trúng 1)',pose(dx=2,lean=3,narm=PUNCH_N,farm=GUARD_F,nleg=STANCE[0],fleg=STANCE[1],hair=2)),
  ('thu tay gần, xoay hông',pose(dx=2,lean=2,narm=GUARD_N,farm=GUARD_F,nleg=STANCE[0],fleg=STANCE[1],hair=1)),
  ('đấm tay xa mạnh (trúng 2)',pose(dx=5,dy=1,lean=5,narm=BACKF,farm=PUNCH_F,nleg=LUNGE[0],fleg=LUNGE[1],hair=3)),
  ('giữ thế',pose(dx=5,dy=1,lean=4,narm=GUARD_N,farm=((8,3),(15,3)),nleg=LUNGE[0],fleg=LUNGE[1],hair=2))],
  'Nắm đấm lóe vàng ở khung trúng. VFX: tia quyền khí ngắn trước nắm tay.'),
 ('B · TOÀN PHONG CƯỚC (đá ngang)',[
  ('= cuối đòn A',pose(dx=5,dy=1,lean=4,narm=GUARD_N,farm=((8,3),(15,3)),nleg=LUNGE[0],fleg=LUNGE[1])),
  ('co gối',pose(dx=4,dy=-1,lean=-3,narm=GUARD_N,farm=GUARD_F,nleg=KNEE[0],fleg=KNEE[1],hair=2)),
  ('ĐÁ NGANG (trúng)',pose(dx=3,dy=-2,lean=-6,narm=((4,7),(9,3)),farm=BACKF,nleg=KICK[0],fleg=KICK[1],hair=4)),
  ('thu chân',pose(dx=4,dy=0,lean=-2,narm=GUARD_N,farm=GUARD_F,nleg=KNEE[0],fleg=KNEE[1],hair=2)),
  ('đứng thủ',pose(dx=5,narm=GUARD_N,farm=GUARD_F,nleg=STANCE[0],fleg=STANCE[1]))],
  'Vệt gió hình trăng theo mũi chân. Đẩy lùi quái.'),
 ('C (+6) · LONG HỔ BẠO QUYỀN (khụy thấp → đấm móc lên, sóng chấn)',[
  ('khụy thấp, tụ lực',pose(dx=2,dy=5,lean=4,narm=BACKF,farm=((-3,9),(-2,13)),nleg=CROUCH[0],fleg=CROUCH[1])),
  ('bật lên',pose(dx=4,dy=2,lean=3,narm=GUARD_N,farm=((4,9),(10,8)),nleg=LUNGE[0],fleg=LUNGE[1],hair=2)),
  ('ĐẤM MÓC LÊN (trúng)',pose(dx=6,dy=-1,lean=2,narm=BACKF,farm=((7,-3),(10,-16)),nleg=LUNGE[0],fleg=LUNGE[1],hair=5)),
  ('giữ đỉnh',pose(dx=6,dy=-1,lean=1,narm=BACKF,farm=((6,-4),(8,-15)),nleg=LUNGE[0],fleg=LUNGE[1],hair=4)),
  ('hạ tay, thủ',pose(dx=4,narm=GUARD_N,farm=GUARD_F,nleg=STANCE[0],fleg=STANCE[1],hair=1))],
  'Cột khí vàng bùng từ nắm tay + vòng sóng chấn trên đất, đánh quanh người.')]
img=Image.open(sys.argv[1].replace('_rigB_body.json','_first.png')).convert('RGBA')
Z2=2;W=N*Z2;rows=[]
for title,fr,note in D:
  o=Image.new('RGBA',(len(fr)*W,W+56),(30,34,40,255));d=ImageDraw.Draw(o);d.text((8,6),title,fill=(255,215,120),font=Fb)
  for i,(lab,p) in enumerate(fr):
    bg=img.resize((W,W),Image.NEAREST);bg.putalpha(bg.getchannel('A').point(lambda a:a//4));o.alpha_composite(bg,(i*W,30))
    Pp={MAP.get(q['label'],q['label']):(q['x']*W+i*W,q['y']*W+30) for q in p}
    for n in names:
      if par[n] and not n.startswith('sword'):d.line([Pp[par[n]],Pp[n]],fill=(0,255,255) if n.startswith('far') else (255,80,200) if n.startswith('near') else (230,230,230),width=4)
    for w in ('near_wrist','far_wrist'):x,y=Pp[w];d.ellipse([x-6,y-6,x+6,y+6],fill=(255,210,90))
    d.text((i*W+6,W+34),lab,fill=(230,230,230),font=F)
  d.text((8,W+8),note,fill=(150,220,170),font=F) if False else None
  o2=Image.new('RGBA',(o.width,o.height+22),(30,34,40,255));o2.alpha_composite(o);ImageDraw.Draw(o2).text((8,o.height+2),note,fill=(150,220,170),font=F);rows.append(o2)
Wd=max(r.width for r in rows);out=Image.new('RGBA',(Wd,sum(r.height+8 for r in rows)),(18,18,22,255));y=0
for r in rows:out.alpha_composite(r,(0,y));y+=r.height+8
out.save(od+'/PHAC_THAO_SONG_QUYEN.png')
