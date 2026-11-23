const {chromium,devices}=require('playwright');
(async()=>{const b=await chromium.launch();
 for(const [n,land] of [['iPhone 14',true],['iPhone 14',false],['Galaxy S9+',true]]){
 const d={...devices[n]};if(land){d.viewport={width:d.viewport.height,height:d.viewport.width}}
 const ctx=await b.newContext(d);const pg=await ctx.newPage();
 try{await pg.goto('https://claude.ai/artifact/7HgwkR1wd2kZ521bQ1oRTA',{timeout:45000});await pg.waitForTimeout(8000)}catch(e){console.log('ERR',e.message.split('\n')[0])}
 const fr=await pg.evaluate(()=>[...document.querySelectorAll('iframe')].map(f=>{const r=f.getBoundingClientRect();return {src:(f.src||'').slice(0,80),x:r.x,y:r.y,w:r.width,h:r.height}}));
 console.log(n,land?'ngang':'dọc','vp',d.viewport,'title',await pg.title(),JSON.stringify(fr));
 await pg.screenshot({path:'art_'+n.replace(/ /g,'')+(land?'_L':'_P')+'.png'});await ctx.close()}
 await b.close()})();
