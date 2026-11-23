const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:0,w:844,h:390,mobile:true});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:'wukong',fold:true,rage:true,god_on:true,forge:6,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.click('#trP [data-t=hoa]');await pg.waitForTimeout(1800);
 await pg.evaluate(()=>{clearInterval(__auto);document.getElementById('trP').style.display='none';const P=TDST.P;for(const s of P.god.sk)s.cd=99;if(P.god.ult)P.god.ult.cd=99});
 fs.mkdirSync(OUT,{recursive:true});let n=0;
 for(let k=0;k<75;k++){await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;for(const s of P.god.sk)s.cd=99;if(P.god.ult)P.god.ult.cd=99});await pg.screenshot({path:OUT+'/f'+String(n++).padStart(3,'0')+'.png'})}
 await pg.evaluate(()=>{const P=TDST.P;P.god.ult.cd=0;P.god.basic.cd=99});
 for(let k=0;k<90;k++){await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;for(const s of P.god.sk)s.cd=99;P.god.basic.cd=99;if(P.god.ult.cd<=0)P.god.ult.cd=0});await pg.screenshot({path:OUT+'/f'+String(n++).padStart(3,'0')+'.png'})}
 console.log(errs);await b.close()})();
