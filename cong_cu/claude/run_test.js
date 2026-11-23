const L=require('./rec_lib');const T=__dirname;
(async()=>{for(const g of ['nam','nu']){const {b,pg,errs}=await L.open(process.argv[2],{gender:g});await L.startRun(pg);
 await pg.evaluate(()=>{const G=TDST.G;G.enemies.length=0;G.spawnAcc=-1e9;G.packT=1e9;TDST.P.hp=1e6});
 await pg.keyboard.down('KeyD');
 // camera bám nhân vật → nhân vật giữa màn, nền trượt
 await L.capture(pg,T+'/run_'+g,48,{x:540,y:250,width:200,height:180});
 await pg.keyboard.up('KeyD');console.log(g,errs);await b.close()}})();
