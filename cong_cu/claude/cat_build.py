import json,os,io,base64,csv,glob
from PIL import Image
S='/tmp/claude-0/-home-user-HoaThan/f578bff3-154a-5e94-b344-26c188d551d1/scratchpad/'
R=S+'goi/04_Integrated/'
chars=json.load(open(S+'catalog/chars.json',encoding='utf-8'))
def b64(p,scale=1):
    im=Image.open(p).convert('RGBA')
    if scale!=1:im=im.resize((int(im.width*scale),int(im.height*scale)),Image.NEAREST)
    bb=im.getbbox()
    if bb:im=im.crop(bb)
    if im.width>160 or im.height>160:
        r=160/max(im.size);im=im.resize((max(1,int(im.width*r)),max(1,int(im.height*r))),Image.NEAREST)
    buf=io.BytesIO();im.save(buf,'PNG',optimize=True);return 'data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()
# ---- đề xuất nhân vật ----
REC={
'玄霄剑宗-掌门':('chinh','Ứng viên NAM CHÍNH số 1 (Kiếm)','Áo trắng, kiếm dài, đòn đâm thẳng rõ lực. Bộ động tác đầy đủ nhất gói: trúng đòn 8 frame, gục 10 frame, có thêm động tác thi triển chiêu.'),
'玄霄剑宗-男弟子':('chinh','Ứng viên NAM CHÍNH số 2 (Kiếm)','Gần giống nhân vật nam hiện tại, đòn bổ kiếm rõ ràng. Chỉ có 1 bộ đòn, phải tự làm thêm đòn B.'),
'碧竹山庄-女掌门':('chinh','Ứng viên NỮ CHÍNH số 1 (Kiếm)','Áo xanh lục, không dải lụa, kiếm đâm thẳng dứt khoát, có 2 bộ đòn. Hợp ý mày muốn bớt lụa.'),
'寒月宫-女弟子':('chinh','Ứng viên NỮ CHÍNH số 2 (đang dùng)','Chính là nhân vật nữ hiện tại. Có 2 bộ đòn nhưng bộ thứ hai là chưởng, không cầm kiếm.'),
'寒月宫-女掌门':('chinh','Ứng viên NỮ CHÍNH số 3 (Kiếm)','Đòn đâm đẹp, 2 bộ đòn đều cầm kiếm, nhưng dải lụa còn dài hơn nhân vật nữ hiện tại.'),
'赤焰刀门-女弟子':('mo','Nhân vật vũ khí phụ / NPC','Áo đỏ, cầm kiếm, chỉ 1 bộ đòn. Hợp làm NPC kiếm khách hoặc bạn đồng hành.'),
'赤焰刀门-掌门':('mo','Nhân vật mở khóa ĐAO','Đòn đao bổ mạnh, áo choàng đỏ, 2 bộ đòn. Hợp làm hình mẫu khi mở vũ khí Đao.'),
'赤焰刀门-男弟子':('mo','Nhân vật mở khóa ĐAO (bản trẻ)','Đao lớn, 2 bộ đòn. Có thể làm nam chính khi chọn Đao.'),
'金刚寺-男弟子':('mo','Nhân vật mở khóa CÔN','Cầm côn, đòn quét ngang. Hợp vũ khí Côn (gần chất Tây Du, kiểu Sa Tăng / tăng nhân).'),
'金刚寺-住持':('npc','NPC chùa / người giao nhiệm vụ','Đòn đánh yếu nhìn, hợp làm NPC Lão Tăng, chùa, cứu chữa.'),
'百花谷-女弟子':('mo','Nhân vật PHÙ CHÚ / dải lụa','Đánh bằng dải lụa tầm xa, đẹp. Hợp vũ khí Phù Chú hoặc quái tầm xa nữ.'),
'百花谷-掌门':('trum','Tinh anh / trùm phụ nữ','Dải lụa đỏ quét rộng, hợp tinh anh tầm xa hoặc trùm phụ "Hoa yêu".'),
'百花谷-男弟子':('npc','NPC thư sinh','Đánh bằng quạt, dáng thư sinh. Hợp NPC thương nhân, kể chuyện.'),
'碧竹山庄-女弟子':('npc','NPC nhạc công','Thổi sáo, không có đòn đánh rõ. Chỉ hợp NPC.'),
'碧竹山庄-男弟子':('bo','Cân nhắc bỏ','Cầm kiếm trúc, 1 bộ đòn, dáng giống nhiều nhân vật khác. Ít giá trị riêng.'),
'寒月宫-男弟子':('bo','Cân nhắc bỏ','Áo trắng giống nhân vật nữ, đòn yếu nhìn, 1 bộ đòn.'),
'玄霄剑宗-女弟子':('mo','Đệ tử kiếm phái / NPC đồng môn','Áo xanh, kiếm, 1 bộ đòn. Hợp NPC đồng môn hoặc quái người.'),
'幽冥教-女弟子':('quai','Quái người: sát thủ','Áo tím đen, dao găm, nhanh. Hợp quái sát thủ (cũng hợp quái "yêu nữ" bối cảnh Tây Du).'),
'幽冥教-男弟子':('quai','Quái người: sát thủ','Áo đen, dao găm. Hợp quái thường loại nhanh.'),
'幽冥教-男掌门':('trum','Tinh anh sát thủ','Dao găm, áo choàng tím, 2 bộ đòn. Hợp tinh anh hoặc trùm phụ.'),
'万毒老祖（boss）':('trum','TRÙM: Vạn Độc Lão Tổ','Lão già độc, ném cầu độc. Trùm vùng đầm lầy.'),
'吊睛猛虎':('quai','Tinh anh thú (đang dùng: Hổ)','Hổ người, vuốt. Game đang dùng làm Lang yêu / Hổ dữ.'),
'山魈':('quai','Quái yêu / tinh anh','Khỉ yêu nanh vuốt, rất hợp Tây Du (yêu khỉ núi).'),
'树妖姥姥':('trum','Tinh anh / trùm rừng: Thụ Yêu','Yêu cây, đòn roi rễ. Hợp trùm ải rừng.'),
'毒娘子':('quai','Quái tầm xa: độc','Ném độc. Hợp quái tầm xa nữ.'),
'毒郎君':('quai','Quái tầm xa: độc','Ném độc. Đi cặp với Độc Nương Tử.'),
'独角山猪王':('quai','Tinh anh: heo rừng húc','Lao húc, hợp quái lao (giống Lang yêu hiện tại) hoặc tinh anh. Hợp Tây Du (Trư yêu).'),
'白骨夫人':('trum','TRÙM: Bạch Cốt Phu Nhân','Nhân vật Tây Du Ký chính hiệu. Kiếm xương, 2 bộ đòn. Rất nên giữ.'),
'白骨妖后（boss）':('trum','TRÙM lớn: Bạch Cốt Yêu Hậu','Quạt xương, vương miện, khí thế trùm cuối.'),
'石头人':('quai','Tinh anh: Thạch nhân','To, chậm, quyền đá. Hợp tinh anh giáp dày.'),
'蓝灰獠牙鬼战士像':('quai','Tinh anh: quỷ tướng rìu','Rìu lớn, nanh quỷ. Hợp tinh anh hoặc lính của trùm.'),
'铁面判官与镇魂笔':('trum','TRÙM: Phán Quan Âm phủ','Hợp ải Địa phủ (Tây Du có đoạn Ngộ Không náo Âm phủ).'),
'鬼火妖僧_192x192':('trum','Tinh anh / trùm phụ: Yêu tăng','Quyền trượng lửa ma. Rất hợp Tây Du (yêu tăng giả sư).'),
'黑风寨主':('quai','Tinh anh (đang dùng: Hắc Phong)','Game đang dùng làm Yêu binh cận chiến, Hỏa Tướng, Thủ lĩnh sơn tặc.'),
'斗笠侠客':('quai','Quái thường (đang dùng: nón lá)','Game đang dùng làm Tiểu yêu, Sơn tặc. Thiếu động tác trúng đòn.'),
}
CAT={'chinh':'Nhân vật chính','mo':'Vũ khí khác / đồng hành','quai':'Quái / tinh anh','trum':'Trùm / trùm phụ','npc':'NPC','bo':'Cân nhắc bỏ'}
for c in chars:
    k,t,r=REC.get(c['id'],('bo','Chưa phân loại',''))
    c['rec']=k;c['recT']=t;c['why']=r
