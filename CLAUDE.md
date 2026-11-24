# Tây Du Sinh Tồn · bàn giao cho Claude (đọc trước khi làm)

Game hành động sinh tồn pixel art một file (`game/index.html` + `game/assets/`), canvas, chạy trên trình duyệt, ưu tiên điện thoại xoay ngang. Chủ game nói tiếng Việt, xưng "tao/mày"; trả lời bằng tiếng Việt.

Repo này để **riêng tư** và có chứa asset mua có giấy phép (`game/assets/`, `nguon/pack_wuxia/`). Chủ game đã đồng ý lưu ở đây và chịu trách nhiệm. Không công khai repo hay link game.

Lịch sử cũ hơn: `BAT_DAU_CLAUDE.md`, `TONG_HOP_TINH_NANG.md`, `tai_lieu/`. Khi mâu thuẫn, file này và code game là bản đúng.

## Luật làm việc của chủ game (bắt buộc)
1. **Cái gì muốn sửa phải báo trước.** Đề xuất, chờ duyệt rồi mới làm. Ngoại lệ: chủ game ra lệnh trực tiếp.
2. **Tạo bằng công cụ có sẵn, không chắp vá.** Hình nhân vật, VFX tạo bằng PixelLab (skeleton animation, VFX creator) hoặc lấy từ gói asset đã mua. Không vẽ VFX bằng code; không ghép, vá frame.
3. **Phác thảo trước, duyệt rồi mới tạo trên PixelLab** (với động tác, tư thế mới).
4. **Kiểm từng frame 98–99% so với master** trước khi gửi: không dư kiếm, không mất tay chân, độ dài kiếm bằng master, trang phục giữ nguyên.
5. Không co giãn (squash/stretch) frame nhân vật, không hitstop, không tự đổi màu nhân vật.
6. Gửi video/ảnh kiểm tra khi xong mỗi phần. Báo đúng sự thật, kể cả lỗi.
7. **PixelLab chỉ dùng khi thật sự cần thiết, không lạm dụng** (chủ game dặn 24/11). Làm trước bằng cách rẻ: phác thảo/xem trước, dùng lại asset đã có, chỉnh timing/vị trí/code, bản mẫu thử trong game. Chỉ gọi PixelLab khi bản đó không ổn. Không "thử cho biết": mỗi lần gọi nói rõ vì sao cần và số lượt dự kiến.

## Hiện trạng game (23/11)
- **Bộ Kiếm (nam và nữ chung):**
  - Đánh thường A → B (khởi kiếm, hồi kiếm); +6 mở C Phá Thế Trảm (quét 360°, vòng elip PixelLab `k5c_*`). Vệt chém A/B/C: bộ Slashes Frostwindz (`zs1-3`), đã đổi màu theo game.
  - **Q Huyết Ảnh Trảm:** khóa mục tiêu, lướt xuyên, xoáy đỏ 6 nhát, vòng kết (VFX PixelLab `hv_*`).
  - **F Thiên Xu Kiếm Trận:** VFX gói Wuxia xuất từ Godot, `tx_in/loop/out`; id vẫn là `k2`.
  - **X Vạn Kiếm Quy Tông:** bản gốc gói Wuxia, phóng ngang (`vk_e`).
  - **Ô tự kích hoạt Hồi Phong Quy Sao** (`k3`, có sẵn từ đầu trận): 3 phi kiếm vàng (`hp_guard`) bay vòng, tự lao chém quái gần rồi về.
  - Đã bỏ Lướt Trảm, Kiếm Ảnh, Kiếm Tâm, Kiếm Ý. Code lướt `cutC` vẫn giữ vì Huyết Ảnh dùng.
- **HUD ô kỹ năng:** hàng trên 4 ô chủ động (Q, F, X + 1 trống). Hàng dưới: 2 ô chiêu tự thi triển có hồi chiêu, máu, mana, 1 ô dự phòng. Nội tại cộng chỉ số không hiện ô.
- **Cấp và phẩm:**
  - Tối đa **Lv200, 12 phẩm**. Ra mắt mở đến **Lv70 và 7 phẩm** (`LV_OPEN`, `TIER_OPEN`).
  - Cấp bắt đầu mỗi phẩm (`TIER_LV`): 1, 7, 14, 22, 32, 43, 56 | khóa: 71, 90, 113, 140, 170. Số cấp mỗi phẩm tăng dần (6 → 31).
  - Kinh nghiệm lên cấp: `200 + 60×L + 3×L²` (đã giảm dốc).
  - Đồ rơi không vượt phẩm theo cấp nhân vật (`makeItem`). Mặc đồ phải đủ cấp của phẩm; chi tiết món đồ hiện "Yêu cầu Cấp X".
  - 5 phẩm khóa: Hồng Hoang, Thái Cổ, Vô Cực, Tạo Hóa, Thiên Đạo.
  - Cường hóa tối đa +12, mở đến +9 (`FORGE_OPEN`).
- **Lực chiến:** `powerOf()` quy đổi chỉ số + cấp, chỉ để hiển thị. Hiện dưới thanh kinh nghiệm ở sảnh (`#lbCp`) và trong trận (`#cpv`).
- **6 ô trang bị:** Vũ khí, Y phục, Hộ phù, Hài, Nhẫn/Bội, Đai/Găng.
- Bản chơi thử (artifact của tài khoản cũ): https://claude.ai/artifact/7HgwkR1wd2kZ521bQ1oRTA. Tài khoản khác sẽ đăng link mới.

## Sở thích thẩm mỹ của chủ game (rút ra từ góp ý)
- VFX phải chau chuốt, dày, có chiều sâu. Nét mỏng, phẳng là "như đồ chơi". Vòng elip đòn C phải có độ dày đáng kể.
- Không để đòn đánh trông như nhân vật bị giật, lag hay xoay 360° bằng cách lật sprite. Cảm giác xoay để VFX lo.
- Đòn A, B, C phải liền mạch như một combo. Vệt chém phải nằm trước mặt, đúng hướng chém.
- Không dùng mảnh, hạt lạ do demo để lại (ví dụ tia trúng cọc trong bản xuất Godot bị xem là "mảnh băng").
- HUD gọn: ô kỹ năng không quá to, thanh máu và mana đủ to, không che màn hình. Joystick cố định góc trái dưới, không hiện ở chỗ chạm khác.
- Điện thoại (iPhone, Samsung): không được tự phóng to khi bấm đúp hoặc khi nhập tên. Nút không được lọt khỏi khung.
- Ngộ Không: khỉ con là con của Ngộ Không, không đeo vòng kim cô. Hình phải cổ trang, không giống võ sĩ hiện đại.
- Chủ game thích được thử ngay trong game: khi cần duyệt hiệu ứng, có thể làm tạm ô kỹ năng TEST, duyệt xong thì xóa.
- Ảnh và video tham chiếu đã gửi: `nguon/tham_chieu/` (xem README trong đó).

