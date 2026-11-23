const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');const ROOT='/home/user/HoaThan/game';
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({...devices['iPhone 14']});const pg=await ctx.newPage();
 await ctx.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png'}[path.extname(f)]||'application/octet-stream'})});
 await pg.goto('http://game.test/');await pg.waitForTimeout(2000);
 console.log(await pg.evaluate(()=>{const i=document.getElementById('crName');return 'cỡ chữ ô tên: '+getComputedStyle(i).fontSize+' | các ô nhập <16px: '+[...document.querySelectorAll('input,select,textarea')].filter(x=>parseFloat(getComputedStyle(x).fontSize)<16).length}));
 await b.close()})();
