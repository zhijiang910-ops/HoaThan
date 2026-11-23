import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)

# 1) Khựng hình (hitstop): thời gian trận chạy chậm 8% trong vài chục ms
rep("  if(G&&G.state==='play'&&!G.paused&&!waiting)update(dt);",
    "  if(G&&G.state==='play'&&!G.paused&&!waiting){if(G.hitstop>0){G.hitstop-=dt;update(dt*0.08)}else update(dt)}")

# 2) Số sát thương có hệ số phóng to
rep("function num(x,y,v,k){if(!SET.nums&&k!=='h'&&k!=='mpn')return;if(G.nums.length>(MOBILE?60:110))G.nums.shift();G.nums.push({x:x+rnd(-10,10),y,v,k,t:0,dx:rnd(-14,14)})}",
    "function num(x,y,v,k,sc){if(!SET.nums&&k!=='h'&&k!=='mpn')return;if(G.nums.length>(MOBILE?60:110))G.nums.shift();G.nums.push({x:x+rnd(-10,10),y,v,k,t:0,dx:rnd(-14,14),sc:sc||1})}")
rep("const base=(crit?24:n.k==='p'?19:n.k==='w'||n.k==='m'?16:15)*zs*pop;",
    "const base=(crit?24:n.k==='p'?19:n.k==='w'||n.k==='m'?16:15)*zs*pop*(n.sc||1);")
rep(" num(e.x,e.y-e.r*1.6-14,Math.round(d),crit?'c':o.t==='m'?'m':'w');\n addCombo();",
    """ num(e.x,e.y-e.r*1.6-14,Math.round(d),crit?'c':o.t==='m'?'m':'w',o.swordBasic?1+Math.min(0.45,(P.combo||0)/120)+(o.numUp||0):1);
 if(o.swordBasic&&!LOWFX&&o.cutFx&&o.cutFx.n++<3){fx({k:'ccut',x:e.x,y:e.y-e.r*1.5,ang:o.cutFx.ang+rnd(-0.35,0.35),T:0.13,wh:1});
  for(let i=0;i<4;i++){const a=o.cutFx.ang+rnd(-0.9,0.9),v=rnd(90,200);part(e.x,e.y-e.r*1.5,Math.cos(a)*v,Math.sin(a)*v-40,rnd(0.15,0.3),rnd(2,4),i%2?'#fff6d8':'#ffd27a',1)}}
 if(o.swordBasic&&o.stop)G.hitstop=Math.max(G.hitstop||0,o.stop);
 addCombo();""")

# 3) A/B: dồn bước, rung nhẹ, khựng hình, vệt chém mới
rep(""" const damage=(heavy?15:lunge?11:9)*pw();
 const color=heavy?'#fff0b2':lunge?'#8cecff':'#bfe2ff';
 arc(P.x,P.y-8,angle,(heavy?108:lunge?96:80)*Ar(),heavy?2.7:1.9,damage,
  H({kb:heavy?60:20,stun:heavy?0.10:0,swordBasic:true,mark:heavy,pierceArmor:upgrade>=3 ? SWORD_FORGE_PIERCE : 0}),color,dir);""",
""" const damage=(heavy?15:lunge?11:9)*pw();
 const color=heavy?'#fff0b2':lunge?'#8cecff':'#bfe2ff';
 const isB=step===1;
 if(!P.moving){P.kx+=Math.cos(angle)*(isB?95:70);P.ky+=Math.sin(angle)*(isB?95:70)}
 if(isB)G.shake=Math.max(G.shake||0,2);
 arc(P.x,P.y-8,angle,(heavy?108:lunge?96:80)*Ar(),heavy?2.7:1.9,damage,
  H({kb:heavy?60:isB?32:20,stun:heavy?0.10:0,swordBasic:true,mark:heavy,pierceArmor:upgrade>=3 ? SWORD_FORGE_PIERCE : 0,
   stop:isB?0.055:0.035,numUp:isB?0.12:0,cutFx:{n:0,ang:angle+(dir>0?1.2:-1.2)},sarc:isB?2:lunge?3:1}),color,dir);""")

# arc(): đòn thường kiếm dùng vệt chém vẽ tay
rep("fx({k:'arc',x,y,ang,r,sp,c,T:0.26,dir:dir||1,spr:P.kit&&P.kit.w==='kiem'&&P.form!=='god'})}",
    "if(o&&o.sarc&&P.form!=='god')fx({k:'sarc',x,y,ang,r,sp,dir:dir||1,lv:o.sarc,T:0.22});else fx({k:'arc',x,y,ang,r,sp,c,T:0.26,dir:dir||1,spr:P.kit&&P.kit.w==='kiem'&&P.form!=='god'})}")

# 4) Vẽ vệt chém: lưỡi trăng khuyết trắng sắc, viền vàng nhạt (B đậm hơn), quét nhanh rồi tan
rep("  case'ctrail':{",
r"""  case'sarc':{const sweep=eout01(Math.min(1,f.t/0.075)),fa=f.t<0.09?1:Math.max(0,1-(f.t-0.09)/(f.T-0.09)),N=18,R=f.r*1.02,W=f.r*(f.lv===2?0.42:0.34);
   const a0=f.ang-f.sp/2*f.dir,span=f.sp*f.dir*sweep,tail=Math.max(0,sweep-0.85)/0.15;
   c.translate(f.x,f.y);c.scale(1,0.78);
   const pts=(rr,wf)=>{const o=[];for(let i=0;i<=N;i++){const u=i/N,a=a0+span*(tail*0.25+u*(1-tail*0.25)),w=Math.sin(Math.PI*Math.pow(u,0.8))*W*wf;o.push([Math.cos(a)*(rr-w),Math.sin(a)*(rr-w),Math.cos(a)*rr,Math.sin(a)*rr])}return o};
   const band=(o,fill)=>{c.beginPath();o.forEach((q,i)=>i?c.lineTo(q[2],q[3]):c.moveTo(q[2],q[3]));for(let i=o.length-1;i>=0;i--)c.lineTo(o[i][0],o[i][1]);c.closePath();c.fillStyle=fill;c.fill()};
   c.globalAlpha=fa*0.35;band(pts(R*1.06,1.5),f.lv===2?'rgba(255,205,120,1)':'rgba(170,215,255,1)');
   c.globalAlpha=fa*0.95;band(pts(R,1),'#ffffff');
   c.globalAlpha=fa;c.strokeStyle=f.lv===2?'#ffd27a':'#e8f6ff';c.lineWidth=2;c.beginPath();pts(R,1).forEach((q,i)=>i?c.lineTo(q[2],q[3]):c.moveTo(q[2],q[3]));c.stroke();break}
  case'ctrail':{""")
# ccut trắng cho A/B
rep("  case'ccut':{c.translate(f.x,f.y);c.rotate(f.ang-0.13);c.globalAlpha=a*0.55;c.strokeStyle='#5ad2f0';",
    "  case'ccut':{c.translate(f.x,f.y);c.rotate(f.ang-0.13);c.globalAlpha=a*0.55;c.strokeStyle=f.wh?'#ffe2a0':'#5ad2f0';")
open(p,'w',encoding='utf-8').write(s);print('ok')
