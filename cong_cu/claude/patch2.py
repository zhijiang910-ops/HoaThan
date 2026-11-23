import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(old,new):
    global s
    n=s.count(old); assert n==1,(n,old[:90]); s=s.replace(old,new)

# Nhịp nhanh, gắt hơn theo clip: lóe kiếm ngắn → đâm lướt → trượt → thu thế
rep("const CUT_C={wind:0.18,dash:0.15,slide:0.14,fin:0.30,range:160,back:8,over:11,dmg:15,width:26};",
    "const CUT_C={wind:0.13,dash:0.13,slide:0.12,fin:0.26,range:170,back:6,over:10,dmg:15,width:26};")
rep("if(t<CUT_C_T1){const k=smooth01(t/C.wind);return{fi:0,sx:1+0.07*k,sy:1-0.14*k,k:-0.10*k}}",
    "if(t<CUT_C_T1){const k=smooth01(t/C.wind);return{fi:0,sx:1+0.05*k,sy:1-0.10*k,k:-0.06*k}}")
rep("if(t<CUT_C_T2)return{fi:1,sx:1.12,sy:0.90,k:0.30};",
    "if(t<CUT_C_T2)return{fi:1,sx:1.16,sy:0.86,k:0.36};")
rep("if(t<CUT_C_T3){const k=eout01((t-CUT_C_T2)/C.slide);return{fi:2,sx:1.12-0.12*k,sy:0.90+0.10*k,k:0.30-0.28*k}}",
    "if(t<CUT_C_T3){const k=eout01((t-CUT_C_T2)/C.slide);return{fi:2,sx:1.16-0.16*k,sy:0.86+0.14*k,k:0.36-0.34*k}}")

# Vào pha lướt: tia kiếm trắng đâm thẳng + vệt vàng
rep("""  if(!LOWFX){c.trail={k:'ctrail',x0:P.x,y0:P.y,x1:P.x,y1:P.y,T:C.dash+C.slide+0.5};fx(c.trail)}}""",
"""  fx({k:'cbeam',x:P.x+ca*14,y:P.y-30,ang:c.ang,len:C.range+70,T:0.24});
  if(!LOWFX){c.trail={k:'ctrail',x0:P.x,y0:P.y,x1:P.x,y1:P.y,T:C.dash+C.slide+0.5};fx(c.trail)}}""")
rep("""   if(!LOWFX)fx({k:'ccut',x:e.x,y:e.y-e.r*1.5,ang:c.ang,T:0.16});
   G.shake=Math.max(G.shake||0,3);""",
"""   e.flash=Math.max(e.flash,0.14);
   fx({k:'cburst',x:e.x+ca*e.r*0.6,y:e.y-e.r*1.5,ang:c.ang,s:0.8+Math.min(0.6,e.r/40),T:0.26});
   if(!LOWFX)fx({k:'ccut',x:e.x,y:e.y-e.r*1.5,ang:c.ang,T:0.16});
   G.shake=Math.max(G.shake||0,4);""")

# Dư ảnh vàng nhạt thay xanh
rep("q.fillStyle='rgba(134,224,240,.62)'","q.fillStyle='rgba(255,214,120,.62)'")
rep("for(const [lag,al] of [[0.075,0.10],[0.05,0.16],[0.025,0.26]]){",
    "for(const [lag,al] of [[0.06,0.12],[0.04,0.18],[0.02,0.28]]){")

# Ánh lóe kiếm: to, sáng, có quầng
rep("""  const k=(t-0.10)/(CUT_C_T1+0.02-0.10),r=3+6*Math.sin(Math.PI*k);
  const cx=P.x-24*facing,cy=P.y-(HERO.id==='hero_nu'?62:27);
  X.save();X.globalCompositeOperation='lighter';X.strokeStyle='rgba(240,255,255,.9)';X.lineWidth=1.6;
  X.beginPath();X.moveTo(cx-r,cy);X.lineTo(cx+r,cy);X.moveTo(cx,cy-r);X.lineTo(cx,cy+r);X.stroke();X.restore();""",
"""  const k=(t-0.03)/(CUT_C_T1+0.02-0.03),r=4+10*Math.sin(Math.PI*k);
  const cx=P.x+14*facing,cy=P.y-30;
  X.save();X.globalCompositeOperation='lighter';
  const g=X.createRadialGradient(cx,cy,0,cx,cy,r*1.6);g.addColorStop(0,'rgba(255,255,235,.95)');g.addColorStop(0.4,'rgba(255,220,130,.55)');g.addColorStop(1,'rgba(255,200,90,0)');
  X.fillStyle=g;X.beginPath();X.arc(cx,cy,r*1.6,0,TAU);X.fill();
  X.strokeStyle='rgba(255,255,240,.95)';X.lineWidth=1.6;
  X.beginPath();X.moveTo(cx-r*1.8,cy);X.lineTo(cx+r*1.8,cy);X.moveTo(cx,cy-r);X.lineTo(cx,cy+r);X.stroke();X.restore();""")
