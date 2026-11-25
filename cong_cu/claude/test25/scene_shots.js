// Chụp cảnh map Âm Giới do game dựng (ẩn nhân vật + HUD) làm ảnh giữa màn tạo nhân vật. Dùng: node scene_shots.js <outdir>
const L=require('/home/user/hoathan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
const SC=[['diemla',15,1600,760],['luanhoi',18,1600,1330],['hoangtuyen',1,1600,780],['nghiepkinh',7,1600,820]];
(async()=>{const {b,pg,errs}=await L.open(process.argv[3]||'/home/user/hoathan/game',{gender:'nam',w:640,h:720,dsf:2});
await pg.evaluate(()=>clearInterval(__auto));const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/30))};
await pg.click('.lbt[data-lb="amgioi"]');await step(2);await pg.click('#amGo');await step(60);
await pg.evaluate(()=>{window.__noP=1});
for(const [n,f,x,y] of SC){
 await pg.evaluate((f)=>{const G=TDST.GG();G.am.floor=f;G.am.start=f;amEnterFloor(f)},f);
 await new Promise(r=>setTimeout(r,800));await step(10);
 await pg.evaluate(([x,y])=>{const G=TDST.GG();G.enemies.length=0;G.spawnQ.length=0;G.later=[];TDST.P.hp=1e9;TDST.P.inv=1e9;TDST.P.x=x;TDST.P.y=y;G.cam.x=x;G.cam.y=y;G.paused=false;for(const s of ['#hud','#joy','#notice','#bossbar'])document.querySelectorAll(s).forEach(e=>e.style.display='none')},[x,y]);
 await step(40);
 await pg.evaluate(()=>{const G=TDST.GG();G.enemies.length=0;G.spawnQ.length=0});await step(4);
 await pg.screenshot({path:`${OUT}/scene_${n}.png`});console.log(n,'ok');
 await pg.evaluate(()=>{for(const s of ['#hud','#joy','#notice','#bossbar'])document.querySelectorAll(s).forEach(e=>e.style.display='')})}
console.log('errors',errs.length,errs.slice(0,2));await b.close()})();
