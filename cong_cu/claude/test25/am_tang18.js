const L=require('/home/user/hoathan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{const {b,pg,errs}=await L.open('/home/user/hoathan/game',{gender:'nam',w:1100,h:620});
await pg.evaluate(()=>clearInterval(__auto));const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/30))};
await pg.click('.lbt[data-lb="amgioi"]');await step(2);await pg.click('#amGo');await step(60);
await pg.evaluate(()=>{const G=TDST.GG();G.am.floor=18;G.am.start=18;amEnterFloor(18)});
await new Promise(r=>setTimeout(r,800));await step(10);
for(const [n,x,y] of [['tam',1600,1280],['rong',1600,1100]]){
 await pg.evaluate(([x,y])=>{const G=TDST.GG();G.enemies.length=0;G.spawnQ.length=0;G.later=[];TDST.P.hp=1e9;TDST.P.inv=1e9;TDST.P.x=x;TDST.P.y=y;G.cam.x=x;G.cam.y=y},[x,y]);
 await step(40);await pg.evaluate(()=>{const G=TDST.GG();G.enemies.length=0;G.spawnQ.length=0});await step(4);
 await pg.screenshot({path:`${OUT}/lh18_${n}.png`})}
console.log('errors',errs.length,errs.slice(0,2));await b.close()})();
