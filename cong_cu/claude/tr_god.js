const L=require('./rec_lib');
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{gender:'nam',forge:0,w:844,h:390,mobile:true});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(2000);
 for(let i=0;i<5;i++){console.log(await pg.evaluate(()=>TDST.P.god.def.name),await pg.textContent('#trP [data-t=god]'));await pg.click('#trP [data-t=god]');await pg.waitForTimeout(1200)}
 await pg.click('#trP [data-t=hoa]');await pg.waitForTimeout(1500);console.log('form',await pg.evaluate(()=>TDST.P.form));await pg.screenshot({path:process.argv[3]});console.log(errs);await b.close()})();
