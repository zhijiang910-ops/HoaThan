// Soi 6 mục hotfix Quyền Cước (29/11): R theo mốc 0,3/0,6/0,72/0,9/1,15/1,35/1,55 s, Q dây chỉ, F trận, E bùa văng + nổ, lướt, ấn Chu Sa, HUD.
// node cong_cu/claude/test28/quyen_hotfix.js <ra> [WxH]
const ROOT=require('path').resolve(__dirname,'../../..');const L=require(ROOT+'/cong_cu/claude/rec_lib');const fs=require('fs');
const OUT=process.argv[2],[W,H]=(process.argv[3]||'852x393').split('x').map(Number);fs.mkdirSync(OUT,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT+'/game',{w:W,h:H,dsf:2});
 await pg.addInitScript(()=>{try{const s=JSON.parse(localStorage.getItem('tdst'));s.prof.sect='thiencuong';s.prof.weapon='quyen';localStorage.setItem('tdst',JSON.stringify(s))}catch(e){}});
 await pg.reload();await pg.waitForTimeout(2500);await pg.evaluate(()=>clearInterval(__auto));
 const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;if(P)P.hp=1e9})};
 await pg.evaluate(()=>document.querySelector('.lbt[data-lb="amgioi"]').click());await step(2);await pg.click('#amGo');await pg.waitForTimeout(1600);await step(60);
 await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.lvl=Math.max(1,s.lvl);P.kit.ult.lvl=Math.max(1,P.kit.ult.lvl);TDST.hudSkills()});
 const gather=async()=>pg.evaluate(()=>{const G=TDST.GG(),P=TDST.P;let i=0;for(const e of G.enemies)if(!e.dead&&!e.boss){const a=i++*0.9;e.x=P.x+150+Math.cos(a)*60;e.y=P.y+Math.sin(a)*40;e.hp=e.mhp}});
 const prep=async()=>{await gather();await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.cd=0;P.kit.ult.cd=0;P.mp=999;P.facing=1;P.aimAng=0;const G=TDST.GG();for(const e of G.enemies)if(!e.dead){e.chuSa=3;e.chuSaT=G.t+6}})};
 const shot=async n=>pg.screenshot({path:`${OUT}/${n}.png`});
 await prep();await step(2);await shot('an_chu_sa');
 const seq=async(key,name,marks)=>{await prep();await pg.keyboard.press(key);let t=0;for(const m of marks){await step(Math.round(m*60)-t);t=Math.round(m*60);await shot(`${name}_${m}`)}await step(40)};
 await seq('KeyX','R',[0.3,0.6,0.7,0.8,1.0,1.15,1.35,1.55]);
 await seq('KeyQ','Q',[0.3,0.4]);
 await seq('KeyF','F',[0.33,0.42,1.6]);
 await seq('KeyC','E',[0.35,0.6,1.0,1.12]);
 await prep();await pg.evaluate(()=>{TDST.P.dashCd=0});await pg.keyboard.press('Space');for(const m of [0.05,0.2,0.65]){await step(Math.round(m*60)-(m===0.05?0:0));await shot('luot_'+m)}
 await step(30);await pg.screenshot({path:`${OUT}/hud.png`,clip:{x:W-260,y:H-140,width:260,height:140}});await pg.screenshot({path:`${OUT}/hud_luot.png`,clip:{x:0,y:H-140,width:260,height:140}});
 console.log('errors',errs.length,errs.slice(0,4));await b.close()})();
