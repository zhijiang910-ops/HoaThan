const L=require('./rec_lib');
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{gender:'nam',forge:6});await L.startRun(pg);
 await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnAcc=-1e9;G.packT=1e9;P.hp=1e6;P.x=1500;P.y=1100;const ET=TDST.ET();for(let i=0;i<3;i++)TDST.spawnEnemy('tieu',100,100);G.enemies.forEach((e,i)=>{e.x=P.x+150+i*40;e.y=P.y;e.hp=e.mhp=1e5;e.stun=999});P.kit.basic.cd=99;P.dashCd=0});
 // giữ Space 0.6s
 await pg.keyboard.down('Space');await pg.waitForTimeout(600);const a=await pg.evaluate(()=>({cut:!!TDST.P.cutC,hcd:TDST.P.holdCcd}));await pg.keyboard.up('Space');
 await pg.waitForTimeout(900);const b2=await pg.evaluate(()=>({hp:TDST.G.enemies.map(e=>Math.round(e.mhp-e.hp))}));
 // chạm nhanh: không ra C
 await pg.evaluate(()=>{TDST.P.dashCd=0;TDST.P.holdCcd=0});await pg.keyboard.press('Space');await pg.waitForTimeout(600);const c=await pg.evaluate(()=>({cut:!!TDST.P.cutC}));
 // kiếm +0 không ra
 console.log(JSON.stringify({a,b2,c}),errs);await b.close();
 const r2=await L.open(process.argv[2],{gender:'nam',forge:0});await L.startRun(r2.pg);await r2.pg.evaluate(()=>{TDST.P.dashCd=0});await r2.pg.keyboard.down('Space');await r2.pg.waitForTimeout(600);console.log('forge0 cut',await r2.pg.evaluate(()=>!!TDST.P.cutC),r2.errs);await r2.b.close()})();
