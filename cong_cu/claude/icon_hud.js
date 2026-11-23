// Đặt thử icon pilot lên HUD thật (chỉ trong trình duyệt test, KHÔNG sửa source game). iPhone ngang 832x357, dpr 3.
const {chromium,devices}=require('playwright');const fs=require('fs'),path=require('path');const ROOT='/home/user/HoaThan/game';
const P='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/icon/03_ICON_PILOT/';const OUT='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/icon/04_HUD_COMPARISON/';
const b64=f=>'data:image/png;base64,'+fs.readFileSync(P+f+'_128.png').toString('base64');
(async()=>{const b=await chromium.launch();const d={...devices['iPhone 15 Pro Max']};d.viewport={width:832,height:357};d.deviceScaleFactor=3;
 const ctx=await b.newContext(d);const pg=await ctx.newPage();
 await ctx.route('http://game.test/**',r=>{const u=new URL(r.request().url());let f=path.join(ROOT,decodeURIComponent(u.pathname));if(u.pathname==='/')f=path.join(ROOT,'index.html');if(!fs.existsSync(f))return r.fulfill({status:404,body:''});let body=fs.readFileSync(f);if(path.extname(f)==='.html')body=body.toString().replace('window.TDST={hit,','window.TDST={GG:()=>G,hit,');r.fulfill({body,contentType:{'.html':'text/html','.png':'image/png'}[path.extname(f)]||'application/octet-stream'})});
 await ctx.addInitScript(()=>{localStorage.setItem('tdst',JSON.stringify({prof:{name:'Kaee',gender:'nam',weapon:'kiem',hair:0,hairC:0,lv:5,exp:0,created:1},tut:1}))});
 await pg.goto('http://game.test/');await pg.waitForTimeout(2000);
 await pg.evaluate(()=>{[...document.querySelectorAll('button')].find(x=>/Vượt Ải/.test(x.textContent)).click()});await pg.waitForTimeout(800);await pg.evaluate(()=>document.getElementById('startBtn').click());await pg.waitForTimeout(3000);
 await pg.evaluate(()=>{clearInterval(window.__a);});
 await pg.screenshot({path:OUT+'hud_main_TRUOC.png'});
 const icons={main:['kiem_A_khoi_kiem','kiem_B_hoi_kiem','kiem_C_pha_the_tram','phu_linh_phu'],p2:['thuong_A_xuat_thuong','quyen_A_ta_quyen','quat_phi_cham','cung_nhat_tien']};
 const M={};for(const k of [...icons.main,...icons.p2])M[k]=b64(k);M.nut='data:image/png;base64,'+fs.readFileSync(P+'hoathan_ton_ngo_khong_nut_144.png').toString('base64');
 const put=async()=>pg.evaluate(([M,icons])=>{const rows=document.querySelectorAll('#skills .skr');
   const fill=(row,list)=>{[...row.querySelectorAll('.sk')].forEach((s,i)=>{if(!list[i])return;let im=s.querySelector('img.pilot');if(!im){im=document.createElement('img');im.className='pilot';s.appendChild(im)}im.src=M[list[i]];Object.assign(im.style,{position:'absolute',inset:'0',width:'100%',height:'100%',imageRendering:'auto',zIndex:3,pointerEvents:'none'});const bb=s.querySelector('b');if(bb)bb.style.visibility='hidden'})};
   if(rows[0])fill(rows[0],icons.main);if(rows[1])fill(rows[1],icons.p2);
   const c=document.getElementById('godIcon');if(c){const g=c.getContext('2d'),i=new Image();i.onload=()=>{g.clearRect(0,0,160,160);g.drawImage(i,0,0,160,160)};i.src=M.nut}},[M,icons]);
 await put();await pg.waitForTimeout(400);await put();await pg.waitForTimeout(200);
 await pg.screenshot({path:OUT+'hud_main_SAU.png'});
 // trạng thái Hóa Thân
 await pg.evaluate(()=>{const P=TDST.P;P.rage=100;P.godCd=0});await pg.keyboard.press('KeyR');await pg.waitForTimeout(2200);
 await put();await pg.waitForTimeout(300);await put();
 await pg.screenshot({path:OUT+'hud_hoathan_SAU.png'});
 await b.close()})();
