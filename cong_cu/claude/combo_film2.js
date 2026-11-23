const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT,GEN]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:GEN||'nam',forge:9,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:9,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 const info=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();G.trForge=6;let e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-70;P.y=e.y;G.enemies.forEach(z=>{if(z!==e)z.x+=400});P.facing=1;for(const s of P.kit.act)s.cd=99;P.kit.ult.cd=99;return {forge:TDST.weaponForge?TDST.weaponForge():null,n:G.enemies.length,x:P.x,y:P.y}});
 fs.mkdirSync(OUT,{recursive:true});const seq=[];
 for(let k=0;k<150;k++){await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;for(const s of P.kit.act)s.cd=99;P.kit.ult.cd=99});const a=await pg.evaluate(()=>[TDST.P.av>0?TDST.P.avAnim:'-',TDST.GG().fx.filter(f=>f.k==='sp').map(f=>f.s).join('+')]);seq.push(a);await pg.screenshot({path:OUT+'/f'+String(k).padStart(3,'0')+'.png',clip:{x:380,y:170,width:340,height:240}})}
 const anims=await pg.evaluate(()=>window.__an||null);
 console.log(JSON.stringify(info),errs);const c=[];for(const [a] of seq){if(!c.length||c[c.length-1]!==a)c.push(a)}console.log(c.join(' '));fs.writeFileSync(OUT+'/seq.json',JSON.stringify(seq));await b.close()})();
