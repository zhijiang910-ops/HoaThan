# MASTER_LOCK — Master nhân vật Tây Du Sinh Tồn (24/11/2026)

Bản sao bất biến: `nguon/master_lock/` (hash trong `SHA256SUMS.txt`). **Không ghi đè, không sửa các file này.** File đang chạy trong game vẫn là `game/assets/hero_*.png`; mọi frame mới phải so với bản khóa này.

## File Master
| File | Kích thước | SHA-256 | bbox alpha cả sheet | bbox alpha ô (0,0) |
|---|---|---|---|---|
| `hero_nam.png` | 3840×384 | `319eedc27accdec925ad839ccaf0a7909ab1443f01a66e8e04511b8d01786ee8` | (46, 2, 3805, 375) | (50, 12, 114, 118) |
| `hero_nu.png` | 3840×384 | `d8b58fc36be627234e0cfbf1746dfe2119b4f843fedfe39652a373d467230ce3` | (30, 0, 3806, 379) | (38, 13, 120, 118) |
| `hero_nam_ns.png` | 3840×384 | `6a4f37991ecee85a8369ade25e489fbd250b3d6614743b516f69050f25a33224` | (46, 2, 3791, 375) | (50, 12, 101, 118) |
| `hero_nu_ns.png` | 3840×384 | `fb785c022dc54f4a1fe804590ec43644bc6b92a82036a645230956d614a5491c` | (30, 0, 3786, 379) | (38, 13, 101, 118) |
| `hero_nam_hand.png` | 3840×384 | `a33f1b1bda05ead7ed6752b1989558e4f2a3f60c066c9b318a76417abc9b5700` | (1207, 203, 2353, 243) | None |
| `hero_nu_hand.png` | 3840×384 | `b6bcfa5e961a3e353e51ce2ccda2e6e8fac8f5b24487231caa75ade97aaf27a7` | (2183, 236, 2356, 244) | None |

- `hero_{nam,nu}.png` = sheet có kiếm (khung gốc). `hero_{nam,nu}_ns.png` = sheet **không kiếm** + `_hand.png` (lớp nắm tay). Game vẽ vũ khí như lớp riêng theo `WSOCK[giới]["x,y"]=[chuôi x, chuôi y, góc, 'b'|'f']`.
- Ô khung: **160×128** (PixelLab canvas 128 đặt lệch dx=16). Hướng mặt: đông (phải). Nhân vật vẽ 1 hướng, hướng trái dùng lật ngang khi chạy (`fx:-1`).
- Pivot chân: `CHM.hero_nam {ax:57, ay:119}`, `hero_nu {ax:77, ay:106}`; game trừ thêm `ay-=2` lúc nạp (dòng `for(const id in CHM)` trong `game/index.html`).
- Điểm gắn kiếm: `WSOCK` trong `game/index.html` (mỗi khung một tọa độ chuôi + góc).
- Tốc độ hiện tại (khung): idle 4, run 8, attack(A) 8, attack2(B) 8→7 dùng, attack3(C) 10, hit 4, death 4.
- Khóa nhận diện: giới tính, tỷ lệ, tóc/màu/phụ kiện, trang phục/họa tiết/bảng màu, thiết kế kiếm, pixel density, độ dày outline, góc nhìn, pivot, kích thước hiển thị. Không dùng nhân vật 3D của Hovl, không tạo nhân vật mới.
- Quy tắc kiểm frame mới: so với Master ở 1× và phóng nearest-neighbor; frame nào PixelLab đổi trang phục/kiếm/màu/tỷ lệ/mặt thì **FAIL**, không generate lại nhân vật từ đầu.
