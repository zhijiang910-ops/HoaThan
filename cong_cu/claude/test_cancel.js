// Kiểm tra: Lướt hủy được lúc lấy đà, không hủy được lúc lướt chém; tường chặn
const fs=require('fs');let src=fs.readFileSync(__dirname+'/test_c.js','utf8');
src=src.replace(/ for\(let k=0;k<16;k\+\+\)[\s\S]*?console\.log\('errs'/,` const r=await pg.evaluate(async()=>{const P=TDST.P,G=TDST.G,w=ms=>new Promise(r=>setTimeout(r,ms));const out={};
  P.kit.basic.step=2;P.kit.basic.cd=0;P.dashCd=0;
  while(!P.cutC)await w(5);await w(60);out.windT=+P.cutC.t.toFixed(2);dispatchEvent(new KeyboardEvent('keydown',{code:'Space',key:' '}));await w(30);dispatchEvent(new KeyboardEvent('keyup',{code:'Space',key:' '}));
  out.afterDashInWind={cutC:!!P.cutC,dashT:+P.dashT.toFixed(2)};
  await w(600);P.x=1500;P.y=1100;G.enemies.forEach((e,i)=>{e.x=P.x+60+i*45;e.y=P.y});P.kit.basic.step=2;P.kit.basic.cd=0;P.dashCd=0;
  while(!P.cutC||P.cutC.t<0.2)await w(5);out.lockedT=+P.cutC.t.toFixed(2);dispatchEvent(new KeyboardEvent('keydown',{code:'Space',key:' '}));await w(20);dispatchEvent(new KeyboardEvent('keyup',{code:'Space',key:' '}));
  out.afterDashInLunge={cutC:!!P.cutC,dashT:+P.dashT.toFixed(2)};return out});
 console.log(JSON.stringify(r));
 console.log('errs'`);
fs.writeFileSync(__dirname+'/test_cancel_run.js',src);