## Vũ khí, aura, trang phục (ĐÃ LÀM, 23/11)
- **Vũ khí là lớp riêng:** nhân vật dùng sheet không kiếm `hero_{nam,nu}_ns.png` + lớp nắm tay `_hand.png`. `WSOCK[giới]["x,y"]` = [chuôi x, chuôi y, góc, 'b' sau thân | 'f' trước thân] cho từng khung. `drawHeroFrame` vẽ vũ khí theo socket.
  - Ảnh vũ khí: `game/assets/wpn/*.png` (nằm ngang, mũi sang phải), thông số trong `WPN`. Tên món → ảnh: `WART` (Thanh Phong, Long Tuyền = kiếm gốc; Thái A, Tử Điện = kiếm đỏ; Hàn Thiết = đại kiếm; Trảm Yêu = trảm mã đao).
  - Công cụ: `cong_cu/claude/build_ns.py` (tách kiếm + socket; khung lệch thì thêm toạ độ tay vào `MAN`), `detsword.py`, `reattach.py`.
- **Aura cường hóa** (`WAURA`, ảnh `vfx/aura_{3,6,9,12}.png`): +3 lục mờ, +6 vàng, +9 tím, +12 đen + sấm (mốc +12 khóa). Kéo theo chiều dài lưỡi.
- **Hồi Phong Quy Sao** bay bằng chính vũ khí đang cầm, kèm aura.
- **Trang phục theo bộ:** `OUTFIT[tên Y phục] = hậu tố sheet`. Hiện có `'Huyền Giáp':'hg'` → `hero_{nam,nu}_hg.png` (+ `_hg_hand.png`), 48 khung mỗi giới, tạo bằng `transfer-outfit-v2` (3 khung/lần, 10 lượt). Ảnh mẫu: `nguon/pixellab/outfit/ref_huyengiap2.png` (nam), `ref_nu.png` (nữ). Làm bộ mới: `nguon/pixellab/outfit` + script `hg/run_tf.py` (đã chép vào `cong_cu/claude/`).
- **Luyện Công** có nút "Áo" và "Kiếm" để thử nhanh (gồm cả Thương và Tay không).
- **Thương / Song Quyền (23/11):** đã có nhân vật pixel (đứng, chạy, lướt, trúng đòn, ngã) dùng chung sheet không kiếm. Thương = ảnh `wpn/thuong1.png` (cầm ở 40% cán), Song Quyền = tay không (`WCLASS_ART`). **Chưa có động tác đánh** (chủ game dặn để sau): khi đánh vẫn giữ tư thế đứng/chạy. Song Quyền chưa có trong `WEAPONS` (chưa có bộ chiêu). Phác thảo combo Song Quyền A/B/C đã gửi: `cong_cu/claude/quyen_sketch.py`.

## Cập nhật 24/11 (Codex + Claude)
- **Rương Boss chờ nhận ĐÃ LÀM:** `recordBossVictory`, `showBossChest`, `claimChest`, nút `#lbBossChest` ở sảnh, `save.bossChest` (một rương, thưởng roll sẵn, trừ 15 thể lực lúc nhận). Hạ Boss lần nữa khi đang có rương chờ thì thưởng mới không cộng dồn. `cp.chestDone` = đã hạ Boss chưa kết toán; "Tiếp tục" hoặc "Vượt Ải" ở sảnh sẽ kết toán trước.
- **Tạo nhân vật:** chọn avatar (8 mẫu mỗi giới, `portraits/avatar-*.webp`, `profile.avatar`), tranh cảnh theo avatar có xem toàn cảnh, nút "Thử chiêu" (`startTraining(true)`, `G.createPreview`), cột Binh khí bên phải. Nguồn gốc ảnh avatar/tranh cảnh cần chủ game xác nhận.

## Cập nhật 24/11 (phiên làm tự động ban đêm)
- **Combo Kiếm mới A7/B7/C12 ĐÃ VÀO GAME** (nam và nữ): thân không kiếm tạo bằng PixelLab `animate-with-skeleton-v3` (chân khép, thân trên làm chuyển động, bỏ 3 khớp kiếm khỏi rig), kiếm là lớp vũ khí gắn socket 'f' lấy từ khung xương. Ô mới ở hàng y=384/512 của `hero_{nam,nu}_ns.png` + `_hand.png`; ô cũ y=256 vẫn dùng cho lướt Huyết Ảnh (`cutC`) và bộ Huyền Giáp (Huyền Giáp vẫn dùng khung đánh cũ). Tổng thời lượng giữ **580/550/800 ms** (vì `dur` quyết định chu kỳ đánh = DPS); khung chạm A4/B5/C4. Chi tiết: `animation_manifest.json`, `QA_REPORT.md`, `ANIMATION_A_B_C/`.
  - Rút kinh nghiệm: tạo kèm kiếm bằng PixelLab cho kiếm nhòe/ngắn/vỡ mũi/mất; chân rộng làm lộ quần (trôi khỏi Master). Cách đúng: ảnh gốc là khung idle không kiếm của `_ns`, chân khép.
  - Còn thiếu: lớp bàn tay mới cho khung mới; VFX elip C vẫn hiện nguyên vòng ngay khung đầu (cần VFX có đầu nhọn); chưa có clip Hovl gốc để so từng khung; bộ Huyền Giáp chưa có combo mới.
