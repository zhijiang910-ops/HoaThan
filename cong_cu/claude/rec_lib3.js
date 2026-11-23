// Thư viện dựng trang game với đồng hồ ảo để chụp từng khung
const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
exports.open=async(ROOT,{gender='nam',forge=6,w=1280,h=720,mobile=false,seed=true}={})=>{
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:w,height:h},isMobile:mobile,hasTouch:mobile});const pg=await ctx.newPage();
 const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push('console:'+m.text())});
 await pg.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');
  if(!fs.existsSync(f))return r.fulfill({status:404,body:''});const ext=path.extname(f);let body=fs.readFileSync(f);if(ext==='.html')body=body.toString().replace('window.TDST={hit,','window.TDST={TIERS,TIER_OPEN,prof,profGain,rollTier,makeItem,forgeMarkup,forgeItem,spawnEnemy,ET:()=>ET,GG:()=>G,hit,');
  r.fulfill({body,contentType:{'.html':'text/html','.png':'image/png','.jpg':'image/jpeg','.mp3':'audio/mpeg','.ogg':'audio/ogg'}[ext]||'application/octet-stream'})});
 await pg.addInitScript(()=>{let vt=0;const q=[];performance.now=()=>vt;window.requestAnimationFrame=cb=>{q.push(cb);return q.length};window.cancelAnimationFrame=()=>{};
  window.__step=ms=>{vt+=ms;const cbs=q.splice(0);for(const cb of cbs)cb(vt)};window.__auto=setInterval(()=>__step(1000/60),16)});
 if(seed)await pg.addInitScript(([g,f])=>{localStorage.setItem('tdst',JSON.stringify({prof:{name:'Thu',gender:g,weapon:'kiem',hair:0,hairC:0,lv:5,exp:0,created:1},inv:[{id:'sw6',slot:'vk',tier:1,st:1,name:'Kiếm',base:{dmgW:5},aff:[],forge:f}],eq:{vk:'sw6'},forgeSeen:{6:1,9:1},tut:1}))},[gender,forge]);
 await pg.goto('http://game.test/');await pg.waitForTimeout(2500);
 return {b,pg,errs};
};
exports.startRun=async pg=>{await pg.evaluate(()=>TDST.newRun());await pg.waitForTimeout(1500)};
exports.capture=async(pg,dir,n,clip,eachFrame)=>{fs.mkdirSync(dir,{recursive:true});await pg.evaluate(()=>clearInterval(__auto));
 for(let k=0;k<n;k++){if(eachFrame)await eachFrame(k);await pg.evaluate(()=>__step(1000/60));const c=typeof clip==='function'?await clip():clip;await pg.screenshot({path:dir+'/f'+String(k).padStart(3,'0')+'.png',clip:c})}
 await pg.evaluate(()=>{window.__auto=setInterval(()=>__step(1000/60),16)})};
