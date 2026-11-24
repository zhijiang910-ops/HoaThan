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
- Làm trên nhánh `claude/relaxed-heisenberg-72j521`, push lên nhánh đó.
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
