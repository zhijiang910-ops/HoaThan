# Tây Du Sinh Tồn: tài liệu bàn giao

Dán tài liệu này vào cuộc trò chuyện mới, kèm file `TayDuSinhTon_game.zip`, rồi nói: "Đây là game tao đang làm, đọc rồi làm tiếp".

---

## 1. Game là gì

- Webgame survivors, nhìn từ trên xuống, nhân vật tự đánh. Cảm giác lấy theo video 40 phút 群侠传：幸存者.
- HUD được biến tấu theo phong cách riêng, không chép video. Riêng phần Hạ gục / Liên kích thì giống clip.
- Đồ họa pixel art Wuxia: nhân vật, quái, bản đồ, hiệu ứng và âm thanh lấy từ gói **Wuxia_Free_Experience**.
- Toàn bộ game nằm trong **một file `index.html`** (canvas 2D, JS thuần), tài nguyên tách riêng trong thư mục `assets/`.
- Chơi trên điện thoại phải **xoay ngang**. Bố cục được tối ưu riêng cho màn hình thấp hơn 520 px (media query `max-height:520px`).
- Để test có hook `window.TDST` (chứa G, P, S, startWave, kill, makeItem, openMarket, openEv, drinkPot…).

## 2. Gameplay hiện tại

- **Màn và đợt:** mỗi màn có 5 đợt. Đợt 5 là trùm Ngưu Ma Vương. Hạ trùm ra rương, mở rương xong vào **Thương hội**, rồi lên màn sau. Quái mạnh dần theo màn.
- **Thanh tiến độ đợt chỉ tăng khi hạ quái** (đứng yên thì không chạy). Đồng hồ đếm thời gian đã đánh.
- **Xong đợt:** game chậm lại một nhịp, hiện dải băng "Đợt X/5 · Hoàn thành", đồ rơi tự bay về người. Khoảng 2 giây sau mới mở bảng chọn sức mạnh (Tu luyện / Kết toán / Võ học / Tiệm thuốc).
- **Đồ rơi từ quái:**
  - Kinh nghiệm: **hình thoi tím**.
  - Máu: **hình thoi đỏ**, hồi rất ít (2% khí huyết). Mana: **hình thoi xanh**, hồi 4% nội lực. Tỷ lệ rơi khoảng 5–6%.
  - Tiền: đồng tiền vàng có lỗ vuông. Lượng tiền tăng 40% mỗi màn.
- **Bình thuốc** (bình rồng đỏ = Khí Huyết hồi 40%, bình rồng xanh = Nội Lực hồi 50%):
  - Phải **mua ở Tiệm thuốc** (15 và 12 tiền) hoặc rơi hiếm khi đập bình, thùng.
  - Giữ vĩnh viễn, tối đa 9 bình mỗi loại.
  - Uống bằng 2 ô cuối hàng dưới bảng kỹ năng, hoặc phím 1 / 2.
- **Bình, thùng, rương phá được** (vò gốm, bình sứ, thùng, chồng thùng, **rương gỗ nhỏ** vẽ pixel bằng code `RUONG_SRC`):
  - Xuất hiện **ít**: đầu đợt 3 cái, sau đó 16–24 giây thêm 1, trên sân tối đa 5. Rương khoảng 1/8 số vật.
  - Rơi hạt máu, hạt mana, bình thuốc, và **đan dược** (Hộ Thể Đan, Cuồng Huyết Đan, tự dùng khi nhặt).
  - Trang bị: vò 1,5% · bình 1,8% · thùng 2,5% · chồng thùng 4,5% · rương 10%, tối đa 2 món mỗi đợt. Phẩm rơi theo `brkTier`: Phàm 77%, Linh 18%, Bảo 3,8%, Tiên 0,76%, Thần 0,16%, Thánh 0,03%, Hỗn Độn 0,005%.
  - **Bẫy** (`brkTrap`): vò, bình 5% · thùng 7% · chồng thùng 9% · rương 15%. Ra độc, mê hồn hương (chậm) hoặc thuốc nổ (choáng). Chỉ dính khi đứng trong 160 px. Hộ Thể Đan chặn được.
- **Đan dược** (`DAN`, buff lưu ở `P.bf`, icon trạng thái 護 và 狂):
  - Hộ Thể Đan: giải độc, choáng, chậm và miễn nhiễm 60 giây.
  - Cuồng Huyết Đan: +25% sát thương 45 giây (nhân trong `pw()` và `gp()`).
- **Cấp trang bị:** món mới có `it.lv`, mặc định bằng cấp nhân vật trong trận. Chỉ số nhân `1+0,025×(lv−1)` thay cho hệ số theo màn. Đồ cũ không có lv vẫn tính theo màn. Cấp hiện ở góc ô đồ và dòng mô tả.
- **Bí tịch** (`BOOKS`, lưu ở `save.books`, tối đa 5 tầng mỗi cuốn, dư thì đổi 30 Tiên ngọc): Dịch Cân Kinh +8 máu · Kim Chung Tráo +2 giáp · Thái Cực Kiếm Phổ +3% sát thương · Bát Quái Bộ Pháp +3% thân pháp, +1% né · Ngũ Cầm Hí +0,3 hồi máu/giây · Thanh Tâm Quyết +1% giảm hồi chiêu, +0,8 hồi nội lực. Tính mỗi tầng, vĩnh viễn. Hiện trong Kho đồ.
- **Trang bị vĩnh viễn**, chia 7 phẩm: Phàm, Linh, Bảo, Tiên, Thần, Thánh, Hỗn Độn.
  - Nguồn chính là rương trùm (1–3 món tùy màn) và Thương hội.
  - Có 5 ô: Vũ khí, Y phục, Hộ phù, Hài, Bội ngọc.
  - Kho đồ lưu trong localStorage.
