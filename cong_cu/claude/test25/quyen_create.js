const L=require('/home/user/hoathan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{for(const [w,h] of [[1100,620],[844,390],[667,375],[550,278]]){
 const {b,pg,errs}=await L.open('/home/user/hoathan/game',{gender:'nu',forge:6,w,h,seed:false});
 await pg.evaluate(()=>clearInterval(__auto));
 await pg.evaluate(()=>{TDST.openCreate()});await pg.waitForTimeout(600);
 await pg.click('[data-sect="thiencuong"]');await pg.waitForTimeout(300);
 await pg.fill('#crName','QuyenThu').catch(()=>{});
 const r=await pg.evaluate(()=>{const g=document.querySelector('#crGo'),e=document.querySelector('#crErr');const bb=g?g.getBoundingClientRect():null;return {lock:!!document.querySelector('[data-sect="thiencuong"].lock'),on:!!document.querySelector('[data-sect="thiencuong"].on'),goDisabled:g&&g.disabled,goBottom:bb&&Math.round(bb.bottom),vh:innerHeight,err:e&&e.textContent,kit:[...document.querySelectorAll('#crKit *,.cxK *')].map(x=>x.textContent).join('|').slice(0,200)}});
 console.log(w+'x'+h,JSON.stringify(r),'errs',errs.length);
 await pg.screenshot({path:`${OUT}/qc_${w}.png`});
 if(w===1100){await pg.click('#crGo');await pg.waitForTimeout(800);const p=await pg.evaluate(()=>JSON.parse(localStorage.getItem('tdst')).prof);console.log('hồ sơ lưu',JSON.stringify({sect:p.sect,weapon:p.weapon,gender:p.gender}))}
 await b.close()}})();
