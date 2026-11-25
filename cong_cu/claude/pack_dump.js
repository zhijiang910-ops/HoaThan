// Xuất danh sách ảnh của từng GÓI (bản đồ, hiệu ứng theo phái, quái theo tầng/map, sheet nhân vật, thần tướng) + dung lượng tải lúc mở game.
// Dùng: NODE_PATH=$(npm root -g) node cong_cu/claude/pack_dump.js <file ra .json>
const path=require('path'),fs=require('fs');const L=require('./rec_lib');
(async()=>{const ROOT=path.resolve(__dirname,'../../game');
const {b,pg,errs}=await L.open(ROOT,{gender:'nam',w:844,h:390,dsf:2,mobile:true});
await pg.waitForTimeout(6000);
const packs=await pg.evaluate(()=>window.__packs());
const boot=await pg.evaluate(()=>performance.getEntriesByType('resource').filter(r=>/\/assets\//.test(r.name)).map(r=>[r.name.replace(/^.*\/assets\//,'assets/'),r.encodedBodySize||0]));
packs.boot=boot;fs.writeFileSync(process.argv[2],JSON.stringify(packs));
console.log('đã ghi',process.argv[2],'| lỗi trang',errs.length);await b.close()})()
