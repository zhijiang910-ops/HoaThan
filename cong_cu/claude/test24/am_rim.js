const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');
(async()=>{const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',w:1100,h:620});
const maps=[[1,'hoang'],[4,'bian'],[7,'nghiep'],[10,'uong'],[12,'vong'],[15,'diemla'],[18,'luan']];
for(const [fl,n] of maps){
await pg.evaluate(()=>{newRun(false,1)});await pg.waitForTimeout(300);
await pg.evaluate((fl)=>{const G=TDST.GG();amStartFloor(fl);G.enemies.length=0;G.spawnQ.length=0;G.boss=null;const P=TDST.P;P.hp=1e9;P.x=1600;P.y=2340},fl);
for(let k=0;k<40;k++)await pg.evaluate(()=>__step(1000/30));
await pg.screenshot({path:`/tmp/rim_${n}.png`});
await pg.evaluate(()=>{TDST.endRun(false)});await pg.waitForTimeout(1100);await pg.evaluate(()=>{document.querySelector('#againBtn').click()});await pg.waitForTimeout(200)}
console.log(errs.slice(0,3));await b.close()})();
