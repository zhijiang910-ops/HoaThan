const L=require('./rec_lib');const fs=require('fs');
const [ROOT,OUT,gender]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender,forge:6,w:844,h:390,mobile:true});await L.startRun(pg);
 await pg.evaluate(()=>{clearInterval(__auto);const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnQ.length=0;G.spawnAcc=-1e9;G.packT=1e9;G.ambush=1;P.hp=1e6;P.x=1400;P.y=1100;
  for(let i=0;i<5;i++)TDST.spawnEnemy('tieu',100,100);G.enemies.forEach((e,i)=>{e.x=P.x+260+(i%3)*34;e.y=P.y-30+i*15;e.hp=e.mhp=1e5;e.stun=999});P.kit.basic.step=0;
  document.querySelector('#quests').classList.add('min')});
 fs.mkdirSync(OUT,{recursive:true});
 for(let k=0;k<200;k++){
  if(k===0)await pg.keyboard.down('KeyD');if(k===50)await pg.keyboard.up('KeyD');
  await pg.evaluate(()=>{__step(1000/60);__step(1000/60)});
  await pg.screenshot({path:OUT+'/f'+String(k).padStart(3,'0')+'.png'})}
 console.log(gender,errs);await b.close()})();
