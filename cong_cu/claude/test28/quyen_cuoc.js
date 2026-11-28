// Thử bộ Phục Ma Quyền Cước (28/11): 4 nhịp đánh thường + Ấn Chu Sa, Q/F/C/X, lướt Bộ Hư Lưu Phù, popup (i). Âm Giới tầng 1.
// node cong_cu/claude/test28/quyen_cuoc.js <thư_mục_ra> [nam|nu] [WxH]
const ROOT=require('path').resolve(__dirname,'../../..');const L=require(ROOT+'/cong_cu/claude/rec_lib');const fs=require('fs');
const OUT=process.argv[2],GEN=process.argv[3]||'nam',[W,Hh]=(process.argv[4]||'1100x620').split('x').map(Number);
(async()=>{const {b,pg,errs}=await L.open(ROOT+'/game',{gender:GEN,forge:0,w:W,h:Hh});
 await pg.addInitScript(()=>{try{const s=JSON.parse(localStorage.getItem('tdst'));s.prof.sect='thiencuong';s.prof.weapon='quyen';localStorage.setItem('tdst',JSON.stringify(s))}catch(e){}});
 await pg.reload();await pg.waitForTimeout(2500);await pg.evaluate(()=>clearInterval(__auto));
 const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/60))};
 await pg.evaluate(()=>document.querySelector('.lbt[data-lb="amgioi"]').click());await step(2);await pg.click('#amGo');await pg.waitForTimeout(1600);await step(90);
 fs.mkdirSync(OUT,{recursive:true});
 const info=await pg.evaluate(()=>({w:TDST.P.kit.w,basic:TDST.P.kit.basic.def.name,acts:TDST.P.kit.act.map(a=>a.def.name+':'+a.lvl+':'+(a.def.hotkey||'')),ult:TDST.P.kit.ult.def.name,pas:TDST.P.kit.pas.map(p=>p.def.name)}));
 console.log(JSON.stringify(info));
 await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)if(!s.lvl)s.lvl=1;if(P.kit.ult.lvl<1)P.kit.ult.lvl=1;TDST.hudSkills()});await step(2);
 await pg.screenshot({path:`${OUT}/hud_${GEN}_${W}x${Hh}.png`});
 // gom quái lại gần, đánh thường, ghi chuỗi đòn + Ấn Chu Sa
 const seq=[];let maxStk=0,shot=0;
 for(let k=0;k<360;k++){const a=await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;P.hp=1e9;const G=TDST.GG();for(const e of G.enemies)if(!e.dead&&Math.hypot(e.x-P.x,e.y-P.y)>120){e.x+=(P.x-e.x)*0.03;e.y+=(P.y-e.y)*0.03}
   return [P.av>0?P.avAnim:'-',Math.max(0,...G.enemies.filter(e=>!e.dead&&e.chuSaT>G.t).map(e=>e.chuSa))]});seq.push(a[0]);maxStk=Math.max(maxStk,a[1]);
  if(a[1]>=2&&shot<2&&k%30===0)await pg.screenshot({path:`${OUT}/an_chu_sa_${shot++}_${GEN}.png`})}
 const c=[];for(const a of seq){if(!c.length||c[c.length-1]!==a)c.push(a)}
 console.log('chuỗi đòn:',c.filter(x=>x!=='-').slice(0,16).join(' '),'| tầng ấn cao nhất',maxStk);
 // lướt
 await pg.evaluate(()=>{TDST.P.dashCd=0});await pg.keyboard.press('Space');await step(14);await pg.screenshot({path:`${OUT}/luot_bua_${GEN}.png`});await step(30);await pg.screenshot({path:`${OUT}/luot_no_${GEN}.png`});
 console.log('dashCd',await pg.evaluate(()=>TDST.P.dashCd.toFixed(2)));
 for(const [key,nm,shots] of [['KeyQ','Q',[12,26]],['KeyF','F',[24,60]],['KeyC','C',[30,70]],['KeyX','X',[30,52,62,80]]]){
  await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.cd=0;P.kit.ult.cd=0;P.mp=TDST.S?TDST.S.mp:100;const G=TDST.GG();for(const e of G.enemies)if(!e.dead&&!e.boss){e.chuSa=3;e.chuSaT=G.t+6}});
  const before=await pg.evaluate(()=>[TDST.GG().enemies.filter(e=>!e.dead).reduce((t,e)=>t+e.hp,0),TDST.P.mp,TDST.P.combo]);
  await pg.keyboard.press(key);let t=0;for(const s0 of shots){await step(s0-t);t=s0;await pg.screenshot({path:`${OUT}/skill_${nm}_${s0}_${GEN}.png`})}
  await step(120-t);
  const after=await pg.evaluate(()=>[TDST.GG().enemies.filter(e=>!e.dead).reduce((t,e)=>t+e.hp,0),TDST.P.mp,TDST.P.combo,TDST.GG().enemies.filter(e=>e.tanHon>TDST.GG().t).length]);
  console.log(nm,'máu quái',Math.round(before[0]),'→',Math.round(after[0]),'| nội lực',Math.round(before[1]),'→',Math.round(after[1]),'| liên kích',before[2],'→',after[2],'| tán hồn',after[3]);
 }
 // popup (i) của 4 ô + lướt
 for(const k of ['a0','a1','a2','u','dash']){const ok=await pg.evaluate(k=>{const el=document.querySelector(`[data-info="${k}"]`);if(!el)return null;el.click();return [document.querySelector('#skillInspectTitle').textContent,[...document.querySelectorAll('#skillInspectStats dt')].map((d,i)=>d.textContent+': '+document.querySelectorAll('#skillInspectStats dd')[i].textContent).join(' | ')]},k);
  console.log('popup',k,JSON.stringify(ok));if(k==='u')await pg.screenshot({path:`${OUT}/popup_${k}_${GEN}.png`});await pg.evaluate(()=>document.querySelector('#skillInspectClose').click());}
 console.log('errors',errs.length,errs.slice(0,6));await b.close()})();
