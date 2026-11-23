const L=require('./rec_lib');const [ROOT,OUT]=process.argv.slice(2);require('fs').mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{w:1100,h:620});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 const tr=pg.locator('#trP');if(await tr.locator('[data-t=fold]').textContent()!=='Thu gọn ▴')await tr.locator('[data-t=fold]').click();
 for(let i=0;i<5;i++){const lab=await tr.locator('[data-t=wxsel]').textContent();await tr.locator('[data-t=wxplay]').click();await pg.waitForTimeout(1800);await pg.screenshot({path:OUT+'/wx'+i+'.png'});console.log(lab);await tr.locator('[data-t=wxsel]').click();await pg.waitForTimeout(2500)}
 console.log(errs);await b.close()})();
