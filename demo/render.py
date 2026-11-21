import math
from pathlib import Path
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W,H,FPS=1100,610,60
P=3
folder=str(Path(__file__).resolve().parent)
sheet=Image.open(Path(folder).parent/'game'/'assets'/'hero_nu.png').convert('RGBA')
body=sheet.crop((1320,111,1485,222))
cut=Image.new('L',body.size)
ImageDraw.Draw(cut).polygon([(83,41),(91,46),(112,49),(124,61),(117,67),(108,66),(101,62),(91,60),(86,58),(80,53)],fill=255)
body.paste((0,0,0,0),mask=cut)
body=body.resize((165*P,111*P),Image.Resampling.LANCZOS)
fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans'
def font(n,bold=False):
    return ImageFont.truetype(fontpath+('-Bold' if bold else '')+'.ttf',n)
fonts=[font(34,True),font(19),font(20,True),font(16),font(22,True)]
stage=Image.new('RGB',(W,H),'#121b21')
d=ImageDraw.Draw(stage)
d.text((32,25),'Nhát C · Phá Thế',font=fonts[0],fill='#f5dfab')
d.text((33,74),'Kiếm +6 trong bản minh họa · Nhân vật nữ',font=fonts[1],fill='#abbabd')
for i,lbl in enumerate(['Tắt vệt chém','Bật vệt chém']):
    x=32+i*526
    d.rounded_rectangle((x,120,x+510,497),16,fill='#28353a',outline='#53666a')
    d.rounded_rectangle((x+16,136,x+175,173),6,fill='#19272d')
    d.text((x+26,143),lbl,font=fonts[2],fill='#e2eceb')
    d.line((x+35,479,x+480,479),fill='#405157',width=1)
d.line((32,519,1068,519),fill='#53666a')
# Seconds, horizontal displacement, torso angle, grip x/y, elbow x/y, blade angle.
keys=[
 (0,0,0,101,59,85,52,-26),
 (.13,-3,-8,93,36,88,49,-80),
 (.25,-8,-17,80,22,86,47,-151),
 (.35,-8,-17,80,20,85,46,-154),
 (.42,4,-1,98,27,87,42,-87),
 (.49,19,16,111,55,89,52,19),
 (.57,22,20,102,73,88,59,53),
 (.72,20,15,100,72,87,58,48),
 (.94,14,3,101,62,85,54,14),
 (1.16,11,0,101,59,85,52,-26),
 (1.4,11,0,101,59,85,52,-26)
]
def smooth(x): return x*x*(3-2*x)
def sample(t):
    if t>=keys[-1][0]: return keys[-1][1:]
    for a,b in zip(keys,keys[1:]):
        if a[0]<=t<b[0]:
            u=smooth((t-a[0])/(b[0]-a[0]))
            return [x+(y-x)*u for x,y in zip(a[1:],b[1:])]
    return keys[0][1:]
def warp(x,y,angle):
    a=math.radians(angle)
    return 75+(x-75)*math.cos(a)-(y-64)*math.sin(a),64+(x-75)*math.sin(a)+(y-64)*math.cos(a)
def grip_geometry(t):
    dx,_,x,y,_,_,angle=sample(t)
    a=math.radians(angle)
    return (dx+x,y), (math.cos(a),math.sin(a))