rep("if(!LOWFX&&t>0.10&&t<CUT_C_T1+0.02){","if(!LOWFX&&t>0.03&&t<CUT_C_T1+0.02){")

# FX: vệt vàng dày, tia kiếm, nổ răng cưa cam
i=s.index("  case'ctrail':{"); j=s.index("  case'ccut':{")
s=s[:i]+r"""  case'ctrail':{const fa=Math.min(1,(f.T-f.t)/0.35),dx=f.x1-f.x0,dy=f.y1-f.y0,L=Math.hypot(dx,dy);if(L<4)break;
   c.translate(f.x0,f.y0-26);c.rotate(Math.atan2(dy,dx));
   const g=c.createLinearGradient(0,0,L,0);g.addColorStop(0,'rgba(230,170,60,0)');g.addColorStop(0.35,'rgba(235,180,70,.38)');g.addColorStop(1,'rgba(255,225,130,.75)');
   c.globalAlpha=fa;c.fillStyle=g;c.beginPath();c.moveTo(0,-4);c.lineTo(L,-13);c.quadraticCurveTo(L+10,0,L,13);c.lineTo(0,4);c.closePath();c.fill();
   c.globalAlpha=fa*0.55;c.fillStyle='rgba(255,245,200,.9)';c.fillRect(L*0.3,-1.5,L*0.7,3);
   c.globalAlpha=fa*0.35;c.strokeStyle='rgba(220,170,90,1)';c.lineWidth=3;c.beginPath();c.moveTo(L*0.2,24);c.lineTo(L,26);c.stroke();break}
  case'cbeam':{const grow=Math.min(1,f.t/0.05),fa=f.t<0.07?1:Math.max(0,1-(f.t-0.07)/(f.T-0.07)),L=f.len*grow;
   c.translate(f.x,f.y);c.rotate(f.ang);
   const g=c.createLinearGradient(0,0,L,0);g.addColorStop(0,'rgba(200,240,255,.2)');g.addColorStop(0.7,'rgba(220,250,255,.85)');g.addColorStop(1,'rgba(255,255,255,0)');
   c.globalAlpha=fa*0.6;c.fillStyle=g;c.beginPath();c.moveTo(0,-5);c.lineTo(L*0.85,-3);c.lineTo(L,0);c.lineTo(L*0.85,3);c.lineTo(0,5);c.closePath();c.fill();
   c.globalAlpha=fa;c.strokeStyle='#fff';c.lineWidth=1.8;c.beginPath();c.moveTo(4,0);c.lineTo(L*0.95,0);c.stroke();break}
  case'cburst':{const sc=f.s*(0.75+0.45*Math.min(1,k*4)),fa=k<0.55?1:1-(k-0.55)/0.45;
   c.globalCompositeOperation='source-over';c.translate(f.x,f.y);c.rotate(f.ang+0.4);c.scale(sc,sc);c.globalAlpha=fa;
   const N=11,star=(R,r)=>{c.beginPath();for(let i=0;i<N*2;i++){const q=i/(N*2)*TAU,rr=i%2?r:R*(i%4===0?1.15:0.85);c.lineTo(Math.cos(q)*rr,Math.sin(q)*rr*0.8)}c.closePath()};
   star(42,17);c.fillStyle='#ff8a1e';c.fill();c.lineWidth=3;c.strokeStyle='#c2410c';c.stroke();
   star(30,12);c.fillStyle='#ffc857';c.fill();
   star(17,7);c.fillStyle='#fff7d6';c.fill();break}
"""+s[j:]
open(p,'w',encoding='utf-8').write(s); print('ok')
