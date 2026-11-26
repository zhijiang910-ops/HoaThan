# Brief cho ChatGPT: vẽ lại ảnh nền màn "Tạo nhân vật" (game Khử Tà Diệt Ma)

## 1. Hiện trạng (đo ngày 26/11)
| Ảnh | Cỡ | Tỉ lệ | Màu | Vai trò |
|---|---|---|---|---|
| `game/assets/ui/creation/co-mieu.webp` | 1122×1402 | 0,80 (DỌC) | ~57.000 (tranh mịn, chỉ 24% khối 2×2 giống nhau, KHÔNG phải lưới pixel sạch) | nền giữa màn, đang dùng |
| `deco-dam.webp` (tranh phong cảnh cột trái) | 1833×858 | 2,14 | ~32.600 | **ĐÃ BỎ khỏi màn** (chủ game 26/11) |

Vấn đề: màn tạo nhân vật là **ngang** (tỉ lệ 1,78 đến 2,17) nhưng nền là ảnh **dọc**. Game phải vẽ ảnh cao 100% màn, nên ở iPhone ngang (956×440) cảnh chỉ rộng 352 px (37% bề ngang), hai bên là phần cắt tối. Muốn đẹp phải có **một ảnh nền NGANG** cùng cảnh.

Hai bảng (tên nhân vật bên trái, môn phái bên phải) là CSS, không phải ảnh, và **che mất ~28% bề ngang mỗi bên**. Chỉ ~42% giữa màn thấy rõ.

## 2. Cỡ màn thật cần phủ (CSS px, đều là ngang)
| Máy | Cỡ | Tỉ lệ |
|---|---|---|
| iPhone (phổ biến nhất) | 852×393, 932×430, 956×440 | **2,17** |
| Khung nhỏ/artifact | 550×278 | 1,98 |
| Điện thoại cũ, tablet, máy tính | 667×375, 1100×620, 1280×720 | 1,78 |

Game dùng `cover` (phóng cho phủ kín rồi cắt). Ảnh tỉ lệ **2,17** thì ở màn 1,78 bị cắt khoảng 9% mỗi bên, chỉ là phần nằm sau bảng nên không mất gì.

## 3. Yêu cầu ảnh mới (MỘT ảnh duy nhất)
- **Tỉ lệ 2,17:1 (ngang).**
- **Lưới pixel thật 1434×660** (mỗi ô pixel = 1 điểm ảnh, KHÔNG khối 2×2, KHÔNG làm mờ). Xuất kèm bản **×2 bằng NEAREST = 2868×1320** (khớp iPhone 3x, 956 px rộng × 3). Nếu không giữ được lưới sạch thì thà vẽ 956×440 pixel thật rồi phóng ×3 NEAREST, đừng làm mịn.
- **Bảng màu ≤ 96 màu**, PNG (alpha không cần), phong cách pixel art tối, đồng bộ với game: chibi master, viền đen mảnh, màu dịu, tô bóng ít.
- **KHÔNG chữ, KHÔNG logo, KHÔNG nhân vật, KHÔNG khung/UI** (nhân vật và bảng game tự vẽ đè lên).
- Cảnh: giữ đúng cảnh hiện tại (cổng quán cổ trên bậc đá dưới trăng lưỡi liềm, hai đèn lồng đỏ, đèn đá hai bên, cây khô lá đỏ, sương xanh, sân đá ướt, lá đỏ rơi). Mở rộng ra hai bên cho thành cảnh ngang.

## 4. Bố cục (tính theo % bề ngang × % bề cao của ảnh)
- **Chủ thể chính (cổng, trăng, bậc đá) nằm trong dải giữa x 30% đến 70%.** Hai dải ngoài (0 đến 28% và 72% đến 100%) bị bảng che, chỉ để cây, đá, sương, đèn phụ, **không đặt thứ quan trọng**.
- **Nhân vật đứng giữa, chân ở khoảng y 78%**, cao khoảng 24% bề cao ảnh. Vùng x 40% đến 60% từ y 45% đến 82% phải **thoáng, sân phẳng, không vật cản**.
- **Đáy ảnh (y 86% đến 100%) tối và đơn giản**: hàng ô chọn màu áo nằm ở đó.
- **Trời và mái cổng ở nửa trên**, trăng đặt gần x 38%, y 12%.
- Rìa trái, phải, trên, dưới tối dần (vignette nhẹ) để hòa với bảng.

## 5. Giao nộp
- File: `nen_tao_nhan_vat_ngang_1434x660.png` (lưới pixel thật) và `nen_tao_nhan_vat_ngang_2868x1320.png` (×2 NEAREST).
- Nhẹ: sau khi nén bảng màu ≤ 1,5 MB (game tải ảnh này ngay lúc mở).
- Nhờ chủ game đặt file vào `game/assets/ui/creation/`; phần code Claude sửa.

## 6. Prompt dán thẳng cho ChatGPT
> Vẽ ảnh nền pixel art NGANG, tỉ lệ 2,17:1, kích thước 1434×660 pixel thật (lưới pixel sạch, mỗi pixel là một ô, không làm mịn, không khối 2×2), bảng màu tối đa 96 màu, PNG. Cảnh: sân đá ướt trước cổng quán cổ phong cách Trung Hoa u tối dưới trăng lưỡi liềm, mái ngói rêu, hai đèn lồng đỏ phát sáng, hai đèn đá hai bên bậc thang, cây khô lá đỏ rơi, sương xanh lam bay thấp, không khí khử tà diệt ma. Phong cách: chibi, viền đen mảnh, màu dịu, tô bóng ít, tông xanh đen và đỏ chu sa. Bố cục: cổng và trăng ở dải giữa (30% đến 70% bề ngang); hai bên (0 đến 28% và 72% đến 100%) chỉ cây, đá, sương, không chi tiết quan trọng; vùng giữa phía dưới (x 40% đến 60%, y 45% đến 82%) là sân đá phẳng thoáng để đặt nhân vật; đáy (y 86% đến 100%) tối và đơn giản; rìa tối dần nhẹ. TUYỆT ĐỐI không chữ, không logo, không nhân vật, không khung giao diện. Sau đó xuất thêm bản phóng ×2 bằng nearest-neighbor kích thước 2868×1320.
