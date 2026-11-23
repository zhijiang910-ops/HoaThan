const L=require('./rec_lib');const fs=require('fs');
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{w:844,h:390,mobile:true,seed:false});
 await pg.fill('input','Thu');await pg.click('#crGo');await pg.waitForTimeout(1200);
 await pg.locator('button',{hasText:'Vượt Ải'}).first().click();await pg.waitForTimeout(800);
 await pg.locator('button',{hasText:'Xuất phát'}).first().click();await pg.waitForTimeout(1500);
 const D=__dirname+'/tut';fs.mkdirSync(D,{recursive:true});
 const dirs=['KeyD','KeyS','KeyA','KeyW'];
 for(let k=0;k<16;k++){
  const st=await pg.evaluate(()=>({tut:TDST.G.tut&&{s:TDST.G.tut.step,st:TDST.G.tut.started},t:+TDST.G.t.toFixed(1),hint:!document.querySelector('#tut').hidden,shade:!document.querySelector('#tutShade').hidden,txt:document.querySelector('#tutT').textContent}));
  console.log(k,JSON.stringify(st));await pg.screenshot({path:D+'/'+String(k).padStart(2,'0')+'.png'});
  if(st.shade){await pg.click('#dashBtn').catch(e=>console.log('dashclick',e.message.slice(0,80)))}
  await pg.keyboard.down(dirs[k%4]);await pg.waitForTimeout(700);await pg.keyboard.up(dirs[k%4]);
 }
 console.log(errs);await b.close()})();
