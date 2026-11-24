const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);fs.mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:0,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 const info=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();P.mp=999;for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9};const e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];P.x=e.x-150;P.y=e.y;P.facing=1;const s=P.kit.act.find(q=>q.def.id==='k7');s.lvl=1;s.cd=0;return {act:P.kit.act.map(q=>q.def.id+':'+q.lvl),hk:s.def.hotkey}});
 console.log(JSON.stringify(info));
 await pg.screenshot({path:OUT+'/hud.png'});
 await pg.keyboard.press('KeyC');
 let n=0;for(let k=0;k<160;k++){await pg.evaluate(()=>__step(1000/60));if(k>=10&&k%9==0&&n<9){await pg.screenshot({path:OUT+`/c${n}.png`,clip:{x:300,y:0,width:500,height:380}});n++}}
 const cd=await pg.evaluate(()=>TDST.P.kit.act.find(q=>q.def.id==='k7').cd);console.log('cd sau cast',cd);
 console.log('errors',errs.slice(0,3));await b.close()})();
