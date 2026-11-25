// Thử bộ chiêu Quyền (Thiên Cương Môn) trong trận Âm Giới tầng 1: A->B->C, Q/F/X, hồ sơ Kiếm không đổi.
const L=require('/home/user/hoathan/cong_cu/claude/rec_lib');const fs=require('fs');const OUT=process.argv[2],GEN=process.argv[3]||'nam',SECT=process.argv[4]||'thiencuong';
(async()=>{const {b,pg,errs}=await L.open('/home/user/hoathan/game',{gender:GEN,forge:6,w:1100,h:620});
 await pg.addInitScript((sect)=>{try{const s=JSON.parse(localStorage.getItem('tdst'));s.prof.sect=sect;localStorage.setItem('tdst',JSON.stringify(s))}catch(e){}},SECT);/* chạy SAU script seed của rec_lib */
 await pg.reload();await pg.waitForTimeout(2500);await pg.evaluate(()=>clearInterval(__auto));
 const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/60))};
 await pg.click('.lbt[data-lb="amgioi"]');await step(2);await pg.click('#amGo');await step(80);
 const info=await pg.evaluate(()=>({w:TDST.P.kit.w,basic:TDST.P.kit.basic.def.name,acts:TDST.P.kit.act.map(a=>a.def.name+':'+a.lvl),ult:TDST.P.kit.ult.def.name}));
 console.log(JSON.stringify(info));
 fs.mkdirSync(OUT,{recursive:true});const seq=[];let shot=0,fxs=new Set();
 for(let k=0;k<420;k++){await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;P.hp=P.maxhp||1e9;const G=TDST.GG();for(const e of G.enemies)if(!e.dead&&!e.amG&&Math.hypot(e.x-P.x,e.y-P.y)>260){e.x+=(P.x-e.x)*0.02;e.y+=(P.y-e.y)*0.02}});
  const a=await pg.evaluate(()=>[TDST.P.av>0?TDST.P.avAnim:'-',TDST.GG().fx.filter(f=>f.k==='sp').map(f=>f.s)]);seq.push(a[0]);a[1].forEach(x=>fxs.add(x));
  if(a[0]==='attack3'&&shot<4&&k%4===0)await pg.screenshot({path:`${OUT}/qk_c_${GEN}_${shot++}.png`,clip:{x:300,y:140,width:500,height:340}})}
 const c=[];for(const a of seq){if(!c.length||c[c.length-1]!==a)c.push(a)}
 console.log('chuỗi đòn:',c.slice(0,24).join(' '));console.log('fx sp:',[...fxs].join(','));
 // kỹ năng: đặt ult lvl 1 và bấm Q,F,X
 for(const [key,nm] of [['KeyQ','Q'],['KeyF','F'],['KeyX','X']]){
  await pg.evaluate(()=>{const P=TDST.P;if(P.kit.ult.lvl<1){P.kit.ult.lvl=1;TDST.hudSkills()}for(const s of P.kit.act)s.cd=0;P.kit.ult.cd=0;P.mp=P.maxmp||999});
  const before=await pg.evaluate(()=>TDST.GG().enemies.filter(e=>!e.dead).reduce((t,e)=>t+e.hp,0));
  await pg.keyboard.press(key);await step(20);await pg.screenshot({path:`${OUT}/qk_skill_${nm}_early_${GEN}.png`,clip:{x:300,y:140,width:500,height:340}});for(let i=0;i<40;i++)await step(3);
  const after=await pg.evaluate(()=>TDST.GG().enemies.filter(e=>!e.dead).reduce((t,e)=>t+e.hp,0));
  const cd=await pg.evaluate(k=>({q:TDST.P.kit.act[0].cd,f:TDST.P.kit.act[1].cd,x:TDST.P.kit.ult.cd}),0);
  console.log(nm,'tổng máu quái trước',Math.round(before),'sau',Math.round(after),'cd',JSON.stringify(cd));
  await pg.screenshot({path:`${OUT}/qk_skill_${nm}_${GEN}.png`,clip:{x:250,y:100,width:600,height:420}});}
 console.log('errors',errs.length,errs.slice(0,4));await b.close()})();
