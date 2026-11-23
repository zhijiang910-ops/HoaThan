const {chromium}=require('playwright');const fs=require('fs'),path=require('path');const ROOT=process.argv[2];
(async()=>{const b=await chromium.launch();
 for(const mode of ['http','file']){
 const pg=await b.newPage({viewport:{width:844,height:390},isMobile:true,hasTouch:true});const errs=[],miss=[];
 pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push('console:'+m.text())});
 pg.on('requestfailed',r=>miss.push(r.url().slice(-60)));
 await pg.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f)){miss.push(u.pathname);return r.fulfill({status:404,body:''})}r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png','.jpg':'image/jpeg','.mp3':'audio/mpeg'}[path.extname(f)]||'application/octet-stream'})});
 await pg.goto(mode==='http'?'http://game.test/':'file://'+ROOT+'/index.html');await pg.waitForTimeout(3000);
 const st1=await pg.evaluate(()=>({create:!document.querySelector('#create').hidden,lobby:!document.querySelector('#lobby').hidden}));
 let st2=null;try{await pg.fill('input','Thu');await pg.click('#crGo');await pg.waitForTimeout(1200);await pg.locator('button',{hasText:'Vượt Ải'}).first().click();await pg.waitForTimeout(800);await pg.locator('button',{hasText:'Xuất phát'}).first().click();await pg.waitForTimeout(2000);
  st2=await pg.evaluate(()=>({state:window.TDST&&TDST.G&&TDST.G.state,t:window.TDST&&TDST.G&&TDST.G.t}))}catch(e){st2='ERR '+e.message.slice(0,150)}
 await pg.screenshot({path:`${ROOT}/../shot_${mode}.png`});
 console.log(mode,JSON.stringify(st1),JSON.stringify(st2),'errs',errs.slice(0,6),'miss',miss.slice(0,6));await pg.close()}
 await b.close()})();
