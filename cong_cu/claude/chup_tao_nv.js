// Chụp màn tạo nhân vật ở 7 cỡ bắt buộc (luật 10) và in vị trí nút Khởi hành.
// Chạy từ gốc repo:  node cong_cu/claude/chup_tao_nv.js <thư_mục_ra> [nam|nu]
// Cần: npm i playwright (Chromium). Không cần mở cổng, đường dẫn tự suy ra.
const path=require('path'),fs=require('fs');
const L=require('./rec_lib');
const ROOT=path.resolve(__dirname,'../../game');
const OUT=path.resolve(process.argv[2]||'anh_kiem');const G=process.argv[3]||'nam';
fs.mkdirSync(OUT,{recursive:true});
(async()=>{let bad=0;
for(const [w,h] of [[550,278],[811,260],[667,375],[852,393],[932,430],[956,440],[1100,620],[1280,720]]){
 const {b,pg,errs}=await L.open(ROOT,{gender:G,w,h,seed:false});
 await pg.evaluate(()=>clearInterval(__auto));
 await pg.evaluate(()=>TDST.openCreate());await pg.waitForTimeout(800);
 const r=await pg.evaluate(()=>{const g=document.querySelector('#crGo').getBoundingClientRect();return {top:Math.round(g.top),bottom:Math.round(g.bottom),vh:innerHeight}});
 const ok=r.bottom<=r.vh&&r.top>=0;if(!ok||errs.length)bad++;
 console.log(`${w}x${h}`,JSON.stringify(r),ok?'nút trong khung':'NÚT LỌT KHUNG','lỗi trang:',errs.length);
 await pg.screenshot({path:`${OUT}/tao_nv_${w}x${h}.png`});await b.close()}
console.log(bad?`CÓ ${bad} cỡ lỗi`:'Đạt cả 7 cỡ. Ảnh ở '+OUT);process.exit(bad?1:0)})();
