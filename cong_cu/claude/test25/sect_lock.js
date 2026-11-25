// Kiểm khóa phái ở màn tạo nhân vật: chỉ Mao Sơn + Thiên Cương mở; 4 phái còn lại có hình ổ khóa, Lưu bị chặn. Dùng: node sect_lock.js <outdir>
const L=require('/home/user/hoathan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{for(const [w,h] of [[1100,620],[667,375],[550,278]]){
 const {b,pg,errs}=await L.open('/home/user/hoathan/game',{gender:'nam',w,h,seed:false});
 await pg.evaluate(()=>clearInterval(__auto));await pg.evaluate(()=>{TDST.openCreate()});await pg.waitForTimeout(600);
 const st=await pg.evaluate(()=>[...document.querySelectorAll('[data-sect]')].map(e=>e.dataset.sect+':'+(e.classList.contains('lock')?'KHÓA':'mở')+(e.querySelector('.lkimg')?'+ổ':'')));
 console.log(w+'x'+h,st.join(' '));
 if(w===1100){
  await pg.click('[data-sect="tramyeu"]');await pg.waitForTimeout(250);await pg.fill('#crName','Thu').catch(()=>{});await pg.waitForTimeout(300);
  console.log('chọn Đao ->',JSON.stringify(await pg.evaluate(()=>({goDisabled:document.querySelector('#crGo').disabled,info:document.querySelector('#crWInfo').textContent,prof:(JSON.parse(localStorage.getItem('tdst')||'{}').prof)||null}))));
  await pg.screenshot({path:`${OUT}/lock_create_${w}.png`});
  await pg.click('[data-sect="maoson"]');await pg.waitForTimeout(250);console.log('chọn Mao Sơn -> goDisabled',await pg.evaluate(()=>document.querySelector('#crGo').disabled));await pg.click('#crGo');await pg.waitForTimeout(600);
  console.log('Lưu với Mao Sơn ->',JSON.stringify(await pg.evaluate(()=>{const p=(JSON.parse(localStorage.getItem('tdst')||'{}').prof)||{};return {sect:p.sect,weapon:p.weapon}})));
 } else {await pg.click('[data-sect="phucma"]');await pg.waitForTimeout(250);await pg.screenshot({path:`${OUT}/lock_create_${w}.png`})}
 console.log('errs',errs.length);await b.close()}})();
