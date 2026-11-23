const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT,GEN]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:GEN||'nam',forge:9,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:9,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 const info=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();G.trForge=9;let e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-230;P.y=e.y;G.enemies.forEach(z=>{if(z!==e)z.x+=400});P.facing=1;for(const s of P.kit.act)s.cd=99;P.kit.ult.cd=99;P.kit.basic.cd=99;return P.kit.act.map(s=>s.def.name+':'+s.lvl)});
 fs.mkdirSync(OUT,{recursive:true});const seq=[];
 await pg.evaluate(()=>{const P=TDST.P;const u=P.kit.ult;u.lvl=Math.max(1,u.lvl);P.mp=999;const e=TDST.GG().enemies.filter(z=>!z.dead)[0];u.def.cast({x:e.x,y:e.y,dead:false},u.lvl)});
 
 for(let k=0;k<150;k++){await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;P.kit.basic.cd=99});seq.push(await pg.evaluate(()=>!!TDST.P.cutC));await pg.screenshot({path:OUT+'/f'+String(k).padStart(3,'0')+'.png',clip:{x:260,y:150,width:560,height:280}})}
 const dmg=await pg.evaluate(()=>TDST.GG().dmgDealt|0);console.log(JSON.stringify(info),'cutC frames',seq.filter(Boolean).length,'dmg',dmg,errs);await b.close()})();
