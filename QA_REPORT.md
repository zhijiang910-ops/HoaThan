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

## Bộ ứng viên A(7) B(7) C(12) nam và nữ — PixelLab thân KHÔNG kiếm + kiếm gắn theo khung xương (24/11/2026) — ỨNG VIÊN, CHƯA PASS
Lý do đổi cách: tạo kèm kiếm bằng PixelLab cho thanh kiếm lúc nhòe, ngắn cụt, vỡ mũi hoặc biến mất (lần 3 + bộ thứ hai). Cách mới khớp kiến trúc game (vũ khí là lớp riêng, `WSOCK`): `first_frame` = khung idle của `hero_{nam,nu}_ns.png` (khớp Master 99,4% nam / 99,1% nữ pixel, chỉ khác kiếm), rig bỏ 3 khớp kiếm, mô tả "hands empty, no weapon"; vị trí chuôi, mũi, góc kiếm từng khung lấy từ khung xương (`socket.json`, hệ 128, góc độ; độ dài rig 24 nam / 30,8 nữ, ảnh kiếm game dài 28 / 32).
File: `ANIMATION_A_B_C/{nam,nu}/{A,B,C}_ung_vien/` (frame 128×128 RGBA không kiếm + `socket.json` + `job.json`). Ảnh/video: `QA_BEFORE_AFTER/UNG_VIEN_ABC_{nam,nu}_sheet.png`, `UNG_VIEN_ABC_{nam,nu}_cham.mp4` (A→B→C×2, 8 khung/s, phóng 5×, kiếm vẽ bằng ảnh kiếm của game xoay theo socket).
Tổng lượt PixelLab đã dùng cho nhánh combo hôm nay: 3 (thử 1) + 3 (thử 2) + 3 (thử 3) + 15 (bộ 2) + 18 (bộ 3) + 18 (bộ không kiếm, kể cả 9 lượt lãng phí do job nữ có kiếm đã gửi nhầm) ≈ 60.
| Tiêu chí | Kết quả |
|---|---|
| Đúng Master (trang phục/màu/tóc) | Đạt cả 26×2 khung (nhìn 2× và đo bảng màu 100% thuộc Master, thô) |
| Đáy chân | Nam 116–117, nữ 116–119 (Master 117/118): không trượt/nổi rõ; C nữ có biên 119 cần kiểm |
| Một thanh kiếm, độ dài cố định | Đạt: vẽ từ socket, mọi khung cùng độ dài |
| Kiếm mất / nhòe / vỡ mũi | Hết (kiếm không do PixelLab vẽ) |
| Đọc rõ chuyển động | A: nâng cao (A2) → chém chéo xuống (A3–A5) → thu; B: kéo kiếm ra sau (B2–B3) → quét ra trước (B5) → thu; C: nâng cao (C2–C3) → chém (C4) → duỗi quét (C5–C8) → thu |
| **Nữ C4: FAIL** | Có hình lưỡi liềm xám hallucinate phía trên đầu |
| Tay cầm kiếm | Chưa có lớp nắm tay: kiếm vẽ đè lên bàn tay, chuôi chưa che bởi ngón; cần lớp `_hand` mới |
| Chưa làm | Đưa vào game (WSOCK + sheet), HIT/timing, VFX mới, hướng trái, so +0 và +6, video 60 FPS trong game |

