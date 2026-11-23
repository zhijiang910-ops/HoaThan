// Tạo dữ liệu lưu bằng bản cũ (hồ sơ + ải đang dở + kiếm +6), rồi mở bản mới với dữ liệu đó
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const [OLD,NEW]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:844,height:390},isMobile:true,hasTouch:true});
 let ROOT=OLD;const errs=[];
 await ctx.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png','.jpg':'image/jpeg','.mp3':'audio/mpeg'}[path.extname(f)]||'application/octet-stream'})});
 const pg=await ctx.newPage();pg.on('pageerror',e=>errs.push(ROOT===OLD?'OLD:'+e.message:e.message));
 await pg.goto('http://game.test/');await pg.waitForTimeout(2500);
 await pg.fill('input','Thu');await pg.click('#crGo');await pg.waitForTimeout(1000);
 await pg.locator('button',{hasText:'Vượt Ải'}).first().click();await pg.waitForTimeout(700);await pg.locator('button',{hasText:'Xuất phát'}).first().click();await pg.waitForTimeout(2500);
 await pg.evaluate(()=>{const it=JSON.parse(localStorage.getItem('tdst'));return 0});
 console.log('old save keys',await pg.evaluate(()=>Object.keys(JSON.parse(localStorage.getItem('tdst')))));
 ROOT=NEW;await pg.goto('http://game.test/');await pg.waitForTimeout(3000);
 const st=await pg.evaluate(()=>({lobby:!document.querySelector('#lobby').hidden,create:!document.querySelector('#create').hidden,cont:!document.querySelector('#lbCont').hidden}));console.log('new',JSON.stringify(st));
 await pg.screenshot({path:NEW+'/../o1.png'});
 for(const t of ['Tiếp tục ải','Vượt Ải']){try{
   if(t==='Vượt Ải'){await pg.goto('http://game.test/');await pg.waitForTimeout(2500)}
   await pg.locator('button',{hasText:t}).first().click({timeout:3000});await pg.waitForTimeout(800);
   if(t==='Vượt Ải'){await pg.locator('button',{hasText:'Xuất phát'}).first().click({timeout:3000})}
   await pg.waitForTimeout(2500);console.log(t,JSON.stringify(await pg.evaluate(()=>({state:TDST.G&&TDST.G.state,t:TDST.G&&TDST.G.t,shown:[...document.querySelectorAll('body > div,section')].filter(e=>!e.hidden&&e.offsetParent).map(e=>e.id).slice(0,8)}))))
   await pg.screenshot({path:NEW+'/../o_'+(t==='Vượt Ải'?'vuotai':'tieptuc')+'.png'});
 }catch(e){console.log(t,'ERR',e.message.slice(0,200))}}
 console.log('errs',errs.slice(0,8));await b.close()})();