def draw_panel(im,t,left,on):
    at=(left+18,144)
    dx,tilt,hx,hy,ex,ey,angle=sample(t)
    gr,unit=grip_geometry(t)
    # Visual step with a planted trail foot and a leading foot at full extension.
    step=(smooth(min(1,max(0,(t-.36)/.15)))*(1-smooth(min(1,max(0,(t-.73)/.4)))))
    lay=Image.new('RGBA',(560,423))
    dr=ImageDraw.Draw(lay,'RGBA')
    def coords(x,y): return (round(x*P),round((y+28)*P))
    def poly(points,col,outline=None,width=1):
        dr.polygon([coords(x,y) for x,y in points],fill=col,outline=outline,width=width)
    def path(points,col,width):
        dr.line([coords(x,y) for x,y in points],fill=col,width=width,joint='curve')
    dr.ellipse((P*(51+dx),P*126,P*(96+dx+step*11),P*136),fill='#151e24')
    # Trail is derived from the same blade trajectory as the physical sword.
    if on and .415<t<.73:
        a=max(.396,t-.19)
        b=min(t,.565)
        if a<b:
            n=22
            ss=[a+(b-a)*i/n for i in range(n+1)]
            fade=max(0,1-max(0,t-.54)/.19)
            for i,(ta,tb) in enumerate(zip(ss,ss[1:])):
                ga,ua=grip_geometry(ta)
                gb,ub=grip_geometry(tb)
                pos=lambda g,v,L:(g[0]+v[0]*L,g[1]+v[1]*L)
                fa=0.25+.75*i/n
                poly([pos(ga,ua,49),pos(gb,ub,49),pos(gb,ub,31),pos(ga,ua,31)],(103,188,220,int(157*fade*fa)))
                path([pos(ga,ua,49),pos(gb,ub,49)],(220,250,255,int(245*fade*fa)),3)
    # Preserve the game sprite's appearance and deform the body around the hip.
    # A positive tilt leans forward when the upper body is above the pivot.
    trans=body.rotate(-tilt,resample=Image.Resampling.BICUBIC,center=(75*P,64*P))
    if step>.04:
        toe=75+dx+step*21
        poly([(toe-15,85),(toe-8,86),(toe-5,97),(toe+2,99),(toe+2,102),(toe-9,103),(toe-13,99)],'#34313a','#171618',2)
        path([(toe-10,99),(toe-1,99)],'#616272',3)
    lay.alpha_composite(trans,(round(dx*P),28*P))
    dr=ImageDraw.Draw(lay,'RGBA')
    sx,sy=warp(77,44,tilt)
    sx+=dx
    ex+=dx
    hx+=dx
    # Bend the same arm at the elbow and keep the hilt inside its closed hand.
    for ax,ay,bx,by,wa,wb,col,light in [
        (sx,sy,ex,ey,5.6,6.2,'#8eacc1','#c6d1cd'),
        (ex,ey,hx,hy,6.8,3.9,'#d3ccba','#f7f0dc')]:
        L=max(1,math.hypot(bx-ax,by-ay))
        nx,ny=-(by-ay)/L,(bx-ax)/L
        ar=[(ax+nx*wa,ay+ny*wa),(bx+nx*wb,by+ny*wb),(bx-nx*wb,by-ny*wb),(ax-nx*wa,ay-ny*wa)]
        poly(ar,col,'#20232e',3)
        if ax==ex and ay==ey:
            dr.ellipse([coords(ax-5.4,ay-5.4),coords(ax+5.4,ay+5.4)],fill=col)
        poly([(ax+nx*wa*.52,ay+ny*wa*.52),(bx+nx*wb*.66,by+ny*wb*.66),(bx-nx*wb*.40,by-ny*wb*.40),(ax-nx*wa*.33,ay-ny*wa*.33)],light)
    a=math.radians(angle)
    ux,uy=math.cos(a),math.sin(a)
    def sword(p): return [(hx+u*ux-v*uy,hy+u*uy+v*ux) for u,v in p]
    poly(sword([(-10,-2.4),(8,-2.4),(8,2.4),(-10,2.4)]),'#672f24','#171a22',2)
    path(sword([(-6,-1.3),(6,-1.3)]),'#b67b54',3)
    poly(sword([(7,-2.2),(38,-2.9),(48,0),(39,2.8),(7,2.15)]),'#7c98aa','#151b23',3)
    poly(sword([(8,-1.95),(38,-2.4),(46,0),(8,.15)]),'#edf9fb')
    poly(sword([(5,-5),(8,-5),(8,5),(5,5)]),'#5d8ca7','#1e2836',2)
    poly(sword([(-2.3,-2),(1,-2.4),(2.2,1.2),(1.1,3),(-2.1,2.2)]),'#f3c7a5','#473334',2)
    lay=lay.resize((476,354),Image.Resampling.LANCZOS)
    im.paste(lay,at,lay)

def render(t,slow=False):
    im=stage.copy()
    for left,on in [(32,False),(558,True)]:
        draw_panel(im,t,left,on)
    d=ImageDraw.Draw(im)
    rate='Quay chậm' if slow else 'Tốc độ thường'
    phases=['Lấy đà','Bổ xuống','Hạ kiếm','Về thế thủ']
    phase=0 if t<.38 else 1 if t<.53 else 2 if t<.78 else 3
    d.text((33,541),rate,font=fonts[4],fill='#f7dfab')
    d.text((33,573),phases[phase],font=fonts[3],fill='#e0eaea')
    for i,txt in enumerate(phases):
        x=338+i*184
        fill='#e9ca8a' if i==phase else '#496066'
        d.rounded_rectangle((x,549,x+157,554),2,fill=fill)
        d.text((x,568),txt,font=fonts[3],fill='#f7e2b8' if i==phase else '#a2b4b9')
    return im

if len(sys.argv)==1:
    picks=[.0,.29,.47,.59]
    contact=Image.new('RGB',(1100,610))
    for i,t in enumerate(picks):
        contact.paste(render(t,True).resize((550,305),Image.Resampling.LANCZOS),((i%2)*550,(i//2)*305))
    contact.save(folder+'/check.jpg',quality=96)
else:
    times=[(min(1.4,max(0,(n/FPS)%2-.28)),False) for n in range(4*FPS)]
    times+= [(min(1.4,max(0,(n/FPS-.5)*.30)),True) for n in range(6*FPS)]
    cmd=['ffmpeg','-v','error','-y','-f','rawvideo','-pixel_format','rgb24','-video_size',f'{W}x{H}','-framerate',str(FPS),'-i','-','-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',sys.argv[1]]
    with subprocess.Popen(cmd,stdin=subprocess.PIPE) as ff:
        for t,s in times:
            ff.stdin.write(render(t,s).tobytes())
        ff.stdin.close()
        sys.exit(ff.wait())
