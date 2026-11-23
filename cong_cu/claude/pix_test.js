const L=require('./rec_lib');const O=process.argv[3];
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{gender:'nam',forge:0});await L.startRun(pg);
 await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnAcc=-1e9;G.packT=1e9;P.hp=1e6;TDST.spawnEnemy('hoa',P.x+90,P.y);TDST.spawnEnemy('tieu',P.x+150,P.y+30);G.enemies.forEach(e=>{e.stun=999;e.hp=e.mhp=1e6});P.rage=100;P.godCd=0;TDST.tryTransform()});
 await pg.waitForTimeout(1600);await pg.screenshot({path:O+'/pix.png',clip:{x:500,y:220,width:300,height:200}});console.log(errs);await b.close()})();
