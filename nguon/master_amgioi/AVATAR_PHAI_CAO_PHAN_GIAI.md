# Vẽ lại avatar 6 phái ở độ phân giải cao (nhờ ChatGPT)

Lý do: 12 avatar hiện tại cắt từ một tấm tổng hợp 1536×1024 nên mỗi ảnh chỉ khoảng 225×320 px. Hiện trong màn tạo nhân vật ảnh bị phóng gấp đôi, nên mềm và vỡ nét. Cần mỗi ảnh vẽ RIÊNG, lớn hơn nhiều.

## Yêu cầu giao
- 12 ảnh riêng (6 phái x nam/nữ), mỗi ảnh một file PNG, **cao 1536 px, rộng 1024 px** (tỉ lệ 2:3), không có khung viền, không chữ, không logo, không nhãn tên phái. Nền xanh đậm như bản cũ.
- Giữ ĐÚNG thiết kế và nhân vật của bản đã duyệt (ảnh tổng hợp chủ game đã đưa): cùng gương mặt, trang phục, phụ kiện, màu. Không sáng tác lại.
- Dàn bố cục: nhân vật từ ngực trở lên, nhìn nghiêng ba phần, mặt nằm ở phần nửa trên, chừa một ít khoảng nền quanh đầu.
- Mép nét rõ, không mờ, không bóng loáng quá mức.

## Prompt gốc (dán kèm ảnh tổng hợp đã duyệt)
> Redraw ONLY the character in the [vị trí: hàng/cột, ví dụ "top row, first card, Mao Son sect male"] card of the attached image as a single high-resolution portrait, 1024x1536 px. Keep the character design exactly identical: same face, hair, clothes, accessories, colours, expression and pose. Painterly pixel-art look, same palette. No card frame, no border, no text, no logo, deep navy background. Bust portrait, three-quarter view, face in the upper half with a little space around the head.

## Danh sách (thứ tự trong ảnh tổng hợp)
Hàng trên: Mao Sơn (nam, nữ), Trảm Yêu (nam, nữ), Phục Ma (nam, nữ). Hàng dưới: Thiên Cương (nam, nữ), Huyền Linh (nam, nữ), Truy Hồn (nam, nữ).

## Khi có ảnh mới
Chủ game gửi 12 ảnh cho Claude. Claude kiểm tra rồi thay file `game/assets/portraits/phai-<phái>-<nam|nu>.webp` (cùng tên, game tự dùng); không cần sửa code. Nếu ảnh lớn hơn nhiều, nén webp chất lượng 90 để file nhẹ cho điện thoại.
