# PROMPT THỰC THI CHO CLAUDE — CHUYỂN CLASS KIẾM (MAO SƠN) SANG 100% TẦM XA (NGỰ KIẾM & PHÙ CHÚ) ĐỒNG BỘ QUY CHUẨN U TỐI

Hãy đọc kỹ `CLAUDE.md` (quy chuẩn đồ họa Kiếm hiệp u tối — Trừ tà của dự án) và bộ tài nguyên mới tôi vừa thêm vào `assets/icons_mao_son/`, `assets/vfx_mao_son/` cùng `skills_mao_son.json`.

Hiện tại Class Kiếm (**Mao Sơn**) trong game đang có 4 điểm bất hợp lý cần làm lại trọn vẹn:
1. Vẫn phải đứng gần chém cận chiến và chiêu Q (*Chu Sa Phá Tà Trảm*) lại lao xộc vào đám quái -> trùng vai trò cận chiến với Thiên Cương Môn (Quyền). Tôi muốn chuyển **Mao Sơn sang 100% PHÁI TẦM XA (Ngự Kiếm + Phù Chú)**.
2. Chiêu F hiện đang đặt nhầm tên *"Thiên Cương Trấn Ma Trận"* (bị trùng tên với Thiên Cương Môn!) -> phải đổi sang tên chuẩn Mao Sơn là **"Bát Quái Tỏa Ma Trận"** (Mao Sơn giữ độc quyền biểu tượng Bát Quái Âm Dương).
3. Chiêu C (*Thái Thượng Trảm Ma*) lúc thanh kiếm lớn cắm xuống đất ở giây `3.0s` đang vẽ 1 hình tròn vàng đặc + vết nứt dây mảnh bằng code rất thô; Chiêu F đang vẽ tia sét bằng vạch gấp khúc vàng đơn điệu.
4. Bốn ô Icon kỹ năng trên HUD của Class Kiếm hiện vẫn là chữ Hán trắng đen (`血 · 陣 · 天 · 萬`) và nút `Lướt` cũ -> cần cập nhật sang bộ 5 Icon nghệ thuật đồng cổ u tối mới đồng bộ 100% với Thiên Cương Môn.

Hãy giữ nguyên toàn bộ code của Thiên Cương Môn, chỉ cập nhật riêng **Class Kiếm (Mao Sơn)** theo đúng 5 nhiệm vụ dưới đây:

---

## NHIỆM VỤ 1: CẬP NHẬT 5 ICON UI & TÊN CHIÊU / POPUP CỦA PHÁI MAO SƠN
1. Khi người chơi chọn Class Kiếm (Mao Sơn), gắn bộ icon mới trong `assets/icons_mao_son/` (nhớ crop bỏ `8%` mép viền ngoài của ảnh gốc như bên Thiên Cương Môn để khít khung nút UI sẵn có, giữ `imageSmoothingEnabled = false`):
   - Nút Lướt: `icon_ms_dash.png` (**Thế Thân Độn Phù**)
   - Ô 1 (`Q`): `icon_ms_q.png` (**Đồng Tiền Dẫn Kiếm Phù** — thay *Chu Sa Phá Tà Trảm*)
   - Ô 2 (`F`): `icon_ms_f.png` (**Bát Quái Tỏa Ma Trận** — thay tên *Thiên Cương Trấn Ma Trận*)
   - Ô 3 (`C`): `icon_ms_c.png` (**Thái Thanh Phù Kiếm Vũ** — nâng cấp *Thái Thượng Trảm Ma*)
   - Ô 4 (`X`): `icon_ms_x_ult.png` (**Bát Quái Vạn Kiếm Quy Tông** — nâng cấp *Vạn Kiếm Tru Ma*)
2. Cập nhật đầy đủ tên hiển thị trên thanh cast bar phía dưới, chữ tên chiêu bay trên đầu và hộp thoại mô tả `(i)` theo đúng `skills_mao_son.json`.

---

## NHIỆM VỤ 2: NỘI TẠI "TAM THANH LINH PHÙ ẤN" & ĐÁNH THƯỜNG TỰ ĐỘNG TẦM XA A - B - C (+6)
1. **Nội tại `Tam Thanh Linh Phù Ấn` (tối đa 3 tầng):**
   - Dùng `assets/vfx_mao_son/vfx_ms_passive_mark.png` (`34px x 34px`) treo ngay trên đỉnh đầu quái (`enemy.x, enemy.y - enemyHeight - 16`, dùng chuẩn tọa độ World-to-Screen).
   - Khi chiêu kích nổ (chiêu C hoặc X) đánh trúng mục tiêu có Ấn: gây nổ lan bán kính `95px` (`+32% ATK / tầng`), hồi `4 Nội lực / tầng` (tối đa `12 NL`), cộng `+2 Liên kích / tầng` và bật `vfx_ms_talisman_burst.png`.