- **Thương hội** (sau mỗi màn):
  - Bày 4 món theo màn, giá theo phẩm (Phàm khoảng 25, Linh khoảng 60, Bảo khoảng 130…).
  - Nút Làm mới: 10 tiền, mỗi lần sau đắt thêm.
  - Mua xong có nút "Mặc ngay".
- **Bảng nhiệm vụ** (dạng thánh chỉ tông tối, bên trái dưới ô tiền):
  - Luôn có 3 nhiệm vụ: hạ quái, tinh anh, đập bình, liên kích, trụ không trúng đòn, Hóa Thân, xong đợt, đạt cấp.
  - Xong thì tự cộng tiền rồi thay nhiệm vụ mới.
- **Kỳ ngộ:**
  - Khoảng 70–110 giây có 1 NPC xuất hiện, có mũi tên vàng chỉ đường. Đi tới gần thì hiện hộp thoại Nhận lời / Từ chối.
  - Thử thách: hạ N quái trong 25 giây, không trúng đòn 15 giây, hoặc hạ yêu vật "Truy nã".
  - NPC chung: Kiếm Tiên, Tảo Địa Tăng, Cáp Mô, Lãng Khách, Lão Ăn Mày. **Riêng Tuyết Sơn** thêm Ưng Khách, Bà Lão Nấu Trà, Thợ Rèn Phương Bắc, Thợ Săn Hươu Tuyết (cờ `snow:1` trong `NPCS`).
  - Kỳ ngộ chọn loại (`evTick`): 62% thử thách, 20% **Thương nhân thần bí**, 18% **kẻ cướp** (từ đợt 2).
  - **Thương nhân thần bí** (sprite `thuong`, hào quang tím, dấu "?"): bán Bình Khí Huyết 8, Bình Nội Lực 6, Hộ Thể Đan 10, Cuồng Huyết Đan 14, và 1 trang bị ngẫu nhiên giá 55% Thương hội. Mỗi món mua 1 lần. Rời đi thì biến mất.
  - **Kẻ cướp** (viền đỏ, tự đuổi theo người chơi rồi chặn đường). **Người chơi không được chọn**: 50% bị cướp ngay (nút "Đành chịu"), 50% bị lôi vào map ẩn (nút "Vào trận"). Kết quả tung trong `openRob` (`e.fight`).
    - Lang Diện Đầu Mục (sprite `sontac`, gói Taiga BM_009): cướp 35% tiền (tối thiểu 10), hoặc bắt vào **Sơn Trại**: lâu la Sơn tặc, Sơn tặc cầm đao, Sơn tặc cung thủ, rồi **Thủ Lĩnh Sơn Tặc**.
    - Lang Nhân Thần Bí (sprite `langnhan`, gói Taiga BM_005): cướp 1 bình thuốc (hết bình thì 30% tiền), hoặc kéo xuống **Hổ Huyệt**: bầy Hổ dữ rồi **Hổ Vương**. Hổ vì sprite `ho` là con hổ.
    - **Map ẩn** (`MAPS.sontrai`, `MAPS.langhuyet`, cờ `hidden` nên không hiện ở menu): `enterArena` cất toàn bộ trạng thái map chính, dựng map mới, quái không tính vào tiến độ đợt. Còn ≤2 lâu la thì trùm ra, có tên và thanh máu trên đầu. Trùm chết rơi rương, mở ra bảng `#tacloot`. Bấm Rời khỏi thì `exitArena` trả về đúng chỗ cũ.
    - **Rương báu:** luôn có tiền và 1 đan dược (dùng ngay), 60% thêm 1 bình thuốc. Trang bị **có tỉ lệ**: 50% ở Sơn Trại, 55% ở Hổ Huyệt, trong đó 10% ra món thứ hai. Cấp từ cấp nhân vật đến +9. Phẩm theo `chestTier` (cao hơn bình thùng một chút): Phàm 71%, Linh 21%, Bảo 5,6%, Tiên 1,4%, Thần 0,35%, Thánh 0,09%, Hỗn Độn 0,024%. Bí tịch 8% ở Sơn Trại, 12% ở Hổ Huyệt. Vận may cộng thêm chút ít.
  - Đợt trùm: **Thổ Địa** thách hạ trùm mà khí huyết không xuống dưới 30%.
- **Hóa Thân** (Tôn Ngộ Không): đủ 100 nộ thì bấm. Khi Hóa Thân có hào quang khí vàng (Qi Aura).
- **Tạm dừng:**
  - Bên trái là thống kê trận.
  - Bên phải là công tắc Âm thanh, thanh Âm lượng, Rung màn hình, Hiện số sát thương, Giảm hiệu ứng (đều được lưu).
  - Nút Tiếp tục, và Bỏ trận (phải bấm 2 lần). **Đã bỏ nút Chơi lại.**

## 3. Bố cục HUD (bản đã chốt)

- **Trái trên:**
  - Chân dung **chỉ để nhìn**, không bấm được, không có vòng nộ hay nhãn "Hóa Thân!". Hóa Thân bấm ở nút dưới. Lúc Hóa Thân thì viền chân dung sáng vàng.
  - Tên, cấp và thanh EXP nằm dưới tên. **EXP màu tím**, khớp với hạt kinh nghiệm tím.
  - Ngay dưới đó là hàng **icon trạng thái** (`#avaFx`): ô vuông tối 20px (18px trên điện thoại), chữ Hán màu theo trạng thái, quét tối theo thời gian còn lại, số giây ở góc, nhấp nháy khi còn dưới 1,5 giây. Buff viền tối thường, debuff nền đỏ sẫm.
    - Buff: 聖 Hóa Thân, 疾 Thần tốc (Phong Hỏa Luân), 遁 Độn thổ.
    - Debuff: 毒 Độc (mất máu theo giây, xuyên miễn thương), 暈 Choáng (không đi, không đánh, không Lướt), 緩 Chậm (giảm tốc chạy).
