const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:844,height:390},isMobile:true,hasTouch:true});const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(process.argv[2],decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(process.argv[2],'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png','.jpg':'image/jpeg'}[path.extname(f)]||'application/octet-stream'})});
 await pg.goto('http://game.test/#xem-hoat-anh');await pg.waitForTimeout(2500);await pg.selectOption('#avA','attack2');await pg.click('text=Chậm ×0,25');await pg.waitForTimeout(800);
 await pg.screenshot({path:process.argv[3],fullPage:true});console.log(errs);await b.close()})();
