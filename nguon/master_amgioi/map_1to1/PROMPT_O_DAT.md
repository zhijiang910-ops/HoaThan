# Nhờ ChatGPT vẽ Ô ĐẤT lặp (1:1) cho mặt đất map Âm Giới nét hơn

Mặt đất giữa map đang mờ vì là ảnh nền 1600×1140 phóng ×2. Thay vì vẽ lại cả map, chỉ cần MỘT ô đất lặp mỗi map; game phủ ô này lên sân giữa, mờ dần ra rìa để giữ kiến trúc của ảnh nền.

## Prompt (dán cho ChatGPT, đính kèm ảnh nền `bg_<map>.png` làm mẫu màu)

Vẽ cho tôi một **ô mặt đất lặp liền mạch (seamless tileable)**, pixel art nhìn chếch từ trên xuống, đúng **512×512 px**, cùng màu sắc và chất đất với sân giữa của ảnh đính kèm (đất khô nứt, sỏi nhỏ, vài vết rêu/tro, tông tối u ám).

Bắt buộc:
- Pixel art thật 1:1: mỗi pixel là ô 1×1, KHÔNG phóng to ảnh nhỏ (không có khối 2×2 cùng màu hàng loạt), không làm mịn, tối đa 48 màu, tương phản vừa phải, nét rõ.
- **Lặp liền mạch**: mép trái khớp mép phải, mép trên khớp mép dưới, ghép 2×2 không thấy đường nối.
- Chi tiết phân bố đều, không có vật nổi bật, không bóng lớn, không hướng sáng rõ (để lặp không lộ).
- Không chữ, không nhân vật, không viền, không nền trong suốt.
- Tự kiểm: ghép thử 2×2 xem có lộ đường nối không.

Map cần ô đất: Hoàng Tuyền (đất vàng nâu tro), Quỷ Môn Quan, Bỉ Ngạn (đất đỏ tím), Nghiệt Kính (đá lạnh xanh xám), Uổng Tử (đất cháy tro đỏ), Vong Xuyên (bùn xanh đen ven sông), Diêm La (gạch lát đá đen đỏ). Thử Hoàng Tuyền trước.
