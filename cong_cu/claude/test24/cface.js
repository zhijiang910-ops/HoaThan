const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const [ROOT]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:0,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 for(const side of [1,-1,1,-1]){
  const r=await pg.evaluate(async(side)=>{const P=TDST.P,G=TDST.GG();for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9};const e=G.enemies.filter(z=>!z.dead)[0];
   P.x=e.x-side*80;P.y=e.y;P.facing=-side;P.kit.basic.step=2;P.kit.basic.cd=0;P.av=0;P.dashT=0;P.swordCut=null;G.fx.length=0;
   let seen=null;for(let k=0;k<80;k++){__step(1000/60);if(!seen){const f=G.fx.find(q=>q.s==='k5c_pro');if(f)seen={fx:f.fx,facing:P.facing,side}}}
   return seen},side);
  console.log(JSON.stringify(r))}
 console.log('errors',errs.slice(0,3));await b.close()})();
