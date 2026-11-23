import json
S='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/'
data=open(S+'catalog/data.json',encoding='utf-8').read()
HTML=r'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lọc Asset Wuxia</title>
<style>
:root{--bg:#16181d;--pn:#1f232b;--pn2:#272c36;--ln:#363c48;--tx:#e9e4d8;--mu:#a8a294;--ac:#e2b45a;--ok:#5cb87a;--no:#d0605a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:14px/1.45 system-ui,"Segoe UI",sans-serif}
header{position:sticky;top:0;z-index:5;background:#121419ee;backdrop-filter:blur(6px);border-bottom:1px solid var(--ln);padding:10px 16px}
h1{margin:0 0 6px;font-size:18px;color:var(--ac)}
.tabs,.chips{display:flex;gap:6px;flex-wrap:wrap}
button{font:inherit;color:var(--tx);background:var(--pn2);border:1px solid var(--ln);border-radius:8px;padding:6px 10px;cursor:pointer}
button.on{background:var(--ac);color:#1a1408;border-color:var(--ac);font-weight:600}
main{padding:14px 16px 80px;max-width:1400px;margin:0 auto}
.note{color:var(--mu);margin:0 0 12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.card{background:var(--pn);border:1px solid var(--ln);border-radius:12px;padding:10px;display:flex;flex-direction:column;gap:8px}
.card.keep{border-color:var(--ok);box-shadow:0 0 0 1px var(--ok) inset}.card.drop{opacity:.55;border-color:var(--no)}
.stage{height:190px;background:repeating-conic-gradient(#2b303a 0 25%,#262a33 0 50%) 0 0/16px 16px;border-radius:8px;display:flex;align-items:flex-end;justify-content:center;overflow:hidden}
.spr{image-rendering:pixelated;background-repeat:no-repeat;transform-origin:bottom center}
.clips{display:flex;gap:4px;flex-wrap:wrap}.clips button{padding:3px 7px;font-size:12px}
.tag{display:inline-block;font-size:12px;padding:2px 8px;border-radius:99px;background:#3a3222;color:var(--ac);font-weight:600}
.t-chinh{background:#2c3c5a;color:#9cc4ff}.t-trum{background:#4a2626;color:#ff9c8c}.t-quai{background:#3d3020;color:#f0c070}.t-mo{background:#26402f;color:#8fe0a8}.t-npc{background:#33304a;color:#c6b8ff}.t-bo{background:#333;color:#aaa}
.nm{font-weight:700;font-size:15px}.sub{color:var(--mu);font-size:12px}.why{font-size:13px}
.sel{display:flex;gap:6px}.sel button{flex:1}.sel .k.on{background:var(--ok);border-color:var(--ok);color:#081a0e}.sel .d.on{background:var(--no);border-color:var(--no);color:#1a0806}
.ig{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.it{background:var(--pn);border:1px solid var(--ln);border-radius:10px;padding:8px;display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center;cursor:pointer}
.it img{width:64px;height:64px;object-fit:contain;image-rendering:pixelated}
.it.keep{border-color:var(--ok);box-shadow:0 0 0 1px var(--ok) inset}.it.drop{opacity:.45}
.it .u{font-size:11px;color:#8fe0a8}
h2{color:var(--ac);font-size:16px;margin:18px 0 8px}
table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid var(--ln);padding:6px 8px;text-align:left;vertical-align:top}th{color:var(--mu);font-weight:600}
.bar{position:fixed;left:0;right:0;bottom:0;background:#121419f2;border-top:1px solid var(--ln);padding:8px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
textarea{width:100%;height:220px;background:#0e1014;color:var(--tx);border:1px solid var(--ln);border-radius:8px;padding:8px;font:12px/1.4 ui-monospace,monospace}
.aud li{color:var(--mu)}
@media(max-width:600px){.grid{grid-template-columns:1fr}}
</style></head><body>
<header><h1>Lọc asset · Wuxia Pixel Assets Vol.2 + game hiện tại</h1>
<div class="tabs" id="tabs"></div></header>
<main id="main"></main>
<div class="bar"><span id="cnt" class="sub"></span><button id="exp">Xuất lựa chọn để gửi Claude</button><button id="clr">Xóa hết lựa chọn</button></div>
<script>
const D=__DATA__;
let st={};try{st=JSON.parse(localStorage.getItem('locasset')||'{}')}catch(e){}
const save=()=>{try{localStorage.setItem('locasset',JSON.stringify(st))}catch(e){};count()};
const TABS=[['chars','Nhân vật (35)'],['items','Vật phẩm (94)'],['skills','Kỹ năng & hiệu ứng (33)'],['aud','Âm thanh (125)'],['src','Nguồn hiện có trong game']];
let tab='chars',flt='all';
const $=s=>document.querySelector(s);
function tabs(){$('#tabs').innerHTML=TABS.map(([k,n])=>`<button data-t="${k}" class="${k===tab?'on':''}">${n}</button>`).join('')}
$('#tabs').onclick=e=>{const b=e.target.closest('button');if(!b)return;tab=b.dataset.t;tabs();render()};
const anims=[];
function selBtns(id){const v=st[id];return `<div class="sel"><button class="k ${v==='k'?'on':''}" data-id="${id}" data-v="k">Giữ</button><button class="d ${v==='d'?'on':''}" data-id="${id}" data-v="d">Bỏ</button></div>`}
const CL={idle:'Đứng',walk:'Đi',attack:'Chém A',attack_secondary:'Chém B',hurt:'Trúng',death:'Gục',cast:'Thi triển'};
function render(){
 anims.length=0;const m=$('#main');
 if(tab==='chars'){
  const order=['chinh','mo','quai','trum','npc','bo'];
  m.innerHTML=`<p class="note">Ảnh động hướng quay phải (game chỉ dùng hướng này, quay trái thì lật ảnh). Bấm tên động tác để xem. Thẻ màu là đề xuất của Claude; mày bấm Giữ/Bỏ theo ý mày.</p>
  <div class="chips" id="flt">${[['all','Tất cả'],...order.map(k=>[k,D.cat[k]])].map(([k,n])=>`<button data-f="${k}" class="${k===flt?'on':''}">${n}</button>`).join('')}</div><br>
  <div class="grid">${D.chars.filter(c=>flt==='all'||c.rec===flt).sort((a,b)=>order.indexOf(a.rec)-order.indexOf(b.rec)).map((c,i)=>{
   const id='c:'+c.id;const ks=Object.keys(c.clips);
   return `<div class="card ${st[id]==='k'?'keep':st[id]==='d'?'drop':''}" data-card="${id}">
   <div class="stage"><div class="spr" data-ci="${D.chars.indexOf(c)}" data-clip="${ks.includes('attack')?'attack':ks[0]}"></div></div>
   <div class="clips">${ks.map(k=>`<button data-ci="${D.chars.indexOf(c)}" data-clip="${k}">${CL[k]||k} <span class="sub">${c.clips[k].n}f</span></button>`).join('')}</div>
   <div><span class="tag t-${c.rec}">${c.recT}</span></div>
   <div class="nm">${c.name}</div><div class="sub">${c.cn}${c.weapon?' · vũ khí: '+c.weapon:''}</div>
   <div class="why">${c.why}</div>${selBtns(id)}</div>`}).join('')}</div>`;
  m.querySelectorAll('.spr').forEach(setupSpr);
 }else if(tab==='items'){
  const g={};D.items.forEach(it=>(g[it.grp]=g[it.grp]||[]).push(it));
  m.innerHTML=`<p class="note">94 icon 64px. Dòng xanh là chỗ Claude đề xuất thay vào game (hiện game vẽ icon bằng code hoặc dùng ảnh tạm). Bấm 1 lần = Giữ, 2 lần = Bỏ, 3 lần = bỏ chọn.</p>`+
   Object.entries(g).map(([k,a])=>`<h2>${k} (${a.length})</h2><div class="ig">${a.map(it=>{const id='i:'+it.id;return `<div class="it ${st[id]==='k'?'keep':st[id]==='d'?'drop':''}" data-cyc="${id}"><img src="${it.src}" alt=""><b>${it.name}</b>${it.use?`<span class="u">→ ${it.use}</span>`:''}</div>`}).join('')}</div>`).join('');
 }else if(tab==='skills'){
  m.innerHTML=`<p class="note">Hiệu ứng chiêu trong gói được viết cho Godot (ảnh + shader), muốn dùng phải viết lại bằng canvas. Claude ghi gợi ý chỗ dùng trong game.</p><h2>21 chiêu môn phái</h2><div class="ig">${D.skills.map(s=>{const id='s:'+s.id;return `<div class="it ${st[id]==='k'?'keep':st[id]==='d'?'drop':''}" data-cyc="${id}">${s.src?`<img src="${s.src}" alt="">`:''}<b>${s.name}</b><span class="sub">${s.sect}</span><span class="sub">${s.desc}</span>${s.use?`<span class="u">→ ${s.use}</span>`:''}</div>`}).join('')}</div>
  <h2>12 hiệu ứng trùm</h2><div class="ig">${D.boss.map(s=>{const id='b:'+s.id;return `<div class="it ${st[id]==='k'?'keep':st[id]==='d'?'drop':''}" data-cyc="${id}"><img src="${s.src}" alt=""><b>${s.name}</b><span class="sub">${s.desc}</span></div>`}).join('')}</div>`;
 }else if(tab==='aud'){
  m.innerHTML=`<p class="note">Âm thanh WAV. Game hiện có 13 file mp3 cùng nguồn (bộ Chung). Claude sẽ chuyển sang mp3/ogg nhẹ khi ghép.</p>`+Object.entries(D.aud).map(([k,a])=>{const id='a:'+k;return `<h2>${k} · ${a.length} file</h2>${selBtns(id)}<ul class="aud">${a.map(x=>`<li>${x}</li>`).join('')}</ul>`}).join('');
 }else{
  m.innerHTML=`<h2>Asset đang dùng trong game</h2><table><tr><th>Nhóm</th><th>Nguồn</th><th>Ghi chú</th></tr>
  <tr><td>6 nhân vật: nam, nữ, Bạch Hoa, Đấu Lạp, Hắc Phong, Hổ</td><td>Wuxia Free Experience (cùng tác giả gói này)</td><td>Có trong gói Vol.2 bản đầy đủ hơn. Nữ = Hàn Nguyệt Cung nữ đệ tử, Hắc Phong = Hắc Phong Trại Chủ, Hổ = Điếu Tình Mãnh Hổ, Đấu Lạp = Đấu Lạp Hiệp Khách.</td></tr>
  <tr><td>~68 ảnh cảnh, nền tuyết, cây, đá, nhà</td><td>Wuxia Free Experience</td><td>Gói Vol.2 có thêm Rừng, Đầm lầy, Sa mạc và 24 công trình.</td></tr>
  <tr><td>13 hiệu ứng (Vạn Kiếm, Như Lai, Thái Cực, vệt chém...)</td><td>Wuxia Free Experience (Common_VFX)</td><td>Cùng nguồn, đã xác nhận trong gói.</td></tr>
  <tr><td>13 âm thanh mp3</td><td>Wuxia Free Experience (Audio/Common)</td><td>Gói Vol.2 có 20 file chung + 105 file chiêu.</td></tr>
  <tr><td>14 NPC × 2 ảnh</td><td>HOANTDZ</td><td>Nguồn khác, giữ ghi công. Phong cách hơi khác, nên so với nhân vật NPC trong gói.</td></tr>
  <tr><td>4 ảnh giao diện (núi mực, nét mực, bánh răng, giọt)</td><td>Chưa rõ</td><td>Cần mày xác nhận nguồn.</td></tr>
  <tr><td>Quái còn lại, icon vật phẩm, nhiều hiệu ứng chiêu</td><td>Vẽ bằng code</td><td>Có thể thay bằng asset gói để đồng bộ.</td></tr></table>
  <h2>Giấy phép gói Vol.2 (tóm tắt)</h2><p>Được dùng thương mại, được chỉnh sửa, được phát hành trong game hoàn chỉnh (kể cả web). Cấm đăng file gốc/đã sửa thành bộ sưu tập hay kho mã công khai, cấm dùng để huấn luyện AI. Font và âm thanh bên thứ ba theo giấy phép riêng (Source Han OFL, xem SOURCE_LICENSES.md). Không bắt buộc ghi công tác giả.</p>`;
 }
 count();
}
function setupSpr(el){
 const c=D.chars[+el.dataset.ci],k=el.dataset.clip,s=c.clips[k];
 el.style.width=s.w+'px';el.style.height=s.h+'px';el.style.backgroundImage=`url(${s.src})`;
 const sc=Math.min(1.25,180/s.h,270/s.w);el.style.transform=`scale(${sc})`;el.style.marginBottom=(-s.bottom*0)+'px';
 anims.push({el,s,f:0,t:0});
}
document.addEventListener('click',e=>{
 const fb=e.target.closest('#flt button');if(fb){flt=fb.dataset.f;render();return}
 const cb=e.target.closest('.clips button');if(cb){const card=cb.closest('.card'),sp=card.querySelector('.spr');sp.dataset.clip=cb.dataset.clip;const i=anims.findIndex(a=>a.el===sp);if(i>=0)anims.splice(i,1);setupSpr(sp);return}
 const sb=e.target.closest('.sel button');if(sb){const id=sb.dataset.id;st[id]=st[id]===sb.dataset.v?undefined:sb.dataset.v;save();const card=sb.closest('.card');if(card){card.classList.toggle('keep',st[id]==='k');card.classList.toggle('drop',st[id]==='d')}sb.parentNode.querySelectorAll('button').forEach(b=>b.classList.toggle('on',st[id]===b.dataset.v));return}
 const cy=e.target.closest('[data-cyc]');if(cy){const id=cy.dataset.cyc;st[id]=st[id]==='k'?'d':st[id]==='d'?undefined:'k';save();cy.classList.toggle('keep',st[id]==='k');cy.classList.toggle('drop',st[id]==='d');return}
});
let last=performance.now();
function loop(now){const dt=now-last;last=now;for(const a of anims){a.t+=dt;const d=a.s.ms[a.f%a.s.ms.length]||100;if(a.t>=d){a.t=0;a.f=(a.f+1)%a.s.n;a.el.style.backgroundPosition=`${-a.f*a.s.w}px 0`}}requestAnimationFrame(loop)}
requestAnimationFrame(loop);
function count(){const v=Object.values(st);$('#cnt').textContent=`Đã chọn: ${v.filter(x=>x==='k').length} giữ · ${v.filter(x=>x==='d').length} bỏ`}
$('#clr').onclick=()=>{if(confirm('Xóa hết lựa chọn?')){st={};save();render()}};
$('#exp').onclick=()=>{
 const nm=id=>{const [t,k]=[id[0],id.slice(2)];if(t==='c'){const c=D.chars.find(x=>x.id===k);return 'Nhân vật: '+(c?c.name:k)}if(t==='i'){const it=D.items.find(x=>x.id===k);return 'Vật phẩm: '+(it?it.name+' ('+k+')':k)}if(t==='s'){const s=D.skills.find(x=>x.id===k);return 'Chiêu: '+(s?s.name:k)}if(t==='b'){const s=D.boss.find(x=>x.id===k);return 'Hiệu ứng trùm: '+(s?s.name:k)}return 'Âm thanh: '+k};
 const K=[],X=[];for(const [id,v] of Object.entries(st)){if(v==='k')K.push(nm(id));else if(v==='d')X.push(nm(id))}
 const txt='GIỮ ('+K.length+'):\n- '+K.join('\n- ')+'\n\nBỎ ('+X.length+'):\n- '+X.join('\n- ');
 const m=$('#main');m.insertAdjacentHTML('afterbegin',`<h2>Copy đoạn này gửi Claude</h2><textarea id="out"></textarea>`);$('#out').value=txt;$('#out').select();try{navigator.clipboard.writeText(txt).catch(()=>{})}catch(e){}window.scrollTo(0,0)};
tabs();render();
</script></body></html>'''
open(S+'Loc_Asset_Wuxia.html','w',encoding='utf-8').write(HTML.replace('__DATA__',data))
import os;print(os.path.getsize(S+'Loc_Asset_Wuxia.html')/1e6,'MB')
