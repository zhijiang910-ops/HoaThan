# PROMPT THỰC THI CHO CLAUDE — CẬP NHẬT BỘ 6 HUY HIỆU ĐẠI DIỆN MÔN PHÁI & TÊN 6 MÔN PHÁI TRÊN GIAO DIỆN CHỌN PHÁI

Tôi gửi kèm gói `assets/sect_crests/` gồm 6 huy hiệu đại diện môn phái (`256x256` PNG tách nền trong suốt `RGBA`, không có khung viền vuông để đặt nổi trực tiếp lên thẻ chọn môn phái màu tối `#0B1E22` thay thế 6 icon vector phẳng cũ).

Hãy cập nhật bảng chọn 6 môn phái (cả tên hiển thị lẫn đường dẫn ảnh huy hiệu) theo đúng danh sách chuẩn của dự án:

| Ô | Tên Môn Phái Mới (Thay tên cũ) | Vũ khí & Lối đánh | File Huy Hiệu Tách Nền (`assets/sect_crests/`) |
| :--- | :--- | :--- | :--- |
| 1 | **Mao Sơn Phái** *(Giữ tên)* | Kiếm & Phù chú · Tầm xa | `crest_2_mao_son_phai.png` |
| 2 | **Thiên Cương Môn** *(Giữ tên)* | Quyền Cước · Cận chiến | `crest_1_thien_cuong_mon.png` |
| 3 | **Đoạn Hồn Cốc** *(Thay Trảm Yêu Môn)* | Trọng Đao · Cận chiến | `crest_4_doan_hon_coc.png` |
| 4 | **Phá Sát Môn** *(Thay Phục Ma Tự)* | Trường Thương · Cận chiến | `crest_3_pha_sat_mon.png` |
| 5 | **Cửu U Tông** *(Thay Huyền Linh Các)* | Hồn Phiên · Tầm xa | `crest_5_cuu_u_tong.png` |
| 6 | **Truy Nguyệt Các** *(Thay Truy Hồn Cốc)* | Cung Tiễn · Tầm xa | `crest_6_truy_nguyet_cac.png` |

Lưu ý hiển thị trên thẻ chọn môn phái:
- Giữ `image-rendering: pixelated` / `Nearest Neighbor` để nét pixel đồng cổ sắc cạnh.
- Với các môn phái đang ở trạng thái khóa (`🔒`), giảm nhẹ độ sáng (`filter: brightness(0.55) saturate(0.75)`) thay vì tô bệt một màu tối để người chơi vẫn nhìn thấy rõ chi tiết vũ khí đặc trưng của từng phái; khi đang được chọn (viền vàng sáng), hiển thị `brightness(1.08)` kèm bóng đổ đen nhẹ `drop-shadow(0 4px 8px rgba(0,0,0,0.65))`.
