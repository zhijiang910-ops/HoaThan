const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const [ROOT,OUT]=process.argv.slice(2);require('fs').mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:0,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9};const e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-60;P.y=e.y;P.facing=1;window.__e=e});
 let n=0;
 for(let k=0;k<720;k++){await pg.evaluate(()=>__step(1000/60));
  if(k%60===59){const r=await pg.evaluate(()=>{const G=TDST.GG(),z=G.zones.find(q=>q.kind==='blades'&&q.passive);return {hpN:TDST.P.hpN,on:z?z.sw.map(s=>s.on?Math.round(s.life*10)/10:0):null}});console.log(k+1,JSON.stringify(r))}
  if(k===300||k===420||k===560){await pg.screenshot({path:OUT+`/s${k}.png`,clip:{x:200,y:90,width:700,height:380}})}}
 console.log('errors',errs.slice(0,3));await b.close()})();
