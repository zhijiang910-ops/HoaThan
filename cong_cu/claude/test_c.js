const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const ROOT=process.argv[2],OUT=process.argv[3],GENDER=process.argv[4]||'nam';
(async()=>{
 const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1280,height:720}});
 const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push('console:'+m.text())});
 await pg.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');
  if(!fs.existsSync(f))return r.fulfill({status:404,body:''});const ext=path.extname(f);let body=fs.readFileSync(f);if(ext==='.html')body=body.toString().replace('window.TDST={hit,','window.TDST={spawnEnemy,ET:()=>ET,hit,');r.fulfill({body,contentType:{'.html':'text/html','.png':'image/png','.jpg':'image/jpeg','.js':'text/javascript','.mp3':'audio/mpeg','.ogg':'audio/ogg'}[ext]||'application/octet-stream'})});
 await pg.addInitScript(g=>{localStorage.setItem('tdst',JSON.stringify({prof:{name:'Thu',gender:g,weapon:'kiem',hair:0,hairC:0,lv:5,exp:0,created:1},inv:[{id:'sw6',slot:'vk',tier:1,st:1,name:'Kiếm',base:{dmgW:5},aff:[],forge:6}],eq:{vk:'sw6'},forgeSeen:{6:1},tut:1}))},GENDER);
 await pg.goto('http://game.test/');await pg.waitForTimeout(2500);
 await pg.evaluate(()=>TDST.newRun());await pg.waitForTimeout(1500);
 for(const txt of ['Bắt đầu di chuyển','Bỏ qua']){const l=pg.getByText(txt,{exact:false}).first();if(await l.isVisible().catch(()=>false)){await l.click();await pg.waitForTimeout(400)}}
 const st=await pg.evaluate(()=>({state:TDST.G&&TDST.G.state,forge:TDST.weaponForge(),gender:TDST.G&&TDST.G.cfg.gender}));console.log('state',JSON.stringify(st));
 await pg.evaluate(()=>{const ET=TDST.ET();const t=Object.keys(ET).find(k=>!ET[k].boss&&!ET[k].elite);for(let i=0;i<3;i++)TDST.spawnEnemy(t,100,100)});
 const info=await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;
  G.enemies=G.enemies.filter(e=>!e.dead).slice(0,3);
  P.x=1500;P.y=1100;P.hp=1e6;
  G.enemies.forEach((e,i)=>{e.x=P.x+60+i*45;e.y=P.y;e.hp=e.mhp=1e5;e.kx=e.ky=0;e.stun=999;e.boss=0});
  G.spawnAcc=-1e9;G.packT=1e9;
  const b=P.kit.basic;b.step=2;b.cd=0;window.__log=[];
  const o=setInterval(()=>{if(P.cutC)window.__log.push({t:+P.cutC.t.toFixed(3),x:+P.x.toFixed(1),hits:P.cutC.hits.size,ph:P.cutC.phase});else if(window.__log.length&&!window.__log.done){window.__log.done=1;window.__log.push({end:1,x:P.x,step:b.step,hp:G.enemies.map(e=>Math.round(e.mhp-e.hp)),mark:G.enemies.map(e=>+(e.swordMarkUntil-G.t).toFixed(2))})}},16);
  return {px:P.x,ens:G.enemies.map(e=>[Math.round(e.x),Math.round(e.y),e.r])}});
 console.log(JSON.stringify(info));
 for(let k=0;k<16;k++){await pg.screenshot({path:OUT+'_'+String(k).padStart(2,'0')+'.png',clip:{x:390,y:220,width:500,height:260}});await pg.waitForTimeout(25)}
 await pg.waitForTimeout(800);
 console.log(JSON.stringify(await pg.evaluate(()=>window.__log.filter((x,i)=>i%3==0||x.end))));
 console.log(JSON.stringify(await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;return{t:G.t,paused:G.paused,state:G.state,step:P.kit.basic.step,cd:P.kit.basic.cd,form:P.form,hp:G.enemies.map(e=>Math.round(e.mhp-e.hp)),insp:G.inspect,clr:G.clearing,tut:G.tut}})));
 console.log('errs',errs.slice(0,5));
 await b.close();
})();