- **Đòn C (cập nhật theo video Hovl):** pose mới bám chuỗi Hovl (khuỵu → dựng → duỗi → hông → cao → vung xuống chạm ở khung C9 = 70% đòn → thu), VFX elip mới `hc_behind`/`hc_front` (PixelLab pro, đầu nhọn, vẽ dần, dày), T 0,28 s bật trước chạm 0,04 s; không còn `zs1` và `k5c_*`. Phân tích Hovl: `nguon/tham_chieu/hovl/MOTION_ANALYSIS.md`. VFX tạo qua `cong_cu/claude/plvfx.py` (GAMEPACK=1, ARTIST=pro, truyền sprite nhân vật không kiếm, mô tả có kích thước và độ dày cụ thể; lite cho kết quả quá mỏng).
- **Thiên Xu Kiếm Trận (F) làm lại:** một đòn nổ x1,2 khi kiếm chạm đất (1,2 s), rồi mỗi giây x0,6 trong 3 đến 5 giây (3 + 0,5/cấp, tối đa 5), bán kính 125.
- **Vạn Kiếm Quy Tông (X):** có tầm ngắm (`aim:'lane'`: di chuột/chạm chọn hướng, hiện làn kiếm 560×140), VFX `vk_e` xuất lại từ Godot 4.7.1 còn 16 kiếm (gốc 36, bản cũ ở `nguon/vfx_goc/`, quy trình ở `cong_cu/claude/rebake_vankiem.md`; **bắt buộc `godot --headless --import` trước khi quay**).
- **Hồi Phong:** kiếm bay có viền tối (trông như mất kiếm trên nền tuyết sáng).
- **Ngộ Không:** đang di chuyển thì giữ khung chạy + nghiêng người theo nhịp đánh (hết trượt chân).
- **UI:** nút Xuất phát/Về sảnh/Kho đồ ghim cả trên điện thoại ngang >900px; avatar 4 cột ở màn hẹp. Kiểm bố cục: `cong_cu/claude` + script audit (xem `QA_REPORT.md`).
- PixelLab chạy được trong môi trường này (key lưu qua `request_credential`, host `api.pixellab.ai`, script `cong_cu/claude/pl.py`); mỗi lần 12 khung = 3 lượt.

## Đã chốt, CHƯA làm vào game (việc tiếp theo)
1. **Thêm các bộ đồ khác** (đề xuất: Kim Lũ Y, Huyết Ma Bào) + hiệu ứng bộ mốc 2/4/6 món (nên đổi lối chơi). Mỗi bộ ~330 lượt PixelLab cho cả nam và nữ.
2. Thêm dáng vũ khí (mỗi cây 1 lượt, pixflux, có thể lấy icon gói Wuxia `UI/Items_64` làm mẫu).
3. Gói Wuxia chỉ có icon vũ khí/trang bị 64px (không có hình cầm tay); danh sách giữ/bỏ đã đề xuất cho chủ game, chưa chốt.

## Công cụ và quy trình
- **PixelLab API v2:** `https://api.pixellab.ai/v2`, header `Authorization: Bearer <key>`. Môi trường mới phải thêm key PixelLab làm network secret cho host `api.pixellab.ai`. Không ghi key vào code; script dùng `Bearer proxy-injected`.
  - Script: `cong_cu/claude/plvfx.py` (VFX; `GAMEPACK=1` ra zip tách lớp `behind/front`; `EFFECT=<thư mục>/<tên>` để sửa tiếp hiệu ứng cũ, 4 lượt).
  - `run5.sh` + `combo5.py` + `combopose.py`: tạo động tác bằng khung xương.
  - `qc*.py`, `ruler.py`: kiểm frame.
  - `nguon/pixellab/pl_openapi.json`: danh sách API.
- **Xuất VFX gói Wuxia từ Godot ra frame:**
  - Gói cần Godot **4.7.1** (tải bản linux x86_64 trên GitHub releases của godotengine). Chạy dưới `xvfb-run` với `--rendering-driver opengl3 --write-movie <thư mục>/f.png --fixed-fps 30`. Bật `rendering/viewport/transparent_background=true` trong `project.godot`.
  - Chiêu môn phái: chép `nguon/godot_bake/Bake.gd`, `Bake.tscn` vào `nguon/pack_wuxia/Skills/Godot/`, chạy `res://Bake.tscn -- <id chiêu>`. Đặt `demo_incoming:false` và không gọi `boundary_attempt`, nếu không demo sẽ để lại tia và mảnh lạ trong hình.
  - Vạn Kiếm: chép `Drive2.gd`, `Rec2.tscn` vào `nguon/pack_wuxia/Common_VFX/`. File này xóa hẳn cọc gỗ, không chỉ giấu, để không còn tia trúng cọc.
  - Đóng sheet bằng PIL: cắt theo bbox chung, rộng ≤4096 px, ≤15 Mpx mỗi ảnh (điện thoại). Khai báo trong `SPX` (`w,h,c,n,px,py`).
- **Kiểm thử:** Playwright + Chromium có sẵn trong môi trường. `cong_cu/claude/rec_lib.js` (đồng hồ ảo `__step`); `combo_film2.js` quay combo ở Luyện Công; `hv_film.js`, `kit2.js`, `run_hp.js` thử chiêu.
- **VFX trong game:** fx `{k:'sp',s:<tên SPX>,x,y,sc,fx:hướng,T,gr:lớp sau,follow:1}`. Ảnh để ở `game/assets/vfx/`.
- Nhân vật: `game/assets/hero_nam.png`, `hero_nu.png`, ô 160×128. Frame PixelLab 128 canvas đặt lệch dx=16.

## Git
- Làm trên nhánh `claude/jolly-ritchie-pitrnx` (phiên này), push lên nhánh đó. Nhánh `claude/relaxed-heisenberg-72j521` là của Codex/phiên khác, chỉ lấy file cần thiết.
- Không tạo PR nếu chủ game không yêu cầu.
- Không ghi tên model vào commit.

## Chốt 24/11 (sau góp ý): A-B-C là MỘT CHUỖI theo video Hovl
Animation và VFX cũ (zs3/zs2, elip k5c_*) mày đã duyệt là đạt. Việc cần là đổi A, B, C thành một chuỗi liền như video: A = khuỵu → dựng → duỗi ngang (chạm) → kéo hông; B = quét từ sau lên → giơ cao; C = vung xuống (chạm, elip k5c_*) → thu. Làm bằng cách xếp lại 12 khung đã có trong `hero_*_ns.png` (hàng y=384/512), `NC`/`TA/TB/TC` trong `game/index.html`, không gọi thêm PixelLab. Các khung hc_* (VFX Hovl do PixelLab tạo) và bản C riêng trong `ANIMATION_A_B_C/*/C_hovl` chỉ để tham khảo, không dùng.

