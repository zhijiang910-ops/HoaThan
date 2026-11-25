const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const OUT=process.argv[2];
(async()=>{const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',forge:6,w:1100,h:620});
 await pg.evaluate(()=>clearInterval(__auto));
 const step=async n=>{for(let i=0;i<n;i++)await pg.evaluate(()=>__step(1000/60))};
 const st=()=>pg.evaluate(()=>{const G=TDST.GG();return G&&G.am?{floor:G.am.floor,phase:G.am.phase,guardOut:G.am.guardOut,chest:!!G.am.chest,open:G.am.chest&&G.am.chest.open,portal:!!G.am.portal,en:G.enemies.filter(e=>!e.dead).length,q:G.spawnQ.length,state:G.state,over:G.over,paused:G.paused}:null});
 const log=[];
 // vào Âm Giới
 await pg.click('.lbt[data-lb="amgioi"]');await step(2);
 const modal=await pg.evaluate(()=>({title:document.querySelector('#lbmT').textContent,go:document.querySelector('#amGo').textContent,dis:document.querySelector('#amGo').disabled,tile:document.querySelector('.lbt[data-lb="amgioi"] small').textContent}));
 log.push(['modal',JSON.stringify(modal)]);
 await pg.screenshot({path:OUT+'/am_modal.png'});
 await pg.click('#amGo');await step(80);
 log.push(['start',JSON.stringify(await st())]);
 await pg.screenshot({path:OUT+'/am_floor1.png'});
 for(let floor=1;floor<=3;floor++){
  // diệt âm binh
  let tries=0;
  while(tries++<400){await pg.evaluate(()=>{const G=TDST.GG();TDST.P.hp=1e9;for(const e of G.enemies){if(!e.dead&&!e.amG)TDST.hit(e,1e9,{src:'h',t:'w'},0,0)}});await step(6);const s=await st();if(s&&s.guardOut)break}
  log.push(['f'+floor+' guardOut',JSON.stringify(await st())]);
  await step(60);await pg.screenshot({path:OUT+`/am_f${floor}_guard.png`});
  const gdesc=await pg.evaluate(()=>TDST.GG().enemies.filter(e=>e.amG&&!e.dead).map(e=>e.nm+':'+e.type));log.push(['f'+floor+' guards',gdesc.join(' | ')]);
  // hạ kẻ canh
  tries=0;while(tries++<200){await pg.evaluate(()=>{const G=TDST.GG();TDST.P.hp=1e9;for(const e of G.enemies){if(!e.dead&&e.amG){e.hp=1;TDST.hit(e,1e9,{src:'h',t:'w'},0,0)}}});await step(10);const s=await st();if(s&&s.chest)break}
  log.push(['f'+floor+' chest',JSON.stringify(await st())]);
  await pg.screenshot({path:OUT+`/am_f${floor}_chest.png`});
  // đi tới rương
  await pg.evaluate(()=>{const G=TDST.GG();TDST.P.x=G.am.chest.x;TDST.P.y=G.am.chest.y});await step(10);
  const loot=await pg.evaluate(()=>({vis:!document.querySelector('#tacloot').hidden,title:document.querySelector('#tlTitle').textContent,go:document.querySelector('#tlGo').textContent,cards:document.querySelectorAll('#tlList .lcard').length}));
  log.push(['f'+floor+' loot',JSON.stringify(loot)]);if(floor===1)await pg.screenshot({path:OUT+'/am_loot.png'});
  await pg.click('#tlGo');await step(10);
  log.push(['f'+floor+' portal',JSON.stringify(await st())]);
  await pg.screenshot({path:OUT+`/am_f${floor}_portal.png`});
  await pg.evaluate(()=>{const G=TDST.GG();TDST.P.x=G.am.portal.x;TDST.P.y=G.am.portal.y});await step(12);
  if(floor<3){
   const br=await pg.evaluate(()=>({brk:!document.querySelector('#brk').hidden,bw:document.querySelector('#bwave').textContent,picks:TDST.GG().picks}));log.push(['f'+floor+' break',JSON.stringify(br)]);
   if(floor===1)await pg.screenshot({path:OUT+'/am_break.png'});
   await pg.evaluate(()=>{TDST.GG().picks=0;});await pg.evaluate(()=>{document.querySelector('#contBtn').disabled=false});await pg.click('#contBtn');await step(90);
   log.push(['f'+(floor+1)+' enter',JSON.stringify(await st())]);
  }
 }
 await step(260);
 const end=await pg.evaluate(()=>({vis:!document.querySelector('#end').hidden,title:document.querySelector('#endTitle').textContent,sub:document.querySelector('#endSub').textContent,again:document.querySelector('#againBtn').hidden,am:JSON.stringify(TDST.save?0:0)}));
 log.push(['end',JSON.stringify(end)]);await pg.screenshot({path:OUT+'/am_end.png'});
 for(const [k,v] of log)console.log(k,v);
 console.log('errors',errs.length,errs.slice(0,3));await b.close()})();
