const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const fs=require('fs');const [ROOT,OUT,MAP]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w:1100,h:620});
 await pg.locator('#lbGo').first().click().catch(async()=>{await pg.locator('button',{hasText:'Vượt Ải'}).first().click()});
 await pg.waitForTimeout(800);
 await pg.screenshot({path:OUT+'/route.png'});
 const has=await pg.locator(`#maps [data-m="${MAP}"]`).count();console.log('map btn',has);
 if(has)await pg.locator(`#maps [data-m="${MAP}"]`).click();
 await pg.waitForTimeout(400);
 await pg.screenshot({path:OUT+'/route2.png'});
 const sb=pg.locator('#startBtn,#go,#startRun').first();
 try{await pg.locator('button',{hasText:'Xuất phát'}).first().click()}catch(e){console.log('no start',e.message.slice(0,80))}
 await pg.waitForTimeout(1500);
 for(let k=0;k<240;k++)await pg.evaluate(()=>{if(window.__step)__step(1000/60)});
 await pg.screenshot({path:OUT+'/play.png'});
 console.log('errors',errs.slice(0,3));await b.close()})();
