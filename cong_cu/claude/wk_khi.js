const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:0,w:844,h:390,mobile:true});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:'wukong',fold:true,rage:true,god_on:true,forge:6,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>clearInterval(__auto));
 await pg.click('#trP [data-t=hoa]');
 await pg.evaluate(()=>{document.getElementById('trP').style.display='none'});
 fs.mkdirSync(OUT,{recursive:true});let n=0;
 const lock=()=>{const P=TDST.P;if(!P.god)return;for(const s of P.god.sk)if(s.cd>0.7)s.cd=99;P.god.basic.cd=99;if(P.god.ult&&P.god.ult.cd>1)P.god.ult.cd=99};
 const seg=async(N,pre)=>{if(pre)await pg.evaluate(pre);for(let k=0;k<N;k++){await pg.evaluate(l=>{__step(1000/60);eval(l)()},'('+lock.toString()+')');await pg.screenshot({path:OUT+'/f'+String(n++).padStart(3,'0')+'.png'})}};
await seg(60,()=>{});
 await seg(30,()=>{const P=TDST.P;for(const s of P.god.sk)s.cd=99;P.god.ult.cd=99;P.god.basic.cd=99;TDST.GG().allies=[]});
 await seg(220,()=>{const P=TDST.P;P.god.sk[0].cd=0;P.god.basic.cd=99});                                // gậy khổng lồ
 console.log(n,errs);await b.close()})();
