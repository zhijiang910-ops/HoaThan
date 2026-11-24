const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');const ROOT=process.argv[2]||'/home/user/HoaThan/game',OUT=process.argv[3]||'lb';fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch();
 for(const [w,h] of [[664,307],[700,310],[844,390],[932,430]]){const d={...devices['iPhone 15 Pro Max']};d.viewport={width:w,height:h};d.deviceScaleFactor=2;
  const ctx=await b.newContext(d);const pg=await ctx.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));
  await ctx.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:f.endsWith('.webp')?'image/webp':f.endsWith('.png')?'image/png':f.endsWith('.html')?'text/html':'application/octet-stream'})});
  await ctx.addInitScript(()=>{localStorage.setItem('tdst',JSON.stringify({prof:{name:'Dff',gender:'nam',avatar:1,weapon:'kiem',hair:'duoi',hairC:'den',lv:1,exp:192,created:1},gender:'nam',tut:1,sta:{v:115,t:Date.now()},cp:{star:1,next:4,ai:3,path:'trai',phase:'go'}}))});
  await pg.goto('http://game.test/');await pg.waitForTimeout(2200);
  // giả lập có ải đang dở nếu có API
  await pg.screenshot({path:`${OUT}/l_${w}x${h}.png`});console.log(w+'x'+h,errs.slice(0,2));await ctx.close()}
 await b.close()})();
