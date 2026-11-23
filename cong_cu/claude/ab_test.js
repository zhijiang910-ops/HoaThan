const L=require('./rec_lib');const T=__dirname;const forge=+process.argv[3]||0;
(async()=>{for(const g of ['nam','nu']){const {b,pg,errs}=await L.open(process.argv[2],{gender:g,forge});await L.startRun(pg);
 await pg.evaluate(()=>{const G=TDST.G,P=TDST.P;G.enemies.length=0;G.spawnAcc=-1e9;G.packT=1e9;P.hp=1e6;P.x=1500;P.y=1100;
  const ET=TDST.ET();const t=Object.keys(ET).find(k=>!ET[k].boss&&!ET[k].elite);
  for(let i=0;i<4;i++){TDST.spawnEnemy(t,100,100)}G.enemies.forEach((e,i)=>{e.x=P.x+62+(i%2)*30;e.y=P.y-25+i*17;e.hp=e.mhp=1e5;e.stun=999});
  P.kit.basic.step=0;P.kit.basic.cd=0;P.combo=40});
 await L.capture(pg,T+'/ab_'+g,150,{x:390,y:220,width:500,height:260});
 console.log(g,errs);await b.close()}})();
