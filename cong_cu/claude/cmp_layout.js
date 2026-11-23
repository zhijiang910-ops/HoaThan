const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');
const [OUT]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
const ROOTS={cu:'/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/oldroot',moi:'/home/user/HoaThan/game'};
const PARENT=`<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><style>body{margin:0;background:#222}header{height:52px;background:#444}iframe{display:block;width:100%;height:100vh;border:0}</style><header></header><iframe src="http://game.test/"></iframe>`;
(async()=>{const b=await chromium.launch();
 for(const [mode,o] of [['thang','L'],['khung','L'],['thang','P']])for(const ver of ['cu','moi']){
  const d={...devices['iPhone 15 Pro Max']};if(o==='L')d.viewport={width:d.viewport.height,height:d.viewport.width};d.deviceScaleFactor=1;
  const ctx=await b.newContext(d);const pg=await ctx.newPage();const ROOT=ROOTS[ver];
  await ctx.route('http://parent.test/**',r=>r.fulfill({body:PARENT,contentType:'text/html'}));
  await ctx.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png'}[path.extname(f)]||'application/octet-stream'})});
  await ctx.addInitScript(()=>{try{localStorage.setItem('tdst',JSON.stringify({prof:{name:'Kaee',gender:'nam',weapon:'kiem',hair:0,hairC:0,lv:1,exp:0,created:1},tut:1}))}catch(e){}});
  await pg.goto(mode==='khung'?'http://parent.test/':'http://game.test/');await pg.waitForTimeout(2500);
  const fr=mode==='khung'?pg.frames().find(f=>f.url().startsWith('http://game.test')):pg.mainFrame();
  const tag=`${mode}_${o}_${ver}`;
  await fr.evaluate(()=>{const b=[...document.querySelectorAll('button')].find(x=>/Vượt Ải/.test(x.textContent));b&&b.click()});await pg.waitForTimeout(1200);await pg.screenshot({path:`${OUT}/${tag}_menu.png`});
  await fr.evaluate(()=>document.getElementById('startBtn').click());await pg.waitForTimeout(3000);await pg.screenshot({path:`${OUT}/${tag}_game.png`});
  console.log(tag,await fr.evaluate(()=>{const r=e=>{const x=document.querySelector(e);if(!x)return null;const q=x.getBoundingClientRect();return [Math.round(q.width),Math.round(q.height)]};return {iw:innerWidth,ih:innerHeight,vbars:r('#vbars'),bars:r('#bars'),dash:r('#dashBtn'),god:r('#godBtn'),skills:r('#skills')}}));
  await ctx.close()}
 await b.close()})();
