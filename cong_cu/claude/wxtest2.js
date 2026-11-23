const L=require('./rec_lib');const [ROOT,OUT,MOB]=process.argv.slice(2);require('fs').mkdirSync(OUT,{recursive:true});
(async()=>{const mob=MOB==='m';const {b,pg,errs}=await L.open(ROOT,mob?{w:844,h:390,mobile:true}:{w:1100,h:620});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{const tr=document.getElementById('trP');if(tr&&!tr.classList.contains('fold'))tr.querySelector('[data-t=fold]').click()});
 const d0=await pg.evaluate(()=>TDST.GG().dmgDealt|0);
 for(let j=0;j<5;j++){await pg.locator('#wxT button').nth(j).dispatchEvent('pointerdown');await pg.waitForTimeout(j==2?600:1900);await pg.screenshot({path:OUT+'/t'+j+'.png'});await pg.waitForTimeout(2500)}
 const d1=await pg.evaluate(()=>TDST.GG().dmgDealt|0);const cds=await pg.evaluate(()=>[...document.querySelectorAll('#wxT i')].map(i=>i.hidden?'-':i.textContent).join(','));
 console.log('dmg',d0,'->',d1,'cd',cds,errs);await b.close()})();
