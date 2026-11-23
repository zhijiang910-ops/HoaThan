const L=require('./rec_lib');const O=process.argv[3];
(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{w:844,h:390,mobile:true,seed:false});
 await pg.screenshot({path:O+'/u1_create.png'});await pg.click('text=Nữ').catch(()=>{});await pg.waitForTimeout(400);await pg.screenshot({path:O+'/u2_create_nu.png'});
 await pg.fill('input','Thu');await pg.click('#crGo');await pg.waitForTimeout(1200);await pg.screenshot({path:O+'/u3_lobby.png'});
 await pg.locator('button',{hasText:'Kho Đồ'}).first().click();await pg.waitForTimeout(800);await pg.screenshot({path:O+'/u4_kho.png'});
 await pg.evaluate(()=>TDST.newRun());await pg.waitForTimeout(1500);await pg.screenshot({path:O+'/u5_play.png'});
 console.log(errs);await b.close()})();
