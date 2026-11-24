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
