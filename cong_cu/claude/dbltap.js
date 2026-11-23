const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');const ROOT=process.argv[2];
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({...devices['iPhone 13 landscape']});const pg=await ctx.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});
  let body=fs.readFileSync(f);if(f.endsWith('index.html'))body=body.toString().replace(/<meta name="viewport"[^>]*>/,'<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">');
  r.fulfill({body,contentType:{'.html':'text/html','.png':'image/png','.jpg':'image/jpeg','.mp3':'audio/mpeg'}[path.extname(f)]||'application/octet-stream'})});
 await pg.goto('http://game.test/');await pg.waitForTimeout(2500);
 const sc=()=>pg.evaluate(()=>visualViewport.scale);
 console.log('vp meta',await pg.evaluate(()=>document.querySelector('meta[name=viewport]').content));
 for(const [x,y] of [[400,200],[100,60],[420,330]]){await pg.touchscreen.tap(x,y);await pg.waitForTimeout(80);await pg.touchscreen.tap(x,y);await pg.waitForTimeout(700);console.log('dbl at',x,y,'scale',await sc())}
 await pg.fill('input','Thu');await pg.waitForTimeout(200);const bb=await pg.locator('#crGo').boundingBox();
 await pg.touchscreen.tap(bb.x+20,bb.y+10);await pg.waitForTimeout(80);await pg.touchscreen.tap(bb.x+20,bb.y+10);await pg.waitForTimeout(1200);
 console.log('after dbl on button scale',await sc(),'lobby',await pg.evaluate(()=>!document.querySelector('#lobby').hidden),errs);await b.close()})();
