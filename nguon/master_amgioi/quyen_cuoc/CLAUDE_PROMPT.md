# Hồ Sơ Tổng Hợp & Master Prompt Thực Thi Cho Claude — Môn Phái Quyền Cước (Khử Tà Diệt Ma)

Tài liệu này tổng hợp toàn bộ tên gọi, thông số chiến đấu, hộp thoại mô tả (Popup Tooltip), sơ đồ ánh xạ tài nguyên Icon/VFX và **Master Prompt** hoàn chỉnh để bạn dán thẳng vào **Claude Code / Cursor / Claude** thực thi ngay trên mã nguồn hiện tại.

## 1. Bảng Ánh Xạ Toàn Bộ Tài Nguyên Hình Ảnh (Trong Gói ZIP Đính Kèm)

Giải nén gói `bo-tai-nguyen-quyen-cuoc-claude.zip` vào thư mục tài nguyên của dự án. Toàn bộ ảnh đã được đổi tên chuẩn hóa, cắt sẵn khung và tách nền trong suốt (`RGBA .png`) cho các hiệu ứng VFX:

| Nhóm | Đường dẫn tệp trong ZIP | Kích thước chuẩn | Chức năng gắn vào Game |
| :--- | :--- | :--- | :--- |
| **Icon UI** | `assets/icons/icon_attack_phuc_ma_lien_quyen.png` | `256×256` | Icon nút Đánh thường (**Phục Ma Liên Quyền**) |
| **Icon UI** | `assets/icons/icon_dash_bo_hu_luu_phu.png` | `256×256` | Icon nút Lướt góc dưới trái (**Bộ Hư Lưu Phù**, hỗ trợ cả khung vuông và mặt nạ tròn) |
| **Icon UI** | `assets/icons/icon_q_phuoc_hon_cuong_quyen.png` | `256×256` | Icon Ô 1 · Phím `Q` (**Phược Hồn Cương Quyền**) |
| **Icon UI** | `assets/icons/icon_f_bat_quai_chan_dia_cuoc.png` | `256×256` | Icon Ô 2 · Phím `F` (**Bát Quái Chấn Địa Cước**) |
| **Icon UI** | `assets/icons/icon_e_toai_phach_bat_cuc_chuong.png` | `256×256` | Icon Ô 3 · Phím `E` (**Toái Phách Bát Cực Chưởng** — lấp ô trống thứ 4) |
| **Icon UI** | `assets/icons/icon_r_quy_mon_tran_nguc_an.png` | `256×256` | Icon Ô 4 · Phím `R` Đại chiêu (**Quỷ Môn Trấn Ngục Ấn**) |
| **Ấn Triện** | `assets/icons_seal/seal_q_phuoc.png` | `256×256` | Biểu tượng chữ Hán triện `縛` (tùy chọn thay thế nếu muốn giữ UI chữ triện) |
| **Ấn Triện** | `assets/icons_seal/seal_f_chan.png` | `256×256` | Biểu tượng chữ Hán triện `震` (vòng lửa Bát Quái) |
| **Ấn Triện** | `assets/icons_seal/seal_e_pha.png` | `256×256` | Biểu tượng chữ Hán triện `破` (vòng bùa vàng) |
| **Ấn Triện** | `assets/icons_seal/seal_r_diet.png` | `256×256` | Biểu tượng chữ Hán triện `滅` (khung đại chiêu xích sắt đỏ) |
| **VFX Sprite** | `assets/vfx/vfx_q_fist_projectile.png` | Tách nền `RGBA` | Viên đạn nắm đấm vàng quấn chỉ đỏ & hoàng phù bay ngang của phím `Q` (thay trăng khuyết trắng) |
| **VFX Sprite** | `assets/vfx/vfx_passive_chu_sa_mark.png` | Tách nền `RGBA` | Dấu ấn **Chưởng Ấn Chu Sa** treo trên quái/nhân vật (thay chữ `卍` tím ở giây 06) |
| **VFX Sprite** | `assets/vfx/vfx_e_talisman_burst.png` | Tách nền `RGBA` | Hiệu ứng bùa vàng & tàn lửa nổ tung khi đòn cuối phím `E` kích nổ Ấn Chu Sa |
| **VFX Sprite** | `assets/vfx/vfx_r_giant_exorcist_palm.png` | Tách nền `RGBA` | Bàn tay cự chưởng chu sa xích đỏ giáng từ trên xuống của phím `R` (thay bàn tay tím ở giây 24) |
| **VFX Sprite** | `assets/vfx/vfx_r_bagua_crater_decal.png` | Tách nền `RGBA` | Hố đá nứt Bát Quái khe ngục vẽ ở lớp mặt đất (`Ground Decal`) cho phím `F` và phím `R` |
| **VFX Sprite** | `assets/vfx/vfx_soft_ghost_smoke_puff.png` | `256×256 RGBA` | Hạt khói mềm biên mờ dùng chung cho khói âm khí 60 FPS (cả chiến đấu lẫn cổng sảnh chính) |
| **Data Config** | `skills_quyen_cuoc.json` | UTF-8 JSON | Dữ liệu cấu hình toàn bộ tên chiêu, mô tả popup, sát thương, hồi chiêu, Nội lực, hitbox |

