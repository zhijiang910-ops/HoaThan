# Nhờ ChatGPT vẽ nền map Âm Giới ĐÚNG CỠ GAME (1:1) cho nét hơn

**Vì sao:** nền map hiện là ảnh 1600×1140 phóng ×2 lên 3200×2280, nên mỗi pixel nền to gấp đôi pixel nhân vật (nhìn thô). Muốn nét bằng nhân vật thì cần ảnh 3200×2280 thật, ChatGPT chỉ xuất tối đa 1600×1140 nên chia làm 4 góc.

**Chi phí trong game:** mỗi map 1:1 nặng ~2,5–3 MB (bản ×2 hiện tại ~0,9 MB), chỉ tải khi vào map đó. Nên thử 1 map trước (đề xuất Hoàng Tuyền, tầng 1–2, chơi nhiều nhất), xem có đáng không rồi mới làm các map còn lại.

**Ảnh mẫu đã cắt sẵn:** `nguon/master_amgioi/map_1to1/<map>/goc_{1_trai_tren,2_phai_tren,3_trai_duoi,4_phai_duoi}_800x570.png` (cắt từ chính nền đang dùng trong game `game/assets/map/bg_<map>.png`, file này là bố cục tổng thể). Map: hoangtuyen, quanmon, biangan, nghiepkinh, uongtu, vongxuyen, diemla.

## Lần 1: GÓC TRÁI TRÊN (dán từ đây, đính kèm `bg_<map>.png` + `goc_1_trai_tren_800x570.png`)

Tôi làm game pixel art nhìn chếch từ trên xuống. Ảnh `bg_<map>.png` là bố cục tổng thể của map, ĐÃ DUYỆT. Ảnh `goc_1_trai_tren_800x570.png` là góc trái trên của bố cục đó.

Hãy **vẽ lại góc này với chi tiết gấp đôi**, xuất **đúng 1600×1140 px**. Giữ nguyên bố cục, vị trí từng vật, màu sắc, ánh sáng và phong cách; chỉ vẽ lại ở độ phân giải gấp đôi (mỗi vật thêm chi tiết, thêm pixel).

Bắt buộc:
- **Pixel art thật 1:1**: mỗi pixel là ô vuông 1×1 px, không khử răng cưa, không làm mịn, KHÔNG phóng to ảnh nhỏ (không được có khối 2×2 cùng màu hàng loạt), tối đa 96 màu.
- Không chữ, không nhân vật, không UI, không nền trong suốt, không viền.
- **Mép phải và mép dưới là địa hình mở** để nối với góc kế bên; vật lớn nằm vắt qua mép thì phải tiếp tục đúng ở góc kia.

## Lần 2–4: GÓC PHẢI TRÊN, TRÁI DƯỚI, PHẢI DƯỚI

Cùng yêu cầu, thay ảnh góc tương ứng, và thêm:
- Đính kèm các góc đã vẽ xong nằm kề bên. **Dải 24 px sát mép chung phải khớp từng pixel** với góc kề (cùng địa hình, cùng vị trí đường/cầu/sông, cùng màu).
- Phần giữa map (góc trong của cả 4 ảnh) là sân đánh: giữ thoáng, không thêm vật nổi bật.

## Sau khi nhận 4 ảnh (việc của Claude)
1. Kiểm cỡ 1600×1140, số màu, tỉ lệ khối 2×2 (<0,3 là pixel thật), độ lệch ở đường nối.
2. Lưu 4 mảnh `game/assets/map/bg1_<map>_{tl,tr,bl,br}.png` (PNG bảng màu), khai báo `M.bgq` (code vẽ 4 mảnh 1:1 đã có sẵn), bỏ `M.bg` của map đó.
3. Dời lại ánh sáng/vùng làm chậm nếu vị trí đèn lệch; chạy `pack_check.sh`, chụp so sánh trước/sau.