## CHỐT 24/11 (cuối): GIỮ ĐÒN A-B-C CŨ
Chủ game xem các bản làm lại (khung 7/7/12 theo guide, chuỗi Hovl, VFX mới) và chọn **giữ lại đòn A, B, C cũ vì animation mới xấu**. Game đã trả về: A 8 khung (`attack`), B 7 khung (`attack2`), C 10 khung (`attack3`), VFX zs3 / zs2 / elip `k5c_*` (đã bỏ `zs1` dư, elip tan trước hết đòn). KHÔNG làm lại combo này nếu chủ game không yêu cầu. Các tài nguyên thử nghiệm giữ trong repo chỉ để tham khảo, không dùng: hàng y=384/512 của `hero_*_ns.png` + `WSOCK`, `ANIMATION_A_B_C/`, VFX `g_a`, `g_b`, `g_c_b`, `g_c_f`, `hc_*`, phân tích Hovl (`nguon/tham_chieu/hovl/`). Các mục "Combo Kiếm mới A7/B7/C12 ĐÃ VÀO GAME", "Đòn C theo Hovl" và "Chốt 24/11: A-B-C là MỘT CHUỖI" ở trên đã bị thay thế bởi mục này.

**Đã xóa (24/11, theo yêu cầu chủ game):** toàn bộ tài nguyên combo thử nghiệm (khung 7/7/12, C Hovl, VFX g_*/hc_*, hàng sheet y=384/512 và WSOCK tương ứng, `ANIMATION_A_B_C/`, phân tích Hovl, ảnh minh họa, `animation_manifest.json`). Sheet `hero_*_ns.png`/`_hand.png` đã về 3840×384 đúng bản Master khóa.

## 24/11 (tối): sửa 2 lỗi người chơi báo
- **Ngộ Không đi + đánh bị méo cả khung:** do phép nghiêng (shear) tao thêm ở `drawGodSprite`; đã bỏ hẳn (luật: không co giãn/biến dạng frame). Khi đang di chuyển vẫn dùng khung chạy gốc (8 khung, không méo), nhịp đánh do VFX gậy lo.
- **Kiếm bay Hồi Phong chỉ có lưỡi, không chuôi:** ảnh `wpn/thanhphong_{nam,nu}.png` chỉ có lưỡi (chuôi nằm dưới nắm tay nên vốn không có). Đã tạo bản có chuôi `wpn/thanhphong_{nam,nu}_f.png` bằng PixelLab `edit-images-v2` (1 lần, 10 lượt, giữ nguyên lưỡi) và chỉ dùng cho kiếm bay (`WPN[...+'_f']` trong `drawZone`); kiếm cầm tay giữ nguyên.
- **Kiếm mặc định nam và nữ dùng chung một thanh** (bản nữ `thanhphong_nu`, chủ game chọn): `heroWeaponArt` trả `thanhphong_nu` cho cả hai giới; ảnh `thanhphong_nam*` không còn dùng.
- **Ngộ Không đánh khi đang di chuyển:** hiện đúng động tác đánh (`attack`/`attack2`), hết nhịp 0,45 s thì về khung chạy (chủ game chọn 24/11; bản 'chỉ chạy rồi VFX hiện' đã bỏ). Hệ quả đã biết: lúc đánh chân đứng yên và trượt theo quãng đường; nếu muốn chân bước trong lúc đánh thì cần animation chạy-đánh mới (tạo bằng PixelLab, chưa làm).
- **Ngộ Không chạy-đánh MỚI (chủ game duyệt 24/11):** animation `runatk` (6 khung từ `animate-with-text-v3`, 12 lượt cho 3 lần thử; bản có `last_frame` = khung đâm gốc là bản dùng), nằm ở hàng y=320 của `god_wukong.png`; khi đang di chuyển và đánh, `drawGodSprite` phát `runatk` (chân bước, gậy đâm thẳng rồi rút về) thay cho khung đánh đứng. Khung gốc trong `nguon/pixellab/wkrun/`. Bài học: text-v3 + `last_frame` điều khiển tư thế cuối tốt hơn chỉ mô tả.
- **Vệt cháy dưới đất (`scorch`) của Kim Cô Bổng/Ngộ Không:** đổi từ hai elip đặc (nhìn như đĩa đen, chủ game chê) sang gradient mờ dần ra rìa, nhạt hơn, tan nhanh; vết nứt `wk_crack` tan sớm và nhạt hơn. `runatk` bỏ đoạn tua ngược (0-5-4-2) cho chân đi một chiều.
- **Kỹ năng Ngộ Không do người chơi BẤM (24/11):** Thổi Lông (Q), Cân Đẩu Vân (F), Kim Cô Bổng mở rộng (X), Kim Cô Bổng khổng lồ (R); ô HUD là nút `BẤM` (chạm hoặc phím). `requestGodSkill` + `castGod` chỉ còn tự đánh thường và hồi chiêu cho Ngộ Không; thần tướng khác vẫn tự thi triển. Cân Đẩu Vân: mây to hơn, sống 0,45 s+, mây dưới chân 0,9 s đi theo người. Vệt `wk_slash` của đòn bổ giảm độ sáng còn 50%.
- **MỌI thần tướng (Ngộ Không, Na Tra, Bát Giới, Thổ Địa) đều do người chơi bấm kỹ năng** (chủ game 24/11): Q/F/X cho kỹ năng 1-3, R cho tuyệt kỹ nếu có; `castGod` chỉ tự đánh thường. Hotkey gán tự động cho mọi `GODS[id]` ngay trước `castGod`. Đã thử cả 4 thần tướng: không bấm thì không tự chạy, bấm thì vào hồi chiêu.
- **Thổi Lông Hóa Khỉ có animation riêng (24/11):** `blow` 8 khung (PixelLab animate-with-text-v3, 1 lần 4 lượt, ảnh gốc = khung idle) ở hàng y=480 của `god_wukong.png`; đưa tay lên miệng, hít, thổi, lông vàng bay ra (lông nằm sẵn trong khung). `P._gBlow` đặt lúc cast, `drawGodSprite` phát trong 0,73 s. Khung gốc: `nguon/pixellab/wkblow/`.
- **Ngộ Không có chuỗi 3 đòn (24/11, theo clip tham chiếu):** bổ → đâm → **bổ từ trên xuống** (`slam`, 8 khung PixelLab, hàng y=640 của `god_wukong.png`, phát 0,62 s). Đòn bổ trên xuống: vệt trăng vàng-nâu `wk_arc` kèm gai bụi bung ở chân (PixelLab VFX pro, bật 0,12 s, chạm 0,33 s), sát thương 26 diện rộng 150 đẩy lùi 220 choáng 0,12 s, nhịp sau đòn này 0,78 s. Khói thổi lông mới `wk_puff2` (cục khói xanh nhạt, PixelLab lite) thay `wk_puff` lúc thổi. Chi phí PixelLab ~28 lượt (khung 4, arc 12, puff 2... xem log). Khung gốc: `nguon/pixellab/wkslam/`. Chưa làm: khỉ con dạng bóng xanh trước khi thành khỉ thật như clip.
- **Sửa sau góp ý:** đòn bổ từ trên xuống bị dư vòng trắng do `arc()` tự vẽ vệt mặc định chồng lên `wk_arc` -> thêm `nofx:1`. Đòn đâm có VFX va chạm: `wk_hit` lớn (sc 0,95) + hạt vàng tại tối đa 3 quái bị đâm.
- **Đồng bộ VFX chuỗi Ngộ Không (24/11):** đòn 1 (bổ) dùng `wk_arc` bản nhỏ 64%, chỉ phần trăng (khung 0-3, không gai bụi), đòn 3 `wk_arc` đủ cỡ + gai bụi; `wk_slash` không còn dùng cho đòn bổ. **Góc trái trên HUD:** avatar 58px thẳng hàng khối tên/cấp/Lực chiến, huy hiệu cấp hiện đủ, ô xu `#coins` nằm riêng dưới thanh Lực chiến (đã gỡ luật `html body #coins` thừa).
- **Đồng bộ nhánh Codex (24/11):** đã gộp `a3e7128` (đồng bộ độ nét pixel 16 tranh nhân vật, khung tranh giữa tăng cỡ nhân vật) vào nhánh làm việc, giữ viền nhẹ khung tranh của Claude. Lực chiến trong trận thu nhỏ nhẹ (chữ 14,5px, icon 20px) và ô xu kéo sát dưới nó.
- **Tranh giữa màn tạo nhân vật hở dải đen (24/11):** `#crBg` của Codex dùng inset/phần trăm cố định nên hở khi khung khác tỉ lệ; đổi sang nền cover 100% + `transform:translate(10.8%,-18.7%) scale(1.72)` (cùng vùng nhìn, luôn phủ kín). Đã thử 5 cỡ máy.
- **Tranh giữa mờ (24/11):** ảnh `scene-*.webp` chỉ 401×501 px, phóng 1,72 trong CSS làm mỗi pixel ảnh kéo giãn >5 lần trên màn 3x. Đã giảm xuống `scale(1.3)` quanh nhân vật (nét hơn, nhân vật vẫn to). Muốn nét hẳn mà vẫn to thì cần ảnh nguồn độ phân giải cao hơn (chưa có).
- **Sửa mục 1 và 2 (24/11):** `runatk` làm lại 16 khung (PixelLab text-v3, seed 32; bắt đầu và kết thúc bằng tư thế vác gậy của khung chạy nên nối liền, chân bước suốt, đâm ở giữa), phát 0,5 s khi đang di chuyển. `slam` làm lại 10 khung (seed 42: giơ gậy qua đầu rồi đập xuống đất trước mặt, vẫn nhìn nghiêng), phát 0,7 s. Cả hai nằm ở hàng y=800/960/1120 của `god_wukong.png` (hàng cũ y=320/640 không còn dùng). Đứng yên khi bổ (0,7 s) và khi thổi lông (0,55 s) qua `P._gRoot`. Khung gốc: `nguon/pixellab/wkfix/`. Chi phí ~24 lượt. Khung đập đất có vài mảnh trắng baked ở đầu gậy.

