const L=require('./rec_lib');const fs=require('fs');
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{w:844,h:390,mobile:true,seed:false});const D=__dirname+'/menu';fs.mkdirSync(D,{recursive:true});
 await pg.fill('input','Thu');await pg.click('#crGo');await pg.waitForTimeout(1200);await pg.screenshot({path:D+'/1_lobby.png'});
 console.log(await pg.evaluate(()=>JSON.stringify({eq:JSON.parse(localStorage.getItem('tdst')).eq,forge:TDST.weaponForge()})));
 await pg.locator('button',{hasText:'Vượt Ải'}).first().click();await pg.waitForTimeout(800);await pg.screenshot({path:D+'/2_menu.png'});
 await pg.locator('button',{hasText:'Xuất phát'}).first().click();await pg.waitForTimeout(1000);
 // chơi nhanh ải 1: tăng sát thương để qua ải
 await pg.evaluate(()=>{TDST.P.hp=1e6;});
 for(let k=0;k<80;k++){const st=await pg.evaluate(()=>TDST.G&&TDST.G.state);if(st&&st!=='play')break;await pg.evaluate(()=>{const G=TDST.G;if(G.tut&&G.tut.step===2)TDST.P.dashCd=0});
  if(await pg.evaluate(()=>!document.querySelector('#tutShade').hidden))await pg.click('#dashBtn').catch(()=>{});
  await pg.keyboard.down(['KeyD','KeyS','KeyA','KeyW'][k%4]);await pg.waitForTimeout(500);await pg.keyboard.up(['KeyD','KeyS','KeyA','KeyW'][k%4])}
 console.log('types',await pg.evaluate(()=>JSON.stringify({amb:TDST.G.ambush,kills:TDST.G.kills,st:TDST.G.state})));await pg.waitForTimeout(2500);await pg.screenshot({path:D+'/3_rest.png'});
 for(const t of ['Tu luyện']){const l=pg.locator('button',{hasText:t}).first();if(await l.count())await l.click().catch(()=>{})}
 await pg.waitForTimeout(500);await pg.screenshot({path:D+'/4_rest_cul.png'});
 console.log(await pg.evaluate(()=>document.querySelector('#contBtn').textContent));
 console.log(errs);await b.close()})();