# ---- vật phẩm ----
IV={'bow':'Cung','dagger':'Dao găm','dart':'Phi tiêu','dual_hammers':'Song chùy','dual_sabres':'Song đao','fan':'Quạt sắt','fly_whisk':'Phất trần','gauntlets':'Thủ sáo sắt','iron_staff':'Côn sắt','iron_sword':'Thiết kiếm','long_sabre':'Trường đao','monk_staff':'Thiền trượng','pudao':'Phác đao','quiver':'Ống tên','short_sword':'Đoản kiếm','soft_whip':'Nhuyễn tiên','spear':'Thương','throwing_knife':'Phi đao','wood_sword':'Mộc kiếm',
'belt':'Đai lưng','cloak':'Áo choàng','cloth_headwrap':'Khăn trùm đầu','cloth_shoes':'Giày vải','cloth_tunic':'Áo vải','iron_armor':'Giáp sắt','iron_helmet':'Mũ sắt','kasaya':'Cà sa','leather_armor':'Giáp da','leather_boots':'Ủng da','sachet':'Túi thơm','shin_guards':'Hộ ống chân','straw_hat':'Nón lá','swordswoman_outfit':'Y phục nữ hiệp','taoist_robe':'Đạo bào','wrist_guards':'Hộ cổ tay',
'antidote':'Thuốc giải độc','bandage':'Băng gạc','clarity_pill':'Thanh Tâm Đan','fire_oil':'Dầu lửa','great_return_pill':'Đại Hoàn Đan','healing_balm':'Cao trị thương','lesser_return_pills':'Tiểu Hoàn Đan','medicine_gourd':'Hồ lô thuốc','miasma_pill':'Tị Chướng Đan','poison_powder':'Độc phấn','qi_pills':'Bổ Khí Đan','revival_pill':'Hồi Sinh Đan','sleeping_powder':'Mê dược','styptic_powder':'Thuốc cầm máu','warming_pill':'Noãn Thân Đan',
'antler':'Gạc nai','bamboo':'Tre','beast_hide':'Da thú','cinnabar':'Chu sa','copper_ingot':'Thỏi đồng','copper_ore':'Quặng đồng','cotton_cloth':'Vải bông','ginseng':'Nhân sâm','iron_ore':'Quặng sắt','lingzhi':'Linh chi','refined_iron':'Huyền Thiết','silk_thread':'Tơ lụa','silver_ore':'Quặng bạc','snake_gall':'Mật rắn','sulfur':'Lưu huỳnh','tiger_bone':'Xương hổ','timber':'Gỗ','venom_sac':'Túi nọc','whetstone':'Đá mài',
'chicken_leg':'Đùi gà','flatbread':'Bánh nướng','grilled_fish':'Cá nướng','noodles':'Mì','rice':'Cơm','rice_wine':'Rượu gạo','roast_meat':'Thịt nướng','steamed_bun':'Bánh bao chay','stuffed_bun':'Bánh bao nhân','tea':'Trà','wild_fruit':'Quả dại',
'bronze_key':'Chìa đồng','escort_writ':'Lệnh tiêu cục','gold_ingot':'Nén vàng','iron_key':'Chìa sắt','secret_letter':'Mật thư','sect_token':'Lệnh bài môn phái','silver_ingot':'Nén bạc','wanted_notice':'Lệnh truy nã','broken_jade':'Ngọc vỡ','jade_pendant':'Ngọc bội','ledger':'Sổ sách','manual':'Bí tịch','prescription':'Đơn thuốc','treasure_map':'Bản đồ kho báu'}
IG={'I01':'Vũ khí','I02':'Trang bị','I03':'Đan dược / thuốc','I04':'Nguyên liệu','I05':'Đồ ăn','I06':'Vật phẩm nhiệm vụ / quý'}
# map vào game hiện tại
USE={'iron_sword':'Vũ khí Kiếm (ô Vũ khí)','long_sabre':'Vũ khí Đao','spear':'Vũ khí Thương','iron_staff':'Vũ khí Côn','monk_staff':'Vũ khí Côn (bậc cao)','fly_whisk':'Vũ khí Phù Chú','cloth_tunic':'Ô Y phục','swordswoman_outfit':'Ô Y phục (nữ)','taoist_robe':'Ô Y phục (bậc cao)','cloth_shoes':'Ô Hài','leather_boots':'Ô Hài (bậc cao)','sachet':'Ô Hộ phù','jade_pendant':'Ô Nhẫn/Bội ngọc','belt':'Ô Đai','gauntlets':'Ô Găng tay','wrist_guards':'Ô Găng tay','lesser_return_pills':'Thuốc hồi máu','qi_pills':'Thuốc hồi nội lực','great_return_pill':'Cuồng Huyết Đan (thay hình)','antidote':'Hộ Thể Đan (thay hình)','ginseng':'Tuyết Sâm (đổi màu trắng)','lingzhi':'Băng Tâm Liên (thay hình)','refined_iron':'Huyền Thiết (cường hóa)','steamed_bun':'Điểm Tâm (bánh bao)','manual':'Bí tịch','silver_ingot':'Tiền','gold_ingot':'Tiên ngọc / thưởng lớn','wanted_notice':'Kỳ ngộ Truy nã','treasure_map':'Rương kho báu'}
items=[]
for p in sorted(glob.glob(R+'UI/Items_64/*.png')):
    n=os.path.basename(p)[:-4];pre=n.split('_')[0];key=n[len(pre)+1:]
    g=IG.get(pre[:3],pre)
    items.append({'id':n,'name':IV.get(key,key),'grp':g,'use':USE.get(key,''),'src':b64(p,2)})
