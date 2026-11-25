// Chụp 7 map Âm Giới trong luồng rương/cổng (vào tầng 1, nhảy tới tầng đại diện từng map). Dùng: node am_maps7.js <outdir>
const L=require('/home/user/hoathan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{const names=['hoangtuyen','biangan','nghiepkinh','uongtu','vongxuyen','diemla','luanhoi'],fl=[1,4,7,10,12,15,18];
const {b,pg,errs}=await L.open('/home/user/hoathan/game',{gender:'nam',w:1100,h:620});
await pg.evaluate(()=>clearInterval(__auto));const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/30))};
await pg.click('.lbt[data-lb="amgioi"]');await step(2);await pg.click('#amGo');await step(60);
for(let i=0;i<7;i++){
 await pg.evaluate((f)=>{const G=TDST.GG();G.am.floor=f;G.am.start=f;amEnterFloor(f);G.enemies.length=0;G.spawnQ.length=0;TDST.P.hp=1e9;TDST.P.x=1600;TDST.P.y=1000;G.cam.x=1600;G.cam.y=900},fl[i]);
 await new Promise(r=>setTimeout(r,700));await step(30);/* fade dùng timer thật */
 const info=await pg.evaluate(()=>({map:TDST.GG().cfg.map,over:TDST.GG().over}));
 console.log(names[i],fl[i],JSON.stringify(info));
 await pg.screenshot({path:`${OUT}/m7_${names[i]}.png`});}
console.log('errors',errs.length,errs.slice(0,3));await b.close()})();