2. **Đánh thường tự động TẦM XA (`Tầm phát hiện & tự bắn = 270px` — KHÔNG chạy lại sát quái chém tay nữa!):**
   - Giữ 2 thanh phi kiếm hộ thể lơ lửng quanh đạo sĩ. Khi có quái trong bán kính `270px`, nhân vật đứng từ xa bấm kiếm quyết bắn theo quy ước toàn game:
   - **Đòn A (`0.22s` · `52% ATK`):** Phóng 1 thanh `vfx_ms_flying_sword.png` (`width = 95px`, xoay đúng góc vector bay tới mục tiêu!) lao xuyên mục tiêu đầu tiên và găm vào mục tiêu sau.
   - **Đòn B (`0.22s` · `64% ATK`):** Phóng liên tiếp 2 lá bùa `vfx_ms_talisman_proj.png` (`width = 72px`, bay lệch cánh cung nhẹ trên-dưới) lao vào mục tiêu, nổ tia lửa chu sa nhỏ khi chạm. *(Nếu vũ khí `< +6`, mỗi 2 chu kỳ A-B gắn `+1 tầng Linh Phù Ấn`).*
   - **Đòn C — Mở khóa khi Vũ khí `>= +6` (`Tam Tài Phân Kiếm Phù` · `0.34s` · `135% ATK`):**
     * Đạo sĩ vung tay phóng cùng lúc **3 thanh `vfx_ms_flying_sword.png` kích thước lớn (`width = 115px`) kèm đuôi bùa `vfx_ms_talisman_proj.png` mờ theo góc rẻ quạt `36°` (`-18°, 0°, +18°`) xuyên thấu TOÀN BỘ quái trên đường bay (`pierce all`)**!
     * Khắc ngay `+1 tầng Linh Phù Ấn` lên tất cả quái trúng 3 luồng kiếm và tạo `hit-stop 2 frame` khi xuyên từ 3 quái trở lên.
3. **Nút Lướt — `Thế Thân Độn Phù` (`CD 2.5s`):**
   - Lướt thoát nhanh khỏi vòng vây quái (ưu tiên hướng joystick hoặc lùi xa đám đông nếu không giữ hướng), để lại 1 lá bùa thế thân `vfx_ms_talisman_proj.png` dựng đứng (`rotation = -Math.PI/2`) tại chỗ cũ; sau `0.55s` phát nổ `vfx_ms_talisman_burst.png` (`95% ATK`), đẩy lùi quái truy đuổi `45px` và làm chậm `40%`.

---

## NHIỆM VỤ 3: CHUYỂN CHIÊU Q SANG TẦM XA ĐẨY LÙI GIỮ KHOẢNG CÁNH ("ĐỒNG TIỀN DẪN KIẾM PHÙ")
- Bỏ cơ chế lao người vào giữa đám quái chém vòng đỏ cận chiến của chiêu Q cũ!
- Từ vị trí đứng hiện tại, đạo sĩ phóng thẳng 1 thanh phi kiếm lớn `vfx_ms_flying_sword.png` (`width = 140px`) dẫn đầu kéo theo **3 lá `vfx_ms_talisman_proj.png` bay xoắn sóng phía sau** xuyên qua hàng quái trong tầm `330px`.
- Ngược với phái Quyền kéo quái lại gần, chiêu Q của Mao Sơn khi xuyên trúng quái sẽ **đẩy lùi bầy quái dạt ra xa người chơi `50px`**, khựng nhẹ `0.3s` và gắn `+1 tầng Linh Phù Ấn` (giúp phái tầm xa giữ khoảng cách an toàn cực sướng!).

---

