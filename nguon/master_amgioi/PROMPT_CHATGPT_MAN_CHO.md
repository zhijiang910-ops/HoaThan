# Brief ChatGPT: ảnh nền màn chờ (loading) game Khử Tà Diệt Ma

## Màn chờ hiện có gì đè lên ảnh (giữ trống các vùng này)
- Trên cùng giữa (~12–30% chiều cao): tên game "Khử Tà Diệt Ma 驅邪滅魔" chữ vàng.
- Giữa-dưới (~62–78%): dòng trạng thái, thanh tải, số %.
- Dưới cùng (~78–95%): hộp "Chỉ dẫn".
=> Chủ thể (cảnh, nhân vật) nằm ở dải giữa 28–60% chiều cao, ở giữa ngang. Đáy và đỉnh tối, đơn giản.

## Kích thước
- Ngang, tỉ lệ 16:9, **2400×1350** (hoặc pixel thật 1200×675 rồi phóng ×2 NEAREST). Máy thật từ 811×260 tới 1280×720 nên game cắt `cover`: giữ chủ thể trong 60% bề ngang giữa và dải 28–60% chiều cao, rìa là phần thừa.
- Lưới pixel sạch: mỗi pixel vuông, không làm mịn, không khối 2×2, không gradient mờ. Bảng màu ≤ 64 màu. Nhẹ ≤ 1 MB.
- KHÔNG chữ, KHÔNG logo, KHÔNG thanh tải, KHÔNG khung UI.

## Prompt dán thẳng
> Vẽ ảnh nền màn chờ game NGANG 16:9, 2400×1350 px, PIXEL ART THẬT (lưới pixel sạch, không anti-alias, không khối 2×2, tối đa 64 màu), phong cách chibi pixel art cổ trang u tối, tông xanh đen + đỏ chu sa + vàng bùa. Cảnh: [để ChatGPT sáng tạo, ví dụ đạo sĩ nhỏ cầm kiếm đứng trước cổng Quỷ Môn Quan dưới trăng đỏ, sương mù, âm binh lấp ló]. Bố cục: chủ thể gọn ở dải giữa (28–60% chiều cao, 60% bề ngang giữa); phần trên và dưới ảnh tối, đơn giản, thưa chi tiết (sẽ có chữ và thanh tải đè lên). Rìa tối dần nhẹ. Tuyệt đối không chữ, không logo, không khung giao diện.
