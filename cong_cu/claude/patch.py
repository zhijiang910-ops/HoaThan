import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(old,new):
    global s
    n=s.count(old)
    assert n==1,(n,old[:80])
    s=s.replace(old,new)

# 1) Giữ frame gốc trước khi setSwordPoses ghi đè, dựng anim 'cutC' (6 frame: lấy đà, lướt, trượt, thu thế x3)
rep("// Pick only frames where the same visible hand grips one sword.\nfunction setSwordPoses",
"""// Nhát C Kiếm +6 · Lướt Trảm: frame lấy từ sheet gốc (trước khi setSwordPoses đổi attack/attack2).
// Thứ tự: lấy đà, lướt chém, trượt dừng, thu thế 1-2-3.
{const C_POSE={hero_nu:[['attack',1],['attack',3],['attack',5],['attack',6],['attack',7],['idle',0]],
 hero_nam:[['run',0],['run',3],['attack2',6],['attack2',7],['attack',7],['idle',0]]};
 for(const id in C_POSE){const A=CHM[id].anims;A.cutC={fps:1,f:C_POSE[id].map(([a,i])=>A[a].f[i].slice())}}}
// Pick only frames where the same visible hand grips one sword.
function setSwordPoses""")

# 2) Sheet tô xanh cho dư ảnh
rep("g.globalCompositeOperation='source-in';g.fillStyle='#fff';g.fillRect(0,0,c.width,c.height);h.flash=c;",
"g.globalCompositeOperation='source-in';g.fillStyle='#fff';g.fillRect(0,0,c.width,c.height);h.flash=c;{const t=document.createElement('canvas');t.width=c.width;t.height=c.height;const q=t.getContext('2d');q.drawImage(h.img,0,0);q.globalCompositeOperation='source-atop';q.fillStyle='rgba(134,224,240,.62)';q.fillRect(0,0,t.width,t.height);h.tint=t}")

# 3) heroFrame + drawHeroFrame
rep(" if(P.hurt>0&&!(P.av>0)&&HERO.meta.anims.hit)",
" if(P.cutC&&HERO.meta.anims.cutC)return['cutC',cutCPose(P.cutC.t).fi];\n if(P.hurt>0&&!(P.av>0)&&HERO.meta.anims.hit)")
rep("""function drawHeroFrame(c,an,fi,x,y,f,sc,flash,alpha){
 const M=HERO.meta,A=M.anims[an],fr=A.f[fi];c.save();c.imageSmoothingEnabled=false;""",
"""function drawHeroFrame(c,an,fi,x,y,f,sc,flash,alpha,tf){
 const M=HERO.meta,A=M.anims[an],fr=A.f[fi];c.save();c.imageSmoothingEnabled=false;""")
rep("""else if(an==='brake')k=-0.16}
 c.translate(Math.round(x),Math.round(y)+bob);c.scale(f*sc,sc);if(k)c.transform(1,0,-k,1,0,0);if(alpha!=null)c.globalAlpha=alpha;
 c.drawImage(flash?HERO.flash:HERO.img,""",
"""else if(an==='brake')k=-0.16}
 if(tf)k=tf.k;
 c.translate(Math.round(x),Math.round(y)+bob);c.scale(f*sc*(tf?tf.sx:1),sc*(tf?tf.sy:1));if(k)c.transform(1,0,-k,1,0,0);if(alpha!=null)c.globalAlpha=alpha;
 c.drawImage(flash?HERO.flash:tf&&tf.tint&&HERO.tint?HERO.tint:HERO.img,""")

# 4) startSwordCut rẽ sang nhát C
rep(""" const heavy=step===2,dir=step===1?-1:1;
 if(lunge)P.truyPhongT=0;""",
""" const heavy=step===2,dir=step===1?-1:1;
 if(heavy&&!target.isBrk){startCutC(angle,upgrade,basic);return}
 if(lunge)P.truyPhongT=0;""")

