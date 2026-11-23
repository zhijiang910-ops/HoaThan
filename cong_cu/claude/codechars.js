const L=require('./rec_lib');const O=process.argv[3];
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{gender:'nam',forge:0});
 const gods=['wukong','nezha','bajie','tudi'];
 for(const g of gods){
  await pg.evaluate(g=>{TDST.sel.god=g;TDST.newRun()},g);await pg.waitForTimeout(1200);
  await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnAcc=-1e9;G.packT=1e9;P.hp=1e6;P.rage=100;P.godCd=0;TDST.tryTransform()});
  await pg.waitForTimeout(1500);await pg.screenshot({path:`${O}/god_${g}.png`,clip:{x:540,y:200,width:200,height:220}});
 }
 await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;G.enemies.length=0;TDST.spawnEnemy('boss',P.x+120,P.y);TDST.spawnEnemy('hoa',P.x-110,P.y);G.enemies.forEach(e=>{e.stun=999;e.hp=e.mhp=1e6})});
 await pg.waitForTimeout(800);await pg.screenshot({path:`${O}/boss_hoa.png`,clip:{x:380,y:150,width:520,height:300}});
 console.log(errs);await b.close()})();
