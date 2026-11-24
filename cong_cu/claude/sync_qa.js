/* Kiểm đồng bộ động tác – VFX – sát thương. node sync_qa.js <game dir> <god|kiem>
   Ghi mốc thời gian (giây): bắt đầu vung, khung chạm theo animation, lúc số sát thương hiện (quái nhận đòn), lúc VFX sáng nhất. Lệch > 60 ms = ghi chú LỆCH. */
const L=require('./rec_lib');const peaks=require('./vfx_peaks.json');const [ROOT,MODE]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:9,w:1100,h:620});
 if(MODE==='god'){await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:'wukong',fold:true,rage:false,god_on:true,forge:0,scale:1}))})}
 else await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:9,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1600);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 await pg.evaluate((m)=>{const P=TDST.P,G=TDST.GG();if(m==='god'){P.rage=100;try{TDST.tryTransform()}catch(e){}}
  G.trForge=6;for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9}const e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-70;P.y=e.y;
  window.__sq={seen:new WeakSet(),ev:[],nseen:new WeakSet()}},MODE);
 for(let k=0;k<(MODE==='god'?120:150);k++){
  await pg.evaluate((a)=>{const [pk]=a;__step(1000/60);const P=TDST.P,G=TDST.GG(),Q=window.__sq,t=G.t;
   for(const s of P.kit?P.kit.act:[])s.cd=99;if(P.kit&&P.kit.ult)P.kit.ult.cd=99;
   if(window.__sq.lastAtk!==undefined&&P.atkT>window.__sq.lastAtk+0.1){Q.ev.push({t,k:'vung',n:'god#'+(P._gN),hit:null})}window.__sq.lastAtk=P.atkT;
   if(P.swordCut&&!Q.seen.has(P.swordCut)){Q.seen.add(P.swordCut);Q.ev.push({t,k:'vung',n:P.avAnim,hit:+(t+P.swordCut.delay).toFixed(3)})}
   for(const f of G.fx)if(f.k==='sp'&&!Q.seen.has(f)){Q.seen.add(f);const pk2=pk[f.s];let pf=null;if(pk2){const f0=f.f0||0,f1=f.f1==null?pk2.n-1:f.f1;let bi=f0;for(let i=f0;i<=f1;i++)if(pk2.a[i]>pk2.a[bi])bi=i;pf=+(t+f.T*(bi-f0+0.5)/(f1-f0+1)).toFixed(3)}Q.ev.push({t,k:'vfx',n:f.s,T:f.T,pk:pf})}
   for(const n of G.nums)if(!Q.nseen.has(n)){Q.nseen.add(n);Q.ev.push({t,k:'dmg',v:n.v})}},[peaks]);}
 const ev=await pg.evaluate(()=>window.__sq.ev);
 // gộp theo từng nhát vung: tìm vfx/dmg trong cửa sổ [t-0.1,t+0.9]
 const sw=ev.filter(e=>e.k==='vung');const rows=[];
 for(const s of sw){const w=ev.filter(e=>e.t>=s.t-0.05&&e.t<=s.t+0.9);const d=w.filter(e=>e.k==='dmg').map(e=>e.t);const v=w.filter(e=>e.k==='vfx'&&e.pk!=null&&!/^hp_/.test(e.n)&&e.n!=='swhit'&&Math.abs(e.t-s.t)<0.3);
  const ref=s.hit!=null?s.hit:s.t+0.3;const dmg0=d.length?d.reduce((a,b)=>Math.abs(b-ref)<Math.abs(a-ref)?b:a):null;
  rows.push({nhat:s.n,vung:+s.t.toFixed(2),cham_anim:s.hit,dmg_dau:dmg0&&+dmg0.toFixed(2),vfx:[...new Set(v.map(x=>x.n))].join(','),dmg_sau_vung_ms:dmg0?Math.round((dmg0-s.t)*1000):null,lech_dmg_ms:dmg0&&s.hit!=null?Math.round((dmg0-s.hit)*1000):null,
   vfx_sang_sau_vung_ms:v.length?[...new Map(v.map(x=>[x.n,Math.round((x.pk-s.t)*1000)])).entries()].map(([n,ms])=>n+':'+ms).join(' '):null})}
 console.table(rows);console.log('vfx khác:',ev.filter(e=>e.k==='vfx').map(e=>e.n).filter((x,i,a)=>a.indexOf(x)===i).join(','),'errors',errs.slice(0,3));await b.close()})();
