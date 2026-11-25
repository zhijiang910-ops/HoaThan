const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');
(async()=>{const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',w:1100,h:620});
await pg.evaluate(()=>{newRun(false,1)});await pg.waitForTimeout(400);
await pg.evaluate(()=>{const G=TDST.GG();amStartFloor(12);G.enemies.length=0;G.spawnQ.length=0;G.boss=null;TDST.P.hp=1e9});
for(const [x,y,n] of [[1600,1200,'a'],[1050,1060,'b']]){await pg.evaluate(([x,y])=>{const P=TDST.P;P.x=x;P.y=y;TDST.GG().enemies.length=0;TDST.GG().spawnQ.length=0},[x,y]);for(let k=0;k<40;k++)await pg.evaluate(()=>__step(1000/30));await pg.screenshot({path:`/tmp/vx_${n}.png`})}
console.log(errs.slice(0,3));await b.close()})();
