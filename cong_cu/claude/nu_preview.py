import sys,json
from PIL import Image,ImageDraw,ImageFont
D='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/'
s=open('/home/user/HoaThan/game/index.html',encoding='utf-8').read()
i=s.find('CHM=')+4;d=0
for n,ch in enumerate(s[i:]):
    if ch=='{':d+=1
    elif ch=='}':
        d-=1
        if d==0:end=i+n+1;break
m=json.loads(s[i:end])['hero_nu'];w,h=m['w'],m['h']
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',16)
rows=[('Gốc','/home/user/HoaThan/game/assets/hero_nu.png')]+[(n,D+'nu_mau/nu_'+k+'.png') for k,n in sys.argv[2:] and [a.split('=') for a in sys.argv[2:]] or []]
P=[('idle',0),('run',1),('run',4),('attack',1),('attack',3),('attack',6),('attack2',2),('hit',1)]
S=2;W=len(P)*w*S+120;o=Image.new('RGB',(W,len(rows)*(h*S+8)),'#5a6470');dr=ImageDraw.Draw(o)
for ri,(nm,path) in enumerate(rows):
    sh=Image.open(path).convert('RGBA');y=ri*(h*S+8);dr.text((6,y+h*S//2),nm,font=F,fill='#fff')
    for k,(an,ix) in enumerate(P):
        x0,y0=m['anims'][an]['f'][ix];c=sh.crop((x0,y0,x0+w,y0+h)).resize((w*S,h*S),Image.NEAREST);o.paste(c,(120+k*w*S,y),c)
o.save(D+sys.argv[1]);print(o.size)
