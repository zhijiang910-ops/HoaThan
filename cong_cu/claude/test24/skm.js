const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
(async()=>{for(const [w,h] of [[667,375],[844,390],[932,430],[1100,620]]){
 const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w,h});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1200);
 const r=await pg.evaluate(()=>[...document.querySelectorAll('#skills .sk')].map(e=>{const b=e.getBoundingClientRect();return [e.className.replace('sk ','').slice(0,22),Math.round(b.width),Math.round(b.height)]}));
 console.log(w+'x'+h,JSON.stringify(r));
 await pg.screenshot({path:`${OUT}/s_${w}x${h}.png`});await b.close()}})();
