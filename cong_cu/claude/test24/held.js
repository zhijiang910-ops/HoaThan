const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:0,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 for(let i=0;i<9;i++){const bt=pg.locator('button[data-t="wpn"]');if((await bt.textContent()).includes('Mực'))break;await bt.click()}
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();P.mp=999;P.kit.ult.cd=0;P.kit.ult.lvl=Math.max(1,P.kit.ult.lvl);for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9};const e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-150;P.y=e.y;P.facing=1;G.fx.length=0;window.__tx=e.x});
 for(let k=0;k<20;k++)await pg.evaluate(()=>__step(1000/60));
 for(let n=0;n<3;n++){for(let k=0;k<14;k++)await pg.evaluate(()=>__step(1000/60));await pg.screenshot({path:OUT+`/h${n}.png`,clip:{x:290,y:200,width:220,height:150}})}
 console.log('errors',errs.slice(0,3));await b.close()})();