const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:0,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:'wukong',fold:true,rage:true,god_on:true,forge:6,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>clearInterval(__auto));await pg.click('#trP [data-t=hoa]');await pg.evaluate(()=>{document.getElementById('trP').style.display='none'});
 for(let k=0;k<70;k++)await pg.evaluate(()=>__step(1000/60));
 const r=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();for(const s of P.god.sk)s.cd=99;P.god.ult.cd=99;let d0=G.dmgDealt;return d0});
 fs.mkdirSync(OUT,{recursive:true});await pg.keyboard.down('KeyD');
 for(let k=0;k<90;k++){await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;for(const s of P.god.sk)s.cd=99;P.god.ult.cd=99});if(k%6==0)await pg.screenshot({path:OUT+'/m'+String(k).padStart(3,'0')+'.png',clip:{x:300,y:120,width:500,height:380}})}
 const r2=await pg.evaluate(()=>[TDST.GG().dmgDealt,TDST.P.moving]);await pg.keyboard.up('KeyD');
 console.log('sát thương khi đang chạy:',Math.round(r2[0]-r),'| đang chạy:',r2[1],errs);await b.close()})();