## Tàng Bảo Các (24/11)
- Ô mới ở Sảnh `Tàng Bảo Các` (`LBT` k:'tangbao', `renderTBC`, `tbcData`, `tbcCount`): 4 tab Vũ Khí (loại + tên vũ khí), Trang Bị, Bí Tịch, Đan Dược. Món đã sở hữu hiện màu + ghi rõ (phẩm, tầng, số lượng); chưa có thì bóng đen "Chưa sở hữu". Đầu cửa sổ ghi tổng "đã có X/Y món" = số món đang có trong game.
- Ghi nhận sở hữu lưu `save.tbc={eq,bk,dan,pot}`; hook ở `addItems` (`tbcNote`), `useDan`, chế đan (`tbcMark`). Danh sách lấy từ `SLOTS`, `BOOKS`, `SEC`, `RECIPE`, `DAN`, `POT` nên thêm món mới vào dữ liệu thì tự xuất hiện; `TBC_LOG` là nhật ký bổ sung tay.

## Sửa vệt chém A/B Kiếm (24/11)
Đòn A (`zs3`) lật dọc (`fl:-1`, `oy:-92`) để quét từ trên xuống cùng chiều lưỡi kiếm, bật sớm 0,18 s trước khung trúng. Đòn B (`zs2`) giữ chiều gốc (kiếm B quét từ dưới lên), chỉ thêm nghiêng theo hướng chém. `comboFx(step,angle)` truyền góc; `sp` hỗ trợ `oy`. C không đổi.

**Đòn A đổi VFX (24/11, chủ game chọn):** vệt `zs3` thay bằng `wx_slash` (gói Wuxia `Common_VFX/Skills/07_Sword_Arc/PNG/slash`, 8 khung 96×96, `assets/vfx/wx_slash.png`), bật trước khung trúng 0,06 s, T 0,34 s, đặt trước ngực (`dx`,`dy` px trong `sp`). `zs3` chỉ còn làm dự phòng. Đòn B và C giữ nguyên VFX cũ. Đã bỏ ý định làm VFX mới bằng PixelLab cho A/B.

