# Brief cho ChatGPT: vẽ lại ảnh nền màn "Tạo nhân vật" (game Khử Tà Diệt Ma), bản 26/11 v2

## 1. Hiện trạng (đo bằng Playwright, 26/11)
- Ảnh đang dùng: `game/assets/ui/creation/co-mieu.webp`, **1122×1402**, tỉ lệ 0,80 (DỌC), tranh mịn (không phải lưới pixel sạch).
- Game vẽ ảnh bằng `cover` trong khung giữa (giữa hai bảng CSS), ảnh kéo ra thêm 30 px mỗi bên. Hai bảng che gần hết hai bên, nên chỉ ~50% bề ngang màn thấy ảnh.
- Vùng ảnh thật cần phủ (CSS px) và độ phân giải cần ở màn 3x:

| Máy | Vùng ảnh | Tỉ lệ | Cần ở @3x | Ảnh hiện thấy |
|---|---|---|---|---|
| 811×260 (Safari có thanh công cụ) | 466×272 | 1,71 | 1397×816 | 47% chiều cao |
| 852×393 | 486×405 | 1,20 | 1458×1215 | 67% |
| 932×430 | 526×442 | 1,19 | 1578×1326 | 67% |
| 956×440 | 538×452 | 1,19 | 1614×1356 | 67% |
| 550×278 | 293×290 | 1,01 | 880×870 | 79% |
| 667×375 | 343×387 | 0,89 | 1028×1161 | 90% |
| 1100×620 | 610×632 | 0,97 | 1830×1896 | 83% |
| 1280×720 | 700×732 | 0,96 | 2100×2196 | 84% |

Ảnh 1122 px rộng chỉ vừa cho màn 2x; iPhone 3x cần ≥1614 px rộng nên ảnh hiện bị phóng và mềm.

## 2. Yêu cầu ảnh mới
- **Tỉ lệ 6:5 (ngang nhẹ), cỡ 1800×1500** (PNG hoặc WebP chất lượng cao). Nếu vẽ được to hơn: 2100×1750.
- **Chủ thể (cổng, trăng, chỗ nhân vật đứng) nằm gọn trong vùng giữa**, khoảng 60% bề ngang × 70% bề cao. Ở màn thấp (811×260) game chỉ thấy dải giữa chiều cao (~47%), nên cổng và sân đứng phải nằm trong dải đó.
- **Hai bên, trên, dưới chỉ là phần thừa** (cây, sương, đá, tối dần). Màn dọc hẹp cắt hai bên, màn rộng cắt trên dưới.
- Chân nhân vật khoảng y 70% (giữa dải), vùng quanh đó là sân phẳng thoáng. Đáy ảnh tối, đơn giản (hàng ô màu áo nằm ở đó).
- Rìa tối dần nhẹ để hòa với bảng.
- Cảnh giữ như hiện tại: cổng quán cổ u tối dưới trăng lưỡi liềm, hai đèn lồng đỏ, đèn đá, cây khô lá đỏ rơi, sương xanh, sân đá ướt. Tông xanh đen + đỏ chu sa.
- **KHÔNG chữ, KHÔNG logo, KHÔNG nhân vật, KHÔNG khung giao diện.**
- Nếu vẽ pixel art thật (lưới sạch, không khối 2×2, không làm mịn): vẽ 900×750 rồi phóng ×2 bằng NEAREST ra 1800×1500 (hoặc 600×500 ×3). Nếu vẽ tranh mịn thì cứ 1800×1500.
- Nhẹ: sau nén ≤ 1,5 MB (game tải ảnh này ngay lúc mở).

## 3. Giao nộp
Tên file `nen_tao_nhan_vat_1800x1500.png`. Chủ game đặt vào `game/assets/ui/creation/` (đè `co-mieu.webp` sau khi đổi sang webp), Claude sửa code.

## 4. Prompt dán thẳng cho ChatGPT
> Vẽ ảnh nền game NGANG NHẸ, tỉ lệ 6:5, kích thước 1800×1500 px, độ nét cao, phong cách pixel art/tranh mịn tối, tông xanh đen và đỏ chu sa. Cảnh: sân đá ướt trước cổng quán cổ Trung Hoa u tối dưới trăng lưỡi liềm, mái ngói rêu, hai đèn lồng đỏ phát sáng, hai đèn đá hai bên bậc thang, cây khô lá đỏ rơi, sương xanh lam bay thấp, không khí khử tà diệt ma. Bố cục: cổng và trăng nằm gọn ở vùng giữa ảnh (khoảng 60% bề ngang, 70% bề cao); sân đá phẳng thoáng quanh y 70% bề cao để đặt nhân vật; hai bên, trên, dưới chỉ là cây, đá, sương, tối dần, không đặt chi tiết quan trọng; đáy ảnh tối và đơn giản; rìa tối dần nhẹ. TUYỆT ĐỐI không chữ, không logo, không nhân vật, không khung giao diện.
