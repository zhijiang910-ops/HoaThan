const L=require('./rec_lib');const O=process.argv[3];const fs=require('fs');
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{gender:'nam',forge:0});
 for(const [look,w] of [['wukong','bong'],['nezha','hoa'],['bajie','ba'],['tudi','truong']]){
  const d=await pg.evaluate(([l,w])=>{const c=document.createElement('canvas');portrait(c,l,w,'#5a6470');return c.toDataURL()},[look,w]);
  fs.writeFileSync(`${O}/god_${look}.png`,Buffer.from(d.split(',')[1],'base64'));
 }
 await L.startRun(pg);
 await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnAcc=-1e9;G.packT=1e9;P.hp=1e6;TDST.spawnEnemy('boss',P.x+60,P.y-20);TDST.spawnEnemy('hoa',P.x-160,P.y+10);G.enemies.forEach(e=>{e.hp=e.mhp=1e6});P.x-=260});
 await pg.waitForTimeout(700);await pg.screenshot({path:`${O}/boss_hoa.png`,clip:{x:500,y:150,width:620,height:330}});
 console.log(errs);await b.close()})();
