# AUDIT combo Kiếm A–B–C HIỆN TẠI (trước khi sửa) — 24/11/2026

Cách đo: Chromium + Playwright, đồng hồ ảo 1/60 s (`cong_cu/claude/combo_film2.js`, Luyện Công, Kiếm +6, nam). Dữ liệu từng tick: `BEFORE_ticks_nam.txt`. Ảnh: `BEFORE_C_nam_60fps_sheet.png`. **Mới đo nam**, chưa đo nữ.

## Timeline thật (ms từ lúc bắt đầu đòn A)
| Đoạn | Khoảng | VFX đang chạy |
|---|---|---|
| A (attack) | 0–583 | `zs3` 100–567; tia trúng `swhit` 283–567 |
| B (attack2) | 583–1133 (550 ms) | `zs2` bật **ngay đầu B** (583), `swhit` 750–1033 |
| C (attack3) | 1133–1933 (800 ms) | `zs1` 1133–1567 **và** `k5c_behind/front` 1200–1933; `swhit` 1233–1517 |
| A kế | 1933– | `zs3` 2033 |

## Nguyên nhân thật (đọc code `comboFx`, `game/index.html` ~dòng 1826–1832)
1. **C phát hai VFX độc lập:** `later(0, zs1)` ngay đầu C + `later(at, k5c_behind + k5c_front)`. `zs1` là "slash 1 độc lập" chồng lên vòng elip (433 ms đầu).
2. **Elip sống gần hết động tác:** `k5c_*` T=0.75 s, bắt đầu 67 ms sau đầu C, tắt đúng lúc anim C kết thúc (1933). Vòng không fade cùng nhịp thu thế; recovery của C bị phủ vòng sáng.
3. **Elip hiện nguyên vòng ngay khung đầu** (tick 72, 1200 ms), không có đầu nhọn kéo dần theo mũi kiếm; nhìn như vòng sáng đều nằm ngang.
4. **HIT quá sớm:** frame HIT của C là frame 2 (`TC=[[0,70],[1,90,1],…]`), tia trúng `swhit` ở 1233 ms (100 ms sau đầu C), trước khi vòng/lưỡi quét xong (vòng đạt kích thước đầy đủ ở ~1200–1330). B: HIT ở frame 3 (`TB` mốc 140 ms) nhưng `zs2` đã chạy từ đầu B nên vệt không gắn với thời điểm lưỡi kiếm quét. A: `zs3` bật `at-0.14` s trước HIT.
5. Các frame cuối C trong ảnh (tick 104–114) có kiếm bay `hp_*` (Hồi Phong, ô tự kích hoạt `k3`) — **không thuộc VFX C**; cần loại khỏi cảnh QA bằng cách tắt `k3` khi quay.
6. Không thấy hai timeline chồng nhau hay sheet chứa frame thừa: lỗi nằm ở **thiết kế sự kiện** (hai `go()` cho C, T cố định) chứ không phải rò rỉ event. Chưa phát hiện auto-attack kế tiếp đè lên recovery C trong lần đo này (A kế bắt đầu 1933, sau khi elip tan).

## Chưa đo / chưa làm
Nữ, 5× slow video, so sánh +0 (A–B) với +6, chạy khi có quái thật.