## 2. Bảng Tổng Hợp Tên Gọi, Thông Số & Hộp Thoại Popup Trong Game

| Mã ID | Vị trí nút | Ấn | Tên hiển thị | Mô tả hộp thoại (Popup Tooltip) | Loại | Hồi chiêu | Nội lực | Hệ số Công | Liên kích |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `qc_basic` | Đánh thường | `斬` | **Phục Ma Liên Quyền** | Tung chuỗi quyền cước dồn dập khắc tối đa ba tầng Chưởng Ấn Chu Sa lên kẻ địch trước mặt. | Cơ bản · giữ để đánh | `0s` | `0` | `45% + 50% + 55% + 80%` | `+1 / đòn` |
| `qc_dash` | Nút Lướt | `影` | **Bộ Hư Lưu Phù** | Hóa sương lướt nhanh qua vật cản, để lại lá bùa vàng phát nổ làm chậm quái truy đuổi. | Thân pháp · bấm để dùng | `2,5s` | `0` | `90%` (bùa nổ trễ `0,6s`) | `+1` |
| `qc_skill_1` | Ô 1 · `Q` | `縛` | **Phược Hồn Cương Quyền** | Tung quyền khí quấn chỉ đỏ xuyên năm kẻ địch trước mặt, giật tụ nhẹ về gần và khắc Ấn Chu Sa. | Chủ động · bấm để dùng | `5s` | `15` | `160%` (xuyên 5 mục tiêu) | `+2 / quái` |
| `qc_skill_2` | Ô 2 · `F` | `震` | **Bát Quái Chấn Địa Cước** | Giậm cước khắc trận Bát Quái xuống đất, làm choáng mọi quái trước mặt và thiêu đốt âm khí. | Chủ động · bấm để dùng | `9s` | `20` | `210%` + `25%/s` trong `3s` | `+4` |
| `qc_skill_3` | Ô 3 · `E` | `破` | **Toái Phách Bát Cực Chưởng** | Lao sát mục tiêu tung sáu chưởng dán bùa liên hoàn, kích nổ toàn bộ Ấn Chu Sa để hồi Nội lực. | Chủ động · bấm để dùng | `12s` | `22` | `6 × 30%` + `110%` nổ cuối | `+8` |
| `qc_ult` | Ô 4 · `R` | `滅` | **Quỷ Môn Trấn Ngục Ấn** | Mở khe Quỷ Môn hút gom tà ma vào tâm rồi giáng cự chưởng xích đỏ trấn sập, gây sát thương cực đại. | Đại chiêu · bấm để dùng | `24s` | `35` | `480%` (`+30%` nếu máu địch dưới `30%`) | `+6` |

