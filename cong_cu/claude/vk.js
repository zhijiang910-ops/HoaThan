const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{w:1100,h:620});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const tr=document.getElementById('trP');if(tr&&!tr.classList.contains('fold'))tr.querySelector('[data-t=fold]').click()});
 const r=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();let e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-170;P.y=e.y+20;const u=P.kit.ult;u.lvl=1;u.def.cast(e,1);return G.zones.map(z=>z.kind+':'+(z.sw?z.sw.length:0))});console.log(r);
 const box=await pg.evaluate(()=>{const c=document.querySelector('canvas').getBoundingClientRect();return [c.width,c.height]});
 for(let j=0;j<150;j++){await pg.evaluate(()=>{__step(1000/30);TDST.P.kit.basic.cd=99});if(j%5==0)await pg.screenshot({path:OUT+'/f'+String(j).padStart(3,'0')+'.png',clip:{x:150,y:60,width:800,height:440}})}
 console.log(await pg.evaluate(()=>TDST.GG().dmgDealt|0),errs);await b.close()})();
