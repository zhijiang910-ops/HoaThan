# Brief cho ChatGPT: vẽ lại 6 kiếm bằng PIXEL ART THẬT (cùng lưới pixel với nhân vật game)

## Vì sao cần
Gói trang bị 26/11 có 5 kiếm vẽ mịn (300–850 px). Trong game nhân vật là pixel art cao 106 px, nên kiếm phải thu về ~62 px thì mất chi tiết, hoặc để mịn thì lệch phong cách nhân vật. Cách đúng: **vẽ lại từng thanh kiếm ngay trên lưới pixel của game**, giữ thiết kế đã duyệt.

## Yêu cầu kỹ thuật (bắt buộc)
- Mỗi thanh một file PNG riêng, **nền trong suốt**, **lưới pixel thật**: mỗi pixel là một ô vuông, KHÔNG làm mịn (anti-alias), KHÔNG khối 2×2, KHÔNG gradient mờ. Chỉ màu đặc.
- **Nằm ngang, mũi kiếm hướng sang PHẢI, chuôi bên TRÁI.** Không xoay chéo.
- **Cỡ: dài 64 px (tối đa 72 px), cao tối đa 22 px.** Đây là cỡ đúng trong game (nhân vật cao 106 px). Không vẽ to hơn rồi thu nhỏ.
- **Bảng màu ≤ 24 màu mỗi thanh.** Viền tối mảnh 1 px quanh thanh, tô bóng ít (2–3 tông mỗi vật liệu), màu dịu. Cùng phong cách nhân vật chibi của game (viền đen mảnh, màu dịu).
- Chi tiết phải **đọc được ở 1 px**: ví dụ mắt hổ phách là chấm cam 2–3 px, xích là chuỗi ô 2 px, mặt ngọc là 2×2 px. Giản lược hoa văn, đừng cố nhồi chi tiết.
- Dây xích, bùa, ngọc treo ở chuôi là một phần của kiếm: giữ nằm trong khung ảnh (rủ xuống dưới chuôi).
- **Đánh dấu điểm nắm:** vẽ thêm file `<tên>_nam.png` giống hệt nhưng có **một pixel đỏ tinh (#FF0000)** đặt đúng giữa phần chuôi nơi bàn tay cầm. File thật dùng trong game là bản KHÔNG có pixel đỏ.
- Kèm bản xem trước phóng ×6 bằng NEAREST (`<tên>_x6.png`) để kiểm.

## 6 thanh cần vẽ (giữ đúng thiết kế đã duyệt trong gói)
1. `kiem01` Hành Giả: thân thép sáng, vải cam quấn gần chuôi, chắn kiếm vân bạc, chuôi chàm, đầu chuôi tròn bạc.
2. `kiem02` Huyền Giáp: thân bạc xám khắc vân mây, chắn kiếm mây cuộn, đầu chuôi là vòng tròn rỗng.
3. `kiem03` Tiền Đồng: không có lưỡi thép, thân là xâu 6–7 đồng tiền xỏ dây đỏ, chuôi quấn dây đỏ có đồng tiền lớn làm chắn, bùa vàng chữ đỏ treo dưới chuôi.
4. `kiem04b` (phương án B) và `kiem04d` (phương án D): kiếm đen đỏ có các mắt hổ phách dọc thân (B: 3 mắt to, chắn kiếm vuông vân đỏ; D: 5 mắt nhỏ, chắn kiếm cong lưỡi liềm), chuôi quấn đỏ, có xích và mặt bài treo.
5. `kiem05` Xích Tím: thân tím có xích chạy dọc, chắn kiếm chữ thập vàng có ngọc đỏ, xích tím rủ xuống kèm mặt ngọc tím.

## Bố cục mẫu (canvas gợi ý 80×28, chuôi sát trái)
```
[chuôi][chắn][=========== thân ===========>mũi]
```

## Prompt dán thẳng cho ChatGPT
> Vẽ 6 thanh kiếm bằng PIXEL ART THẬT, mỗi thanh một file PNG nền trong suốt. Lưới pixel sạch: mỗi pixel là một ô vuông, tuyệt đối không làm mịn, không anti-alias, không khối 2×2, không gradient mờ. Mỗi thanh nằm NGANG, mũi hướng sang phải, chuôi bên trái, dài 64 pixel (tối đa 72), cao tối đa 22 pixel, tối đa 24 màu, viền tối 1 pixel, tô bóng ít, màu dịu, phong cách chibi pixel art game (viền đen mảnh). Chi tiết nhỏ phải đọc được ở 1 pixel (mắt hổ phách là chấm cam 2–3 pixel, xích là chuỗi ô 2 pixel). Giữ đúng thiết kế các kiếm đã duyệt: [đính kèm ảnh kiếm gốc từng thanh]. Với mỗi thanh xuất thêm bản `_nam` có một pixel đỏ #FF0000 ở giữa phần chuôi nơi tay cầm, và bản `_x6` phóng ×6 bằng nearest-neighbor để xem. Không chữ, không nền, không nhân vật.

## Giao nộp
Thả 18 file (6 thanh × 3 bản) cho Claude; Claude đặt vào `game/assets/wpn/` đè lên bản hiện tại (`kiem01.png` …), tự đọc điểm nắm từ pixel đỏ, khai báo lại `WPN` về cỡ thật (không cần phóng thu nữa) và kiểm trong game ở 8 cỡ màn.
