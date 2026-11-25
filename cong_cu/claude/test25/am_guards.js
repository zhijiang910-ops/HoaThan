// Kiểm kẻ canh tầng (trùm/mini-boss/Quỷ Sai) ở các tầng đại diện, trong luồng rương/cổng. Dùng: node am_guards.js <outdir>
const L=require('/home/user/hoathan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{const {b,pg,errs}=await L.open('/home/user/hoathan/game',{gender:'nam',w:1100,h:620});
await pg.evaluate(()=>clearInterval(__auto));const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/30))};
await pg.click('.lbt[data-lb="amgioi"]');await step(2);await pg.click('#amGo');await step(60);
for(const f of [4,6,7,10,13,16,17,18]){
 await pg.evaluate((f)=>{const G=TDST.GG();G.am.floor=f;G.am.start=f;amEnterFloor(f)},f);
 await new Promise(r=>setTimeout(r,700));await step(20);
 const r=await pg.evaluate(()=>{const G=TDST.GG();G.enemies.length=0;G.spawnQ.length=0;TDST.P.hp=1e9;amSpawnGuards();return 1});await step(60);
 const g=await pg.evaluate(()=>TDST.GG().enemies.filter(e=>e.amG&&!e.dead).map(e=>e.nm+':'+e.type+' r'+e.r+' hp'+Math.round(e.hp)));
 console.log('tầng',f,JSON.stringify(g));
 if([4,7,10,13].includes(f)){await pg.screenshot({path:`${OUT}/g_${f}.png`,clip:{x:250,y:60,width:600,height:420}})}}
console.log('errors',errs.length,errs.slice(0,3));await b.close()})();