# 5) Logic nhát C
rep("const VAN_KIEM={range:420,radius:180,impact:58};",
r"""/* ===== Nhát C Kiếm +6 · Lướt Trảm =====
 Lấy đà (hạ người, kéo lùi) → lướt chém xuyên hàng → trượt dừng → thu thế.
 Mỗi mục tiêu trúng đúng 1 lần, gắn Phá Thế 3 giây, dừng khi gặp địa hình, vẫn nhận sát thương.
 Lướt (dash) hủy được lúc lấy đà và lúc thu thế; chạy hoặc dùng chiêu cũng cắt được thu thế. */
const CUT_C={wind:0.18,dash:0.15,slide:0.14,fin:0.30,range:160,back:8,over:11,dmg:15,width:26};
const CUT_C_T1=CUT_C.wind,CUT_C_T2=CUT_C_T1+CUT_C.dash,CUT_C_T3=CUT_C_T2+CUT_C.slide,CUT_C_T4=CUT_C_T3+CUT_C.fin;
const smooth01=x=>{x=clamp(x,0,1);return x*x*(3-2*x)},eout01=x=>{x=clamp(x,0,1);return 1-(1-x)**3};
function cutCPose(t){
 const C=CUT_C;
 if(t<CUT_C_T1){const k=smooth01(t/C.wind);return{fi:0,sx:1+0.07*k,sy:1-0.14*k,k:-0.10*k}}
 if(t<CUT_C_T2)return{fi:1,sx:1.12,sy:0.90,k:0.30};
 if(t<CUT_C_T3){const k=eout01((t-CUT_C_T2)/C.slide);return{fi:2,sx:1.12-0.12*k,sy:0.90+0.10*k,k:0.30-0.28*k}}
 return{fi:3+Math.min(2,Math.floor((t-CUT_C_T3)/C.fin*3)),sx:1,sy:1,k:0};
}
function cutCDist(t){
 const C=CUT_C;
 if(t<CUT_C_T1)return -C.back*smooth01(t/C.wind);
 if(t<CUT_C_T2)return -C.back+(C.range+C.back)*eout01((t-CUT_C_T1)/C.dash);
 if(t<CUT_C_T3)return C.range+C.over*eout01((t-CUT_C_T2)/C.slide);
 return C.range+C.over;
}
function startCutC(angle,upgrade,basic){
 P.swordCut=null;P.swordGuard=null;P.runSwing=false;P.avAlt=false;
 P.atkT=0.22;P.atkAng=angle;P.av=P.avTotal=CUT_C_T4;
 if(Math.abs(Math.cos(angle))>0.15)P.facing=Math.cos(angle)>=0?1:-1;
 sfx('sword_slash',0.18,0.05);
 P.cutC={t:0,ang:angle,upgrade,basic,d:0,stop:false,hits:new Set(),trail:null,ghosts:[],phase:0};
}
function endCutC(){
 const c=P.cutC;if(!c)return;
 P.cutC=null;P.av=0;P.atkT=0;
 if(c.trail)c.trail.T=Math.min(c.trail.T,c.trail.t+0.2);
 if(c.phase<2){c.basic.step=0}
}
// Lướt / chiêu chủ động chỉ cắt được nhát C ngoài pha lướt + trượt.
const cutCLocked=()=>!!(P.cutC&&P.cutC.t>=CUT_C_T1&&P.cutC.t<CUT_C_T3);
function segDist(px,py,x0,y0,x1,y1){const dx=x1-x0,dy=y1-y0,L=dx*dx+dy*dy;const u=L?clamp(((px-x0)*dx+(py-y0)*dy)/L,0,1):0;return Math.hypot(px-x0-dx*u,py-y0-dy*u)}
function updCutC(dt){
 const c=P.cutC,C=CUT_C,ca=Math.cos(c.ang),sa=Math.sin(c.ang);
 c.t+=dt;const t=c.t;
 if(t>=CUT_C_T4||(t>=CUT_C_T3&&P.moving)){endCutC();return}
 // vào pha lướt
 if(c.phase===0&&t>=CUT_C_T1){c.phase=1;sfx('sword_slash',0.42,0.06);
  if(!LOWFX){c.trail={k:'ctrail',x0:P.x,y0:P.y,x1:P.x,y1:P.y,T:C.dash+C.slide+0.5};fx(c.trail)}}
 const x0=P.x,y0=P.y,nd=c.stop?c.d:cutCDist(t),step=nd-c.d;
 if(step){
  P.x=clamp(P.x+ca*step,24,AW-24);P.y=clamp(P.y+sa*step,24,AH-24);solidPush(P,P.r);
  if(step>1.5&&Math.hypot(P.x-x0,P.y-y0)<step*0.45)c.stop=true; // chạm địa hình / mép ải
  c.d=nd;
 }
 if(c.trail){c.trail.x1=P.x;c.trail.y1=P.y;if(c.phase>=1&&t<CUT_C_T3)c.trail.T=Math.max(c.trail.T,c.trail.t+0.3)}
 if(c.phase>=1&&t<CUT_C_T3+0.02){
  // Chém mọi mục tiêu thân người lướt qua, mỗi mục tiêu đúng 1 lần
  const mx=(x0+P.x)/2,my=(y0+P.y)/2,half=Math.hypot(P.x-x0,P.y-y0)/2;
  for(const e of enemiesIn(mx,my,half+C.width+40)){
   if(e.dead||c.hits.has(e))continue;
   if(segDist(e.x,e.y,x0,y0,P.x,P.y)>e.r+C.width)continue;
   c.hits.add(e);
   hit(e,C.dmg*pw(),H({kb:45,stun:0.12,swordBasic:true,mark:true,pierceArmor:c.upgrade>=3?SWORD_FORGE_PIERCE:0}),e.x-ca*40,e.y-sa*40);
   if(!LOWFX)fx({k:'ccut',x:e.x,y:e.y-e.r*1.5,ang:c.ang,T:0.16});
   G.shake=Math.max(G.shake||0,3);
  }
  for(const b of G.brk||[]){if(b.dead||c.hits.has(b))continue;if(segDist(b.x,b.y-10,x0,y0,P.x,P.y)<C.width+10){c.hits.add(b);hitBrk(b)}}
 }
 // vào pha trượt: bụi, kiếm khí +9, reset chuỗi
 if(c.phase===1&&t>=CUT_C_T2){c.phase=2;
  c.basic.step=0;tutHook('cut',2);
  for(let i=0;i<(LOWFX?4:9);i++)part(P.x+ca*10+rnd(-8,8),P.y-2,-ca*rnd(20,70)+rnd(-25,25),rnd(-40,-10),rnd(0.3,0.5),rnd(5,10),'rgba(205,220,226,.55)',0);
  if(c.upgrade>=9){const x=P.x+ca*30,y=P.y+sa*30-8;
   shoot(x,y,c.ang,370,{dmg:C.dmg*pw()*.35,pierce:3,r:18,life:.26,kind:'crescent',c:'#8cecff',o:H({pierceArmor:SWORD_FORGE_PIERCE})})}
 }
 if(c.phase===2&&t>=CUT_C_T3)c.phase=3;
 if(!LOWFX&&t>CUT_C_T1-0.03&&t<CUT_C_T2+0.08){c.ghosts.push({t,x:P.x,y:P.y});if(c.ghosts.length>12)c.ghosts.shift()}
}
function drawCutC(facing){
 const c=P.cutC,t=c.t,an='cutC';
 // dư ảnh 3 lớp
 if(!LOWFX&&c.ghosts.length&&t>CUT_C_T1-0.02&&t<CUT_C_T2+0.06){
  for(const [lag,al] of [[0.075,0.10],[0.05,0.16],[0.025,0.26]]){
   let g=null;for(const q of c.ghosts)if(q.t<=t-lag)g=q;
   if(!g)continue;const ps=cutCPose(Math.max(CUT_C_T1,g.t));
   drawHeroFrame(X,an,ps.fi,g.x,g.y,facing,HERO.SC,false,al,{sx:ps.sx,sy:ps.sy,k:ps.k,tint:1});
  }
 }
 const ps=cutCPose(t);
 X.fillStyle='rgba(0,0,0,.4)';ell(P.x,P.y,15*ps.sx,5);
 const flick=P.inv>0&&P.hurt>0&&Math.floor(G.t*30)%2;
 drawHeroFrame(X,an,ps.fi,P.x,P.y,facing,HERO.SC,P.hurt>0.12,flick?0.55:1,{sx:ps.sx,sy:ps.sy,k:ps.k});
 // ánh lóe kiếm lúc lấy đà
 if(!LOWFX&&t>0.10&&t<CUT_C_T1+0.02){
  const k=(t-0.10)/(CUT_C_T1+0.02-0.10),r=3+6*Math.sin(Math.PI*k);
  const cx=P.x-24*facing,cy=P.y-(HERO.id==='hero_nu'?62:27);
  X.save();X.globalCompositeOperation='lighter';X.strokeStyle='rgba(240,255,255,.9)';X.lineWidth=1.6;
  X.beginPath();X.moveTo(cx-r,cy);X.lineTo(cx+r,cy);X.moveTo(cx,cy-r);X.lineTo(cx,cy+r);X.stroke();X.restore();
 }
}
const VAN_KIEM={range:420,radius:180,impact:58};""")

