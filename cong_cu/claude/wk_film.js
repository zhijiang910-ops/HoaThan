const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT,mv]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:0,w:844,h:390,mobile:true});
 await pg.evaluate(()=>{TDST.sel.god='wukong'});await L.startRun(pg);
 await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnQ.length=0;G.spawnAcc=-1e9;G.packT=1e9;G.ambush=1;P.hp=1e6;P.x=1400;P.y=1100;P.rage=100;P.godCd=0;TDST.tryTransform()});
 await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const G=TDST.G,P=TDST.P;for(let i=0;i<3;i++)TDST.spawnEnemy('tieu',100,100);G.enemies.forEach((e,i)=>{e.x=P.x+(i==0?90:140+i*20);e.y=P.y-10+i*12;e.hp=e.mhp=1e6;e.stun=999});P.godDur=999;document.querySelector('#quests').classList.add('min')});
 fs.mkdirSync(OUT,{recursive:true});if(mv==='1')await pg.keyboard.down('KeyS');
 for(let k=0;k<90;k++){await pg.evaluate(()=>{__step(1000/60);if(TDST.P.y>1160)TDST.P.y=1040});await pg.screenshot({path:OUT+'/f'+String(k).padStart(3,'0')+'.png',clip:{x:260,y:70,width:380,height:260}})}
 console.log('form',await pg.evaluate(()=>TDST.P.form),errs);await b.close()})();
