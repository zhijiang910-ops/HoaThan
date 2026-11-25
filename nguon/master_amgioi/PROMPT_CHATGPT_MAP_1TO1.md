# Prompt: vẽ lại map Vong Xuyên ĐÚNG CỠ GAME (1:1), 4 góc 1600×1140

Mục tiêu: map game rộng 3200×2280 px, mỗi pixel art = 1 px màn hình ở độ phóng gốc, nên nhân vật và nền cùng mật độ pixel. Chủ game xác nhận ChatGPT xuất được đúng 1600×1140 px. Ta chia map thành 4 góc 1600×1140, ghép lại bằng code.

**Đính kèm cho mỗi lần:** `tong_the_1600x1200.png` (bố cục tổng thể, ĐÃ DUYỆT, đây là nguồn sự thật) + ảnh góc tương ứng `goc_*_800x600.png` + (từ góc thứ 2) các góc đã vẽ xong kề bên.

## Lần 1: GÓC TRÁI TRÊN (dán từ đây)

Tôi làm game pixel art nhìn chếch từ trên xuống. Ảnh `tong_the_1600x1200.png` là bố cục map tổng thể đã duyệt (sông ngang phía trên, cầu đá bắc dọc ở giữa, thuyền, bến gỗ, liễu, quán canh Mạnh Bà, đất trống phía dưới).

Hãy **vẽ lại góc TRÁI TRÊN** (ảnh `goc_1_trai_tren_800x600.png`, tức nửa trái-nửa trên của bố cục) với **chi tiết gấp đôi**: xuất **đúng 1600×1140 px**. Giữ nguyên bố cục, vị trí vật, màu sắc, phong cách của ảnh gốc, chỉ vẽ lại ở độ phân giải gấp đôi (mỗi vật chi tiết hơn, nhiều pixel hơn). Hơi kéo giãn chiều dọc 5% là được.

Yêu cầu bắt buộc:
- **Pixel art thật 1:1**: mỗi pixel là một ô vuông 1×1 px, không khử răng cưa, không làm mịn, không phóng to ảnh nhỏ (không được có khối 2×2 cùng màu hàng loạt), tối đa 96 màu.
- Không chữ, không nhân vật, không UI. Ảnh chữ nhật đầy đủ, không nền trong suốt, không viền.
- **Mép phải và mép dưới của ảnh phải là địa hình "mở"** để nối tiếp được với góc kế bên: đừng cắt ngang một vật lớn ở mép trừ khi vật đó tiếp tục sang góc kia (cầu ở giữa map sẽ nằm vắt qua mép phải của góc này và mép trái của góc phải).
- Tự kiểm sau khi xuất: kích thước, số màu, tỉ lệ khối 2×2 cùng màu (dưới 0.3 là pixel thật).

## Các lần sau (GÓC PHẢI TRÊN, TRÁI DƯỚI, PHẢI DƯỚI)

Cùng yêu cầu như trên, thay `goc_*` tương ứng, và thêm:
- Đính kèm các góc đã vẽ xong kề bên. **Cột pixel ngoài cùng của ảnh mới phải KHỚP từng pixel với cột/hàng pixel ngoài cùng của ảnh kề** (cùng địa hình, cùng vị trí cầu/sông/đường, cùng màu), rộng ít nhất 24 px; chi tiết sau đó phát triển tự do.
- Góc phải trên: tiếp từ mép phải của góc trái trên (phần nửa phải của cầu, liễu, quán Mạnh Bà).
- Góc trái dưới và phải dưới: phần lớn là đất trống để chiến đấu, rải rác sậy, đá, hoa bỉ ngạn ở rìa; **không đặt vật nổi bật ở phần giữa** (tôi sẽ thêm quái và ánh sáng). Rìa ngoài cùng của map (hai bên và đáy) tối dần như cũ.

## Sau khi nhận 4 ảnh (việc của Claude)
1. Kiểm kích thước, số màu, khối 2×2, và độ lệch ở các đường nối (cột/hàng giữa hai góc).
2. Ghép thành 3200×2280, nếu nối lệch thì hòa mép 16–24 px (bằng code), hoặc chọn đường nối đi qua chỗ đất trống.
3. Thay `bg_vongxuyen.png` (hiện phóng ×2, thô) bằng ảnh 1:1; giữ ánh sáng, đom đóm, vùng làm chậm trong sông.
4. Ảnh nặng ~7 Mpx: tách 4 mảnh tải riêng để không quá 15 Mpx một ảnh trên điện thoại.
