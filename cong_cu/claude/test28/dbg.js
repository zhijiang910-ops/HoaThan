const ROOT='/home/user/hoathan';const L=require(ROOT+'/cong_cu/claude/rec_lib');
(async()=>{const {b,pg,errs}=await L.open(ROOT+'/game',{w:852,h:393,dsf:1,forge:6});
 await pg.addInitScript(()=>{try{const s=JSON.parse(localStorage.getItem('tdst'));s.prof.sect='thiencuong';s.prof.weapon='quyen';localStorage.setItem('tdst',JSON.stringify(s))}catch(e){}});
 await pg.reload();await pg.waitForTimeout(2500);
 const g=await pg.evaluate(()=>document.querySelector('#lbGrid .lbt[data-s="6"]').getBoundingClientRect());await pg.mouse.click(g.x+g.width/2,g.y+g.height/2);await pg.waitForTimeout(2500);
 await pg.evaluate(()=>{clearInterval(__auto)});
 for(let i=0;i<120;i++)await pg.evaluate(()=>__step(1000/60));
 console.log(JSON.stringify(await pg.evaluate(()=>{const G=TDST.GG(),P=TDST.P;return {P:[P.x|0,P.y|0],state:G.state,dealt:G.dmgDealt,en:G.enemies.map(e=>[e.x|0,e.y|0,e.type,e.hp|0]).slice(0,4),basic:P.kit.basic&&P.kit.basic.def.id,range:P.kit.basic.def.range,cd:P.kit.basic.cd}})));
 await b.close()})();