## Sửa 24/11 (tối): kiếm Nam lúc trúng đòn, Hồi Phong
- Nam: khung trúng đòn 2-3 (`1280,128`, `1440,128`) kiếm thò ra từ sau hông, tay không cầm chuôi. Đã đổi socket sang 'f', góc 29°/30° như khung 1 và 4 (`WSOCK.nam`). Các khung khác của Nam/Nữ đã kiểm (chuôi nằm trên thân).
- Hồi Phong: kiếm bay nhỏ lại ~19% (`58/WPN[..][0]`, trước 72).
- **Nữ Huyền Giáp (`hero_nu_hg.png`)**: đối chiếu pixel với Master (24/11) cho thấy thân gốc cũng gần như không lộ cổ; khác biệt chỉ là cổ áo đỏ/viền trắng bị thay bằng cổ giáp đen. Nhận định ban đầu 'mất cổ' là quá lời. Chủ game nói còn 'một số chi tiết' mất: chưa xác định được, cần chủ game chỉ rõ.

## Đồng bộ màu A/B/C, elip C dày, bàn tay (24/11)
- `wx_slash` (đòn A) đổi sang bảng màu của `zs2` (đòn B), bớt đậm (gốc: `nguon/vfx_goc/wx_slash_goc.png`). Elip C (`k5c_behind/front`) dày thêm ~6px bằng chồng bản dịch ±1..3px trong từng ô (gốc: `nguon/vfx_goc/k5c_*_goc.png`).
- Lớp tay `hero_nam_hand.png` và `hero_nam_hg_hand.png`: thêm bàn tay ở ô `1280,128` và `1440,128` (chép từ ô `1120,128`). Hai file này vì thế khác Master khóa (chủ game đã cho vẽ thêm tay). `hero_*_ns.png`, `hero_*.png`, `hero_nu_hand.png` vẫn trùng hash Master.
- Kiểm đối chiếu Master: sheet thân không kiếm của Nam/Nữ trùng Master. Nữ Huyền Giáp: không phát hiện mất cổ so với Master (xem mục trên). Kiếm dùng chung bản nữ dài 32 so với kiếm Master của Nam ~28.

## Đòn C làm lại (24/11, chủ game duyệt phác thảo)
- Elip `k5c_behind/front` dựng lại bằng `cong_cu/claude/c_ellipse.py` (không PixelLab): nhát cong dày giữa-mỏng đuôi, vẽ dần từ sau lưng qua trước xuống dưới, tan từ đuôi (3 lớp màu bảng A/B). Giữ kích thước ô, 15 khung. Bản dilation cũ không còn.
- Góc kiếm 10 khung C trong `WSOCK` (khóa `2240..3680,256`, cả nam/nữ) đổi thành -150,-115,-75,-35,0,30,52,62,50,38: kiếm vung từ sau-trên đầu xuống trước theo vệt. Thân nhân vật không đổi (Master).
- (24/11 tối) Elip C v2: bản đầu bị chê xấu vì phẳng như vector. `c_ellipse.py` giờ dựng 3 dải lồng nhau (ngoài mảnh, chính dày 5 lớp màu viền→lõi trắng, trong ngắn), quầng sáng mờ, vệt tốc độ + hạt. Chạy: `python3 cong_cu/claude/c_ellipse.py` (tham số tùy chọn: thư mục ra).
- (24/11 tối, v3) Chủ game gửi ảnh mẫu `nguon/tham_chieu/anh_mau_vfx_kiem.png` (elip dẹt rộng, chùm sợi mảnh, dày dưới-trái, trắng–xanh lam, quầng sáng). Không tách được vòng sạch từ ảnh (bị nhân vật/quái/nền đè) nên `c_ellipse.py` dựng bám đúng hình dạng đó. Ô mới 360×200 (`SPX k5c_*: w360,h200,px180,py144`). **Màu ba đòn A/B/C đổi sang xanh lam–trắng**: `zs2` và `wx_slash` xoay hue +38° (gốc teal ở `nguon/vfx_goc/*_teal.png`).
- (24/11 tối, v3b) Thêm ~34 sợi mảnh lẻ ở nhiều bán kính (0,45–1,35 lần elip), dài ngắn khác nhau, quầng sáng giảm để không ra viền xám trên nền tuyết. Ô k5c_* nay 360×224 (`py:154`).

## Cân Đẩu Vân bay thật, Hóa Thân gọn, đồng bộ, số sát thương (24/11, chủ game duyệt thứ tự)
- **Cân Đẩu Vân (F):** nhân vật bay thật theo đường mây 0,55 s (`P._gFly`, nội suy trong vòng cập nhật vị trí, bất tử + đứng yên input), mây đi cùng dưới chân, rồi `later(D)` đáp xuống nện đất, scorch, whirl, rung. Có chốt chặn nếu `later` bị purge.
- **Hóa Thân:** `wk_puff` 2→1,75, `wk_roar` 1,2→1,06 (al 0,85), aura lửa alpha 0,85 (≈ -23% diện tích, lớp trước đỡ che người).
- **Số sát thương:** gộp số cùng loại gần nhau (<26 px) trong 0,3 s thành một số lớn; trần cùng lúc 60 (điện thoại 34); số nằm trên người chơi mờ còn 40%.
- **Kiểm đồng bộ:** `cong_cu/claude/sync_qa.js <game> kiem|god` (+ `vfx_peaks.json`): đo lúc vung, khung chạm, lúc số sát thương hiện, lúc VFX sáng nhất. Đã chỉnh: đòn C chuyển khung chạm sang khung 4 (TC) và elip bật sớm 0,24 s (trước đó sát thương rơi 190–320 ms trước vệt sáng nhất); đòn A vệt bật at-0,02; Ngộ Không bổ: wk_arc nhỏ T 0,22; đâm: chớp gậy và va chạm sáng nhất ngay lúc trúng. Kết quả hiện tại: mọi đòn A/B/C và 3 đòn Ngộ Không lệch ≤ 76 ms.
- Chưa kiểm đồng bộ bằng script: Q/F/X của Kiếm, Thổi Lông, Kim Cô Bổng mở rộng/khổng lồ, Hóa Thân.

