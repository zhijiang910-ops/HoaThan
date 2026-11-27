// nghiệm thu: mở từ nút sảnh thật, chọn một món, chụp; Thụ Lộc trong khung mở, nhận 1 miếng, chụp, đóng mở lại, Trở lại
const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
const sizes=process.argv[3].split(',').map(s=>s.split('x').map(Number));
(async()=>{for(const [w,h] of sizes){const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{w,h,seed:true,dsf:+(process.env.DSF||1),mobile:!!process.env.DSF});await pg.waitForTimeout(1200);
 const tap=async sel=>{const r=await pg.evaluate(s=>{const e=document.querySelector(s);if(!e)return null;const R=e.getBoundingClientRect();return [R.left+R.width/2,R.top+R.height/2]},sel);if(!r)return 'không có '+sel;if(process.env.DSF)await pg.touchscreen.tap(r[0],r[1]);else await pg.mouse.click(r[0],r[1]);await pg.waitForTimeout(350);return 'ok'};
 await tap('#lbGrid .lbt[data-lb=inv]');await pg.waitForTimeout(600);
 const before=await pg.evaluate(()=>document.querySelector('#idet').textContent.trim().slice(0,40));
 await tap('#bag .gb.has .item');await pg.waitForTimeout(300);
 const after=await pg.evaluate(()=>({det:document.querySelector('#idet .gdn')&&document.querySelector('#idet .gdn').textContent,act:[...document.querySelectorAll('#ipAct button')].map(b=>b.textContent+(b.disabled?'(tắt)':'')).join(' | '),sel:document.querySelectorAll('#bag .gb.sel').length,lobbyVisible:!document.querySelector('#lobby').hidden}));
 await pg.screenshot({path:`${OUT}/nt_hanhnang_${w}x${h}.png`});
 console.log(w,h,'HN trước:',before,'| sau:',JSON.stringify(after),'| Trở lại:',await tap('#invBackTop'),await pg.evaluate(()=>({inv:document.querySelector('#inv').hidden,lobby:document.querySelector('#lobby').hidden})));
 await pg.evaluate(()=>{const d=new Date();d.setUTCHours(7,30,0,0);window.__TDST_NOW=d.getTime()});
 await tap('#lbGrid .lbt[data-lb=diemtam]');await pg.waitForTimeout(600);
 const st=()=>pg.evaluate(()=>({lit:document.querySelectorAll('.dtbites i.on').length,msg:document.querySelector('#dtMsg').textContent}));
 const s0=await st();await tap('#dtBun');const s1=await st();await pg.waitForTimeout(200);
 await pg.screenshot({path:`${OUT}/nt_thuloc_${w}x${h}.png`});
 await tap('#dtX');await tap('#lbGrid .lbt[data-lb=diemtam]');await pg.waitForTimeout(500);const s2=await st();
 await tap('#dtX');console.log(w,h,'TL trước',JSON.stringify(s0),'sau chạm bánh',JSON.stringify(s1),'mở lại',JSON.stringify(s2),'về sảnh',await pg.evaluate(()=>({lbm:document.querySelector('#lbm').hidden,lobby:document.querySelector('#lobby').hidden})),'lỗi',errs.length,errs.slice(0,2));
 await b.close()}process.exit(0)})();
