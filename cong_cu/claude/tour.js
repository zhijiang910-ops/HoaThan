const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');
const ROOT=process.argv[2],OUT=process.argv[3];
(async()=>{
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:844,height:390},deviceScaleFactor:1,isMobile:true,hasTouch:true});const pg=await ctx.newPage();
 const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push('console:'+m.text())});
 await pg.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');
  if(!fs.existsSync(f))return r.fulfill({status:404,body:''});const ext=path.extname(f);r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png','.jpg':'image/jpeg','.mp3':'audio/mpeg','.ogg':'audio/ogg','.webp':'image/webp'}[ext]||'application/octet-stream'})});
 let n=0;const shot=async name=>{await pg.screenshot({path:`${OUT}/${String(n++).padStart(2,'0')}_${name}.png`})};
 await pg.goto('http://game.test/');await pg.waitForTimeout(3000);await shot('start');
 const vis=async()=>pg.evaluate(()=>[...document.querySelectorAll('button')].filter(x=>x.offsetParent&&x.getBoundingClientRect().width>0).map(x=>x.textContent.trim().slice(0,30)).slice(0,40));
 console.log('buttons1',JSON.stringify(await vis()));
 await pg.fill('input',"Thử Kiếm");await pg.click('#crGo');await pg.waitForTimeout(2000);await shot('lobby');
 console.log('buttons2',JSON.stringify(await vis()));
 await pg.locator('button',{hasText:'Vượt Ải'}).first().click();await pg.waitForTimeout(1500);await shot('vuotai');
 console.log('buttons3',JSON.stringify(await vis()));
 await shot('chonai');await pg.locator('button',{hasText:'Xuất phát'}).first().click();await pg.waitForTimeout(2000);await shot('vaoai');
 const seen=new Set();const dirs=['KeyD','KeyS','KeyA','KeyW'];
 for(let k=0;k<70;k++){
  const st=await pg.evaluate(()=>({s:TDST.G&&TDST.G.state,w:TDST.G&&TDST.G.wave,hp:TDST.P&&Math.round(TDST.P.hp),lv:TDST.G&&TDST.G.level,en:TDST.G&&TDST.G.enemies.filter(e=>!e.dead).length}));
  const bs=await vis();const key=JSON.stringify(bs);
  if(!seen.has(key)){seen.add(key);console.log(k,JSON.stringify(st),key.slice(0,400));await shot('t'+k)}
  else if(k%10==0)await shot('t'+k);
  // ưu tiên bấm nút hướng dẫn / tiếp tục / thẻ đầu
  const pref=['Bắt đầu','Đã hiểu','Tiếp tục','Thử','Hiểu rồi','Nhận','Chọn','Vào ải','Đi tiếp'];
  let clicked=false;
  for(const p of pref){const l=pg.locator('button:visible',{hasText:p}).first();if(await l.count()&&await l.isVisible().catch(()=>false)){await l.click().catch(()=>{});clicked=true;break}}
  if(!clicked){const c=pg.locator('.card:visible, .pick:visible').first();if(await c.count())await c.click().catch(()=>{})}
  const d=dirs[k%4];await pg.keyboard.down(d);await pg.waitForTimeout(900);await pg.keyboard.up(d);
  if(k%5==2){await pg.keyboard.press('KeyQ')}
  if(k%7==3){await pg.keyboard.press('Space')}
 }
 fs.writeFileSync(OUT+'/errs.json',JSON.stringify(errs));
 await b.close();
})();