# 6) Vẽ người chơi khi đang C
rep("""  const[an,fi]=heroFrame();X.fillStyle='rgba(0,0,0,.4)';ell(P.x,P.y,15,5);""",
"""  if(P.cutC&&HERO.meta.anims.cutC&&!P.deadAt){drawCutC(P.facing);return}
  const[an,fi]=heroFrame();X.fillStyle='rgba(0,0,0,.4)';ell(P.x,P.y,15,5);""")

# 7) Di chuyển: nhát C điều khiển vị trí thay cho joystick
rep("""else{P.x+=ix*spd*dt;P.y+=iy*spd*dt}
 P.x+=P.kx*dt;""","""else if(P.cutC){if(!stun&&G.state==='play')updCutC(dt);else endCutC()}
 else{P.x+=ix*spd*dt;P.y+=iy*spd*dt}
 P.x+=P.kx*dt;""")
rep(" if(stun||G.state!=='play'){P.swordCut=null;P.swordGuard=null}",
    " if(stun||G.state!=='play'){P.swordCut=null;P.swordGuard=null;if(P.cutC)endCutC()}")

# 8) Lướt hủy lấy đà / thu thế, không hủy pha lướt chém
rep("""function dash(){
 if(!G||G.state!=='play'||G.paused||P.dashCd>0||P.transT>0||stOn('choang'))return;
""","""function dash(){
 if(!G||G.state!=='play'||G.paused||P.dashCd>0||P.transT>0||stOn('choang')||cutCLocked())return;
 if(P.cutC)endCutC();
""")

