/* Đo thời điểm sát thương / VFX của từng chiêu. node skill_qa.js <game dir> <kiem|god> */
const L=require('./rec_lib');const peaks=require('./vfx_peaks.json');const [ROOT,MODE]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:9,w:1100,h:620});
 await pg.evaluate((m)=>{localStorage.setItem('tdst_tr',JSON.stringify(m==='god'?{god:'wukong',fold:true,rage:false,god_on:true,forge:0,scale:1}:{god:null,fold:true,rage:false,god_on:false,forge:9,scale:1}))},MODE);
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1600);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 const names=await pg.evaluate((m)=>{const P=TDST.P;if(m==='god'){P.rage=100;try{TDST.tryTransform()}catch(e){}}return m==='god'?[...P.god.def.skills.map(s=>s.name),P.god.def.ult.name]:[...P.kit.act.map(s=>s.def.id+':'+s.def.name),P.kit.ult.def.id+':'+P.kit.ult.def.name]},MODE);
 console.log(MODE,names);
 const rows=[];
 for(let si=0;si<names.length;si++){
  await pg.evaluate(()=>{for(let k=0;k<1;k++);});
  for(let k=0;k<120;k++)await pg.evaluate(()=>__step(1000/60));
  await pg.evaluate(({si,m})=>{const P=TDST.P,G=TDST.GG();for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9;x.stun=0;x.dead=false}
   const e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-150;P.y=e.y;P.facing=1;P.mp=999;P.rage=100;
   G.fx.length=0;window.__q={t0:G.t,d0:G.dmgDealt,last:G.dmgDealt,ev:[],fx:[],seen:new WeakSet()};
   if(m==='god'){const sk=si<P.god.def.skills.length?P.god.def.skills[si]:P.god.def.ult;sk.cast(e)}
   else{const list=[...P.kit.act,P.kit.ult];list[si].def.cast(e,Math.max(1,list[si].lvl||1))}},{si,m:MODE});
  for(let k=0;k<260;k++){await pg.evaluate((pk)=>{__step(1000/60);const G=TDST.GG(),Q=window.__q,t=+(G.t-Q.t0).toFixed(3);
    const P=TDST.P;if(P.kit){for(const s of P.kit.act)s.cd=99;P.kit.ult.cd=99}
    if(G.dmgDealt>Q.last+0.5){Q.ev.push([t,Math.round(G.dmgDealt-Q.last)]);Q.last=G.dmgDealt}
    for(const f of G.fx){if(f.k==='sp'&&!Q.seen.has(f)){Q.seen.add(f);const p=pk[f.s];let pf=null;if(p){const f0=f.f0||0,f1=f.f1==null?p.n-1:f.f1;let bi=f0;for(let i=f0;i<=f1;i++)if(p.a[i]>p.a[bi])bi=i;pf=+(t+f.T*(bi-f0+0.5)/(f1-f0+1)).toFixed(2)}Q.fx.push([f.s,t,pf])}}},peaks)}
  const q=await pg.evaluate(()=>window.__q);
  const first=q.ev.length?q.ev[0][0]:null;const tot=q.ev.reduce((s,x)=>s+x[1],0);
  const fxs={};for(const [n,t,pf] of q.fx){if(!fxs[n])fxs[n]=[t,pf]}
  rows.push({chieu:names[si].slice(0,28),dmg_dau:first,so_lan:q.ev.length,tong:tot,dmg_cuoi:q.ev.length?q.ev[q.ev.length-1][0]:null,vfx:Object.entries(fxs).filter(([n])=>!/^hp_|^wk_puff/.test(n)).slice(0,5).map(([n,[t,pf]])=>n+'@'+t+(pf!=null?'(sáng '+pf+')':'')).join(' ')});
 }
 console.table(rows);console.log('errors',errs.slice(0,3));await b.close()})();
