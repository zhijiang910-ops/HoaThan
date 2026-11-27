// Quay Vạn Kiếm Tru Ma (X) trong Luyện Công: mặc Bát Quái Bào nam (sprite tư thế mới), nhắm phải/trái/chéo, tốc độ thường và ×0,25.
// node cong_cu/claude/test25/vankiem_luyencong.js <thư_mục_ra> [852x393] [outfit ms|''] [gender nam|nu]
const path=require('path'),fs=require('fs');const L=require('../rec_lib');
const ROOT=path.resolve(__dirname,'../../../game');const OUT=path.resolve(process.argv[2]||'vk_lc');fs.mkdirSync(OUT,{recursive:true});
const [W,Hh]=(process.argv[3]||'852x393').split('x').map(Number);const OUTFIT=process.argv[4]??'ms';const GEN=process.argv[5]||'nam';
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:GEN,forge:0,w:W,h:Hh,dsf:2,mobile:true});
 await pg.evaluate(o=>{localStorage.setItem('tdst_tr',JSON.stringify({god:null,fold:true,rage:false,god_on:false,forge:0,scale:1,outfit:o}))},OUTFIT);
 await pg.reload();await pg.waitForTimeout(1500);
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 const step=n=>pg.evaluate(n=>{for(let i=0;i<n;i++)__step(1000/60)},n);
 await step(30);
 const info=await pg.evaluate(()=>({pose:window.__vkPose(),ult:TDST.P.kit.ult.def.id}));console.log('info',JSON.stringify(info));
 const log=[];
 for(const [name,deg] of [['phai',0],['trai',180],['cheo',35]]){
  await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();P.x=1600;P.y=1140;P.vx=P.vy=0;for(const e of G.enemies){e.maxhp=e.hp=1e9}});
  await step(20);
  for(const sp of (name==='phai'?['thuong','x025']:['thuong'])){
   const d=`${OUT}/${name}_${sp}`;fs.mkdirSync(d,{recursive:true});
   await pg.evaluate(dg=>{const P=TDST.P,a=dg*Math.PI/180,u=P.kit.ult;u.lvl=Math.max(1,u.lvl);u.cd=0;P.mp=999;u.def.cast({x:P.x+Math.cos(a)*330,y:P.y+Math.sin(a)*330},u.lvl)},deg);
   const dtPer=sp==='thuong'?1000/30:1000/120; // thường: 30 khung/giây video; ×0,25: mỗi khung video tiến 1/120 s game
   if(sp==='x025')await step(120);/* ×0,25: tua tới 2,0 s rồi quay 2,0–3,6 s */
   for(let k=0;k<(sp==='thuong'?120:192);k++){
    await pg.evaluate(ms=>{__step(ms)},dtPer);
    const r=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG(),z=G.zones.find(q=>q.kind==='vkx2');return{t:z?+z.t.toFixed(3):null,pose:window.__vkPose().fi,on:window.__vkPose().on,ex:z?z._ex||0:0}});
    log.push(Object.assign({run:name+'_'+sp,k},r));
    await pg.screenshot({path:`${d}/f${String(k).padStart(3,'0')}.png`});
   }
   await step(90);
  }
 }
 fs.writeFileSync(OUT+'/log.json',JSON.stringify(log));
 console.log('errors',errs.length,errs.slice(0,3));await b.close();process.exit(0)})();
