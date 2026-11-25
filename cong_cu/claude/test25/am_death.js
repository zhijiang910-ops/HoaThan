const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>clearInterval(__auto));const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/60))};
 const q=s=>pg.evaluate(s=>document.querySelector(s)&&document.querySelector(s).textContent,s);
 const am=()=>pg.evaluate(()=>JSON.parse(localStorage.getItem('tdst')||'{}').am||null);
 const out=[];
 // lượt 1: gục ngã
 await pg.click('.lbt[data-lb="amgioi"]');await step(2);await pg.click('#amGo');await step(80);
 out.push(['sau khi vào',JSON.stringify(await am())]);
 await pg.evaluate(()=>{document.querySelector('#quitBtn').click();document.querySelector('#quitBtn').click()});await step(80);await pg.evaluate(()=>{});
 await new Promise(r=>setTimeout(r,200));await step(70);
 out.push(['end1',JSON.stringify({vis:await pg.evaluate(()=>!document.querySelector('#end').hidden),t:await q('#endTitle'),again:await pg.evaluate(()=>document.querySelector('#againBtn').hidden)})]);
 out.push(['am sau gục',JSON.stringify(await am())]);
 await pg.screenshot({path:OUT+'/am_death.png'});
 await pg.click('#menuBtn');await step(5);
 out.push(['tile sau về sảnh',await q('.lbt[data-lb="amgioi"] small'),'againBtn hidden='+await pg.evaluate(()=>document.querySelector('#againBtn').hidden)]);
 // lượt 2 -> hết lượt
 await pg.click('.lbt[data-lb="amgioi"]');await step(2);await pg.click('#amGo');await step(80);
 await pg.evaluate(()=>{document.querySelector('#quitBtn').click();document.querySelector('#quitBtn').click()});await step(80);await new Promise(r=>setTimeout(r,200));await step(70);
 await pg.click('#menuBtn');await step(5);
 await pg.click('.lbt[data-lb="amgioi"]');await step(2);
 out.push(['hết lượt',JSON.stringify({tile:await q('.lbt[data-lb="amgioi"] small'),goDisabled:await pg.evaluate(()=>document.querySelector('#amGo').disabled),am:await am()})]);
 // qua ngày
 await pg.evaluate(()=>{const s=JSON.parse(localStorage.getItem('tdst'));s.am.day='2000-01-01';localStorage.setItem('tdst',JSON.stringify(s))});
 await pg.reload();await pg.waitForTimeout(2500);await pg.evaluate(()=>clearInterval(__auto));
 out.push(['sau reload ngày cũ',await q('.lbt[data-lb="amgioi"] small')]);
 for(const [k,...v] of out)console.log(k,...v);console.log('errors',errs.length,errs.slice(0,3));await b.close()})();
