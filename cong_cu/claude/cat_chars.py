"""Dựng dải frame hướng đông (quay phải) cho từng nhân vật trong gói, xuất JSON để làm trang lọc."""
import json,os,io,base64
from PIL import Image
R='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/goi/04_Integrated/'
OUT='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/catalog/'
VN={'寒月宫':'Hàn Nguyệt Cung','幽冥教':'U Minh Giáo','玄霄剑宗':'Huyền Tiêu Kiếm Tông','百花谷':'Bách Hoa Cốc','碧竹山庄':'Bích Trúc Sơn Trang','赤焰刀门':'Xích Diễm Đao Môn','金刚寺':'Kim Cương Tự'}
ROLE={'女弟子':'Nữ đệ tử','男弟子':'Nam đệ tử','女掌门':'Nữ chưởng môn','男掌门':'Nam chưởng môn','掌门':'Chưởng môn','住持':'Trụ trì'}
VIL={'万毒老祖（boss）':'Vạn Độc Lão Tổ (trùm)','吊睛猛虎':'Điếu Tình Mãnh Hổ','山魈':'Sơn Tiêu','树妖姥姥':'Thụ Yêu Lão Lão','毒娘子':'Độc Nương Tử','毒郎君':'Độc Lang Quân','独角山猪王':'Độc Giác Sơn Trư Vương','白骨夫人':'Bạch Cốt Phu Nhân','白骨妖后（boss）':'Bạch Cốt Yêu Hậu (trùm)','石头人':'Thạch Đầu Nhân','蓝灰獠牙鬼战士像':'Tượng Quỷ Chiến Sĩ Nanh Xám','铁面判官与镇魂笔':'Thiết Diện Phán Quan','鬼火妖僧_192x192':'Quỷ Hỏa Yêu Tăng','黑风寨主':'Hắc Phong Trại Chủ'}
WP={'剑击':'kiếm','剑劈':'kiếm bổ','匕首':'dao găm','绸缎':'dải lụa','折扇':'quạt','吹笛':'sáo','竹剑':'kiếm trúc','刀劈':'đao','虎爪':'vuốt hổ','利爪爪击':'vuốt','单角顶撞':'húc sừng','骨剑':'kiếm xương','骨扇':'quạt xương','石拳':'quyền đá','巨斧劈':'rìu lớn','权杖':'quyền trượng','长刀劈':'trường đao'}
def vn(name):
    if name in VIL:return VIL[name]
    if '-' in name:
        s,r=name.split('-',1);return f"{VN.get(s,s)} · {ROLE.get(r,r)}"
    return name
def strip(files,base):
    ims=[Image.open(os.path.join(base,f)).convert('RGBA') for f in files]
    W=max(i.width for i in ims);H=max(i.height for i in ims)
    # khung chung, căn đáy-giữa
    canv=[]
    for i in ims:
        c=Image.new('RGBA',(W,H));c.paste(i,((W-i.width)//2,H-i.height));canv.append(c)
    bb=None
    for c in canv:
        b=c.getbbox()
        if b:bb=b if bb is None else (min(bb[0],b[0]),min(bb[1],b[1]),max(bb[2],b[2]),max(bb[3],b[3]))
    bb=bb or (0,0,W,H)
    fw,fh=bb[2]-bb[0],bb[3]-bb[1]
    s=Image.new('RGBA',(fw*len(canv),fh))
    for k,c in enumerate(canv):s.paste(c.crop(bb),(k*fw,0))
    buf=io.BytesIO();s.save(buf,'PNG',optimize=True)
    return {'w':fw,'h':fh,'n':len(canv),'src':'data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode(),'bottom':H-bb[3]}
lib=json.load(open(R+'Characters/ANIMATION_LIBRARY.json',encoding='utf-8'))
out=[]
for c in lib['characters']:
    item={'id':c['name'],'name':vn(c['name']),'cn':c['name'],'cat':c['category'],'clips':{},'weapon':''}
    for k in ['idle','walk','attack','attack_secondary','hurt','death','cast']:
        if k not in c['clips']:continue
        v=c['clips'][k];e=v.get('east') or v[list(v)[0]]
        st=strip(e['files'],R);st['ms']=e.get('durations_ms') or [1000//(e.get('fps') or 10)]*st['n'];st['dir']='east' if 'east' in v else list(v)[0]
        item['clips'][k]=st
        if k=='attack' and e.get('weapon'):item['weapon']=WP.get(e['weapon'],e['weapon'])
    out.append(item);print(item['name'],sum(len(x['src']) for x in item['clips'].values())//1024,'KB')
# Đấu Lạp Hiệp Khách
B=R+'Characters/Original_Hero_Limited/';cl=json.load(open(B+'CLIPS.json',encoding='utf-8'))['clips']
item={'id':'斗笠侠客','name':'Đấu Lạp Hiệp Khách (thưởng, thiếu trúng đòn)','cn':'斗笠侠客','cat':'sect','clips':{},'weapon':'kiếm'}
for k,kk in [('idle','idle'),('walk','walk'),('attack','attack3'),('cast','cast_swift_step'),('death','death')]:
    v=cl.get(kk)
    if not v:continue
    e=v.get('east') or v[list(v)[0]];st=strip(e['files'],B);st['ms']=e.get('durations_ms') or [1000//(e.get('fps') or 10)]*st['n'];st['dir']='east';item['clips'][k]=st
out.append(item)
json.dump(out,open(OUT+'chars.json','w',encoding='utf-8'),ensure_ascii=False)
print('total MB',os.path.getsize(OUT+'chars.json')/1e6)
