const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{for(const [w,h] of process.argv[3].split(',').map(s=>s.split('x').map(Number))){const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{w,h,seed:true,dsf:+(process.env.DSF||1),mobile:!!process.env.DSF});await pg.waitForTimeout(1100);
 const tap=async sel=>{const r=await pg.evaluate(s=>{const e=document.querySelector(s);if(!e)return null;const R=e.getBoundingClientRect();return [R.left+R.width/2,R.top+R.height/2]},sel);if(!r)return 'không có '+sel;if(process.env.DSF)await pg.touchscreen.tap(r[0],r[1]);else await pg.mouse.click(r[0],r[1]);await pg.waitForTimeout(350);return 'ok'};
 await tap('#lbGrid .lbt[data-lb=inv]');await pg.waitForTimeout(400);await pg.evaluate(()=>{document.querySelector('#invTest').click();document.querySelector('#invTest').click()});await pg.waitForTimeout(300);
 await pg.screenshot({path:`${OUT}/v4_hn0_${w}x${h}.png`});
 await tap('#bag .gb3:nth-child(3) .item');await pg.screenshot({path:`${OUT}/v4_hn_${w}x${h}.png`});
 const nm=await pg.evaluate(()=>document.querySelector('#ipName').textContent);
 // menu trái: bấm Thụ Lộc? Hành Nang menu không có Thụ Lộc -> bấm Luyện Đan
 await tap('#ipNav [data-nav=luyendan]');await pg.waitForTimeout(500);const ld=await pg.evaluate(()=>({lbm:!document.querySelector('#lbm').hidden,t:document.querySelector('#lbmT').textContent,inv:document.querySelector('#inv').hidden}));
 await pg.evaluate(()=>document.querySelector('#lbmX').click());await pg.waitForTimeout(300);
 await pg.evaluate(()=>{document.querySelector('#invTestClr').click()});
 await pg.evaluate(()=>{const d=new Date();d.setUTCHours(7,30,0,0);window.__TDST_NOW=d.getTime()});
 await tap('#lbGrid .lbt[data-lb=diemtam]');await pg.waitForTimeout(400);
 const r=await pg.evaluate(()=>{const e=document.querySelector('#dtBun').getBoundingClientRect();return [e.left+e.width*.3,e.top+e.height*.5]});
 if(process.env.DSF)await pg.touchscreen.tap(r[0],r[1]);else await pg.mouse.click(r[0],r[1]);await pg.waitForTimeout(300);
 const lit=await pg.evaluate(()=>document.querySelectorAll('.dtbites i.on').length);await pg.screenshot({path:`${OUT}/v4_tl_${w}x${h}.png`});
 await tap('#dtX');const back=await pg.evaluate(()=>document.querySelector('#lbm').hidden&&!document.querySelector('#lobby').hidden);
 console.log(w,h,'chọn:',nm,'| menu Luyện Đan:',JSON.stringify(ld),'| chạm bánh lit',lit,'| Trở lại',back,'| lỗi',errs.length,errs.slice(0,2));await b.close()}process.exit(0)})();