## ĐƯA COMBO MỚI VÀO GAME — A(7) B(7) C(12), nam và nữ (24/11/2026) — QA chạy thật, CHƯA tuyên bố PASS toàn bộ
Thay đổi: thêm 2 hàng ô (y=384, 512) vào `hero_{nam,nu}_ns.png` và `_hand.png` (ô cũ giữ cho lướt Huyết Ảnh `cutC` và bộ Huyền Giáp), socket kiếm 'f' từng khung vào `WSOCK`, `NC` và `TA/TB/TC` mới. **Tổng thời lượng giữ 580/550/800 ms** nên nhịp đánh và DPS không đổi (`dur` quyết định chu kỳ đánh). Chi tiết: `animation_manifest.json`.
Đo ở 60 FPS, nam và nữ, Luyện Công:
| Tiêu chí | Kết quả |
|---|---|
| A→B→C liền mạch, không reset về idle giữa các đòn | Đạt (timeline tick: attack 0–583, attack2 583–1133, attack3 1133–1933 ms) |
| +0 chỉ A–B; +6 có C | Đạt (forge 0: chỉ attack/attack2; forge 6: có attack3) |
| HIT đúng pha ra đòn | A ở 283 ms (A4), B ở khoảng 900 ms (B5), C ở khoảng 1400 ms (C4). HIT của B, C trễ hơn cũ (B 150→310 ms, C 100→255 ms trong đòn) vì khung chạm mới nằm ở pha quét thật |
| C: một elip, tan trước hết động tác | Đạt: elip 1350–1850 ms, anim C đến 1933 ms; không còn `zs1` |
| Quay mặt trái (lật) | Đạt: kiếm vẫn gắn đúng tay, elip đúng chiều (`QA_BEFORE_AFTER/AFTER_ABC_game_quay_trai.png`) |
| Kiếm đúng một thanh, đúng độ dài | Đạt trên các khung chụp (kiếm vẽ bằng ảnh kiếm của game) |
| Lỗi script | Không có |
Bằng chứng: `AFTER_ABC_game_{nam,nu}_sheet.png`, `AFTER_ABC_game_khung_cham_zoom.png`, `AFTER_ABC_{nam,nu}_60fps.mp4`, `AFTER_ABC_{nam,nu}_slow5x.mp4`, `AFTER_ABC_game_quay_trai.png`.
**Còn tồn tại / chưa kiểm:**
- Chưa có lớp bàn tay mới: kiếm vẽ đè lên bàn tay ở khung mới (chuôi chưa che bởi ngón).
- Pha quét C5–C8 vẫn là tay duỗi ngang (góc nhìn nghiêng), phần quét do elip đảm nhiệm. Elip PixelLab hiện vẫn hiện nguyên vòng ngay khung đầu, chưa có đầu nhọn kéo dần (cần VFX mới).
- Chưa so khung-từng-khung với video Hovl (chưa có clip nguồn).
- Chưa kiểm khi nhân vật đang di chuyển và đánh (run-swing) với khung mới, chưa kiểm bộ Huyền Giáp với combo mới (Huyền Giáp vẫn dùng khung đánh cũ), chưa kiểm iPhone thật.
- Kiếm bay Hồi Phong to và dễ che nhân vật trong ảnh QA (đã thêm viền để nhìn rõ).

## Các sửa khác trong phiên 24/11 (đo/chạy thật)
| Mục | Kiểm | Kết quả |
|---|---|---|
| Hồi Phong mất kiếm | Chụp 60 FPS nam/nữ trước/sau | Kiếm bay có viền tối, thấy chuôi và lưỡi trên tuyết |
| Thiên Xu | Đo sát thương theo thời gian, cấp 1/3/5 | Nổ ở 1,18 s; sau đó mỗi 1 s đúng 3/4/5 nhịp |
| Vạn Kiếm | Ngắm 4 hướng (Đông, Tây, Bắc, Đông Nam), bấm X rồi click | Làn kiếm hiện trước khi thả, VFX và vùng trúng đi đúng hướng ngắm; rebake gốc khớp sheet cũ sai khác 0,0 |
| Ngộ Không đi + đánh | Đếm `runPh` trong lúc đánh | Chân bước liên tục (67 giá trị khác nhau); chưa có video riêng |
| UI/HUD | Audit 5 cỡ màn (667×375, 740×360, 844×390, 915×412, 932×430), 5 màn | Sửa: nút Xuất phát ở >900px; avatar nhỏ. Còn: nút "i" kỹ năng 12 px (chủ ý, tăng vùng bấm sẽ nuốt cú bấm vvào ô kỹ năng) |
| Asset VFX | 40 mục SPX vs file | Không thiếu/hỏng kích thước |
| Soak 3600 tick nam+nữ, bấm Q/F/X + click ngắm | Lỗi script | 0 |
**Chưa kiểm:** Safari iPhone thật, Ngộ Không khi quay trái, bộ Huyền Giáp với combo mới, chạy với quái tinh anh/boss.

