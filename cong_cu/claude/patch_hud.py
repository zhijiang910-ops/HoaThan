import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:80]); s=s.replace(a,b)

CSS=r"""
/* ===== Điện thoại ngang (22/11): nút to cho ngón cái, bỏ nhãn chữ li ti, chữ tối thiểu ~10px ===== */
@media (max-height:520px){
 .sk-mode,.hud-press,.sk-key{display:none!important}
 #skills{gap:8px!important;right:max(10px,env(safe-area-inset-right))!important;bottom:max(8px,env(safe-area-inset-bottom))!important}
 .skr{gap:8px!important;align-items:flex-end!important}
 .sk.manual{width:54px!important;height:54px!important}
 .sk.manual.ult{width:58px!important;height:58px!important}
 .sk.manual b,.sk.ult b{font-size:26px!important}
 .sk.auto{width:42px!important;height:42px!important;box-shadow:0 0 0 2px rgba(110,220,200,.65)!important}
 .sk.auto b{font-size:20px!important}
 .skr.s2 .sk{width:38px!important;height:38px!important}
 .skr.s2 .sk b{font-size:17px!important}
 .sk-info{width:16px!important;height:16px!important;font-size:11px!important;line-height:16px!important}
 #dashBtn{width:70px!important;height:70px!important}#dashBtn svg{width:28px!important;height:21px!important}#dashBtn span{font-size:13px!important}
 #godBtn{transform:scale(1.08);transform-origin:right bottom}
 #hptxt{font-size:11px!important}#mptxt{font-size:10px!important}#xptxt,#lvlv,#avaLv{font-size:10px!important}
 #godMeter,#godTxt{font-size:10.5px!important}
 #qHead b{font-size:11px!important}.qi{font-size:10.5px!important}
}
</style>"""
rep("</style>",CSS) if s.count("</style>")==1 else None
if "Điện thoại ngang (22/11)" not in s:
    i=s.rindex("</style>",0,s.index("<body") if "<body" in s else len(s)); s=s[:i]+CSS[:-len("</style>")]+s[i:]

# Camera gần hơn trên điện thoại (trước: 390/600 = 0,65 → giờ ≈ 0,83)
rep("ZOOM=clamp(Math.min(VW,VH)/(Math.min(VW,VH)<520?600:700),0.5,1.5);","ZOOM=clamp(Math.min(VW,VH)/(Math.min(VW,VH)<520?470:700),0.5,1.5);")

# Viền tối quanh nhân vật + sheet bóng tối
rep("h.flash=c;{const t=document.createElement('canvas');","h.flash=c;{const d=document.createElement('canvas');d.width=c.width;d.height=c.height;const q=d.getContext('2d');q.drawImage(h.img,0,0);q.globalCompositeOperation='source-in';q.fillStyle='rgba(14,20,30,.85)';q.fillRect(0,0,d.width,d.height);h.dark=d}{const t=document.createElement('canvas');")
rep(" c.drawImage(flash?HERO.flash:tf&&tf.tint&&HERO.tint?HERO.tint:HERO.img,",
    " if(c===X&&!flash&&!(tf&&tf.tint)&&HERO.dark&&!LOWFX){const ga=c.globalAlpha;c.globalAlpha=ga*0.9;for(const[ox,oy]of[[-1,0],[1,0],[0,-1],[0,1]])c.drawImage(HERO.dark,fr[0],fr[1],M.w,M.h,-M.ax+ox,-M.ay+oy,M.w,M.h);c.globalAlpha=ga}\n c.drawImage(flash?HERO.flash:tf&&tf.tint&&HERO.tint?HERO.tint:HERO.img,")
# Vòng sáng dưới chân
rep("  const[an,fi]=heroFrame();X.fillStyle='rgba(0,0,0,.4)';ell(P.x,P.y,15,5);",
    "  const[an,fi]=heroFrame();X.fillStyle='rgba(0,0,0,.4)';ell(P.x,P.y,15,5);heroRing();")
rep(" X.fillStyle='rgba(0,0,0,.4)';ell(P.x,P.y,15*ps.sx,5);",
    " X.fillStyle='rgba(0,0,0,.4)';ell(P.x,P.y,15*ps.sx,5);heroRing();")
rep("function drawCutC(facing){",
    "function heroRing(){X.save();X.strokeStyle='rgba(255,214,120,.55)';X.lineWidth=1.5;X.beginPath();X.ellipse(P.x,P.y,20,7,0,0,TAU);X.stroke();X.restore()}\nfunction drawCutC(facing){")

# Nền tuyết dịu, tối hơn chút để nhân vật áo trắng nổi
rep(" if(pat){c.fillStyle=pat;c.fillRect(cx-hw,cy-hh,hw*2,hh*2)}",
    " if(pat){c.fillStyle=pat;c.fillRect(cx-hw,cy-hh,hw*2,hh*2)}\n if(M.ground==='g_snow'){c.fillStyle='rgba(30,44,60,.16)';c.fillRect(cx-hw,cy-hh,hw*2,hh*2)}")

# Nhiệm vụ: thu gọn mặc định trên điện thoại, tiêu đề hiện tiến độ
rep("try{if(localStorage.getItem('tdst_qmin')==='1')$('#quests').classList.add('min')}catch(e){}",
    "try{const v=localStorage.getItem('tdst_qmin');if(v==='1'||(v===null&&innerHeight<=520))$('#quests').classList.add('min')}catch(e){}")
rep("<em>${q.done?'✓':Math.floor(q.p)+'/'+q.n}</em><u style=\"width:${Math.min(100,q.p/q.n*100)}%\"></u></div>`).join('');el_.innerHTML=h}",
    "<em>${q.done?'✓':Math.floor(q.p)+'/'+q.n}</em><u style=\"width:${Math.min(100,q.p/q.n*100)}%\"></u></div>`).join('');el_.innerHTML=h;\n const hb=$('#qHead b');if(hb){const t='Nhiệm vụ '+G.qs.filter(q=>q.done).length+'/'+G.qs.length;if(hb.textContent!==t)hb.textContent=t}}")
open(p,'w',encoding='utf-8').write(s);print('ok')
