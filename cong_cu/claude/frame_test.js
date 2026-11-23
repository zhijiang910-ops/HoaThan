const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');
const ROOT='/home/user/HoaThan/game',OUT=process.argv[2]||'frt';fs.mkdirSync(OUT,{recursive:true});
const PARENT=`<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><style>body{margin:0;background:#222}header{height:56px;background:#444;color:#fff;font:16px sans-serif;display:flex;align-items:center;padding:0 12px}iframe{display:block;width:100%;height:100vh;border:0}</style><header>claude.ai (giả lập)</header><iframe src="http://game.test/"></iframe>`;
const CASES=[['iPhone 14','L'],['iPhone 14','P'],['iPhone 15 Pro Max','L'],['iPhone 15 Pro Max','P'],['Galaxy S9+','L'],['Galaxy S9+','P']];
const vis=`(()=>{const H=innerHeight,W=innerWidth,bad=[];for(const b of document.querySelectorAll('button')){const r=b.getBoundingClientRect();if(!r.width)continue;let p=b,v=true;while(p){const cs=getComputedStyle(p);if(p.hidden||cs.display==='none'||cs.visibility==='hidden'){v=false;break}p=p.parentElement}if(!v)continue;
 if(r.bottom>H+1||r.right>W+1||r.top<-1||r.left<-1)bad.push((b.id||b.textContent.trim().slice(0,16))+'@'+[r.left,r.top,r.right,r.bottom].map(Math.round))}return bad})()`;
(async()=>{const b=await chromium.launch();
 for(const [dn,o] of CASES){for(const mode of ['khung','thang']){
  const d={...devices[dn]};if(o==='L')d.viewport={width:d.viewport.height,height:d.viewport.width};
  const ctx=await b.newContext(d);const pg=await ctx.newPage();
  await ctx.route('http://parent.test/**',r=>r.fulfill({body:PARENT,contentType:'text/html'}));
  await ctx.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});r.fulfill({body:fs.readFileSync(f),contentType:{'.html':'text/html','.png':'image/png'}[path.extname(f)]||'application/octet-stream'})});
  await pg.goto(mode==='khung'?'http://parent.test/':'http://game.test/');await pg.waitForTimeout(2500);
  const fr=mode==='khung'?pg.frames().find(f=>f.url().startsWith('http://game.test')):pg.mainFrame();
  const tag=`${dn.replace(/ /g,'')}_${o}_${mode}`;
  const info=await fr.evaluate(()=>({VIEW:{...__VIEW,vis:undefined},iw:innerWidth,ih:innerHeight}));
  await pg.screenshot({path:`${OUT}/${tag}_1.png`});
  // tìm nút chính bằng tọa độ thật trên màn hình rồi chạm vào đó (đi qua cả xoay)
  const tapText=async t=>{const el=fr.locator('button:visible',{hasText:t}).first();if(!await el.count())return 'không có';const bb=await el.boundingBox();if(!bb)return 'không thấy';
   const vp=pg.viewportSize();const cx=bb.x+bb.width/2,cy=bb.y+bb.height/2;if(cx<0||cy<0||cx>vp.width||cy>vp.height)return 'NGOÀI MÀN HÌNH '+JSON.stringify(bb);
   await pg.touchscreen.tap(cx,cy);await pg.waitForTimeout(1500);return 'ok'};
  await fr.fill('#crName','Thu');const r1=await tapText('Bước vào giang hồ');
  await pg.screenshot({path:`${OUT}/${tag}_2.png`});
  const r2=await tapText('Vượt Ải');await pg.screenshot({path:`${OUT}/${tag}_3.png`});
  const r3=await (async()=>{const el=fr.locator('#startBtn');if(!await el.count()||!await el.isVisible())return 'không có';const bb=await el.boundingBox();const vp=pg.viewportSize();const cx=bb.x+bb.width/2,cy=bb.y+bb.height/2;if(cx<0||cy<0||cx>vp.width||cy>vp.height)return 'NGOÀI '+JSON.stringify(bb);await pg.touchscreen.tap(cx,cy);await pg.waitForTimeout(2500);return 'ok'})();
  const bad=await fr.evaluate(vis);await pg.waitForTimeout(400);bad.push(await fr.evaluate(()=>{const r=id=>lrect(document.getElementById(id));const a=r('dashBtn'),b=r('vbars'),c=r('skills'),g=r('godBtn');const x=(p,q)=>p.left<q.right&&q.left<p.right&&p.top<q.bottom&&q.top<p.bottom;return [x(a,b)?'LUOT-DE-MAU':'',x(b,c)?'MAU-DE-KYNANG':'',x(g,c)?'HOATHAN-DE-KYNANG':'',x(g,b)?'HOATHAN-DE-MAU':''].filter(Boolean).join(',')||'khong de'}));await pg.screenshot({path:`${OUT}/${tag}_4.png`});
  // kéo cần: từ 1/4 trái-giữa của khung game sang phải (theo hướng khung game) 
  const V=await fr.evaluate(()=>({...__VIEW,vis:undefined}));const fo=mode==='khung'?await (await pg.$('iframe')).boundingBox():{x:0,y:0};
  const loc2scr=(x,y)=>V.on?(V.rot?[fo.x+V.L+V.W-y,fo.y+V.T+x]:[fo.x+V.L+x,fo.y+V.T+y]):[fo.x+x,fo.y+y];
  const cw=V.on?(V.rot?V.H:V.W):pg.viewportSize().width,ch=V.on?(V.rot?V.W:V.H):pg.viewportSize().height;
  const p0=await fr.evaluate(()=>TDST.P?[TDST.P.x,TDST.P.y]:null);let mv='không vào trận';
  if(p0){const cdp=await ctx.newCDPSession(pg);const jc=await fr.evaluate(()=>joyCenter());const a=loc2scr(jc[0],jc[1]),b2=loc2scr(jc[0]+45,jc[1]);
   await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:a[0],y:a[1]}]});
   for(let i=1;i<=5;i++){await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:a[0]+(b2[0]-a[0])*i/5,y:a[1]+(b2[1]-a[1])*i/5}]});await pg.waitForTimeout(40)}
   await pg.waitForTimeout(700);const p1=await fr.evaluate(()=>[TDST.P.x,TDST.P.y]);await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
   mv='dx='+Math.round(p1[0]-p0[0])+' dy='+Math.round(p1[1]-p0[1])}
  console.log(tag,JSON.stringify(info.VIEW),'vào game:',r1,'| Vượt Ải:',r2,'| Bắt đầu:',r3,'| kéo phải ->',mv,'| nút lọt:',JSON.stringify(bad));
  await ctx.close()}}
 await b.close()})();