## NHIỆM VỤ 4: NÂNG CẤP CHIÊU F TẦM XA ("BÁT QUÁI TỎA MA TRẬN")
- Cho phép **khai trận tại vị trí đám quái phía trước cách nhân vật tới `155px`** (ném 1 lá bùa `vfx_ms_talisman_proj.png` bay nhanh ra tâm `(cx, cy)` rồi bung trận đồ trong `0.18s`).
- Dưới đất (`Ground Decal Layer`, dưới chân quái & nhân vật):
  * Vẽ vành hố đá nứt 2.5D `vfx_ms_crater_ring.png` (`craterW = 410px`) đứng cố định, và vẽ pháp trận **`vfx_ms_bagua_seal.png`** (`sealDiam = craterW * 0.54`, ép `ctx.scale(1, 0.62)` trước khi `ctx.rotate(angle)`) xoay tròn trầm mặc bên trong lòng hố suốt `3.5s`!
  * Giữ 8 cọc gỗ treo bùa dựng quanh vành trận rất đẹp của bản hiện tại, nhưng **XÓA các vạch sét gấp khúc vàng vẽ code đơn điệu**, thay bằng: cứ mỗi `0.65s`, triệu hồi **2–3 thanh `vfx_ms_flying_sword.png` cắm thẳng từ trên trời (`rotation = Math.PI / 2`)** xuống đầu quái đứng trong vòng Bát Quái kèm chớp lục ngọc nhẹ, làm chậm `60%` mọi âm binh bước vào trận!

---

## NHIỆM VỤ 5: NÂNG CẤP CHIÊU C ("THÁI THANH PHÙ KIẾM VŨ") & ĐẠI CHIÊU X ("BÁT QUÁI VẠN KIẾM QUY TÔNG")
1. **Chiêu C (`Thái Thanh Phù Kiếm Vũ` · `CD 12s` · `22 NL` · Tầm xa `175px`):**
   - Trong `0.9s` đầu: Triệu hồi `8` thanh `vfx_ms_flying_sword.png` kèm lá bùa `vfx_ms_talisman_proj.png` từ sau lưng đạo sĩ bay vồng lên cao rồi **cắm xiên liên hoàn xuống vùng quái phía trước** (cày nhanh bộ đếm Liên kích).
   - Nhịp kết liễu (`t = 0.95s` — **XÓA SẠCH cái hình elip vàng đặc và vết nứt dây mảnh vẽ bằng code ở giây 3.0s bản cũ!**):
     * Hiện hố đá `vfx_ms_crater_ring.png` (`width = 300px`) dưới chân bầy quái.
     * Xoay dọc tấm **Cự Kiếm `vfx_ms_colossal_sword.png` (`rotation = Math.PI / 2`, mũi kiếm chúc thẳng xuống đất, chiều dài `310px`, `alpha = 1.0`)** lao sập từ đỉnh màn hình cắm ngập mũi kiếm vào tâm hố đá! Giữ Cự Kiếm cắm đứng yên rõ nét trên mặt đất `0.40s` kèm `hit-stop 2 frame`, **kích nổ toàn bộ Linh Phù Ấn** (`vfx_ms_talisman_burst.png`) để hồi Nội lực rồi mới mờ dần!
2. **Đại chiêu X (`Bát Quái Vạn Kiếm Quy Tông` · `CD 24s` · `35 NL`):**
   - **Nhịp 1 (`0.0s -> 1.25s` · Pháp Luân Khai Vạn Kiếm):** Dựng 1 vòng `vfx_ms_bagua_seal.png` xoay đứng nghiêng sau lưng đạo sĩ (`ctx.scale(0.42, 1.0)`), bắn xối xả **24 thanh `vfx_ms_flying_sword.png` xen kẽ `vfx_ms_talisman_proj.png`** bay ngang xuyên suốt màn hình theo hướng khóa `lockedDir`, găm đẩy bầy âm binh tụ dồn về phía trước.
   - **Nhịp 2 (`1.25s -> 2.20s` · Cự Kiếm Trấn Yêu Trảm Tà):** Thay thanh kiếm xám đơn giản ở giây `2.1s` bản cũ bằng tấm **`vfx_ms_colossal_sword.png` khổng lồ (`width = 420px`, `alpha = 1.0`, mũi hướng theo `lockedDir`)**: tụ khí lơ lửng ngang người đạo sĩ `0.30s` rồi **lao xuyên táo toàn màn hình** với vệt sương xám lục mỏng (`vfx_ms_soft_mist_puff.png`, `alpha <= 0.38`) + `hit-stop 3 frame` + rung camera `5px`, kích nổ toàn bộ Linh Phù Ấn gây sát thương Bạo kích cực đại!
