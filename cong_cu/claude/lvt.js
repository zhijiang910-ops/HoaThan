const L=require('./rec_lib3');(async()=>{const {b,pg,errs}=await L.open(process.argv[2],{w:1100,h:620});
 const r=await pg.evaluate(()=>{const o={};const {TIERS,TIER_OPEN,prof,profGain,rollTier,makeItem,forgeMarkup,forgeItem}=TDST;o.tiers=TIERS.length;o.open=TIER_OPEN;
  const P0=prof();P0.lv=68;P0.exp=0;profGain(1e9);o.lv=P0.lv;o.exp=P0.exp;
  const t=[];for(let i=0;i<3000;i++)t.push(rollTier(5,true));o.maxTier=Math.max(...t);
  const it=makeItem(3,6,30);it.forge=9;o.mk=forgeMarkup(it).includes('sẽ mở sau');o.fi=forgeItem(it.id,false);return o});
 console.log(JSON.stringify(r),errs);await b.close()})();