- **Dưới chân dung:** ô tiền có khung viền vàng đồng, đinh hình thoi hai đầu. Bên dưới là bảng nhiệm vụ thánh chỉ, bấm tiêu đề để thu gọn.
- **Giữa trên:** thanh "Đợt 1/5 … %" khung xanh ngọc, **ruột vàng sáng chia 10 ô bằng vạch tối** (theo ảnh mẫu người dùng gửi; vạch là `#tbar #wbar:after`), và ô đồng hồ đỏ.
- Quy ước màu: Nộ cam vàng, Nội lực xanh dương, Khí huyết đỏ, EXP tím, tiến độ đợt vàng sáng có vạch chia ô (khác Nộ nhờ vạch). Đừng cho 2 thanh trông giống nhau.
- **Phải trên:** nút tạm dừng khung vàng có tua rua đỏ. Bên dưới là số **Hạ gục** và **Liên kích** kiểu clip: số pixel trắng to viền đen, nhãn vàng nghiêng.
- **Giữa đáy:** 3 thanh Nộ / Nội lực / Khí huyết, đầu thanh vát nhọn.
  - Icon **pixel art** (SVG ô vuông, crispEdges): tia sét vàng, giọt nước xanh, trái tim đỏ, nằm trong vòng đồng. **Không có chữ chú thích.**
  - Có vệt sáng lướt và vệt "máu vừa mất" màu vàng. Máu dưới 30% thì nhấp nháy đỏ.
  - Icon Nộ chớp như sét; đầy nộ thì chớp nhanh.
- **Hai bên thanh máu:** nút **Lướt** bên trái, nút **Hóa Thân** bên phải. Góc trái dưới để trống cho cần điều khiển.
- **Phải dưới:** bảng kỹ năng gồm 2 hàng ô vuông chữ Hán. Hàng trên là 3 chiêu và tuyệt kỹ, hàng dưới là 2 nội tại và 2 ô bình thuốc.

## 4. Sở thích và những thứ người dùng ĐÃ TỪ CHỐI (đừng làm lại)

- **Không** phong cách thủy mặc (nét mực, con dấu, núi mờ).
- **Không** ô trang bị nền màu sáng kiểu mobile. Giữ nền tối, viền màu theo phẩm.
- **Không** mix kiểu DNF cuộn ngang. Bản cuộn ngang đã bỏ.
- **Không** đổi kiểu Liên kích (đã thử nền mũi tên, vòng nổ, người dùng bảo trả về cũ). Riêng số Hạ gục có hiệu ứng nảy thì được giữ.
- **Không** dùng tài nguyên không rõ bản quyền (ví dụ ảnh từ aigei.com).
- Muốn tông **tối, viền vàng đồng, pixel Wuxia**. Đổi gì có thể làm thay đổi cảm giác chung thì **hỏi trước**.
- Người dùng hay gửi ảnh mẫu từ clip: làm theo hình dạng và tông màu trong ảnh.
- Đồ rơi phải dễ nhìn trên nền tuyết. Phân biệt bằng màu: tím = kinh nghiệm, đỏ = máu, xanh = mana.
- Trả lời bằng tiếng Việt, ngắn gọn, xưng "mình". Người dùng xưng "tao / mày".

## 5. Tài nguyên trong `assets/` và giấy phép

