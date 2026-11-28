// Luyện Công (Quyền): F hố, R timeline, Q nối quái
const ROOT='/home/user/KhuTaDietMa';const L=require(ROOT+'/cong_cu/claude/rec_lib');const O=process.argv[2],[W,H]=(process.argv[3]||'852x393').split('x').map(Number);require('fs').mkdirSync(O,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT+'/game',{w:W,h:H,dsf:2});
 await pg.addInitScript(()=>{try{const s=JSON.parse(localStorage.getItem('tdst'));s.prof.sect='thiencuong';s.prof.weapon='quyen';localStorage.setItem('tdst',JSON.stringify(s))}catch(e){}});
 await pg.reload();await pg.waitForTimeout(2500);
 const g=await pg.evaluate(()=>document.querySelector('#lbGrid .lbt[data-s="6"]').getBoundingClientRect());await pg.mouse.click(g.x+g.width/2,g.y+g.height/2);await pg.waitForTimeout(2500);
 await pg.evaluate(()=>{clearInterval(__auto);const f=document.querySelector('#trP');if(f)f.classList.add('fold')});
 const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;if(P)P.hp=1e9})};
 await step(30);
 const info=await pg.evaluate(()=>{const G=TDST.GG(),P=TDST.P;return {map:G.map||null,en:G.enemies.length,w:P.kit&&P.kit.act.map(s=>s.def.id)}});console.log(JSON.stringify(info));
 await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.lvl=Math.max(1,s.lvl);P.kit.ult.lvl=Math.max(1,P.kit.ult.lvl);TDST.hudSkills()});
 const prep=async()=>pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.cd=0;P.kit.ult.cd=0;P.mp=999;P.facing=1;P.aimAng=0});
 const seq=async(key,name,marks)=>{await prep();await pg.keyboard.press(key);let t=0;for(const m of marks){await step(Math.round(m*60)-t);t=Math.round(m*60);await pg.screenshot({path:`${O}/${name}_${m}.png`})}await step(120)};
 await seq('KeyF','F',[0.4,1.5,2.8]);
 await seq('KeyX','R',[0.3,0.6,0.66,0.72,0.95,1.15,1.35,1.5]);
 await seq('KeyQ','Q',[0.3,0.42,0.5,0.6]);
 console.log('errors',errs.length,errs.slice(0,4));await b.close()})();
