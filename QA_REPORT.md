# QA_REPORT — Lifecycle VFX đòn C (24/11/2026) — CHƯA PHẢI PASS TOÀN COMBO

Phạm vi lần này: **chỉ sửa lifecycle code của VFX C**. Chưa đổi pose, chưa tạo VFX mới, chưa đụng A/B, chưa đụng sát thương/hồi chiêu/phạm vi/HIT.

## Thay đổi (`game/index.html`, `comboFx`)
- Bỏ `zs1` (slash độc lập) khỏi đòn C.
- Elip `k5c_behind` + `k5c_front` cùng bắt đầu tại khung HIT, cùng T = 0,5 s (trước 0,75 s), fade 0,2 ở cuối; lớp sau `gr=1`, lớp trước `gr=0`.
- `go()` nhận thêm tham số `fade`.

## Đo (Chromium, đồng hồ ảo 1/60 s, Luyện Công, Kiếm +6, nam và nữ)
| Tiêu chí | Trước | Sau | Kết quả |
|---|---|---|---|
| Số slash chính trong C | 2 (`zs1` + elip) | 1 (elip) | PASS (đo) |
| Slash dư chồng lên elip | `zs1` 1133–1567 ms | không còn | PASS (đo, nam + nữ) |
| Elip tồn tại | 1200–1933 ms (hết đúng lúc anim C) | 1200–1683 ms; 1683–1933 ms (250 ms) không còn VFX | PASS (đo) |
| Hai lớp behind/front cùng timeline | có | có | PASS |
| Elip tan trước khi anim C kết thúc | không | có | PASS |
| Vệt dư sau C (anim tiếp theo) | không thấy | không thấy | PASS (một lần đo) |
| Thời điểm HIT (`swhit`) | 1233 ms | 1233 ms (không đổi, cố ý) | Chưa đổi, xem dưới |
| Sát thương, hồi chiêu, phạm vi | – | không đổi | Không đụng |
| Pose C, đầu nhọn kiếm khí, elip không đều | – | **chưa sửa** | FAIL (còn tồn tại) |
| A trông giống chém, B timing | – | chưa sửa | Chưa kiểm |

## Còn FAIL / chưa làm
1. **Hình elip vẫn hiện nguyên vòng ngay khung đầu**, thiếu mũi nhọn kéo dần theo lưỡi kiếm: cần VFX mới từ PixelLab (đang bị chặn, xem báo cáo).
2. **HIT C vẫn sớm** (100 ms sau đầu C) so với lúc thân quét: cần dựng lại pose C rồi mới đặt lại HIT, không dời số.
3. Pose A, B, C chưa dựng mới. Chưa so với Hovl (thiếu file tham chiếu).
4. Mới kiểm bằng ảnh/video **trong Luyện Công, 1 cọc gỗ**, chưa kiểm khi có quái; không kiểm +0 (A–B) riêng; chưa kiểm 5× của combo đầy đủ ngoài đoạn C.
5. Kiếm bay trong ảnh là Hồi Phong Quy Sao (ô tự kích hoạt), không thuộc C.

## Bằng chứng
`QA_BEFORE_AFTER/BEFORE_C_nam_60fps_sheet.png`, `AFTER_C_{nam,nu}_60fps_sheet.png`, `AFTER_C_{nam,nu}_60fps.mp4`, `AFTER_C_{nam,nu}_slow5x.mp4`, `AFTER_timeline_{nam,nu}.txt`, `BEFORE_ticks_nam.txt`, `BEFORE_AUDIT_ABC.md`.

