// node sectclip.js <ra> <sect> <weapon> <forge> <WxH> <seq>  seq: tên:phím:giây[:hold],... ; phím rỗng = chỉ chờ
const ROOT='/home/user/hoathan';const L=require(ROOT+'/cong_cu/claude/rec_lib');const [O,SECT,WP,FG,WH,SEQ]=process.argv.slice(2);const [W,H]=WH.split('x').map(Number);require('fs').mkdirSync(O,{recursive:true});
(async()=>{const {b,pg,errs}=await L.open(ROOT+'/game',{w:W,h:H,dsf:2,forge:+FG});
 await pg.addInitScript(([a,c])=>{try{const s=JSON.parse(localStorage.getItem('tdst'));s.prof.sect=a;s.prof.weapon=c;localStorage.setItem('tdst',JSON.stringify(s))}catch(e){}},[SECT,WP]);
 await pg.reload();await pg.waitForTimeout(2500);
 const g=await pg.evaluate(()=>document.querySelector('#lbGrid .lbt[data-s="6"]').getBoundingClientRect());await pg.mouse.click(g.x+g.width/2,g.y+g.height/2);await pg.waitForTimeout(2500);
 await pg.evaluate(()=>{clearInterval(__auto);const f=document.querySelector('#trP');if(f)f.classList.add('fold')});
 const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>{__step(1000/60);const P=TDST.P;if(P)P.hp=Math.max(P.hp,1e9)})};
 await pg.evaluate(n=>{window.__near=n},process.env.NEAR?1:0);await step(30);
 await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.lvl=Math.max(1,s.lvl);P.kit.ult.lvl=Math.max(1,P.kit.ult.lvl);TDST.hudSkills()});
 let n=0;for(const it of SEQ.split(',')){const [name,key,sec,hold]=it.split(':');
  await pg.evaluate(()=>{const P=TDST.P;for(const s of P.kit.act)s.cd=0;P.kit.ult.cd=0;P.mp=999;P.facing=1;P.aimAng=0;if(window.__near){const es=TDST.GG().enemies.filter(e=>!e.dead);if(es.length){const m=es.reduce((a,e)=>e.x<a.x&&e.x>P.x-300?e:a,es[0]);P.x=m.x-60;P.y=m.y}}});
  if(key){if(hold)await pg.evaluate(()=>{window.__dhQdown=true});await pg.keyboard.press(key)}
  const tot=Math.round(+sec*30),hh=hold?Math.round(+hold*30):-1;
  for(let i=0;i<tot;i++){if(i===hh)await pg.evaluate(()=>{window.__dhQdown=false});await step(2);await pg.screenshot({path:`${O}/${String(n++).padStart(4,'0')}_${name}.png`})}}
 console.log('errors',errs.length,errs.slice(0,3));await b.close()})();