# ---- kỹ năng ----
SECT={'玄霄剑宗':'Huyền Tiêu Kiếm Tông','寒月宫':'Hàn Nguyệt Cung','赤焰刀门':'Xích Diễm Đao Môn','碧竹山庄':'Bích Trúc Sơn Trang','百花谷':'Bách Hoa Cốc','幽冥教':'U Minh Giáo','金刚寺':'Kim Cương Tự'}
SKV={'天枢剑阵':('Thiên Xu Kiếm Trận','Trận kiếm vây quanh','Thay/nâng Kiếm Ảnh'),'一线开天':('Nhất Tuyến Khai Thiên','Tia kiếm thẳng xuyên','Thay Kiếm Khí Trảm (Q)'),'回风归鞘':('Hồi Phong Quy Sao','Kiếm bay vòng quanh rồi về','Hợp bí tịch Hồi Phong'),'镜月回澜':('Kính Nguyệt Hồi Lan','Trăng khuyết bay ra','Chiêu tầm xa'),'霜华定影':('Sương Hoa Định Ảnh','Băng đóng chân địch','Hợp map Tuyết Sơn (làm chậm)'),'踏月无痕':('Đạp Nguyệt Vô Ngân','Lướt không dấu','Hợp hiệu ứng Lướt / Truy Phong'),'赤龙断岳':('Xích Long Đoạn Nhạc','Đao bổ lửa lớn','Chiêu Đao'),'燎原三叠':('Liệu Nguyên Tam Điệp','Ba nhát đao lửa','Chiêu Đao'),'烬火回身':('Tẫn Hỏa Hồi Thân','Xoay người vòng lửa','Thay Hoành Tảo (F)'),'听竹回风':('Thính Trúc Hồi Phong','Lá trúc bay','Chiêu tầm xa'),'节节生锋':('Tiết Tiết Sinh Phong','Măng trúc đâm lên','Chiêu khống chế'),'虚竹卸劲':('Hư Trúc Tá Kình','Phản đòn','Chiêu phòng thủ'),'千瓣归心':('Thiên Biện Quy Tâm','Mưa cánh hoa','Thay Vạn Kiếm (X) cho Phù Chú'),'花影移香':('Hoa Ảnh Di Hương','Phân thân mồi','Chiêu né'),'回春花阵':('Hồi Xuân Hoa Trận','Trận hồi máu','Hồi máu (Suối Ấm)'),'冥影锁魂':('Minh Ảnh Tỏa Hồn','Xích trói','Khống chế'),'夜渡无声':('Dạ Độ Vô Thanh','Lướt bóng tối','Hiệu ứng Lướt'),'蚀月归墟':('Thực Nguyệt Quy Khư','Hố đen hút','Chiêu tối thượng'),'金钟震岳':('Kim Chung Chấn Nhạc','Chuông vàng chấn','Phòng thủ / Côn'),'伏魔镇山掌':('Phục Ma Trấn Sơn Chưởng','Chưởng Phật lớn','Đã có Như Lai Thần Chưởng (Hóa Thân)'),'不动明王身':('Bất Động Minh Vương Thân','Kim thân hộ thể','Khiên / bất tử ngắn')}
sk=[]
for f in sorted(glob.glob(R+'Skills/Godot/SectVFX/Skills/*.json')):
    d=json.load(open(f,encoding='utf-8'));mode=d['mode']
    ic=R+f'UI/Skill_Icons/master_{mode}.png'
    vn_,desc,use=SKV.get(d['name'],(d['name'],'',''))
    sk.append({'id':d['id'],'sect':SECT.get(d['sect'],d['sect']),'name':vn_,'desc':desc,'use':use,'src':b64(ic,2) if os.path.exists(ic) else ''})