## Thử PixelLab pose C (nam) — 24/11/2026 — FAIL, đã dùng hết 2 lần thử có kiểm soát
Quy trình: `/animate-with-skeleton-v3`, 12 khung C1–C12 từ bảng key pose (`nguon/phac_thao/KEYPOSE_COMBO_KIEM_nam.png`), ảnh gốc `xt_nam_first.png`. Mỗi lần 12 khung = 3 lượt (tổng 6 lượt). Ảnh: `QA_BEFORE_AFTER/TRIAL1_..._FAIL.png`, `TRIAL2_..._FAIL.png`.
| Tiêu chí | Lần 1 (seed 7) | Lần 2 (seed 11, tay gần buông xuống, mô tả "side profile, long skirt") |
|---|---|---|
| Đúng Master (trang phục) | FAIL: lộ quần đen, áo choàng ngắn/xòe, khác Master | FAIL: vẫn lộ quần đen và váy xòe, mất vạt trắng của Master |
| Góc nhìn | FAIL: thân xoay 3/4 về phía camera | FAIL: vẫn xoay 3/4 |
| Tay gần | FAIL: bị vẽ thành vật tròn như khiên trước ngực | Đã hết |
| Chuyển động chém quét | FAIL: C4–C8 chỉ là tay duỗi thẳng kiếm, đọc ra như đâm | FAIL: tương tự; C2 kiếm chĩa ra trước thay vì nâng cao |
| Chiều dài kiếm / một thanh | Đạt (một thanh) | Đạt |
Kết luận: **không dùng được frame PixelLab này**. Theo luật: dừng generate ngẫu nhiên, chuyển sang retarget/chỉnh khung có kiểm soát từ Master. Chưa đưa gì vào game.

## Phát hiện: khung C hiện có trong game CŨNG lệch Master (24/11/2026)
Ảnh: `QA_BEFORE_AFTER/BEFORE_C_frames_game_{nam,nu}.png` (10 khung C kèm ms và khung HIT), `MASTER_vs_TRIAL_PixelLab.png`.
- Master (idle/run, `xt_nam_first.png`): thân nhìn nghiêng hẳn, áo choàng dài chấm gót có vạt trắng.
- 10 khung C đang chạy trong game: lộ quần đen, thân xoay 3/4, tức cũng lệch Master giống kết quả thử PixelLab. Tư thế gần như không đổi giữa các khung (kiếm duỗi ngang trước ngực, chỉ đổi nhẹ góc kiếm); không có lấy đà, không có quét. HIT ở C2 (70 ms) khi kiếm đã duỗi sẵn.
- Hệ quả: retarget từ khung C cũ sẽ kế thừa lệch nhận diện; không thể coi nó là "đúng Master".

## Thử PixelLab lần 3 — pose C (nam), chân khép, chuyển động ở thân trên — ỨNG VIÊN, CHƯA PASS
Ảnh: `QA_BEFORE_AFTER/TRIAL3_PixelLab_C_nam_UNG_VIEN.png`; frame: `ANIMATION_A_B_C/nam/C_ung_vien_lan3/` (chưa đưa vào game). 3 lượt, seed 5.
| Tiêu chí | Kết quả |
|---|---|
| Trang phục / màu so Master | Đạt rõ: áo choàng dài, vạt trắng, thắt lưng, dải tóc, màu đúng. Đo bảng màu: 100% màu thuộc bảng Master (lượng tử hóa thô, chỉ kiểm màu lạ) |
| Góc nhìn | Gần đạt: thân nghiêng, cổ áo trắng hơi lộ phía trước ở C3–C7 |
| Chân / trọng tâm | Đáy chân ổn 116–117 so Master 117 (không trượt, không nổi); C4–C7 hạ người ~5 px do khuỵu (chủ ý) |
| Kiếm một thanh, đúng tay | Đạt |
| Chuyển động | C2–C3 nâng kiếm cao đọc rõ; C4 chém chéo xuống rõ; C5–C8 kiếm duỗi ngang (sweep đọc như duỗi tay, VFX phải kể phần quét) |
| Lỗi còn lại | C5: mũi kiếm bị vỡ/nhòe (FAIL khung này); quần đen lộ nhẹ ở cổ chân C4–C7 cần kiểm 1× và phóng; C1/C12 chưa trùng tuyệt đối Master idle |
