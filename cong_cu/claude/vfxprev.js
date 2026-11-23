const L=require('./rec_lib2');const fs=require('fs');const [ROOT,OUT,GEN,KEYS]=process.argv.slice(2);
const META=JSON.parse(fs.readFileSync(ROOT+'/bake/meta.json'));
(async()=>{const {b,pg,errs}=await L.open(ROOT,{gender:GEN||'nam',forge:6,w:1100,h:620});
 await pg.locator('button',{hasText:'Luyện Công'}).first().click();await pg.waitForTimeout(1500);
 await pg.evaluate(()=>{clearInterval(__auto);const t=document.getElementById('trP');if(t)t.style.display='none'});
 await pg.evaluate(async M=>{for(const k in M){const i=new Image();i.src='bake/'+k+'.png';await new Promise(r=>{i.onload=r;i.onerror=r});TDST.VFX['bk_'+k]=i;const m=M[k];TDST.SPX['bk_'+k]={w:m.w,h:m.h,c:m.c,n:m.n,px:m.px,py:m.py}}},META);
 fs.mkdirSync(OUT,{recursive:true});let fr=0;
 for(const k of KEYS.split(',')){const m=META[k];
  await pg.evaluate(([k,m])=>{const P=TDST.P,G=TDST.GG();if(!window.__pos){let e=G.enemies.filter(z=>!z.dead).sort((a,b)=>Math.hypot(a.x-P.x,a.y-P.y)-Math.hypot(b.x-P.x,b.y-P.y))[0];window.__pos=[e.x-200,e.y+40]}P.x=__pos[0];P.y=__pos[1];P.vx=P.vy=0;G.fx=G.fx.filter(f=>f.k!=='sp');P.facing=1;for(const s of P.kit.act)s.cd=99;P.kit.ult.cd=99;P.kit.basic.cd=99;
   TDST.fx({k:'sp',s:'bk_'+k,x:P.x,y:P.y,sc:m.sc,T:m.T,follow:1})},[k,m]);
  const n=Math.ceil((m.T+0.4)*30);
  for(let j=0;j<n;j++){await pg.evaluate(()=>{const P=TDST.P;P.x=__pos[0];P.y=__pos[1];__step(1000/30);P.kit.basic.cd=99});await pg.screenshot({path:OUT+'/'+k+'_'+String(j).padStart(3,'0')+'.png'})}
  console.log(k,n)}
 console.log(errs);await b.close()})();