## Đổi tên kỹ năng Ngộ Không (24/11, theo gợi ý ChatGPT, chủ game duyệt)
Hóa Thân (Ngộ Không) = **Tề Thiên Giáng Thế** (`GODS.wukong.tf`; nút và mục chung vẫn ghi "Hóa Thân" vì các thần tướng khác dùng chung, thông báo và bảng thông tin hiện tên riêng). Đánh thường = **Như Ý Liên Bổng** (basic), Q = **Bạt Mao Triệu Hầu**, F = **Cân Đẩu Trấn Địa**, X = **Như Ý Xuyên Thiên**, R = **Định Hải Trấn Thiên**.

## Như Ý Xuyên Thiên (X) và Định Hải Trấn Thiên (R) sửa (24/11)
Chủ game duyệt, cho phép PixelLab ở VFX Ngộ Không nhưng chỉ khi thật cần. Đã làm bằng tài nguyên có sẵn + code:
- **X:** dài ra mượt trong ~0,34 s (easeOut), dày 0,6→1,35 lần, ánh vàng chạy dọc thân gậy lúc xuyên (`staffGlow`: vẽ lại ảnh gậy, tô vàng bằng source-atop rồi cộng sáng), chớp `wk_hit` ở đầu gậy và ở từng quái bị xuyên, khói ở tay lúc ra và lúc thu về, T 0,75 s.
- **R:** gậy khổng lồ ×2,2 (ảnh `wk_staff_big`), bóng đổ lớn dần, vệt tốc độ, ánh vàng phủ nhẹ, chớp sáng khi chạm. Vết cháy 2,2→1,0 s, vết nứt 1,2→0,85 s và mờ sớm hơn (cả Cân Đẩu Trấn Địa).
- Chưa dùng PixelLab. Điểm còn yếu: thân gậy X vẫn là một thanh đỏ thẳng có đầu vàng (ảnh `wk_staff`); muốn đẹp hơn cần ảnh thân gậy có hoa văn/rãnh vàng, khi đó mới nên gọi PixelLab (ước 12 lượt VFX pro).
- Test: `scratchpad/xr_test.js` cần đặt cd kỹ năng = 0 trước khi bấm (cd sau Hóa Thân không giảm khi chạy đồng hồ ảo).
- (24/11 tối) **R (Định Hải Trấn Thiên)** choáng 1,0→1,8 s (tinh anh nửa thời gian, trùm miễn choáng theo luật `hit`), sao choáng trên đầu quái 3→4 và to hơn. **X (Như Ý Xuyên Thiên)** sát thương xuyên 35% giáp (`pierceArmor:0.35`, hiện trong mô tả).
- (24/11 tối) Đòn C thêm **một vòng nhỏ bên trong** (chủ game xin): `ring_small` trong `c_ellipse.py` (0,46 lần elip lớn, 12 sợi sáng, bắt đầu trễ 0,12, tan sớm hơn). Đây là chủ ý theo yêu cầu, không phải vệt chém phụ độc lập.

