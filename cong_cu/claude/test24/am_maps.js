const L=require('/home/user/HoaThan/cong_cu/claude/rec_lib');
(async()=>{const maps=['am_hoangtuyen','am_biangan','am_nghiepkinh','am_uongtu','am_vongxuyen','am_diemla','am_luanhoi'];
const {b,pg,errs}=await L.open('/home/user/HoaThan/game',{gender:'nam',w:1100,h:620});
for(let f=0;f<7;f++){const fl=[1,4,7,10,12,15,18][f];
 await pg.evaluate(()=>{newRun(false,1)});await pg.waitForTimeout(500);
 await pg.evaluate((fl)=>{const G=TDST.GG();amStartFloor(fl);G.enemies.length=0;G.spawnQ.length=0;TDST.P.hp=1e9},fl);
 for(let k=0;k<20;k++)await pg.evaluate(()=>__step(1000/30));
 await pg.screenshot({path:`/tmp/mp_${maps[f]}.png`});
 await pg.evaluate(()=>{const P=TDST.P;P.x=1600;P.y=900;TDST.GG().cam.x=1600;TDST.GG().cam.y=800});for(let k=0;k<20;k++)await pg.evaluate(()=>__step(1000/30));
 await pg.screenshot({path:`/tmp/mp2_${maps[f]}.png`});
 await pg.evaluate(()=>{TDST.endRun(false)});await pg.waitForTimeout(1200);await pg.evaluate(()=>{document.querySelector('#againBtn').click()});await pg.waitForTimeout(300);
 await pg.evaluate(()=>{window.save&&0});
}
console.log('errors',errs.slice(0,5));await b.close()})();
