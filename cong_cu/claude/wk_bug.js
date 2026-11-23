// Soi lỗi từng chiêu Ngộ Không: quái thật, nhiều hướng, đứng/chạy. Chụp cận cảnh quanh Ngộ Không.
const L=require('./rec_lib');const fs=require('fs');const [ROOT,OUT]=process.argv.slice(2);
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:'nam',forge:0,w:1100,h:620,mobile:false});
 await pg.evaluate(()=>{localStorage.setItem('tdst_tr',JSON.stringify({god:'wukong',fold:true,rage:true,god_on:true,forge:6,scale:1}))});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>clearInterval(__auto));await pg.click('#trP [data-t=hoa]');await pg.evaluate(()=>{document.getElementById('trP').style.display='none'});
 for(let k=0;k<70;k++)await pg.evaluate(()=>__step(1000/60));
 fs.mkdirSync(OUT,{recursive:true});let n=0;const log=[];
 const lock=`(()=>{const P=TDST.P;for(const s of P.god.sk)if(s.cd>0.7)s.cd=99;if(P.god.ult&&P.god.ult.cd>1)P.god.ult.cd=99;if(window.__nob)P.god.basic.cd=99})()`;
 const shot=async(N,tag,mv)=>{for(let k=0;k<N;k++){await pg.evaluate(([l,mv])=>{if(mv)window.__mv=mv;__step(1000/60);eval(l)},[lock,mv]);
   const p=await pg.evaluate(()=>{const P=TDST.P,G=TDST.GG();const cx=innerWidth/2,cy=innerHeight/2;return {x:P.x,y:P.y,f:P.facing}});
   await pg.screenshot({path:`${OUT}/${tag}_${String(k).padStart(3,'0')}.png`,clip:{x:250,y:110,width:600,height:400}})}};
 const clear=()=>pg.evaluate(()=>{const G=TDST.GG();for(const e of G.enemies)e.dead=true;G.enemies=G.enemies.filter(e=>!e.dead);G.allies=[];G.fx=[];G.zones=[]});
 const spawn=(dx,dy,t)=>pg.evaluate(([dx,dy,t])=>{const P=TDST.P;const e=TDST.spawnEnemy(t||'soi',P.x+dx,P.y+dy);if(e){e.hp=e.mhp=1e7;e.spd=0}},[dx,dy,t]);
 // 1. đòn thường, quái bên trái
 await clear();await spawn(-110,0);await spawn(-100,40);await pg.evaluate(()=>{window.__nob=0;const P=TDST.P;for(const s of P.god.sk)s.cd=99;P.god.ult.cd=99});await shot(60,'a_trai');
 // 2. đòn thường, quái phía trên
 await clear();await spawn(10,-120);await shot(50,'b_tren');
 // 3. đòn thường khi đang chạy (giữ phím D)
 await clear();await spawn(130,0);await pg.keyboard.down('KeyD');await shot(50,'c_chay');await pg.keyboard.up('KeyD');
 // 7. ult
 await clear();await spawn(-60,-150);await spawn(-40,-120);await pg.evaluate(()=>{window.__nob=1;TDST.P.god.ult.cd=0});await shot(55,'g_ult');
 // 4. khỉ con
 await clear();await spawn(-160,0);await spawn(150,30);await spawn(60,-140);await pg.evaluate(()=>{window.__nob=1;TDST.P.god.sk[0].cd=0});await shot(80,'d_khi');
 // 5. Cân Đẩu Vân
 await clear();await spawn(250,40);await spawn(270,70);await pg.evaluate(()=>{TDST.P.god.sk[1].cd=0});await shot(50,'e_may');
 // 6. Kim Cô Bổng mở rộng
 await clear();await spawn(-200,0);await spawn(150,90);await pg.evaluate(()=>{TDST.P.god.sk[2].cd=0});await shot(55,'f_morong');
 console.log(errs);await b.close()})();