## Đòn C theo Hovl: pose mới + VFX elip mới (24/11/2026) — ỨNG VIÊN trong game, chưa tuyên bố PASS
Nguồn: bản quay màn hình Hovl của chủ game (`nguon/tham_chieu/hovl/MOTION_ANALYSIS.md`). Pose C dựng lại bám chuỗi Hovl: khuỵu thấp kiếm sau hông → đứng dậy kiếm dựng → duỗi ngang → kéo về hông → giơ cao sau lưng → vung xuống (chạm C9) → thu. Chân khép, thân trên làm chuyển động. PixelLab thân không kiếm (nam seed 51, nữ seed 52, 3 lượt mỗi giới), kiếm gắn socket.
VFX: PixelLab VFX creator. Lần 1 (lite, 2 lượt) FAIL: mỏng, nhỏ. Lần 2 (pro, 12 lượt) đạt: cung elip ngang to (275×106), dày tới ~18 px, đầu nhọn, vẽ dần theo chiều quét rồi mờ dần, thân dày đuôi thuôn, lõi trắng viền xanh. Hai lớp `hc_behind`/`hc_front` (12 khung) thay `k5c_*`.
Timing giữ tổng 800 ms; **khung chạm C9 bắt đầu ở 560 ms (70%)** (Hovl ~77%) để VFX 0,28 s kết thúc đúng lúc hết đòn.
| Tiêu chí | Kết quả (đo 60 FPS, nam và nữ) |
|---|---|
| Một elip duy nhất, không nhát chém dư | Đạt (fx trong C: chỉ `hc_behind`, `hc_front`, tia trúng) |
| Elip tan trước khi hết đòn | Đạt: C+520..800 ms, đòn kết 800 ms |
| Elip vẽ dần, đầu nhọn, dày | Đạt ở ảnh QA |
| Pose đọc ra chuỗi Hovl | Đạt trên 12 khung (xem `AFTER_C_hovl_*`) |
| Đúng Master | Đạt (màu 100% thuộc bảng Master, đáy chân 116–119) |
| Cảm giác: HIT của C trễ hơn rất nhiều | HIT ở 0,58 s sau khi bắt đầu đòn (cũ 0,1 s), do khởi động dài như Hovl. DPS không đổi (chu kỳ 800 ms); cần chủ game cảm nhận |
**Còn thiếu:** ít streak bên trong cung và ít tia lửa so với Hovl; chưa tạo VFX mới cho A, B (còn `zs3`, `zs2`); chưa có lớp bàn tay; Huyền Giáp vẫn khung cũ; chưa chơi thử trên iPhone.

## Chuỗi A-B-C liền theo Hovl, dùng lại khung có sẵn (24/11/2026)
Không gọi PixelLab. A 6 khung (580 ms, chạm A4), B 5 khung (550 ms, chạm B3), C 6 khung (800 ms, chạm C3). VFX trả về bản đã duyệt: zs3 (A), zs2 (B), elip k5c_* (C, sống 0,6 s, tan trước hết đòn). Đo 60 FPS nam và nữ: attack 0–583, attack2 583–1133, attack3 1133–1933 ms, không reset về idle, elip tan ở 1833 ms, không nhát dư. Ảnh/video: `QA_BEFORE_AFTER/CHUOI_ABC_*`.
Còn lại: khung nối A→B và B→C dùng khung của các đòn khác nên có chỗ nhảy tư thế nhẹ; HIT mới (A 280 ms, B 170 ms, C 190 ms trong đòn) cần mày cảm nhận; chưa có lớp bàn tay; Huyền Giáp vẫn khung cũ.

## Combo theo Sword Combo Keyframe Guide: khung A7/B7/C12 + VFX mới tạo theo ảnh (24/11/2026)
Khung: dùng lại 26 khung đã tạo theo đúng thứ tự guide (A1–A7, B1–B7, C1–C12; thân PixelLab không kiếm, kiếm gắn socket). VFX: PixelLab pro, 3 lần (A 10 lượt, B 10, C 12), mô tả bám hình guide: A chém chéo xuống từ trên-sau xuống dưới-trước, đỉnh A4, tia lửa mũi; B quét ngang rộng thấp, đỉnh B5; C nhát nhọn rơi xuống C4 rồi mở thành MỘT elip quanh chân (trước/bên/sau, lớp sau/trước tách) rồi mờ thành vệt, không còn gì sau đó. Nhịp giữ 580/550/800 ms, chạm A4/B5/C4.
Đo 60 FPS nam và nữ: A vệt bật 183–567 ms (A3 → đỉnh A4); B bật ~733 ms, tắt trước khi C bắt đầu (đã rút T còn 0,34 s); C bật tại C4 (1333 ms), tan trước 1933 ms; không còn zs1/zs2/zs3/k5c, không nhát dư.
Chưa làm: lớp bàn tay; Huyền Giáp; so từng khung với Hovl; chơi iPhone thật. Vệt A khá lớn, che một phần nhân vật khi đỉnh (giống guide).
