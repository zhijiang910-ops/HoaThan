const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1280,height:900}});const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file://'+process.argv[2]);await pg.waitForTimeout(1500);await pg.screenshot({path:process.argv[3]+'_1.png'});
 await pg.click('.sel .k');await pg.click('#tabs button:nth-child(2)');await pg.waitForTimeout(400);await pg.click('.it');await pg.screenshot({path:process.argv[3]+'_2.png'});
 await pg.click('#tabs button:nth-child(3)');await pg.waitForTimeout(400);await pg.screenshot({path:process.argv[3]+'_3.png'});
 await pg.click('#exp');await pg.waitForTimeout(300);console.log(await pg.$eval('#out',e=>e.value));
 const m=await b.newPage({viewport:{width:390,height:844},isMobile:true});await m.goto('file://'+process.argv[2]);await m.waitForTimeout(1200);await m.screenshot({path:process.argv[3]+'_m.png'});
 console.log(errs);await b.close()})();