## 3. Master Prompt Thực Thi Dành Cho Claude (Copy-Paste Nguyên Khối Dưới Đây)

Sao chép toàn bộ nội dung bên dưới và gửi trực tiếp cho **Claude Code / Cursor** sau khi bạn đã chép thư mục `assets/` và `skills_quyen_cuoc.json` vào dự án:

```text
Bạn là Senior Gameplay & VFX Programmer cho dự án game ARPG 2D pixel-art "Khử Tà Diệt Ma".
Tôi đã thêm bộ tài nguyên mới vào thư mục `assets/icons/`, `assets/icons_seal/`, `assets/vfx/` và file cấu hình `skills_quyen_cuoc.json`.

Hãy đọc codebase hiện tại của môn phái Quyền Cước (hiện đang có đánh thường "Thiên Cương Liên Hoàn", nút "Lướt", kỹ năng Q "Cương Khí Phá Không", kỹ năng F "Chấn Địa Quyền", chiêu bàn tay tím chữ Vạn hồi chiêu 24s, và 1 ô kỹ năng thứ 4 đang để trống) rồi thực thi trọn vẹn các nâng cấp sau mà KHÔNG làm hỏng kiến trúc UI, thanh Nội lực (100/100), thanh Sinh lực (100/100), hệ thống Liên kích (Nộ +% · Bạo +%) hay bảng công cụ Luyện Công:

### NHIỆM VỤ 1: NÂNG CẤP UI ICON, RÀNG BUỘC 4 Ô KỸ NĂNG & POPUP MÔ TẢ
1. Cập nhật icon cho nút Đánh thường (`assets/icons/icon_attack_phuc_ma_lien_quyen.png`), nút Lướt (`assets/icons/icon_dash_bo_hu_luu_phu.png`) và đủ 4 ô kỹ năng chủ động Q, F, E, R từ thư mục `assets/icons/` (giữ chế độ render pixel sắc nét `Nearest Neighbor / Point` / `image-rendering: pixelated`). Hỗ trợ hằng số cấu hình `USE_SEAL_ICONS` nếu muốn chuyển nhanh sang bộ chữ triện `縛 / 震 / 破 / 滅` trong `assets/icons_seal/`.
2. Kích hoạt ô kỹ năng thứ 3 (phím nhanh `E` — trước đây đang để trống `◇`) và chuyển đại chiêu 24 giây sang ô thứ 4 (phím nhanh `R`).
3. Cập nhật nội dung hộp thoại Popup khi bấm nút `(i)` trên từng chiêu đúng theo `skills_quyen_cuoc.json` (giữ nguyên layout hộp thoại: Tiêu đề vàng, câu mô tả, Loại, Hồi chiêu, Nội lực, Phím nhanh, nút Đóng / Dùng).

### NHIỆM VỤ 2: CƠ CHẾ NỘI TẠI "CHƯỞNG ẤN CHU SA" (THAY DẤU CHỮ VẠN TÍM)
1. Mỗi mục tiêu có bộ đếm debuff `chuSaStacks` (tối đa 3 tầng, tồn tại 6 giây, làm mới thời gian khi cộng thêm).
2. Hiển thị `assets/vfx/vfx_passive_chu_sa_mark.png` trên ngực/đầu mục tiêu có Ấn (quy mô/độ sáng tăng nhẹ từ tầng 1 -> 3; bỏ hoàn toàn ký hiệu chữ `卍` màu tím cũ).
3. Hàm `detonateChuSa(target, player)`: Khi kỹ năng kích nổ đánh trúng mục tiêu đang có `chuSaStacks > 0`:
   - Gây thêm `35% ATK * chuSaStacks` sát thương bạo phát.
   - Hồi ngay `4 * chuSaStacks` Nội lực cho người chơi (tối đa hồi 12 Nội lực trên mục tiêu chính để không tràn vô hạn khi đánh bầy đông).
   - Cộng thêm `2 * chuSaStacks` vào bộ đếm Liên kích.
   - Nếu `chuSaStacks == 3`, áp trạng thái `tanHon` (Tán Hồn) trong 4 giây: quái nhận thêm 18% sát thương và tỏa hạt sương xám lạnh từ chân.
   - Bật hiệu ứng nổ bùa `assets/vfx/vfx_e_talisman_burst.png` tại vị trí mục tiêu rồi reset `chuSaStacks = 0`.

### NHIỆM VỤ 3: TRIỂN KHAI LOGIC & HITBOX 6 CHIÊU THỨC QUYỀN CƯỚC TRỪ TÀ
1. Đánh thường — **Phục Ma Liên Quyền** (thay *Thiên Cương Liên Hoàn*):
   - Chuỗi 4 nhịp cận chiến (`45% / 50% / 55% / 80% ATK`). Đổi vệt đánh sang tông vàng kim - đỏ chu sa (`#FFE082` -> `#FF6E40`). Nhịp thứ 4 khắc `+1 chuSaStacks` lên quái trúng đòn.
