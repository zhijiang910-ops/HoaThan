const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{for(const [w,h,m] of [[1100,620,false],[844,390,true],[664,307,true],[932,430,true]]){
 const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',forge:6,w,h,mobile:m,dsf:2});
 await pg.waitForTimeout(800);
 const r=await pg.evaluate(()=>{const g=document.querySelector('#lbGrid'),ts=[...g.children],R=g.getBoundingClientRect();return {tiles:ts.length,cols:getComputedStyle(g).gridTemplateColumns.split(' ').length,gridBottom:Math.round(R.bottom),vh:innerHeight,overflowText:ts.filter(t=>t.scrollWidth>t.clientWidth+1).map(t=>t.dataset.lb)}});
 console.log(w+'x'+h,JSON.stringify(r),'errors',errs.length);await pg.screenshot({path:`${OUT}/lobby7_${w}x${h}.png`});await b.close()}})();