## Đồng bộ 16 tranh cảnh mới (24/11, commit nguồn 819e7a2)
Lấy từ `origin/claude/relaxed-heisenberg-72j521` commit `819e7a23d6d9f18e93c42cd6419d56b2eb90b852` ("Ve lai 16 tranh pixel va bo phong anh bang CSS"): 16 file `game/assets/portraits/scene-{nam,nu}-{1..8}.webp` (793×992) và dòng CSS `.cxill #crBg` (inset 0, 100%, `object-fit:contain`, nền #110d0a, không còn `transform:scale`). Thay luật `scale(1.3)` cũ của Claude. Đã kiểm 8 ảnh nam + 8 ảnh nữ đổi theo avatar (script `scratchpad/scene16.js`, ảnh `nguon/tham_chieu/scene16_kiem_tra.png`). Chép file chứ không merge nhánh (nhánh làm việc vẫn `claude/jolly-ritchie-pitrnx`).
- (24/11 tối) Avatar góc trái trên to thêm ~12%: khung 58→65 px (ảnh 50→57), điện thoại ngang thấp 50→57 (ảnh 43→50); ô xu dịch theo (+7 px). Kiểm ở 667/844/932 px, không đè Lực chiến.
- (24/11 tối) **Thân gậy Như Ý có hoa văn (PixelLab `edit-images-v2`, 1 lần = 10 lượt, seed 7, đầu vào `nguon/pixellab/gay/in_staff.png` 32×192, đầu ra `out1/g1_00.png`)**: giữ hai mũ vàng (giống bản gốc 98,5%/99,2%), thân đỏ có vệt sáng + nét vàng mảnh dạng mây cuộn theo ảnh mẫu `anh_mau_kim_co_bong.jpg`. `wk_staff.png` nay 20×192 (mũ 65 + gạch thân 62 + mũ 65, `STF.wk_staff={t:65,b:65,tile:62}`); `drawWkStaff` lặp gạch thân, lật gương xen kẽ để mép khớp. Dùng cho X (Như Ý Xuyên Thiên) và R (gậy khổng lồ nay là `wk_staff` phóng ×4, bỏ `wk_staff_big`). Gốc đỏ trơn: `nguon/vfx_goc/wk_staff_do_tron.png`. Hai mũ vàng chưa chạm khắc thêm.

## Lỗi chọn Nam thành Nữ (24/11, đã sửa)
Nguyên nhân: `startTraining` gán `P0.gender=TR.gender` (giới tính thử ở Luyện Công, lưu bền ở `tdst_tr`) lên hồ sơ thật, nên lần vào/ra Luyện Công sau đó (kể cả "Thử chiêu" ở màn tạo nhân vật) làm hồ sơ Nam tự thành Nữ. Sửa: `TR.gender=null` mỗi lần tải game; `startTraining` nhớ giới tính thật vào `window.__trG0`; `showLobby` trả lại; `persist` không lưu giới tính tạm. Test: `scratchpad/gender_test4.js` (hồ sơ nam + tdst_tr gender nu → vào Luyện Công → Ra sảnh → tải lại: vẫn nam).

## Sửa 24/11 (đêm): mũ vàng, đòn 3 Ngộ Không, X/R, dash, ô xu, méo khung Kiếm
- **Mũ vàng gậy chạm khắc (PixelLab edit-images-v2, 10 lượt, seed 11, `nguon/pixellab/gay/out2`)** thay hai mũ cũ, thân giữ nguyên.
- **Đòn 3 Ngộ Không (bổ trên xuống) nhanh hơn:** animation/đứng yên 0,7→0,5 s, chạm 0,33→0,24 s, nhịp sau 0,78→0,58 s.
- **X:** thêm nổ `wk_stomp` + vòng sáng + hạt + rung nhẹ tại mỗi quái bị xuyên và ở đầu gậy.
- **R:** gậy rơi chậm (đáp ở 0,95 s, `T` 1,7 s, rơi easeIn mũ 3), đáp xong tan từ từ (~0,5 s), bóng đổ là gradient mềm lớn dần.
- **Dash:** bỏ vệt mực đen; thay bằng vệt tốc độ sáng, vòng và bụi lúc bắt đầu.
- **Ô xu** `#coins` sát mép trái (dưới avatar).
- **Méo khung Kiếm lúc vừa chạy vừa đánh:** do `runSwingTurn` ép bề ngang 24% khi đổi hướng (squash). Đã tắt (`turn=1`).
- (24/11 đêm) Đòn 3 Ngộ Không nhanh thêm: anim/đứng yên 0,36 s, chạm 0,17 s, nhịp sau 0,45 s. Đòn C Kiếm: elip phóng 1,35 lần, đuôi tan hết trước 80% đòn (hết mảnh vụn nhỏ cuối đòn), mặc định tia sao ở đầu nhát chém (chủ game chọn), không còn vòng nhỏ.
- (24/11 đêm) Chủ game chọn GIỮ elip chùm sợi (`c_ellipse.py`), chỉ lấy từ video Spine (thử ở `c_ellipse2.py`, không dùng) phần **đuôi tối dần sang xanh đậm – tím** (`tailmix`). Cung đặc kiểu video đã bỏ.
- (24/11 đêm) Đòn C: VFX elip chậm lại (T 0,5→0,72 s, bật sớm hơn 0,4 s trước chạm để đỉnh sáng vẫn gần khung chạm). Đòn A/B: `wx_slash` và `zs2` đổi màu theo cùng bảng với C (đầu trắng → lam sáng → xanh đậm → tím ở đuôi, tô theo độ sáng, từ gốc `nguon/vfx_goc/*_teal.png`).

## Đòn C nâng cấp 1-2-3 (24/11 đêm, chủ game muốn >9 điểm)
1. `c_ellipse.py`: elip nhỏ hơn (RX 128, RY 60), đuôi tím đậm hơn (`tailmix` k 0,95), tia sao ở đầu to hơn (44/24 px).
2. Điểm chạm đòn C (`finishSwordCut`): 2 vòng xung kích, bụi tuyết bắn lên, chớp `swhit` ×1,7, vết nứt, rung 5.
3. **PixelLab VFX pro** (18 lượt, 1 lần, `nguon/pixellab/c_pro/`): nhát chém cong dày nhiều dải, đầu sáng đuôi xanh đậm, `k5c_pro.png` (whole, 15 khung 196×200, anchor px:89 py:104). **CHƯA vào game** (chỉ thử ở bản sao): chờ chủ game chọn giữa bản code (1-2) và bản PixelLab. Bản PixelLab đẹp, sạch hơn nhưng là một vành đứng cố định phía trước (tự vẽ dần), không quét từ sau lưng như bản code.
- (24/11 đêm) **Bản ghép đòn C ĐÃ VÀO GAME (chủ game duyệt):** vành PixelLab `k5c_pro` (T 0,5 s, bật 0,12 s trước chạm, `dx:26,dy:-48`, al 0,92) là vệt chính phía trước; elip code `k5c_behind/front` giữ làm sợi mảnh + đuôi tím + tia sao (T 0,64, tan sớm hơn, độ đục 0,85/0,7 để bớt chồng rối). Hoàn nguyên: xóa dòng `go('k5c_pro'...)` trong `comboFx` (không cần đổi ảnh).
- (24/11 đêm) Bản ghép bị chê "2 VFX xếp chồng". Đã bỏ lớp code `k5c_behind/front` khỏi đòn C: chỉ còn **một vành PixelLab `k5c_pro`** (đuôi tô tím trực tiếp trong ảnh: hàm tô theo vị trí trên-trái; T 0,56 s, scale 1,25) + điểm chạm. Ảnh gốc PixelLab chưa tô: `nguon/pixellab/c_pro/k5c_pro.png`. Muốn quay lại bản code: thêm lại 2 dòng `go('k5c_behind'...)`, `go('k5c_front'...)`.
- (24/11 đêm) Thêm lại **tia sao ở đầu vành** đòn C: vẽ thẳng vào các khung 3–9 của `k5c_pro.png` tại đầu mũi vành (khung 8–9 mờ 55%). Ảnh gốc chưa tô tím chưa vẽ tia: `nguon/pixellab/c_pro/k5c_pro.png`.
- (24/11 đêm) **Vành đòn C có chuyển động quét thật:** PixelLab VFX pro `EFFECT=` sửa tiếp hiệu ứng cũ (**7 lượt**, `nguon/pixellab/c_pro/o2`, ảnh gốc `k5c_pro_quet.png`): đầu sáng chạy từ trên-trái vòng qua phải xuống dưới, đuôi tan dần. Đã tô đuôi tím + tia sao ở đầu (khung 1–10, vị trí đầu = điểm x+y lớn nhất) rồi thay `game/assets/vfx/k5c_pro.png` (ô 196×202, `px:89 py:104`). Tổng PixelLab cho vành C: 18 + 7 = 25 lượt. Bản vành cố định cũ: `nguon/pixellab/c_pro/k5c_pro.png`.

## Vạn Kiếm Quy Tông có va chạm (24/11)
Mỗi đợt kiếm (6 đợt) tại mỗi quái bị trúng: chớp `swhit` ×2, vòng sáng nhỏ, hạt, tiếng `sword_hit`; ở cuối làn mỗi đợt có chớp lớn ×2,6 + vòng (lớp sau người). Giới hạn số fx (60 điện thoại / 150) để không nặng. Không dùng bộ `impact` của Wuxia vì toàn mảnh pha lê xanh ngọc (chủ game từng chê "mảnh băng"). Chưa làm: vòng sét Thiên Xu (cần PixelLab, đang chờ chủ game xác nhận gọi).
