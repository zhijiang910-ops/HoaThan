const L=require('./rec_lib');const [ROOT,OUT]=process.argv.slice(2);require('fs').mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{w:1100,h:620});await L.startRun(pg);
 const r0=await pg.evaluate(()=>TDST.P.kit.act.map(s=>s.def.name+':'+s.lvl));console.log(r0);
 await pg.evaluate(()=>clearInterval(__auto));let seen=0;
 for(let j=0;j<600;j++){await pg.evaluate(()=>__step(1000/30));if(j%30==0){const z=await pg.evaluate(()=>TDST.GG().zones.filter(z=>z.kind==='blades').length);seen+=z;if(z&&seen<3)await pg.screenshot({path:OUT+'/r'+j+'.png'})}}
 console.log('blades seen',seen,errs);await b.close()})();
