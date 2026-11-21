import math,sys,subprocess,random
from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageEnhance
from pathlib import Path

root=Path(__file__).resolve().parent
assets=root.parent/'game'/'assets'
src=(root/'render.py').read_text().split('if len(sys.argv)==1:')[0]
actor={'__file__':str(root/'render.py')}
exec(src,actor)

W,H,FPS=1260,600,48
panel_w,panel_h=584,330
floor=245
snow=Image.open(assets/'map'/'g_snow.jpg').convert('RGB')
snow=ImageEnhance.Brightness(snow.resize((650,650))).enhance(.58)
scene=snow.crop((34,106,34+panel_w,106+panel_h))
scene=Image.blend(scene,Image.new('RGB',scene.size,'#293b42'),.39)
D=ImageDraw.Draw
F=actor['font']
enemy_sheet=Image.open(assets/'daulap.png').convert('RGBA')
enemy_idle=enemy_sheet.crop((0,0,133,122)).transpose(Image.Transpose.FLIP_LEFT_RIGHT).resize((112,102),Image.Resampling.LANCZOS)
enemy_hit=enemy_sheet.crop((133*9,122,133*10,244)).transpose(Image.Transpose.FLIP_LEFT_RIGHT).resize((112,102),Image.Resampling.LANCZOS)
# Shared opening attacks, followed by the +6-only lunge.
opening=[
(0,0,0,101,59,85,52,-26),
(.10,1,-7,91,41,87,50,-73),
(.23,10,10,115,59,92,52,20),
(.32,9,6,105,68,90,55,37),
(.40,4,0,96,70,85,58,51),
(.51,10,12,112,55,91,51,-23),
(.61,9,6,104,47,89,48,-62),
(.76,0,0,101,59,85,52,-26),
(2,0,0,101,59,85,52,-26)]
lunge=[k for k in opening if k[0]<.76]+[
(.76,0,7,76,66,84,59,154),
(.88,0,17,68,69,80,60,165),
(.99,0,21,69,69,80,60,169),
(1.04,0,30,74,64,83,56,178),
(1.13,0,39,77,59,89,55,180),
(1.25,0,34,86,48,91,53,198),
(1.34,0,21,108,48,94,47,247),
(1.43,0,10,108,61,93,50,365),
(1.51,0,9,101,71,91,57,395),
(1.68,0,2,101,60,85,53,388),
(1.98,0,0,101,59,85,52,334),
(2.20,0,0,101,59,85,52,334)]
def ease(t): return actor['smooth'](max(0,min(1,t)))
def pos(t,upgrade):
    if not upgrade: return 124
    if t<1.0: return 124-16*ease((t-.76)/.21)
    if t<1.35: return 108+336*ease((t-1)/.35)
    return 444+10*ease((t-1.35)/.19)
def hero(t,upgrade):
    actor['keys']=lunge if upgrade else opening
    matte=Image.new('RGBA',(476,498))
    actor['draw_panel'](matte,t,-18,False)
    py=8 if upgrade and 1.02<t<1.36 else 0
    return matte.crop((0,144,476,498)).resize((314,234),Image.Resampling.BILINEAR),int(pos(t,upgrade)-126),py
rand=random.Random(80)
sparks=[(rand.uniform(-1,1),rand.uniform(-1,-.15),rand.uniform(20,90),rand.uniform(.6,3)) for _ in range(16)]
targets=[230,326,412]
impact_times=[1.13,1.19,1.25]
def ground_fx(v,t):
    if t<1.03 or t>1.69: return
    fx=Image.new('RGBA',v.size); d=D(fx)
    front=min(489,pos(t,True)+15)
    fade=1-ease((t-1.34)/.35)
    back=110+(front-110)*.26
    thickness=max(1,round(6*fade))
    d.polygon([(back,222),(front,201),(front+14,194),(front,211),(back,232)],fill=(56,194,223,int(142*fade)))
    d.line([(back,225),(front,203)],fill=(231,255,255,int(230*fade)),width=thickness)
    for i in range(8):
        d.line((max(back,front-26-i*23),214+i*2, min(550,front+16-i*19),211+i*2),
            fill=(139,230,251,int((170-i*14)*fade)),width=2)
    v.alpha_composite(fx)
def finish_fx(v,t):
    u=(t-1.35)/.30
    if not 0<u<1: return
    fx=Image.new('RGBA',v.size);d=D(fx)
    o=(446,205)
    angle=-155+306*ease(min(1,u*1.8))
    points=[]
    for i in range(22):
        a=math.radians(angle-96+96*i/21)
        points.append((o[0]+math.cos(a)*82,o[1]+math.sin(a)*37))
    d.line(points,fill=(83,206,240,int(210*(1-u))),width=13)
    d.line(points,fill=(229,251,255,int(255*(1-u))),width=4)
    v.alpha_composite(fx)
