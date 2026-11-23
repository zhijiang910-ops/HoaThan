const L=require('./rec_lib');
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{gender:'nam',w:844,h:390,mobile:true});await L.startRun(pg);await pg.waitForTimeout(800);
 const r=await pg.evaluate(()=>{const out=[];const q=s=>[...document.querySelectorAll(s)];
  for(const sel of ['#dashBtn','#skills','#skills > *','.sk','#quests','#hud','#vbars','#avatar','#godBtn','.skr']){for(const e of q(sel).slice(0,12)){const b=e.getBoundingClientRect();if(!b.width)continue;out.push(sel+' id='+e.id+' cls='+e.className+' '+[b.x,b.y,b.width,b.height].map(Math.round).join(',')+' txt='+(e.innerText||'').replace(/\s+/g,' ').slice(0,30))}}
  // tiny text
  const tiny={};for(const e of q('#game *, body *')){if(!e.offsetParent||!e.childNodes.length)continue;const t=[...e.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim()).map(n=>n.textContent.trim()).join(' ');if(!t)continue;const fs=parseFloat(getComputedStyle(e).fontSize);if(fs<10.5){const k=fs.toFixed(1);(tiny[k]=tiny[k]||[]).push((e.id||e.className||e.tagName)+':'+t.slice(0,18))}}
  return {out,tiny}});
 console.log(r.out.join('\n'));for(const k in r.tiny)console.log('FONT',k,r.tiny[k].slice(0,14).join(' | '));
 await pg.screenshot({path:__dirname+'/'+(process.argv[3]||'hud_after')+'.png'});console.log(errs);await b.close()})();
