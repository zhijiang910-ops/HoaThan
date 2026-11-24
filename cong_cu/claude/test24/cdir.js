const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const [ROOT,OUT]=process.argv.slice(2);require('fs').mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:0,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 const cases=[['phai',1,0],['tren',0,-1],['duoi',0,1],['trai',-1,0]];
 for(const [nm,dx,dy] of cases){
  await pg.evaluate(([dx,dy])=>{const P=TDST.P,G=TDST.GG();for(const x of G.enemies){x.maxhp=1e9;x.hp=1e9;x.x=-999;x.y=-999};const e=G.enemies.filter(z=>!z.dead)[0];
   P.x=P.x;e.x=P.x+dx*90;e.y=P.y+dy*90;P.facing=dx||1;P.kit.basic.step=2;P.kit.basic.cd=0;P.av=0;P.dashT=0;P.swordCut=null;G.fx.length=0},[dx,dy]);
  for(let k=0;k<34;k++)await pg.evaluate(()=>__step(1000/60));
  const pos=await pg.evaluate(()=>({x:TDST.P.x,y:TDST.P.y}));
  await pg.screenshot({path:OUT+`/${nm}.png`,clip:{x:200,y:130,width:400,height:300}});
  for(let k=0;k<90;k++)await pg.evaluate(()=>__step(1000/60));
 }
 console.log('errors',errs.slice(0,3));await b.close()})();
