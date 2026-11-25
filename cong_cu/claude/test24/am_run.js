const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');
(async()=>{const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',forge:6,w:900,h:420,mobile:true});
await pg.waitForTimeout(500);
await pg.evaluate(()=>{showLobby()});await pg.waitForTimeout(500);
const lb=await pg.evaluate(()=>{const t=[...document.querySelectorAll('.lbt')].map(x=>x.textContent.trim().slice(0,30));return t});console.log(JSON.stringify(lb));
await pg.evaluate(()=>{openLbm('amgioi')});await pg.waitForTimeout(300);await pg.screenshot({path:'/tmp/am_menu.png'});
await pg.evaluate(()=>{document.querySelector('[data-am="1"]').click()});await pg.waitForTimeout(500);
for(let k=0;k<120;k++)await pg.evaluate(()=>__step(1000/30));
let r=await pg.evaluate(()=>({am:TDST.GG().am&&TDST.GG().am.floor,sw:TDST.GG().sw,wave:TDST.GG().wave,map:TDST.GG().cfg.map,en:TDST.GG().enemies.length,st:TDST.GG().state,tw:document.querySelector('#tWave')?.textContent,ts:document.querySelector('#tStage')?.textContent}));console.log('f1',JSON.stringify(r));
await pg.screenshot({path:'/tmp/am_f1.png'});
// force-clear floors up to boss floor 3
for(const f of[1,2]){await pg.evaluate(()=>{TDST.GG().wK=TDST.GG().wTarget+1});for(let k=0;k<150;k++)await pg.evaluate(()=>__step(1000/30));
 r=await pg.evaluate(()=>({st:TDST.GG().state,floor:TDST.GG().am.floor,picks:TDST.GG().picks}));console.log('after',f,JSON.stringify(r));
 await pg.evaluate(()=>{TDST.GG().picks=0;const c=document.querySelector('#contBtn');c.disabled=false;c.click()});for(let k=0;k<30;k++)await pg.evaluate(()=>__step(1000/30))}
r=await pg.evaluate(()=>({floor:TDST.GG().am.floor,wave:TDST.GG().wave,map:TDST.GG().cfg.map,sq:TDST.GG().spawnQ.length,en:TDST.GG().enemies.length}));console.log('f3 start',JSON.stringify(r));
for(let k=0;k<120;k++)await pg.evaluate(()=>__step(1000/30));
r=await pg.evaluate(()=>({bosses:TDST.GG().enemies.filter(e=>e.boss).map(e=>e.type),bar:document.querySelector('#bossbar .bn')?.textContent}));console.log('boss',JSON.stringify(r));
await pg.screenshot({path:'/tmp/am_f3.png'});
await pg.evaluate(()=>{for(const e of TDST.GG().enemies)if(e.boss)TDST.hit(e,1e9,{src:'h',t:'w'},0,0)});for(let k=0;k<60;k++)await pg.evaluate(()=>__step(1000/30));
r=await pg.evaluate(()=>({bosses:TDST.GG().enemies.filter(e=>!e.dead&&e.boss).length}));console.log('after1',JSON.stringify(r));
await pg.evaluate(()=>{for(const e of TDST.GG().enemies)if(e.boss&&!e.dead)TDST.hit(e,1e9,{src:'h',t:'w'},0,0)});for(let k=0;k<180;k++)await pg.evaluate(()=>__step(1000/30));
r=await pg.evaluate(()=>({st:TDST.GG().state,brk:!document.querySelector('#brk').hidden,ngoc:TDST.GG().am.ngoc}));console.log('after boss',JSON.stringify(r));
await pg.evaluate(()=>{TDST.P.hp=0});for(let k=0;k<60;k++)await pg.evaluate(()=>__step(1000/30));await pg.waitForTimeout(1200);
r=await pg.evaluate(()=>({sub:document.querySelector('#endSub')?.textContent,btn:document.querySelector('#againBtn').textContent,save:JSON.stringify(window.TDST.save?TDST.save.am:null)}));console.log('end',JSON.stringify(r));
await pg.screenshot({path:'/tmp/am_end.png'});
console.log('errors',errs.slice(0,5));await b.close()})();
