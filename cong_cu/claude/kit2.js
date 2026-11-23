const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT,MOB]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
(async()=>{const mob=MOB==='m';const {b,pg,errs}=await L.open(ROOT,mob?{w:844,h:390,mobile:true}:{w:1100,h:620});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const tr=document.getElementById('trP');if(tr&&!tr.classList.contains('fold'))tr.querySelector('[data-t=fold]').click()});
 const info=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();let e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-180;P.y=e.y+30;P.facing=1;const k=P.kit;for(const s of k.act){s.lvl=Math.max(1,s.lvl);s.cd=0}P.mp=999;return {act:k.act.map(s=>s.def.name+(s.def.hotkey||'auto')),pas:k.pas.length,ult:k.ult.def.name,hud:[...document.querySelectorAll('#skills .skr')].map(r=>r.children.length)}});
 console.log(JSON.stringify(info));
 await pg.screenshot({path:OUT+'/hud.png'});
 await pg.keyboard.press('KeyF');
 for(let j=0;j<240;j++){await pg.evaluate(()=>{__step(1000/30);TDST.P.kit.basic.cd=99});if(j%6==0)await pg.screenshot({path:OUT+'/f'+String(j).padStart(3,'0')+'.png'})}
 const d=await pg.evaluate(()=>[TDST.GG().dmgDealt|0,TDST.GG().zones.map(z=>z.kind).join(',')]);console.log('dmg',d,errs);await b.close()})();
