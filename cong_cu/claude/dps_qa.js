const L=require('./rec_lib');const [ROOT,MODE,FORGE]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:+FORGE,w:1100,h:620});
 await pg.evaluate((m)=>{localStorage.setItem('tdst_tr',JSON.stringify(m==='god'?{god:'wukong',fold:true,rage:false,god_on:true,forge:0,scale:1}:{god:null,fold:true,rage:false,god_on:false,forge:+0,scale:1}))},MODE);
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1600);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 await pg.evaluate(({m,f})=>{const P=TDST.P,G=TDST.GG();G.trForge=f;if(m==='god'){P.rage=100;try{TDST.tryTransform()}catch(e){}}
  for(const x of G.enemies){x.maxhp=1e12;x.hp=1e12;x.stun=0}const e=G.enemies.filter(z=>!z.dead)[0];P.x=e.x-70;P.y=e.y;P.facing=1;
  for(const s of(P.kit?P.kit.act:[]))s.cd=1e9;if(P.kit)P.kit.ult.cd=1e9;if(P.god){for(const s of P.god.sk)s.cd=1e9;if(P.god.ult)P.god.ult.cd=1e9}},{m:MODE,f:+FORGE});
 for(let k=0;k<120;k++)await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;for(const s of(P.kit?P.kit.act:[]))s.cd=1e9;if(P.kit)P.kit.ult.cd=1e9;if(P.god){for(const s of P.god.sk)s.cd=1e9;if(P.god.ult)P.god.ult.cd=1e9}});
 const d0=await pg.evaluate(()=>TDST.GG().dmgDealt);
 for(let k=0;k<60*12;k++)await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;for(const s of(P.kit?P.kit.act:[]))s.cd=1e9;if(P.kit)P.kit.ult.cd=1e9;if(P.god){for(const s of P.god.sk)s.cd=1e9;if(P.god.ult)P.god.ult.cd=1e9}});
 const d1=await pg.evaluate(()=>TDST.GG().dmgDealt);console.log(MODE,'+'+FORGE,'DPS đòn thường =',Math.round((d1-d0)/12),errs.slice(0,1));await b.close()})();