BOSS={'cleave':('Bổ đôi','Trùm chém ngang lớn'),'whirl':('Lốc xoáy','Vòng xoáy quanh trùm'),'charge':('Lao húc','Lao thẳng (Hổ, Heo)'),'needles':('Mưa kim','Bắn kim độc diện rộng'),'gourd':('Hồ lô hút','Hồ lô thu người (rất Tây Du)'),'field':('Vùng độc','Vùng độc dưới đất'),'chain':('Xích sắt','Quăng xích kéo'),'prison':('Lồng giam','Nhốt người chơi'),'summon':('Triệu hồi','Gọi lâu la'),'claws':('Vuốt','Ba vệt vuốt'),'roar':('Gầm','Sóng âm làm choáng'),'slam':('Dậm đất','Nứt đất quanh trùm')}
boss=[]
for p in sorted(glob.glob(R+'UI/Skill_Icons/boss_*.png')):
    k=os.path.basename(p)[:-4].split('_',2)[2];n,dsc=BOSS.get(k,(k,''))
    boss.append({'id':k,'name':n,'desc':dsc,'src':b64(p,2)})
# ---- âm thanh ----
aud={'Chung (chém, trúng, chiêu cơ bản)':sorted(os.path.basename(p) for p in glob.glob(R+'Audio/Common/*.wav'))}
for sdir in sorted(glob.glob(R+'Audio/Skill_Kit/Audio/sects/*')):
    aud['Chiêu môn phái · '+os.path.basename(sdir)]=sorted(os.path.basename(p) for p in glob.glob(sdir+'/*.wav'))
bd=glob.glob(R+'Audio/Skill_Kit/Audio/bosses/**/*.wav',recursive=True)
if bd:aud['Chiêu trùm']=sorted(os.path.basename(p) for p in bd)
json.dump({'chars':chars,'cat':CAT,'items':items,'skills':sk,'boss':boss,'aud':aud},open(S+'catalog/data.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(chars),len(items),len(sk),len(boss),{k:len(v) for k,v in aud.items()},os.path.getsize(S+'catalog/data.json')/1e6)