| Thư mục / file | Nguồn | Giấy phép |
|---|---|---|
| hero_nam/hero_nu, daulap, hacphong, bachhoa, ho, map/*, vfx/*, sfx/* | Wuxia_Free_Experience | Dùng và chỉnh sửa trong game được. Cấm đăng lại nguyên bộ file gốc. Danh sách tác giả âm thanh bên thứ ba cần kiểm tra trước khi phát hành. |
| hero_nam.png, hàng chạy | Khung chạy 8 khung do ChatGPT vẽ lại, đã ép bảng màu | Của người dùng |
| map/brk_*.png (vò, bình sứ, thùng) | Từ gói Wuxia, bình sứ tô lại | Như trên |
| ui/gear.png (icon trang bị) | Wuxia Pixel Icons Mega (HOANTDZ) + Xianxia Cultivation 90 Items (lazyman254, $1) | Cả hai cho dùng thương mại, cấm bán lại file gốc |
| ui/drops.png (bình rồng đỏ/xanh) | Xianxia 90 Items | Như trên |
| vfx/qi_aura.png | PixelDreamer Xianxia VFX demo | Miễn phí cả thương mại |
| npc/*.png (8 NPC) | Asia Fantasy Mega Collection free sample (HOANTDZ) | Dùng thương mại được. Cấm chia file rời, cấm dùng huấn luyện AI. Nên ghi credit "HOANTDZ". |
| npc/sontac (BM_009), npc/langnhan (BM_005) | Northern Steppe & Frozen Taiga free sampler (HOANTDZ) | Như dòng dưới |
| npc/ungkhach, balao, thoren, thosan (_m 78px cao, _p 128px) | Northern Steppe & Frozen Taiga free sampler (HOANTDZ), BM_011/016/008/013 | Dùng thương mại được, **bắt buộc** credit "HOANTDZ". Cấm chia file rời. Ảnh do AI tạo rồi chỉnh tay. |

- Dòng ghi công nằm ở màn hình mở đầu, dưới tiêu đề (`.mhead .credit`).
- Gói Northern Steppe: chỉ lấy 4/16. Bỏ 12 hình còn lại vì trang phục hoàng tộc hoặc pháp sư Mông Cổ, đô vật cởi trần, đá khắc chữ rune, quá lệch chất Tây Du.
- Gói đã xem nhưng không dùng:
  - Wuxia RTS Pixel Lite: chibi, lệch tông.
  - Spirit Herbs và Cultivation Essentials: tranh mịn, không phải pixel.
  - Magic Artifacts 110: tranh mịn, chỉ hợp làm icon kho đồ.
- **Lưu ý:** file zip chỉ để người dùng tự giữ và làm tiếp. Không đăng zip này công khai, vì giấy phép cấm phát tán file gốc.

## 6. Kỹ thuật quan trọng (cho người làm tiếp)

- Sprite gói Wuxia: `CHM` là meta JSON nhúng trong file, `CH[id]={meta,img,flash,ok,SC,AV}`. Hàm vẽ là `drawSpr` và `drawHeroFrame`. Bảng `ESPR` ánh xạ quái sang sprite. `HERO.SC=0.98`.
- `ZOOM=clamp(min(VW,VH)/(min<520?600:700),0.5,1.5)`; kích thước bản đồ `AW=3200`, `AH=2280`.
- `resize()` đo trực tiếp kích thước canvas. Có ResizeObserver và một vòng kiểm tra mỗi 400 ms, vì trình duyệt trong app Claude trên iPhone không báo sự kiện xoay màn hình (trước đây bị lỗi hình dẹt).
- Mỗi lần sửa, mình nối CSS mới vào trước `</style>` để đè lên quy tắc cũ (nhiều `!important`). Khi dọn code nên gom lại.
- Hàm chính:
  - Đợt: `startWave`, `endWave(fast)`, `finishWave`, `director` (đợt kết thúc khi `G.wK>=G.wTarget`).
  - Đồ rơi: `dropOrb`, `collect`, `drawOrb`.
  - Bình, thùng: `BRK`, `spawnBrk`, `brkDirector`, `hitBrk`.
  - Bình thuốc: `POT`, `pots()`, `drinkPot`, `gotPot`.
  - Nhiệm vụ: `QDEF`, `qHook`, `renderQuests`.
  - Kỳ ngộ: `NPCS`, `evTick`, `openEv`, `evWin`, `evFail`.
  - Thương hội: `openMarket`, `rollMarket`, `PRICE`.
  - Trang bị: `TIERS`, `SLOTS`, `makeItem`, `rollTier`, `gearCell`.
  - Trạng thái: `STX` (định nghĩa), `addStatus(k,T,v)`, `stOn`, `updStatus`, `fxList`, `renderFx`. Debuff lưu ở `P.st`. Hóa Thân xóa sạch debuff, không bị choáng khi đang Hóa Thân hoặc Độn thổ. Test: `TDST.addStatus('doc',4,8)`.
- **Kích thước NPC:** nhân vật chính cao khoảng 107 px (tính cả tóc). Sprite NPC trên sân (`_m`) cao 96–112 px: người lớn đứng khoảng 110, lão ông / Thổ Địa / Cáp Mô thấp hơn. NPC cũ dựng lại từ ảnh `_p` 128 px, NPC gói Taiga dựng từ ảnh gốc 320 px với cùng một tỉ lệ. Tên và dấu "!" tự đặt theo chiều cao sprite (`drawNpc`).
- **Bảng sau đợt trên màn thấp:** thẻ thu gọn, luôn 3 cột khi rộng từ 600 px, thanh Đổi thẻ / Tiếp tục ghim ở đáy (`#brk .bfoot` sticky). Trước đây nút Tiếp tục nằm ngoài màn hình điện thoại.
- Dòng Kỳ ngộ trong bảng nhiệm vụ dùng chữ ngắn (`c.q`), thời gian hiện ở cột phải.
- Test bằng Playwright (google-chrome + swiftshader) ở khung điện thoại 844×390 và máy tính 1280×720.

## 7. Việc có thể làm tiếp (chưa làm)

- Icon trạng thái đã xong, nhưng **quái chưa gây độc / choáng / chậm**. Cần chọn loại quái nào gây gì (gắn `addStatus` vào đòn đánh quái hoặc `hurtPlayer`).
- Thương nhân lưu động giữa đợt, đàn cầu phúc (buff 30 giây), thử thách cuối tuần.
- Chạy đổ người mạnh hơn, vạt áo bay; thêm động tác lướt, trúng đòn, ngã (cần vẽ sprite).
- Dựng lại Tuyết Sơn thành sân đá có bậc thang.
- Cân bằng đồ Hỗn Độn và giá Thương hội.
- Gom và dọn CSS trùng lặp.
- Quái gây độc, choáng, chậm khi đánh trúng (hệ thống đã có, chưa gắn vào quái).
- Kiểm tra cân bằng cấp trang bị: hệ số 0,025 mỗi cấp có thể làm đồ mới mạnh hơn đồ cũ theo màn.


## Cập nhật 21/11: chặng 1 (hồ sơ nhân vật, sảnh, thể lực)

- **Font số pixel riêng** "TDST Pixel" (dựng bằng fontTools theo dáng số trong clip, nhúng base64 trong CSS, chỉ áp cho chữ số 0–9) dùng cho số Hạ gục và Liên kích. Số Liên kích màu kem `#f6e7c1`. Màu đen tràn từ trên xuống theo `--cd = 1 − comboT/(COMBO_HOLD+COMBO_DECAY)`, hết thì mờ dần.
- **Tạo nhân vật** (`#create`, `save.prof`): tên 2–14 ký tự, giới tính, vũ khí (chỉ Kiếm mở, các vũ khí khác khóa "thử nghiệm"), kiểu tóc và màu tóc (chỉ mở lựa chọn có sprite: nam Đuôi ngựa, nữ Búi dải lụa, màu Đen). Tạo một lần. Save cũ chưa có hồ sơ thì hiện màn tạo, kho, bí tịch, thuốc và cài đặt giữ nguyên.
- **Sảnh** (`#lobby`, `showLobby`): có hồ sơ thì vào thẳng sảnh. Có chân dung, tên, cấp nhân vật, EXP tím, **Thể lực xanh ngọc** (số hiện tại/tối đa và đếm ngược điểm hồi kế). Nhân vật đứng thở trên nền Tuyết Sơn. Nút Vượt Ải mở màn chuẩn bị (màn menu cũ, đã ẩn phần chọn người phàm). Nút Tiếp tục ải đang dở đang khóa, chờ checkpoint ở chặng 2. Các ô Kho Đồ (chạy), Điểm Tâm, Luyện Đan, Luyện Vũ Khí, Chiêu Mộ (Sắp mở), Bang Hội (Cần máy chủ).
- **Cấp nhân vật lâu dài**: `prof.lv`, `prof.exp`, cần `150+90·lv+8·lv²`. Cộng toàn bộ EXP nhặt trong trận (`G.xpGain`) khi trận kết thúc, hiện ở bảng kết thúc.
- **Thể lực** (`save.sta={v,t}`, `STA`): tối đa 100, hồi 1 điểm/15 phút kể cả offline, ngừng hồi khi đầy. Trần 115 dành cho Điểm Tâm. Chưa trừ ở đâu (rương trùm ở chặng 3).
- **Màu số Liên kích theo mốc thưởng** (`#combov.t-rage / t-crit / t-dmg`): dưới 25 màu kem, từ 25 (Nộ +5%) cam, từ 100 (thêm Bạo +4%) vàng, từ 300 (thêm ST +5%) tím. Lên mốc thì số nảy sáng một nhịp (`tierup`). Đếm lùi tụt mốc thì màu tụt theo. Dòng thưởng nhỏ bên dưới cùng tông màu.
- **Sảnh** dùng `#lobby:not([hidden])` cho quy tắc display, để thuộc tính `hidden` vẫn ẩn được sảnh khi vào trận. HUD trong trận hiện tên hồ sơ.
- **Màn tạo nhân vật 3 cột** (`#create`, `.cx`): trái là tên, giới tính, hàng icon binh khí (Kiếm và Phù Chú lấy từ `gear.png` ô 0 và 10; Đao, Thương, Côn là icon pixel 64 px vẽ bằng code, nhúng PNG base64 trong `WICON`), kèm mô tả. Giữa là nhân vật trong game cỡ lớn đứng thở trên nền Tuyết Sơn, mũi tên ◀ ▶ đổi kiểu tóc (kiểu chưa có sprite thì tối hình và ghi "Chưa có sprite"), ô màu tóc. Phải là thông tin nhân vật và võ học tiêu biểu (Chiêu thức: đánh thường, 3 chiêu, tuyệt kỹ; Nội tại: 2), bấm ô để xem mô tả, hồi chiêu, nội lực. Xem được vũ khí thử nghiệm nhưng nút "Bước vào giang hồ" tắt. Đã có hồ sơ thì mở `#tao-nhan-vat` để xem lại màn này (chỉ xem, không ghi đè).
- **Màn tạo nhân vật, bố cục chốt:** cột trái là tên, giới tính, icon binh khí, rồi **nhân vật trong game** (mũi tên ◀ ▶ đổi kiểu tóc, ô màu tóc ngay dưới). Cột giữa là **tranh minh họa** vùng khởi đầu (tạm dùng cảnh Tuyết Sơn vẽ bằng `paintMapPack`, kèm tên và lời dẫn, vì chưa có tranh minh họa riêng). Cột phải là thông tin nhân vật và võ học tiêu biểu.
- **Tài nguyên cần thêm:** tranh minh họa riêng cho màn tạo nhân vật (hoặc mỗi vũ khí một tranh), sprite kiểu tóc và màu tóc.
- **Hiệu năng:** `frame()` bỏ qua `render()` thế giới khi sảnh, tạo nhân vật hoặc kho đồ đang che toàn màn (`coverOn`). Trước đó map nền vẫn vẽ 60 lần/giây phía sau sảnh. Nền sảnh và tạo nhân vật làm tối trực tiếp trên canvas (`dimCanvas`), không dùng `filter` CSS. Lớp đen Liên kích chỉ cập nhật theo 25 nấc. Tránh thêm `filter`, `backdrop-filter` trên phần tử lớn, vì Safari iPhone rất nặng.


## Cập nhật 21/11: chặng 2 (Vượt Ải, bảng nghỉ, checkpoint)

- **Tuyến ải** (`ROUTE.tuyet`, `G.route`): Tuyết Sơn có 5 ải, mỗi ải là 1 đợt, ải 5 là trùm Ngưu Ma Vương. Các bản đồ khác hiện "Sắp mở". Số ải để trong `ROUTE` để sau mở 7 hoặc 9 ải.
- **Sao 1–5** (`STARS`, `sel.star`): trục riêng với số ải, nhân máu, sát thương, tốc ra quái (★1 ×1 → ★5 máu ×3,3). `G.stage = sao` nên cấp quái và phẩm rương tăng theo sao. Hạ trùm ★n thì mở ★n+1. Tiến độ ở `save.route.tuyet = {star, best:{sao:ải cao nhất}, clear:{sao:true}}`. Màn Vượt Ải hiện 5 nút sao (khóa sao chưa mở), dải tiến độ 1–2–⑂–3–4–主 và ô **Kèo săn trùm**.
- **Bảng nghỉ** có 5 tab: Kết toán, Tu luyện, **Trang bị** (5 ô, danh sách đồ cùng ô, so món đang mặc với món chọn, nút Trang bị ngay), Võ học (2 cột Người phàm và Thần tướng), **Tạp hóa** (mua thuốc). Nội dung cuộn riêng (`#bbody`), nút Tiếp tục ghim đáy, nút Đổi thẻ chỉ hiện ở Tu luyện. Màn thấp: dải chỉ số 1 hàng cuộn ngang.
- **Hai đường** (`G.path`): xong ải 2 phải chọn ở Kết toán mới Tiếp tục được, lợi ích hiện trước khi chọn.
  - `ven` (Ven núi): ải 3–4 cần hạ ít hơn 28%, tốc ra quái ×0,8, mỗi ải có **Suối Ấm** (`G.heal`, đứng trong vòng hồi 6% khí huyết mỗi giây).
  - `trai` (Trại cướp): ải 3–4 thêm 2 tinh anh, tinh anh 40% rơi **Tuyết Sâm** (dược liệu thường, orb `mat`).
  - Hai đường cùng dẫn về trùm.
- **Kèo săn trùm** (`G.keo`): ải 5 có 2 **cột băng** (breakable `cotbang`, 12 đòn, sprite vẽ bằng code `ICE_SRC`). Phá đủ 2 cột trước khi trùm ngã thì `G.keoDone`, rương trùm thêm 1 lượt roll dược liệu. Tiến độ kèo hiện trong bảng nhiệm vụ.
- **Nguyên liệu** (`save.mat = {duoc, hiem}`, `MATN`): Tuyết Sâm (thường), **Băng Tâm Liên** (hiếm). Rương trùm luôn roll 1 lượt (45% Băng Tâm Liên, còn lại 1–2 Tuyết Sâm), kèo thành công thêm 1 lượt. Hiện trong Kho đồ.
- **Checkpoint** (`save.cp`, `saveCP(phase,next)`, `resumeCP()`): lưu lúc vào ải 1, sau mỗi ải (`phase:'rest'`, kèm 3 thẻ đang bày), khi chọn thẻ, đổi thẻ, đổi đồ, mua thuốc, chọn đường, và khi bấm Tiếp tục (`phase:'ready'`). Lưu tiền, cấp, EXP, thẻ đã chọn (`P.mods`, `P.stacks`, cấp chiêu), nhiệm vụ, đường, kèo.
  - Sảnh: nút **Tiếp tục ải đang dở** khôi phục đúng trạng thái.
  - Thua: nút **Thử lại ải N** quay lại đúng ải đó với nhân vật và thẻ đã tích lũy.
  - Chống trùng: thẻ được lưu sẵn nên tải lại không đổi thẻ; tiền sau khi mua được lưu cùng lúc với thuốc nên không hoàn tiền; rương trùm đánh dấu `cp.chestDone` cùng lúc cất đồ, tải lại thì không nhận lại mà kết thúc tuyến luôn; EXP nhân vật cộng ở mỗi checkpoint; Tiên ngọc khi thua chỉ tính phần tiền vượt mốc đã trả (`cp.paid`).
- Xuất phát mới sẽ bỏ ải đang dở (có ghi chú trên màn Vượt Ải).
- **Test nghiệm thu** (Playwright, 844×390, 1280×720, 747×325, cả 2 đường): PASS khóa sao, checkpoint lúc xuất phát, nghỉ sau ải, tải lại khi đang nghỉ giữ nguyên thẻ, Đổi thẻ ẩn ngoài Tu luyện, đổi đồ khi nghỉ, mua thuốc rồi tải lại không hoàn tiền, phải chọn đường mới đi tiếp, hiệu ứng từng đường, thua rồi thử lại đúng ải, kèo và rương, rương chỉ nhận 1 lần, mở ★2.


## Cập nhật 21/11: chặng 3 và 4

**Chặng 3: thể lực, Điểm Tâm, rương, kho**
- **Rương trùm tốn thể lực** (`CHEST_STA = 15`, `routeChest`, `claimChest`): mở rương thì hiện phí và bảng rơi, bấm "Nhận thưởng" mới trừ thể lực và trao đồ. Không đủ thể lực thì nút tắt, chỉ có "Hoàn thành (tập ải)": vẫn tính vượt ải, mở sao, nhưng không có thưởng. Phí và bảng rơi cũng hiện ở màn Vượt Ải (`.stafee`). Chống trùng: `cp.chestDone` và trừ thể lực cùng một lần lưu.
- **Bảng rơi theo sao** (`CHEST_T`, `chestRoll`, thông số thử nghiệm): luôn có Huyền Thiết (3 ở ★1 đến 7 ở ★5) và 1 lượt dược liệu (+1 nếu kèo). Trang bị và bí tịch roll theo bảng của từng sao. Đã bỏ kiểu phẩm tăng vọt theo số màn liên tiếp ở rương trùm.
- **Điểm Tâm** (`DT`, `dtInfo`, `eatBite`): giờ Việt Nam (UTC+7) lúc 07:00, 14:00, 21:00, mỗi khung 2 giờ, nhận +15 thể lực một lần, được vượt trần tới 115. Nếu đang gần trần thì chỉ cộng phần vừa đủ và giữ quyền nhận phần còn lại tới hết khung (`save.dt = {key, got}`). Mini game: bấm bánh bao 5 lần (mỗi lần cách tối thiểu 110 ms), đủ 5 lần mới cộng. Số miếng đã ăn không lưu, nên tải lại giữa chừng thì không được cộng. Test giả giờ bằng `window.__TDST_NOW`.
- **Kho đầy** (`INV_MAX = 120`, `addItems`, `save.pend`): không còn tự xóa đồ cũ. Đồ mới khi kho đầy vào mục "Đồ mới chờ xử lý" trong Kho Đồ, có nút Cất vào kho (khi có chỗ) và Phân giải. **Món đang mặc không phân giải được.**
- Nguyên liệu mới: **Huyền Thiết** (`mat.thiet`, nguyên liệu cường hóa).

**Chặng 4: Luyện Đan, bí tịch, Chiêu Mộ, Luyện Vũ Khí** (mở từ ô ở sảnh, khung `#lbm`)
- **Dược liệu:** mọi tinh anh 12% rơi Tuyết Sâm (đường Trại cướp 40%). Rương trùm roll Băng Tâm Liên.
- **Luyện Đan** (`RECIPE`):
  - **Cuồng Huyết Đan, dùng trong ải:** 3 Tuyết Sâm, mang tối đa 5 viên (`save.danBag`). Trong trận bấm nút 狂 cạnh nút Lướt hoặc phím 3 (`useDanNow`, đang có hiệu lực thì không dùng chồng). Khi nghỉ vẫn có thể bấm "Dùng khi vào ải tới" ở tab Tạp hóa (`G.danNext`, lưu trong checkpoint).
  - **Trúc Cơ Đan, vĩnh viễn, có giới hạn:** 2 Tuyết Sâm + 1 Băng Tâm Liên, mỗi viên +20 khí huyết tối đa, áp cả trong và ngoài ải. Mỗi mốc vượt map mở thêm 1 viên được dùng: hạ trùm Tuyết Sơn ở một mức sao lần đầu thì +1 (`truccoMax` = số mức sao đã vượt, tối đa 5). Chưa vượt mốc nào thì chưa luyện được.
- **Bí tịch Hồi Phong** (`SEC`, `save.sec`): học trong Kho Đồ, mục Bí tịch võ công (thử nghiệm: 1 Băng Tâm Liên + 40 Tiên ngọc), bấm "Mang theo" để chọn ngoài ải. Sau khi Lướt, Hoành Tảo kế tiếp trong 2,5 giây quét gần trọn vòng, rộng hơn 50%, mạnh hơn 20%, vẫn dùng động tác chém của Kiếm.
- **Chiêu Mộ** (`CM`, `save.gods`, **cấu hình thử nghiệm**): khởi đầu có Tôn Ngộ Không. Mỗi lần chiêu mộ 30 Tiên ngọc, 4 Hóa Thân cùng trọng số; trùng thì +1 Mảnh Hóa Thân, 3 mảnh đổi 1 Hóa Thân chưa có. Màn Vượt Ải khóa Hóa Thân chưa có.
- **Luyện Vũ Khí** (`ENH`, `it.plus`): cường hóa vũ khí đang mặc từ +1 đến +9. Phẩm đá, tỉ lệ thành công và xử lý khi xịt **chưa chốt**. Bản thử nghiệm: luôn thành công, tốn (cấp+1) Huyền Thiết, mỗi cấp +5% chỉ số gốc (`equipBonus`).
- **Test** (Playwright, 844×390, 1280×720, 747×325): PASS Điểm Tâm (tải lại giữa chừng không cộng, đủ 5 miếng +15, một lần mỗi khung, trần 115 giữ quyền nhận phần còn lại, ngoài khung thì khóa), rương tốn 15 thể lực và chỉ nhận 1 lần kể cả tải lại, hết thể lực tập ải, kho đầy vào hàng chờ, bảo vệ món đang mặc, luyện 2 loại đan, chiêu mộ, cường hóa +2, học và mang Hồi Phong, trong trận có +20 máu và hiệu ứng Hồi Phong sau Lướt. Chạy lại toàn bộ test chặng 2: PASS.


## Cập nhật 21/11: chặng 5 và ghép bản thử chiến đấu và trang bị (`TDST_ChienDau_TrangBi_BanThu.zip`)

**Chặng 5 (HUD)**
- Avatar chỉ để hiển thị. Nộ nằm trong vòng tròn của nút Hóa Thân viền lục giác. Giữa đáy chỉ còn Khí huyết (dày) và Nội lực.
- Số bình thuốc in đậm trong huy hiệu tròn viền vàng.
- **Cảnh báo máu thấp:**
  - Từ 20% đến dưới 30%: chữ "Máu thấp" trên đầu nhân vật (`G.lowTag`).
  - Vừa tụt dưới 20%: viền màn hình đỏ nháy 2 nhịp trong 2 giây (`#lowEdge.pulse`), sau đó giữ viền đỏ nhạt cố định (`.steady`).
  - Hồi lên từ 20% thì tắt hẳn, chỉ nháy lại khi tụt xuống dưới 20% lần nữa (`G.below20`, `G.edgeT`).
  - Viền nằm dưới HUD (z-index 1).
- Liên kích giữ bản đã chốt: giữ 2,2 giây, đếm lùi 2,4 giây, màu đổi theo mốc 25/100/300.

**Chặng 6 (online):** chưa có máy chủ. Bang Hội, raid, cứu đồng đội, đấu giá, PvP chưa làm. Sảnh ghi "Cần máy chủ".

**Ghép bản thử:** dựng lại bản gốc của patch bằng cách áp ngược `TDST_ChienDau_TrangBi.patch` lên `index.html` của bản thử, rồi ghép 3 bên (`git merge-file`) với bản hiện tại. Ghép tự động 9/18 đoạn, còn 12 khối xung đột gỡ tay như sau:

| Khối | Bản thử | Bản hiện tại | Đã xử lý |
|---|---|---|---|
| Cường hóa | `it.forge`, "Đá thử" (`save.forgeStones`), bảng `FORGE_ODDS`, hư hỏng/sửa, mốc +3/+6/+9, 4% mỗi cấp, cường hóa trong Kho đồ | `it.plus`, Huyền Thiết, luôn thành công, 5% mỗi cấp, Luyện Vũ Khí ở sảnh | **Giữ hệ của bản thử.** Đá = Huyền Thiết (`forgeStones()` đọc `mats().thiet`). Luyện Vũ Khí ở sảnh gọi chung `forgeItem`. Đồ cũ `plus` tự chuyển sang `forge`. |
| Truy Phong Kiếm và Hồi Phong | `save.truyPhong`, học khi mở rương trùm đầu | Hồi Phong trong `save.sec` | Đưa Truy Phong vào `SEC` (`secOn('truyphong')`). Chỉ mang được **một bí tịch Lướt**. Save cũ có `truyPhong` tự chuyển. |
| Rương trùm | `openChest` cho +4 đá và Truy Phong ngay khi mở | `routeChest` và `claimChest` tốn 15 thể lực, chống trùng | Đưa 4 Huyền Thiết và Truy Phong vào `claimChest`: chỉ nhận khi bấm Nhận thưởng, đúng một lần. `CHEST_T.thiet` = 4 ở mọi sao. |
| Kho | Bỏ tự xóa bằng cách thêm thẳng (không giới hạn) | `INV_MAX` 120 + hàng chờ | Giữ `addItems` và hàng chờ. |
| Phân giải | Cho phân giải món đang mặc (tự tháo) | Chặn | Giữ chặn. Thêm: món hư hỏng không mặc được. |
| Nhãn thanh đợt/trùm | "Màn/Đợt" + boss-phase | ★/Ải | Giữ nhãn ★/Ải, thêm boss-phase (tên, %, thanh đỏ) và "· Pha 2". |
| `dash()` | Hủy nhát đang lấy đà, bật `truyPhongT` | Bật `hoiPhong` | Gộp cả hai trên cùng dòng. |
| Xác nhận đập ≥+7 | `confirm()` | | `confirm()` bị chặn trong khung artifact, đổi sang bấm 2 lần trên nút. |
| Mô tả đánh thường | Ghi rõ +6/+9 | | Đổi mô tả. Mốc +6/+9 hiện "??? tự khám phá" tới khi đạt (`save.forgeSeen`), đạt mốc thì báo đòn mới. |
| CSS | Chèn cùng vị trí với CSS mới | | Giữ cả hai. |

Các phần còn lại của bản thử ghép nguyên văn:
- Chiêu Kiếm A–B, C ở +6, kiếm khí ở +9, dấu Phá Thế, xuyên 5% giáp ở +3, áp sát thương theo thời điểm (`startSwordCut`, `finishSwordCut`).
- Lướt hủy nhát đang lấy đà.
- Sáu ô (thêm `tay`: Đai / Găng tay).
- Thanh HP tinh anh luôn hiện.
- Quái thường ẩn HP.
- Thưởng mốc theo ô.

**Thêm mới**
- **Hướng dẫn** (`TUT`, `tutInit`, `tutHook`, `save.tut`) ở ải đầu tiên: Di chuyển (220 px), Chém (4 nhát), Lướt, Chém tiếp trong 2,5 giây sau Lướt. Bước Chém và Chém tiếp gọi 3 yêu binh tập luyện ngay gần nhân vật. Nút Lướt nhấp nháy ở bước Lướt. Xong một lần thì không hiện lại.
- **Màn Vượt Ải** có khối "Mục tiêu săn" (`huntList`): trùm, Truy Phong Kiếm (khi chưa có), Huyền Thiết, dược liệu, trang bị 6 ô kèm phẩm cao nhất, bí tịch, cơ chế tinh anh/trùm theo sao. Ngay dưới là phí nhận rương và bảng rơi.
- **Tinh anh ★3+ có Hộ Thể Cương Khí:** khiên bằng 35% máu (thanh xanh trên thanh HP, vòng sáng quanh tinh anh). Nhát C (Phá Thế) gây gấp đôi lên khiên. Phá khiên thì tinh anh choáng 1,6 giây. 6 giây không trúng đòn thì khiên hồi đầy.
- **Trùm ★5 có pha 2 ở 50% máu** (`bossPhase2`): chạy nhanh hơn 30%, đánh mạnh hơn 25%, gọi 2 Hỏa Tướng, có hào quang đỏ, thanh trùm ghi "· Pha 2". Đây là thông số thử.
- **Sprite còn thiếu:** icon Đai / Găng tay (`gear.png` chưa có ô, đang vẽ tạm bằng code), động tác riêng cho nhát C và Truy Phong (đang dùng lại sprite chém, nhát C giữ tư thế lâu hơn), hiệu ứng khiên Cương Khí, hào quang pha 2.

**Nghiệm thu** (Playwright, Chrome, 844×390 · 1280×720 · 747×325)
- Luồng solo PASS 9/9: Sảnh → chọn ải (mục tiêu săn, phí) → vào Tuyết Sơn ải 1 có hướng dẫn → chạy, chém, Lướt, chém tiếp → bảng nghỉ → tải lại và tiếp tục đúng chỗ (cùng thẻ) → trùm ải 5, thanh HP trùm ở giữa trên → nhận thưởng đúng một lần (−15 thể lực, tải lại không nhận lại, có Truy Phong) → nâng Kiếm +1 ở Luyện Vũ Khí.
- Chiến đấu PASS 9/9: +0 A–B, vừa đi vừa chém, +6 A–B–C, Lướt hủy nhát lấy đà, Truy Phong sau Lướt, +9 kiếm khí, đan trong ải (nút và phím 3, không dùng chồng), tinh anh ★3 Cương Khí, trùm ★5 pha 2.
- Cảnh báo máu thấp PASS (đủ 7 trạng thái). Chạy lại test chặng 2, 3, 4: PASS.
- Clip `TDST_clip_chem_A-B-C_Luot.mp4`: 7,2 giây, tốc độ thật. Game chạy 59–60 FPS, ghi 25 khung/giây. Nhật ký: Chạy 0,67s → A 1,27 → B 1,78 → C 2,30 → A 2,82 → B 3,32 → Lướt 3,40 → Truy Phong 3,82 → B 5,05 → C 5,57. Trong clip đã tắt chiêu chủ động để chỉ thấy đánh thường.
- Chưa xác nhận: Safari iPhone thật, cảm giác tay cầm thật.
