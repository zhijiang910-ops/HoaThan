const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');const ROOT='/home/user/HoaThan/game';
(async()=>{const b=await chromium.launch();const d={...devices['iPhone 15 Pro Max']};d.viewport={width:832,height:357};d.deviceScaleFactor=1;
 const ctx=await b.newContext(d);const pg=await ctx.newPage();
 await ctx.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png'}[path.extname(f)]||'application/octet-stream'})});
 await ctx.addInitScript(()=>{localStorage.setItem('tdst',JSON.stringify({prof:{name:'Kaee',gender:'nam',weapon:'kiem',hair:0,hairC:0,lv:1,exp:0,created:1},tut:1}))});
 await pg.goto('http://game.test/');await pg.waitForTimeout(2000);
 await pg.evaluate(()=>{[...document.querySelectorAll('button')].find(x=>/Vượt Ải/.test(x.textContent)).click()});await pg.waitForTimeout(800);await pg.evaluate(()=>document.getElementById('startBtn').click());await pg.waitForTimeout(2500);
 const cdp=await ctx.newCDPSession(pg);const p0=await pg.evaluate(()=>[TDST.P.x,TDST.P.y]);
 await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:500,y:150}]});for(let i=1;i<=5;i++){await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:500+i*10,y:150}]});await pg.waitForTimeout(40)}
 await pg.waitForTimeout(400);const p1=await pg.evaluate(()=>[TDST.P.x,TDST.P.y,getComputedStyle(document.getElementById('joy')).left]);await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
 console.log('chạm giữa màn: nhân vật dịch',Math.round(p1[0]-p0[0]),'| đế cần ở',p1[2]);
 await pg.waitForTimeout(500);await pg.screenshot({path:'joy_832.png'});await b.close()})();
