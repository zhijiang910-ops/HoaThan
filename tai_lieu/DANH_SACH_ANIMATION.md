# Bộ animation làm lại · nhân vật chính (nam + nữ)

Mục tiêu: một bộ hoạt ảnh thống nhất cho mỗi nhân vật. Kiếm luôn rút, cầm cùng một tay, cùng một kiểu cầm khi đứng, chạy và đánh. Không còn chuyện chạy thì giấu kiếm, đứng lại thì kiếm hiện ra.

## Cách làm trên PixelLab (khuyến nghị)

1. Dựng **1 nhân vật gốc** từ `hero_xxx_MASTER.png`: quay sang phải, đứng thủ, kiếm cầm tay trước, chuôi ngang hông, mũi chĩa chéo xuống trước. Duyệt kỹ bản gốc này trước, mọi animation sau đều dựng từ nó.
2. Từ nhân vật gốc, tạo từng animation theo bảng dưới. Dùng chức năng tạo dáng bằng khung xương nếu có, nhưng **chỉ xuất frame PNG**, không xuất file rig.
3. Một nhân vật dùng **một cỡ canvas cố định** cho mọi animation. Chân trụ luôn đặt cùng một điểm.
4. Không vẽ hiệu ứng (vệt chém, bụi, tia sáng), không đổ bóng. Game tự vẽ phần này.

## Cỡ khung

- Nên dùng canvas vuông 128×128 trở lên. Nhân vật cao khoảng 90–100 px (tính cả búi tóc hoặc đuôi ngựa). Chân trụ ở khoảng (55, 118).
- Chừa chỗ phía trước mặt cho kiếm: tư thế đâm thẳng cần khoảng 70 px tính từ thân ra mũi kiếm.
- Nếu PixelLab chỉ cho canvas nhỏ hơn thì cứ làm, tao sẽ phóng và căn lại. Chỉ cần mọi frame cùng cỡ.

## Danh sách (theo thứ tự ưu tiên)

| # | Tên trong game | Số frame | Nhịp | Lặp | Nội dung |
|---|---|---|---|---|---|
| 1 | `idle` đứng thủ | 4 | 6 fps | có | Thở nhẹ, vai nhún, tóc và vạt áo đung đưa. Kiếm đứng yên đúng kiểu cầm gốc. |
| 2 | `run` chạy | 8 | theo tốc độ (~16 fps) | có | Chạy nhanh, thân ngả trước ~15°, kiếm giữ kiểu cầm gốc, chỉ nhún theo bước. Chân trụ lùi dần về sau. |
| 3 | `attack` chém A | 6 | ~15 fps (0,4 s) | không | 1 lấy đà: giơ kiếm cao sau vai · 2 bắt đầu bổ · **3 kiếm giữa đường chém (chạm địch)** · 4 kiếm hết đường, thân cúi theo · 5 giữ thế · 6 về gần tư thế thủ. |
| 4 | `attack2` chém B | 6 | ~15 fps | không | Nối từ cuối A: 1 kéo kiếm thấp ra sau hông · 2 xoay người · **3 chém ngang mạnh (chạm địch)** · 4 kiếm hết đường lên cao trước mặt · 5 giữ · 6 về thủ. |
| 5 | `cutC` lướt đâm (kiếm +6) | 6 | theo code | không | 1 lấy đà hạ thấp, kiếm kéo sau hông · 2 bật đi · **3 lướt đâm, thân gần nằm ngang, kiếm chĩa thẳng** · 4 như 3, đổi nhịp chân · 5 chạm đất phanh, gối trước khuỵu · 6 đứng dậy vẩy kiếm về thủ. |
| 6 | `dash` lướt né | 3 | 15 fps | có | Thân thấp lao về trước, kiếm giữ sát người. |
| 7 | `hit` trúng đòn | 3 | 12 fps | không | Giật người ra sau, kiếm vẫn cầm. |
| 8 | `death` gục | 4 | 6 fps | không | Khuỵu gối → ngã nằm, kiếm rơi cạnh người. |
| 9 | Tranh sảnh | 1 | – | – | Nửa người hoặc toàn thân, khổ dọc 600×800, tư thế oai. |

Tổng cho mỗi nhân vật khoảng 40 frame. Nên làm theo cặp: xong idle và run thì gửi tao ghép thử, duyệt xong rồi mới làm các đòn đánh.

## Yêu cầu chung để ghép mượt

- Frame cuối A nối được vào frame đầu B, frame cuối B nối được về idle.
- Kiểu cầm kiếm ở frame đầu và frame cuối của mọi đòn phải trùng với idle.
- Mọi frame giữ đúng màu và chi tiết trong bảng master. Không tự thêm hay bớt phụ kiện, dải lụa, hoa văn.
- Gửi tao file PNG từng frame hoặc 1 dải ngang, đặt tên theo animation, ví dụ `nu_run_01..08.png`.
