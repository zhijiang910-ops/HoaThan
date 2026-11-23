// Kiểm tra mọi màn hình ở nhiều kích thước điện thoại: nút nào lọt ra ngoài khung nhìn
const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');
const ROOT='/home/user/HoaThan/game',OUT=process.argv[2]||'devt';fs.mkdirSync(OUT,{recursive:true});
const SIZES=[['ip14_full',844,390],['ip14_safari',750,342],['ip14_claude',750,290],['ip16pm',932,340],['s23_chrome',780,300],['s23_claude',780,250],['se',667,250]];
const check=`(()=>{const H=innerHeight,W=innerWidth,bad=[];for(const b of document.querySelectorAll('button,.btn,[role=button],input,a')){const r=b.getBoundingClientRect();if(!r.width||!r.height)continue;const st=getComputedStyle(b);if(st.visibility==='hidden'||st.display==='none')continue;let p=b;let vis=true;while(p){if(p.hidden||getComputedStyle(p).display==='none'){vis=false;break}p=p.parentElement}if(!vis)continue;
 if(r.bottom>H+1||r.right>W+1||r.top<-1||r.left<-1)bad.push((b.id||b.className||b.tagName)+':'+(b.textContent||'').trim().slice(0,20)+' '+Math.round(r.top)+'-'+Math.round(r.bottom)+'/'+H)}return bad})()`;
(async()=>{const b=await chromium.launch();
 for(const [name,w,h] of SIZES){for(const fresh of [true,false]){
  const ctx=await b.newContext({viewport:{width:w,height:h},isMobile:true,hasTouch:true,deviceScaleFactor:1,userAgent:devices['iPhone 14'].userAgent});const pg=await ctx.newPage();
  await pg.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png'}[path.extname(f)]||'application/octet-stream'})});
  if(!fresh)await pg.addInitScript(()=>localStorage.setItem('tdst',JSON.stringify({prof:{name:'Thu',gender:'nam',weapon:'kiem',hair:0,hairC:0,lv:5,exp:0,created:1},tut:1})));
  await pg.goto('http://game.test/');await pg.waitForTimeout(2000);
  const tag=name+(fresh?'_moi':'_cu');await pg.screenshot({path:`${OUT}/${tag}_1.png`});
  console.log(tag,'màn 1:',JSON.stringify(await pg.evaluate(check)));
  // bấm nút chính để vào tiếp
  for(const t of ['Bước vào giang hồ','Vào trận','Chiến','Bắt đầu']){const l=pg.locator('button:visible',{hasText:t}).first();if(await l.count()){try{await l.click({timeout:1500});await pg.waitForTimeout(1500);await pg.screenshot({path:`${OUT}/${tag}_2_${t.replace(/ /g,'_')}.png`});console.log(tag,'sau',t,JSON.stringify(await pg.evaluate(check)))}catch(e){console.log(tag,'KHÔNG BẤM ĐƯỢC',t,e.message.split('\n')[0])}}}
  await ctx.close()}}
 await b.close()})();
