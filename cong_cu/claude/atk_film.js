// Quay đòn A→B khi ĐỨNG và khi VỪA ĐI VỪA ĐÁNH, 60 khung/giây
const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT,g,mv]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:g,forge:0,w:844,h:390,mobile:true});await L.startRun(pg);
 await pg.evaluate(()=>{clearInterval(__auto);const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnQ.length=0;G.spawnAcc=-1e9;G.packT=1e9;G.ambush=1;P.hp=1e6;P.x=1400;P.y=1100;
  for(let i=0;i<3;i++)TDST.spawnEnemy('tieu',100,100);G.enemies.forEach((e,i)=>{e.x=P.x+70+i*22;e.y=P.y-14+i*14;e.hp=e.mhp=1e5;e.stun=999});P.kit.basic.step=0;P.kit.basic.cd=0;document.querySelector('#quests').classList.add('min')});
 fs.mkdirSync(OUT,{recursive:true});
 if(mv==='1')await pg.keyboard.down('KeyS');
 for(let k=0;k<75;k++){await pg.evaluate(()=>{__step(1000/60);if(TDST.P.y>1160)TDST.P.y=1040});await pg.screenshot({path:OUT+'/f'+String(k).padStart(3,'0')+'.png',clip:{x:300,y:110,width:300,height:200}})}
 console.log(g,mv,errs);await b.close()})();
