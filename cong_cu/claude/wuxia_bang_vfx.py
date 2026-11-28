from PIL import Image,ImageDraw,ImageFont
import glob,os,sys
WX=sys.argv[1];V='game/assets/vfx/';OUT='nguon/tham_chieu/thu_vien_vfx/'
fV=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15);fS=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
fC=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',15);fT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',17)
CW=116;LW=300;BG=(58,52,62)
def cell(im):
    c=Image.new('RGBA',(CW-6,CW-6),BG+(255,));im=im.convert('RGBA');bb=im.split()[3].getbbox()
    if bb: im=im.crop(bb)
    im.thumbnail((CW-10,CW-10));c.alpha_composite(im,((CW-6-im.width)//2,(CW-6-im.height)//2));return c
def sheetframes(path,w,h,c,n,k=7):
    im=Image.open(path).convert('RGBA');idx=[round(i*(n-1)/(k-1)) for i in range(k)]
    return [im.crop(((i%c)*w,(i//c)*h,(i%c)*w+w,(i//c)*h+h)) for i in idx]
fD=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
def mixed(d,xy,t,fill,cj=None,vi=None):
    cj=cj or fC;vi=vi or fD;x,y=xy
    for ch in t:
        f=cj if ord(ch)>=0x2E80 else vi
        d.text((x,y),ch,font=f,fill=fill);x+=d.textlength(ch,font=f)
def fit(d,t,f,w):
    while d.textlength(t,font=f)>w and len(t)>3:t=t[:-2]+'…'
    return t
def build(title,rows,out,ncol=7,notes=None):
    H=40+len(rows)*CW+(len(notes)*24+16 if notes else 0);W=LW+ncol*CW;img=Image.new('RGB',(W,H),(22,18,26));d=ImageDraw.Draw(img)
    d.text((10,10),title,font=fT,fill=(240,220,170))
    for r,(l1,l2,cn,l3,cells) in enumerate(rows):
        y=40+r*CW;d.rectangle((0,y,W,y+CW-2),fill=(30,26,34))
        d.text((8,y+8),fit(d,l1,fV,LW-14),font=fV,fill=(250,215,120));d.text((8,y+30),fit(d,l2,fV,LW-14),font=fV,fill=(235,230,235))
        if cn:mixed(d,(8,y+54),cn,(200,190,210))
        d.text((8,y+82),fit(d,l3,fS,LW-14),font=fS,fill=(170,170,180))
        for i,cc in enumerate(cells[:ncol]):img.paste(cell(cc).convert('RGB'),(LW+i*CW+3,y+3))
    if notes:
        y=40+len(rows)*CW+8
        for t in notes:mixed(d,(10,y),t,(220,180,140));y+=24
    img.save(OUT+out);print(out,img.size)
SPX={'dq_cleave':(272,326,8,16),'dq_triple':(285,338,8,23),'dq_ring':(460,232,6,17),'pm_bell':(202,225,8,34),'pm_palm':(293,207,8,17),'pm_guard':(312,321,8,25),'hl_petals':(338,183,8,23),'hl_decoy':(85,106,8,25),'hl_heal':(304,179,8,28),'th_bind':(412,124,6,27),'th_dash':(406,183,6,20),'th_eclipse':(465,168,6,28),'tx_in':(365,604,11,30)}
rows=[]
def addsect(k,vn,sect,cn,used):
    w,h,c,n=SPX[k];rows.append((k+'  ·  '+sect,vn,cn,used,sheetframes(V+k+'.png',w,h,c,n)))
addsect('tx_in','Thiên Xu Kiếm Trận','Huyền Tiêu Kiếm Tông','玄霄剑宗 天枢剑阵','Kiếm F bản cũ, nay chỉ dự phòng')
rows.append(('wx_02_beam  ·  Huyền Tiêu','Nhất Tuyến Khai Thiên','玄霄剑宗 一线开天','Chưa dùng',[Image.open(V+'wx_02_beam.png').crop((i*601,0,i*601+601,380)) for i in range(6)]))
rows.append(('wx_03_orbit  ·  Huyền Tiêu','Hồi Phong Quy Sao','玄霄剑宗 回风归鞘','Chưa dùng',[Image.open(V+'wx_03_orbit.png').crop((i*670,0,i*670+670,553)) for i in range(6)]))
for k,vn,sect,cn,used in [('dq_cleave','Xích Long Đoạn Nhạc','Xích Diễm Đao Môn','赤焰刀门 赤龙断岳','Dùng: Đao Q'),('dq_triple','Liệu Nguyên Tam Điệp','Xích Diễm Đao Môn','赤焰刀门 燎原三叠','Dùng: Đao F, đánh thường Đao'),('dq_ring','Tẫn Hỏa Hồi Thân','Xích Diễm Đao Môn','赤焰刀门 烬火回身','Dùng: Đao X'),
 ('pm_bell','Kim Chung Chấn Nhạc','Kim Cương Tự','金刚寺 金钟震岳','Dùng: Trượng Q, chuông Quyền (tím)'),('pm_palm','Phục Ma Trấn Sơn Chưởng','Kim Cương Tự','金刚寺 伏魔镇山掌','Dùng: Trượng F, Minh Vương'),('pm_guard','Bất Động Minh Vương Thân','Kim Cương Tự','金刚寺 不动明王身','Dùng: Trượng X, C'),
 ('hl_petals','Thiên Biện Quy Tâm','Bách Hoa Cốc','百花谷 千瓣归心','Dùng: Quạt Q'),('hl_decoy','Hoa Ảnh Di Hương','Bách Hoa Cốc','百花谷 花影移香','Dùng: Quạt F'),('hl_heal','Hồi Xuân Hoa Trận','Bách Hoa Cốc','百花谷 回春花阵','Dùng: Quạt X'),
 ('th_bind','Minh Ảnh Tỏa Hồn','U Minh Giáo','幽冥教 冥影锁魂','Dùng: Cung Q'),('th_dash','Dạ Độ Vô Thanh','U Minh Giáo','幽冥教 夜渡无声','Dùng: Cung F'),('th_eclipse','Thực Nguyệt Quy Khư','U Minh Giáo','幽冥教 蚀月归墟','Dùng: Cung X')]:
    addsect(k,vn,sect,cn,used)
build('Gói Wuxia · KỸ NĂNG MÔN PHÁI đã xuất ra ảnh (15/21)',rows,'wuxia_1_mon_phai_da_xuat.png',notes=['CHƯA XUẤT 6 chiêu (cần chạy Godot 4.7.1 để xuất ra ảnh):','Hàn Nguyệt Cung 寒月宫: Kính Nguyệt Hồi Lan 镜月回澜 · Sương Hoa Định Ảnh 霜华定影 · Đạp Nguyệt Vô Ngân 踏月无痕','Bích Trúc Sơn Trang 碧竹山庄: Thính Trúc Hồi Phong 听竹回风 · Tiết Tiết Sinh Phong 节节生锋 · Hư Trúc Tá Kình 虚竹卸劲'])
rows=[];P=WX+'Common_VFX/Skills/'
def fr(d):return [Image.open(f) for f in sorted(glob.glob(d+'/frame_*.png'))][:7]
rows.append(('07 Sword_Arc · slash','Kiếm Hồ: vệt chém','剑弧','Dùng: vệt A Kiếm, va chạm',fr(P+'07_Sword_Arc/PNG/slash')))
rows.append(('07 Sword_Arc · projectile','Kiếm Hồ: kiếm khí bay','剑弧','Chưa dùng',fr(P+'07_Sword_Arc/PNG/projectile')))
rows.append(('07 Sword_Arc · impact','Kiếm Hồ: va chạm','剑弧','Đã bỏ (chủ game chê mảnh băng)',fr(P+'07_Sword_Arc/PNG/impact')))
rows.append(('02 Wanjian','Vạn Kiếm Quy Tông','万剑归宗','Kiếm + va chạm; va chạm đã bỏ',[Image.open(P+'02_Wanjian/PNG/wanjian_sword.png')]+fr(P+'02_Wanjian/PNG/impact')[:6]))
rows.append(('04 Rulai','Như Lai Thần Chưởng','如来神掌','Bàn tay, hố, bụi, đá; trùm dùng',[Image.open(P+'04_Rulai/PNG/'+n+'.png') for n in ['buddha_hand_back_v2','buddha_crater','buddha_dust','buddha_rock']]))
rows.append(('05 Taiji','Thái Cực','太极','Vòng thái cực + xoáy, chưa dùng',[Image.open(P+'05_Taiji/PNG/'+n+'.png') for n in ['taiji','taiji_bolt']]))
rows.append(('06 Moying','Mặc Ảnh','墨影','Vệt mực, chưa dùng',[Image.open(P+'06_Moying/PNG/'+n+'.png') for n in ['ink_slash','ink_impact','ink_ground_trail']]))
rows.append(('03 Zanghua','Táng Hoa','葬花','Cánh hoa, chưa dùng',[Image.open(P+'03_Zanghua/PNG/petal.png')]))
build('Gói Wuxia · VFX DÙNG CHUNG (Common_VFX)',rows,'wuxia_2_dung_chung.png',notes=['01 Suodi 缩地 (Súc Địa) chỉ có code Godot, không có ảnh PNG.'])
VN={'01_cleave':'Bổ chém','02_whirl':'Lốc xoáy','03_charge':'Lao húc','04_needles':'Mưa kim','05_gourd':'Hồ lô độc','06_field':'Vùng độc','07_chain':'Xích trói','08_prison':'Ngục xương','09_summon':'Triệu hồi','10_claws':'Cào vuốt','11_roar':'Gầm sóng','12_slam':'Đập đất'}
rows=[]
for d in sorted(glob.glob(WX+'VFX/Boss_Clips_12/*')):
    n=os.path.basename(d);rows.append((n,VN.get(n,''),'','8 khung, chưa dùng',fr(d+'/frames')))
build('Gói Wuxia · 12 CLIP HIỆU ỨNG BOSS (Boss_Clips_12)',rows,'wuxia_3_boss_12.png')