2. Nút Lướt — **Bộ Hư Lưu Phù** (CD `2.5s`, Nội lực `0`):
   - Giữ logic lướt miễn nhiễm va chạm ngắn hiện tại, để lại vệt sương xám mờ và đặt 1 bẫy bùa vàng tại điểm xuất phát. Sau `0.6s`, bùa tự nổ (`90% ATK`, bán kính nhỏ `90px`), làm chậm `35%` trong `1.5s` và khắc `+1 chuSaStacks`.
3. Ô 1 [Phím Q] — **Phược Hồn Cương Quyền** (CD `5s`, Nội lực `15` — nâng cấp từ *Cương Khí Phá Không*):
   - Dùng sprite đạn `assets/vfx/vfx_q_fist_projectile.png` (tự động `flipX` khi nhân vật quay trái), bay thẳng xuyên tối đa 5 kẻ địch, gây `160% ATK` và khắc `+1 chuSaStacks`.
   - QUAN TRỌNG: Sửa hành vi đẩy lùi cũ (vốn làm quái văng khỏi tầm tay Quyền Cước) thành **giật tụ nhẹ về phía người chơi `35px - 45px`** trong `0.25s` kèm khựng nhẹ `0.35s` để người chơi nối tiếp chuỗi đấm thường mượt mà.
4. Ô 2 [Phím F] — **Bát Quái Chấn Địa Cước** (CD `9s`, Nội lực `20` — nâng cấp từ *Chấn Địa Quyền*):
   - Nện gót cước/đấm đất gây `210% ATK` vùng tròn trước mặt, hất nảy tại chỗ (không hất văng xa) và làm choáng `1.3s`.
   - Đặt lớp decal `assets/vfx/vfx_r_bagua_crater_decal.png` ở lớp mặt đất (`Z-order` dưới chân quái và nhân vật, tuyệt đối không che nhân vật) tồn tại `3.0s`, mỗi giây đốt `25% ATK` và làm chậm `25%` quái bước vào.
5. Ô 3 [Phím E] — **Toái Phách Bát Cực Chưởng** (CD `12s`, Nội lực `22` — ô kỹ năng mới):
   - Lao nhanh áp sát mục tiêu gần nhất theo hướng mặt (tối đa `180px`), tung liên hoàn 6 chưởng nhanh trong `0.75s` (`6 x 30% ATK`, mỗi hit `+1` Liên kích, tạo tàn ảnh bàn tay vàng cam), sau đó tung đòn song chưởng kết thúc (`110% ATK`) gọi `detonateChuSa()` kích nổ toàn bộ Ấn Chu Sa trong vùng trước mặt.
