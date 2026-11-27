// Luồng thật: tạo nhân vật mới -> đặt tên, chọn chân dung, đổi màu, chọn phái, bấm Khởi hành 3 lần liền -> vào sảnh
const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');const fs=require('fs');const OUT=process.argv[2];fs.mkdirSync(OUT,{recursive:true});
(async()=>{for(const [w,h] of (process.argv[3]||'852x393,811x260').split(',').map(x=>x.split('x').map(Number))){
 const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',w,h,seed:false,dsf:2});
 await pg.evaluate(()=>clearInterval(__auto));
 await pg.evaluate(()=>TDST.openCreate());await pg.waitForTimeout(900);
 await pg.screenshot({path:`${OUT}/${w}x${h}_0_chua_ten.png`});
 await pg.fill('#crName','Lý Tiêu Dao');
 const av=await pg.$$('#crAvatars button');await pg.click('#crAvatars button >> nth=3');
 const oc=await pg.$$('#crOutC button');await pg.click('#crOutC button >> nth=3');
 const sc=await pg.$$('#crSect button');const names=[];for(const x of sc)names.push(await x.evaluate(e=>e.textContent.trim()));
 await pg.click('#crSect button >> nth=3');await pg.waitForTimeout(300);
 await pg.screenshot({path:`${OUT}/${w}x${h}_1_thiencuong.png`});
 await pg.click('#crSect button >> nth=1');await pg.waitForTimeout(300);
 const dis=await pg.evaluate(()=>document.querySelector('#crGo').disabled);
 await pg.screenshot({path:`${OUT}/${w}x${h}_2_phai_khoa.png`});
 await pg.click('#crSect button >> nth=0');await pg.waitForTimeout(300);
 await pg.screenshot({path:`${OUT}/${w}x${h}_3_maoson.png`});
 const g=await pg.evaluate(()=>{const r=document.querySelector('#crGo').getBoundingClientRect(),R=document.querySelector('.cxR').getBoundingClientRect(),q=document.querySelector('#crSkD').getBoundingClientRect();
  return{btn:[r.left,r.top,r.width,r.height].map(Math.round),panel:[R.left,R.top,R.width,R.height].map(Math.round),desc_bottom:Math.round(q.bottom),vh:innerHeight,
   hitCenter:document.elementFromPoint(r.left+r.width/2,r.top+r.height/2).id,hitEdge:document.elementFromPoint(r.left+6,r.top+r.height/2).id,
   cls:document.querySelector('#crGo').className}});
 await pg.evaluate(()=>{window.__nLobby=0;const o=window.showLobby;});
 const bx=g.btn[0]+g.btn[2]/2,by=g.btn[1]+g.btn[3]/2;
 await pg.mouse.click(bx,by);await pg.waitForTimeout(60);await pg.mouse.click(bx,by);await pg.waitForTimeout(60);await pg.mouse.click(bx,by);await pg.waitForTimeout(1500);
 const st=await pg.evaluate(()=>{const s=JSON.parse(localStorage.getItem('tdst')||'{}');return{createHidden:document.querySelector('#create').hidden,lobbyHidden:document.querySelector('#lobby').hidden,prof:s.prof&&{name:s.prof.name,sect:s.prof.sect,avatar:s.prof.avatar,outC:s.prof.outC,created:s.prof.created}}});
 await pg.screenshot({path:`${OUT}/${w}x${h}_4_sanh.png`});
 console.log(w+'x'+h,JSON.stringify({g,lockedDisabled:dis,sects:names,st}),'errs',errs.length,errs.slice(0,2));await b.close()}process.exit(0)})();