# 9) Chiêu bấm tay: chờ hết pha lướt, rồi cắt nhát C
rep(" if(P.dashT>0||P.swordCut||G.t<(P.manualLock||0))return false;\n P.manualQueue=null;",
    " if(P.dashT>0||P.swordCut||cutCLocked()||G.t<(P.manualLock||0))return false;\n if(P.cutC)endCutC();\n P.manualQueue=null;")

# 10) Các chỗ reset khác
rep("cancelSkillAim();P.manualQueue=null;P.swordCut=null;P.swordGuard=null;P.transT=0.7;",
    "cancelSkillAim();P.manualQueue=null;P.swordCut=null;P.swordGuard=null;P.cutC=null;P.transT=0.7;")
rep("cancelSkillAim();P.manualQueue=null;P.swordGuard=null;\n if(G.nextStage)",
    "cancelSkillAim();P.manualQueue=null;P.swordGuard=null;if(P.cutC)endCutC();\n if(G.nextStage)")

# 11) FX: vệt lướt + đường cắt
rep("  case'ring':{",
r"""  case'ctrail':{const fa=Math.min(1,(f.T-f.t)/0.25),dx=f.x1-f.x0,dy=f.y1-f.y0,L=Math.hypot(dx,dy);if(L<4)break;
   c.globalAlpha=fa*0.45;c.strokeStyle='rgb(150,225,240)';c.lineWidth=2;c.beginPath();c.moveTo(f.x0+dx*0.12,f.y0+dy*0.12);c.lineTo(f.x1,f.y1);c.stroke();
   c.translate(f.x0,f.y0-34);c.rotate(Math.atan2(dy,dx));
   c.globalAlpha=fa*0.5;c.fillStyle='#50c8e6';c.beginPath();c.moveTo(L*0.15,-2);c.lineTo(L+12,-5);c.lineTo(L+22,0);c.lineTo(L+12,5);c.lineTo(L*0.15,2);c.closePath();c.fill();
   c.globalAlpha=fa;c.strokeStyle='#ebffff';c.lineWidth=2;c.beginPath();c.moveTo(L*0.15,0);c.lineTo(L+16,0);c.stroke();break}
  case'ccut':{c.translate(f.x,f.y);c.rotate(f.ang-0.13);c.globalAlpha=a*0.55;c.strokeStyle='#5ad2f0';c.lineWidth=9;c.beginPath();c.moveTo(-35,0);c.lineTo(35,0);c.stroke();
   c.globalAlpha=a;c.strokeStyle='#ebffff';c.lineWidth=Math.max(1,5*a);c.beginPath();c.moveTo(-31,0);c.lineTo(31,0);c.stroke();break}
  case'ring':{""")

# 12) Dấu Phá Thế trên đầu quái (3 giây)
rep("  for(const z of G.zones)if(z.kind==='whirl'",
r"""  for(const t of G.enemies)if(!t.dead&&t.swordMarkUntil>G.t){const left=(t.swordMarkUntil-G.t)/3,x=t.x,y=t.y-t.r*3.4-(t.nm?26:10);c.save();c.fillStyle='#f2c562';c.strokeStyle='#5a3a12';c.lineWidth=1.5;c.beginPath();c.moveTo(x,y-7);c.lineTo(x+5.5,y);c.lineTo(x,y+7);c.lineTo(x-5.5,y);c.closePath();c.fill();c.stroke();c.strokeStyle='#ffe3a0';c.lineWidth=2;c.beginPath();c.arc(x,y,10,-Math.PI/2,-Math.PI/2+TAU*left);c.stroke();c.restore()}
  for(const z of G.zones)if(z.kind==='whirl'""")

open(p,'w',encoding='utf-8').write(s)
print('ok')
