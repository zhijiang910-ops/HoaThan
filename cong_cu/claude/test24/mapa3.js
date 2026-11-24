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
 await pg.evaluate(()=>{const G=TDST.GG();for(const e of G.enemies)e.hp=e.maxhp=1e9;TDST.P.hp=TDST.P.maxhp=1e9;});
 for(const [i,pt] of [[0,[0.5,0.5]],[1,[0.25,0.3]],[2,[0.75,0.7]]]){await pg.evaluate(([fx,fy])=>{const P=TDST.P;P.x=3200*fx;P.y=2280*fy;TDST.GG().cam.x=P.x;TDST.GG().cam.y=P.y;for(const e of TDST.GG().enemies){e.x=-999;e.y=-999}},pt);for(let k=0;k<20;k++)await pg.evaluate(()=>__step(1000/60));await pg.screenshot({path:OUT+`/play${i}.png`})}
 console.log('errors',errs.slice(0,3));await b.close()})();
