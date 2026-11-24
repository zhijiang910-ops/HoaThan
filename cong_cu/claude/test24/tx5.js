const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:0,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();const e=G.enemies.filter(z=>!z.dead)[0];P.x=e.x-170;P.y=e.y;const s=P.kit.act.find(x=>x.def.id==='k2');s.lvl=3;window.__tg=e;for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9}});
 await pg.evaluate(()=>{const s=TDST.P.kit.act.find(x=>x.def.id==='k2');s.def.cast(window.__tg,s.lvl)});
 let n=0;for(let k=0;k<360;k++){await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;for(const s of P.kit.act)s.cd=99;P.kit.ult.cd=99;P.mp=999});
  if(k>=90&&k%8==0&&n<12){await pg.screenshot({path:OUT+`/t${String(n).padStart(2,'0')}.png`,clip:{x:150,y:60,width:800,height:470}});n++}}
 console.log('errors',errs.slice(0,3));await b.close()})();
