# HoaThan · Bàn giao trang bị

Mở repo zhijiang910-ops/HoaThan trên nhánh main, đọc CLAUDE.md và MASTER_LOCK.md trước khi tích hợp. Gói này chứa hình nguồn và icon đã tách; sprite áo theo từng khung master còn phải dựng. Các mẫu trong ảnh cầm kiếm chỉ để duyệt ngoại hình.

| Số | Áo | Kiếm |
|---|---|---|
| 01 | Hành Giả, áo chàm đai cam | Thép quấn vải cam |
| 02 | Huyền Giáp đen, vai vân mây | Kiếm đen vân mây |
| 03 | Bát Quái Bào chàm viền vàng | Kiếm tiền đồng có bùa |
| 04 | Giáp đen đỏ | Kiếm đen đỏ mắt hổ phách. B và D đang so sánh, chưa chốt |
| 05 | Áo cổ cao tím đen, viền vàng | Kiếm xích tím, chuôi treo ngọc tím |

## Tệp trong gói

- icons/ — icon PNG trong suốt, 64×64. Icon 04 gốc và hai phương án B/D được đặt tên riêng. Cặp B/D cũng có PNG vũ khí tách riêng trong weapon-sources/.
- weapon-sources/ — ảnh vũ khí riêng, chưa chuẩn hóa kích thước và điểm nắm. Các mẫu 01, 02, 03, 05 tách từ hình nguồn icon, đang đặt chéo. Mẫu 04 gốc đã nằm ngang. B và D đã lật để chuôi bên trái, mũi bên phải.
- references/ — mẫu áo không kiếm, mẫu cầm kiếm, bảng 4 phương án của kiếm 04 và ảnh cầm thử B/D.

## Việc cần làm trong game

1. Nối icon theo món trong drawItemIcon và nhánh tải lại icon, bảo đảm icon riêng được ưu tiên hơn atlas chung nếu món nằm trong bộ trang bị. Dùng cơ chế kho và nút Trang bị hiện có.
2. Chuẩn hóa vũ khí vào game/assets/wpn/. Căn ảnh theo trục ngang và đánh dấu điểm nắm giữa chuôi, kiểm kích thước khi cầm. Móc vào cơ chế WPN/WART và WSOCK hiện có. Giữ lớp thân không kiếm và lớp bàn tay riêng. Khi đổi hoặc tháo kiếm, bàn tay phải còn nguyên. Dây xích và mặt treo thuộc vũ khí.
3. Dựng áo theo từng ô 160×128 của master. Giữ đúng đầu, tóc, bàn tay, chân và điểm neo, kiểm pixel ở 1×. Nối áo theo món đang mặc bằng OUTFIT. Làm trước mẫu nam đã duyệt, giữ ngoại hình có sẵn cho mọi giới hoặc động tác chưa có sprite thay thế.
4. Cho thử trong Luyện Công hoặc qua đồ test trong túi. Trang bị và tháo áo, đổi kiếm độc lập. Kiểm khi đứng, chạy, đánh và quay trái/phải. Kiểm cả lưu rồi mở lại. Gửi ảnh hoặc clip sau khi chạy được.
5. Chưa gán Lv, phẩm hoặc nguồn rơi cho các mẫu mới. Cho thử B và D riêng. Chờ chủ game chọn cây 04 trước khi thay mẫu chính. Không gọi PixelLab theo quy định hiện tại của dự án.
