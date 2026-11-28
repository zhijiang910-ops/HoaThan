// Phá Sát Môn (Trường Thương) trong Luyện Công: node phasat.js <ra> [WxH] [forge]
const ROOT='/home/user/hoathan';const L=require(ROOT+'/cong_cu/claude/rec_lib');const O=process.argv[2],[W,H]=(process.argv[3]||'852x393').split('x').map(Number);const FORGE=+(process.argv[4]||6);require('fs').mkdirSync(O,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT+'/game',{w:W,h:H,dsf:2,forge:FORGE});
 await pg.addInitScript(()=>{try{const s=JSON.parse(localStorage.getItem('tdst'));s.prof.sect='phucma';s.prof.weapon='truong';localStorage.setItem('tdst',JSON.stringify(s))}catch(e){}});
 await pg.reload();await pg.waitForTimeout(2500);
 const g=await pg.evaluate(()=>document.querySelector('#lbGrid .lbt[data-s="6"]').getBoundingClientRect());await pg.mouse.click(g.x+g.width/2,g.y+g.height/2);await pg.waitForTimeout(2500);
 await pg.evaluate(()=>{clearInterval(__auto);const f=document.querySelector('#trP');if(f)f.classList.add('fold')});
 const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;if(P)P.hp=Math.max(P.hp,1e9)})};
 await step(30);
 const info=await pg.evaluate(()=>{const P=TDST.P;return {w:P.kit.w,act:P.kit.act.map(s=>s.def.id),ult:P.kit.ult&&P.kit.ult.def.id,pf:Object.keys(P.pf||{}),en:TDST.GG().enemies.length}});console.log(JSON.stringify(info));
 await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.lvl=Math.max(1,s.lvl);P.kit.ult.lvl=Math.max(1,P.kit.ult.lvl);TDST.hudSkills()});
 const prep=async()=>pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.cd=0;P.kit.ult.cd=0;P.mp=999;P.facing=1;P.aimAng=0});
 let n=0;const rec=async(key,name,secs)=>{await prep();if(key)await pg.keyboard.press(key);for(let i=0;i<secs*30;i++){await step(2);await pg.screenshot({path:`${O}/${name}_${String(n++).padStart(4,'0')}.png`})}};
 const dump=async()=>pg.evaluate(()=>TDST.GG().enemies.filter(e=>e.psB).map(e=>[e.psB,Math.round(e.hp)]).slice(0,5));
 await rec(null,'A',3);console.log('bleed after basic',JSON.stringify(await dump()));
 await rec('KeyQ','Q',1.6);console.log('bleed after Q',JSON.stringify(await dump()));
 await prep();await pg.keyboard.press('KeyF');await step(20);await pg.evaluate(()=>TDST.hurtPlayer(50,null));console.log('parry',JSON.stringify(await pg.evaluate(()=>({q:TDST.P.kit.act.find(s=>s.def.hotkey==='Q').cd,qe:TDST.P.psQE}))));
 for(let i=0;i<45;i++){await step(2);await pg.screenshot({path:`${O}/F_${String(n++).padStart(4,'0')}.png`})}
 await rec('KeyC','C',1.6);console.log('bleed after C',JSON.stringify(await dump()));
 await rec('KeyX','X',2.2);console.log('bleed after X',JSON.stringify(await dump()));
 await rec('KeyV','V',3.4);
 console.log('errors',errs.length,errs.slice(0,4));await b.close()})();