6. Ô 4 [Phím R · Đại Chiêu] — **Quỷ Môn Trấn Ngục Ấn** (CD `24s`, Nội lực `35` — nâng cấp đại chiêu bàn tay 24s):
   - Chia làm 3 nhịp rõ ràng thay cho kiểu bụp ra rồi phủ khói tím đặc che màn hình:
     * Nhịp 1 (`0.0s - 0.6s` · Khai Môn Hút Quái): Hiện `vfx_r_bagua_crater_decal.png` rực đỏ dưới đất tại tâm vùng mục tiêu, tạo lực hút kéo mọi quái trong bán kính `220px` tụ vào tâm và làm chậm `70%`.
     * Nhịp 2 (`0.6s - 1.0s` · Cự Chưởng Giáng Thế): Cho `assets/vfx/vfx_r_giant_exorcist_palm.png` lao từ phía trên xuống tâm trận theo hàm gia tốc `Cubic Ease-In`. Ngay khoảnh khắc chạm đất: chớp sáng vàng-đỏ `0.05s`, dừng khựng chuyển động quái (hit-stop) `3 frame` (`~0.05s`), rung camera nhẹ `3px` trục dọc, gây `480% ATK` diện rộng (nếu mục tiêu dưới `30%` máu nhận thêm `+30%` sát thương Trảm Tà) và gọi `detonateChuSa()`.
     * Nhịp 3 (`1.0s - 1.6s` · Âm Khí Tán Hồn): Cự chưởng mờ dần trong `0.35s`; tỏa 6-8 hạt khói mềm `assets/vfx/vfx_soft_ghost_smoke_puff.png` tông xám xanh lạnh với `Alpha` tối đa `0.45` (TUYỆT ĐỐI không để đặc 100% như đám mây tím cũ để người chơi nhìn rõ cọc gỗ/quái và số BẠO KÍCH nhảy lên).

### NHIỆM VỤ 4: HỆ THỐNG KHÓI ÂM KHÍ MƯỢT 60 FPS DÙNG CHUNG (CHO CẢ CHIẾN ĐẤU & CỔNG QUỶ MÔN QUAN Ở SẢNH CHÍNH)
1. Viết module/hàm dùng chung `spawnGhostMist(x, y, options)` sử dụng `assets/vfx/vfx_soft_ghost_smoke_puff.png` nội suy ở 60 FPS:
   - `Alpha` đi theo đường cong mềm: tăng `0 -> maxAlpha (0.45 - 0.60)` trong `15%` thời gian đầu, sau đó giảm mượt về `0` theo `Ease-Out`.
   - `Scale` nở dần từ `0.6 -> 1.45` theo `Cubic Ease-Out`, dịch chuyển chậm sang hai bên kết hợp xoay nhẹ ngẫu nhiên `-12°` đến `+12°`.
2. Tại màn hình Sảnh Chính (khi click mở cổng **Quỷ Môn Quan**):
   - Kích hoạt `spawnGhostMist` ngay khoảnh khắc 2 cánh cửa vừa tách khe (không chờ cửa mở hết mới hiện khói), đặt thêm một quầng sáng đỏ mờ phía sau khe cửa và duy trì làn khói tràn mềm xuống bậc thềm cho đến tận lúc màn hình fade sang màn Loading (xóa bỏ hiện tượng giật 12 FPS, cắt ngang đáy sprite và khoảng trống 0.7s cuối trước khi chuyển cảnh).

Hãy kiểm tra kỹ thứ tự lớp vẽ (Z-Order): Ground Decal Bát Quái dưới chân quái -> Quái & Nhân vật -> Đạn/Bùa/Cự chưởng -> Khói sương bán trong suốt (Alpha <= 0.45) -> Số sát thương & UI luôn ở trên cùng. Sau khi code xong, hãy liệt kê các file đã chỉnh sửa để tôi vào phòng Luyện Công kiểm thử ngay.
```