def combat(t,upgrade):
    v=scene.convert('RGBA')
    d=D(v)
    d.line((31,floor+4,553,floor+4),fill='#879691',width=1)
    if upgrade: ground_fx(v,t)
    for i,x in enumerate(targets):
        hits=[impact_times[i]] if upgrade else []
        if i==0: hits=[.23,.51]+hits
        prior=[h for h in hits if h<=t]
        dt=t-max(prior) if prior else 50
        impulse=max(0,1-dt/.56) if upgrade and prior and prior[-1]>1 else 0
        recoil=math.sin(min(1,dt/.26)*math.pi)*12+8*impulse
        py=round(floor-100-10*impulse)
        x=int(x+recoil)
        d=D(v)
        d.ellipse((x-21,floor-4,x+19,floor+7),fill='#39413e')
        img=enemy_idle.rotate(14*math.sin(math.pi*min(1,dt/.24)),resample=Image.Resampling.BICUBIC,center=(56,91)) if dt<.24 else enemy_idle
        if .01<dt<.09:
            img=Image.blend(img,Image.new('RGBA',img.size,'#fff0c3'),.25)
            img.putalpha(enemy_idle.getchannel('A'))
        v.alpha_composite(img,(x-56,py))
        if dt<.32:
            fx=Image.new('RGBA',v.size);d=D(fx)
            alpha=int(255*(1-dt/.32))
            x0,y0=x-2,py+52
            for vx,vy,power,size in sparks:
                cx=x0+vx*power*dt*3
                cy=y0+vy*power*dt*3
                d.line((cx,cy,cx+vx*size*5,cy+vy*size*5),fill=(255,220,142,alpha),width=2)
            d.ellipse((x0-6,y0-6,x0+6,y0+6),fill=(255,245,208,alpha))
            v.alpha_composite(fx)
    if upgrade and 1.06<t<1.40:
        for delay,alpha in ((.075,.16),(.04,.32)):
            older,x,dy=hero(t-delay,True)
            ghost_alpha=older.getchannel('A')
            older=Image.blend(older,Image.new('RGBA',older.size,'#82deef'),.62)

            older.putalpha(ghost_alpha.point(lambda px:int(px*alpha)))
            v.alpha_composite(older,(x,floor-225+dy))
    spr,x,dy=hero(t,upgrade)
    v.alpha_composite(spr,(x,floor-225+dy))
    if upgrade: finish_fx(v,t)
    return v

stage=Image.new('RGB',(W,H),'#132026')
d=D(stage)
d.text((34,23),'Phá Thế',font=F(48,True),fill='#ffe5ae')
d.text((36,88),'So sánh cùng một vị trí và cùng một cụm quái',font=F(21),fill='#b3c6c8')
for l,head,color in [(34,'DƯỚI +6   ·   Chuỗi A–B','#d4dedb'),(642,'KIẾM +6   ·   Chuỗi A–B–C','#9fe9ef')]:
    d.text((l,139),head,font=F(23,True),fill=color)
d.line((34,554,1226,554),fill='#41555c',width=1)
def render(t,rate):
    im=stage.copy()
    for i,l in enumerate((34,642)):
        combat_area=combat(t,i==1)
        im.paste(combat_area,(l,182))
    d=D(im)
    if t<.75:
        parts=['A–B · Chém tại chỗ','A–B · Chém tại chỗ']
    elif t<1.03:
        parts=['Hết chuỗi A–B','C · Hạ bộ, kéo kiếm về sau']
    elif t<1.38:
        parts=['Hai mục tiêu ngoài tầm','C · Lướt chém qua cụm quái']
    else:
        parts=['Chỉ trúng mục tiêu gần','C · Đổi vị trí, trúng cả ba mục tiêu']
    for i,l in enumerate((34,642)):
        d.text((l,521),parts[i],font=F(19,True),fill='#afe8ec' if i else '#d6dfdf')
    d.text((34,566),rate,font=F(17),fill='#b5c8cc')
    d.text((709,566),'Demo chuyển động nữ · Chờ duyệt',font=F(17),fill='#b5c8cc')
    return im
if len(sys.argv)<2:
    picks=[.86,1.21,1.39,1.59]
    still=Image.new('RGB',(1260,600))
    for i,t in enumerate(picks):
        still.paste(render(t,'Quay chậm').resize((630,300)),(i%2*630,i//2*300))
    still.save(root/'lunge-check.jpg',quality=94)
else:
    times=[(max(0,min(2.17,n/FPS-.37)),'Tốc độ thường') for n in range(3*FPS)]
    times += [(max(0,min(2.17,(n/FPS-.36)*.34)),'Quay chậm ×0,34') for n in range(7*FPS)]
    cmd=['ffmpeg','-v','error','-y','-f','rawvideo','-pixel_format','rgb24','-video_size',f'{W}x{H}','-framerate',str(FPS),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',sys.argv[1]]
    with subprocess.Popen(cmd,stdin=subprocess.PIPE) as proc:
        for t,rate in times:
            proc.stdin.write(render(t,rate).tobytes())
        proc.stdin.close()
        sys.exit(proc.wait())
