# Tây Du Sinh Tồn · Tổng hợp tính năng và quyết định

Đây là game hành động cổ trang 2D với nhân vật tăng lực chiến qua nhiều ải, trang bị, cường hóa và võ học. Vũ khí quyết định bộ chiêu. Người chơi giữ phát triển lâu dài và có thể thử lại từ checkpoint khi thua. Tu luyện trong ải cho sức mạnh tạm thời.

## 1. Tình trạng hệ thống

| Hệ thống | Tình trạng trong ZIP | Thiết kế và việc còn lại |
|---|---|---|
| Tạo nhân vật | Kiếm của nhân vật nam đã dài thêm ~30% trên toàn sheet (22/11). Có tên, nam/nữ, xem vũ khí và lựa chọn tóc. Kiếm là vũ khí mở để chơi. Tóc và màu chỉ mở khi có sprite. | Vũ khí dự kiến gồm Kiếm, Côn, Thương, Đao, Phù Chú. Trang bị và võ học gắn với vũ khí. Đổi loại vũ khí sau tạo nhân vật để sau vì mỗi loại cần chuyển động riêng. Cần thêm tóc, màu tóc và tranh minh họa. |
| Sảnh và cấp lâu dài | Có hồ sơ, cấp, kinh nghiệm, thanh thể lực dưới cấp, Vượt Ải, tiếp tục ải, kho, Điểm Tâm, Luyện Đan, Luyện Vũ Khí và Chiêu Mộ thử nghiệm. | Mở dịch vụ online ở giai đoạn sau. Kiểm tra bố cục trên Safari iPhone thật. |
| Tuyến ải và sao | Tuyết Sơn có 5 ải, ải cuối là Ngưu Ma Vương. Có sao 1–5, mở sao kế khi vượt trùm, thanh nhiệm vụ và mục tiêu săn. | Các map có thể dài 5, 7 hoặc 9 ải. Dùng chung cấu trúc bảng rơi. Sao 2/4 tăng áp lực và thưởng, sao 3/5 có thay đổi lớn. Bản thử: tinh anh từ ★3 có Cương Khí, boss ★5 có pha 2 dưới 50% máu. |
| Rẽ đường và kèo boss | Có chọn Ven núi hoặc Trại cướp sau ải 2. Ven núi dễ hơn và có Suối Ấm. Trại cướp thêm tinh anh và cơ hội Tuyết Sâm. Phá hai cột băng trước boss ngã cho thêm một lượt roll dược liệu. | Dùng làm mẫu khi mở tuyến khác. |
| Nghỉ giữa ải | Có Kết toán, Tu luyện, Trang bị, Võ học, Tạp hóa. Mặc đồ, xem chiêu, mua thuốc và chọn thẻ tại chỗ. | Cho thấy tiến độ và tài nguyên cần thiết, giữ nút Tiếp tục dễ bấm. Thẻ tu luyện chỉ có hiệu lực trong tuyến hiện tại. |
| Checkpoint | Có tiếp tục từ sảnh, giữ lựa chọn đường, thẻ, tiền, thuốc và trạng thái ải. Có nút thử lại chính ải vừa thua. Rương có ghi nhận để tránh nhận hai lần khi tải lại. | Kiểm thử hồi quy khi sửa giao diện nghỉ, kho, thưởng và lưu game. |
| Vật phẩm, nhiệm vụ, kỳ ngộ | Có vật phẩm nhặt trong trận, bình/thùng/rương phá được, bẫy, bảng nhiệm vụ và hệ kỳ ngộ NPC, thương nhân, kẻ cướp, Sơn Trại/Hổ Huyệt. | Chi tiết và các thông số ban đầu xem hồ sơ chặng cũ. Kiểm thử lại khi chỉnh tỷ lệ rơi hoặc thêm tuyến. |
| Rương boss và tiến trình | **Đang chạy:** hạ boss hoàn thành ải/mở sao kể cả khi không đủ thể lực; rương nhận thưởng tốn 15 thể lực, bảo đảm 4 Huyền Thiết + lượt dược liệu, có tỷ lệ trang bị/bí tịch tăng theo sao; lần đầu nhận Truy Phong Kiếm. | **Đã chốt, CHƯA triển khai:** khi thiếu thể lực, giữ một rương chờ nhận hợp lệ thay vì bỏ qua là mất thưởng; nhận sau khi đủ 15 thể lực, không cần đánh boss lại; chống nhận trùng/farm vô hạn không tốn thể lực. Giữ tỷ lệ thưởng ★1–★5 hiện có. Bí tịch trùng cần công dụng khi mở hệ nâng cấp bí tịch; kinh tế/phẩm đá cân sau. |
| Trang bị và kho | **Đang chạy:** 6 ô (Vũ khí, Y phục, Hài, Hộ phù, Nhẫn/Bội ngọc, Đai/Găng tay), so/mặc đồ, phân giải, kho 120 món và hàng chờ, bảo vệ đồ đang mặc. | **Đã chốt, CHƯA triển khai:** thêm ô thứ 7 là **Nón** (trang bị riêng), có nút **Ẩn/Hiện Nón** chỉ tác động phần hình ảnh; khi ẩn vẫn mặc Nón và hưởng đủ chỉ số. Cần UI, asset Nón, hệ hiển thị Nón cho nhân vật nam/nữ và kiểm tra lưu game cũ. |
| Cường hóa | Đang chạy +0 đến +9 cho 6 ô hiện tại, rủi ro rớt cấp từ +5, hư hỏng ở +8/+9; món hỏng giữ lại để sửa. Có đọc đồ cũ và báo mốc lần đầu. | **Đã chốt cho thiết kế mới:** Vũ khí +3 tăng chỉ số ẩn, +6 mở đòn C, +9 tăng hiệu ứng/sát thương/phạm vi tùy loại. Trang bị +3/+6 tăng chỉ số; +9 tăng chỉ số hoặc passive/buff phòng ngự theo món. Thêm Nón thứ 7 theo quy tắc chung, chỉ số riêng chưa chốt. Không tự đổi các chỉ số đã ghi ở bảng; kinh tế/phẩm đá còn chờ cân. |
| Đòn thường Kiếm | **Hiện trạng code (23/11):** có cơ chế liên kích A–B, kiếm +6 mở đòn C và hiệu ứng đi kèm, nhưng animation/VFX đang dùng thuộc **phiên bản cũ**. Mốc +3 xuyên 5% giáp cho đòn thường. | **ĐÃ CHỐT: LOẠI BỎ BỘ TƯ THẾ CHÉM A–B–C CŨ khỏi định hướng sản xuất.** Không dùng demo C Lướt Trảm, chuỗi pose A/B/C cũ hay thông số chuyển động cũ làm chuẩn mới; **chưa có bản animation A–B–C thay thế được duyệt**. Giữ ý nghĩa cơ chế: Kiếm +6 mở đòn C, +9 thêm hiệu ứng hoặc sát thương sau C. Đề xuất/duyệt concept động tác mới riêng trước khi triển khai; **không hiểu quyết định loại pose là lệnh xóa code combo A–B–C hiện đang chạy**. |
| Kỹ năng Kiếm | Kiếm Khí Trảm (Q), Hoành Tảo (F), Vạn Kiếm Quy Tông (X) chủ động. Vạn Kiếm chọn vùng đặt mưa kiếm. Kiếm Ảnh là ba kiếm tự xoay quanh người, có vòng hồi. Có nội tại Kiếm Tâm. | Chủ động nhìn rõ nút dùng. Tự kích hoạt hiển thị vòng hồi riêng. Bấm xem chú thích thuốc và kỹ năng, gồm sát thương đơn/diện, hiệu ứng, hồi chiêu, nội lực và số lượng thuốc tùy mục. |
| Lướt và bí tịch | Có Lướt và hủy nhát đang lấy đà. Có bí tịch cộng chỉ số vĩnh viễn và biến thể Truy Phong Kiếm, Hồi Phong. Truy Phong dùng được từ +0 và biến đổi nhát đầu sau Lướt. Hồi Phong ảnh hưởng Hoành Tảo sau Lướt. Chọn một bí tịch Lướt mang theo. | Tối đa một ô bí tịch chủ động ở giai đoạn thử, chưa xác nhận ô riêng trong bản đóng gói. Ưu tiên thay đổi cách dùng một chiêu; có thể thử tăng tốc ngắn hoặc thêm dư ảnh Lướt. Dịch chuyển xuyên địa hình và nhiều biến thể đồng thời để sau. |
| Luyện đan | Tinh anh và boss cho đường lấy Tuyết Sâm/Băng Tâm Liên. Có Cuồng Huyết Đan dùng tạm trong ải và Trúc Cơ Đan vĩnh viễn giới hạn trong bản thử. Có Hộ Thể Đan giải trạng thái. | Định hướng bản đầu ưu tiên đan dùng trong ải. Trúc Cơ Đan hiện vẫn tồn tại trong code (+20 HP/viên, một lượt dùng mở theo mỗi sao đã vượt, tối đa 5). Để chủ game chốt phần thử này trước khi mở rộng; bỏ hướng làm nhiều đan cộng vĩnh viễn nhiều chỉ số. |
| Hóa Thân và Chiêu Mộ | Có Hóa Thân dùng Nộ, vòng Nộ trong nút Hóa Thân. Có Chiêu Mộ local để thử thần tướng và đổi mảnh từ bản trùng. | Chiêu Mộ chính thức để sau solo. Bản thử bắt đầu với Tôn Ngộ Không; giá, tỷ lệ và đổi mảnh còn để cân trước khi mở online. |
| HUD và cảnh báo | Avatar hiển thị, viền nút Hóa Thân lục giác. Khí huyết và Nội lực ở dưới, EXP tím và tiến độ đợt vàng. Hạ gục và Liên kích riêng. Quái thường ẩn HP, tinh anh có HP trên đầu, boss có thanh riêng trên cùng. | Máu dưới 30% có trạng thái cảnh báo; vừa xuống dưới 20% nháy viền 2 giây rồi giữ đỏ nhẹ. Kiểm tra đọc được máu khi đông quái và trên màn nhỏ. |
| Liên kích | Có đếm tụt dần khi ngừng đánh, lớp màu đen đi qua chữ số và thưởng theo mốc. Bản hiện tại giữ 2,2 giây rồi tụt trong 2,4 giây. | Mốc 25 tích Nộ nhanh hơn 5%, 100 thêm 4 điểm phần trăm chí mạng, 300 thêm 5% sát thương. Thưởng mất theo mốc khi tụt. Đây là phần Claude đã sửa, ưu tiên giữ hành vi hiện tại. |
| Hướng dẫn lần đầu | Có luồng đi, đánh, Lướt và nối đòn. Ghi nhận để lần sau không lặp. Tạm dừng khi chờ xác nhận, có spotlight vào nút Lướt ở bước tương ứng. | Giữ nguyên tắc chỉ hiện ở lần đầu và chiếu đúng ô cần thao tác. Mở rộng có chọn lọc cho Hóa Thân, thuốc, nghỉ giữa ải và rèn nếu bổ sung hướng dẫn mới. |
| Màn hình điện thoại | Có chặn dọc, hiện yêu cầu xoay ngang và dừng chạy trận khi đang dọc. Chặn tự thu phóng khi chạm/chạm đúp/chụm ngón trên vùng chơi (22/11). | Xác nhận trên iPhone/Safari thật và trường hợp mở link trong app chat. |
| Hiệu ứng và chuyển động | Game còn đang chứa hoạt ảnh/VFX Kiếm A–B–C ở phiên bản cũ; có video demo lịch sử. | **Bộ tư thế Kiếm A–B–C cũ bị loại khỏi kế hoạch tiếp tục**, không dùng để duyệt master. Khi dựng bộ mới phải có concept được duyệt, khóa sprite/master nam nữ, kiểm đồng bộ vũ khí, chân trụ, chuyển hướng và hit timing; xuất clip thật/chậm để QA. Không tự thay code game trước khi chủ game giao làm. |

## 2. Các thông số thử quan trọng

### Thể lực và phần thưởng

- Thể lực thường tối đa 100, hồi 1 điểm mỗi 15 phút. Điểm Tâm lúc 07:00, 14:00 và 21:00 giờ Việt Nam, cửa sổ 2 giờ, bấm bánh bao 5 lần để nhận tối đa 15 thể lực cho khung, trần điểm tâm 115.
- **Hiện có:** rương boss tốn 15 thể lực; bảo đảm 4 Huyền Thiết + một lượt dược liệu (+1 lượt nếu hoàn thành kèo phụ); tỷ lệ bí tịch từ ★1 đến ★5 là 6%, 8%, 10%, 12%, 15%; thưởng rương lần đầu mở Truy Phong Kiếm. Tỷ lệ/trọng số phẩm và số món giữ theo `CHEST_T`.
- **Đã chốt, chưa code:** nếu thắng boss nhưng thiếu 15 thể lực, ghi nhận hoàn thành ải/mở sao và lưu **một quyền nhận rương đang chờ** cho chiến thắng hợp lệ, không nhận vật phẩm ngay. Khi đủ 15 thể lực, người chơi có thể nhận rương mà không phải đánh lại; tiêu hao thể lực **tại lúc nhận**. Lưu trạng thái nhận/chưa nhận bền vững; chống nhận lặp, sao chép và farm vật phẩm/tài nguyên vĩnh viễn không tốn thể lực. Không để nút Bỏ qua làm mất quyền nhận rương đang chờ.
- Thưởng lần đầu tách khỏi thưởng farm; giữ nguyên bảng roll theo sao hiện hành. Bí tịch trùng sẽ có công dụng khi triển khai hệ nâng cấp bí tịch (chưa chốt công thức/chỉ số), không tự thêm tỷ lệ mới.
- Cuồng Huyết Đan cộng 25% sát thương trong 45 giây, mang tối đa 5, luyện từ 3 Tuyết Sâm. Hộ Thể Đan giải độc/choáng/chậm và miễn trạng thái tương ứng 60 giây. Trúc Cơ Đan hiện tốn 2 Tuyết Sâm + 1 Băng Tâm Liên.

### Ô trang bị Nón thứ 7 — ĐÃ CHỐT, CHƯA TRIỂN KHAI

- Thêm ô **Nón** độc lập, nâng tổng ô trang bị từ **6 lên 7** khi triển khai; 6 ô cũ giữ nguyên, không thay thế hoặc gộp ô nào.
- Trong giao diện Trang bị/Kho, có nút **Ẩn/Hiện Nón** (biểu tượng con mắt hoặc nút chữ rõ ràng). **Ẩn chỉ tắt hình Nón trên nhân vật**, không tháo vật phẩm; toàn bộ chỉ số, độ cường hóa và hiệu ứng của Nón vẫn có tác dụng. Nút bấm lại để hiện Nón.
- Mặc định khi trang bị Nón mới: **hiện hình Nón**; lựa chọn ẩn/hiện do người chơi đổi được lưu theo hồ sơ và tồn tại sau khi thoát/vào game. Khi chưa có Nón, không hiển thị vật thể trên đầu.
- Nón cần được gắn đúng vùng đầu theo sprite/animation nam và nữ, kể cả khi chạy/đánh/trúng đòn và khi đổi Y phục; không làm biến dạng Master, không để Nón giật hoặc che sai khuôn mặt. Kỹ thuật layer và xử lý tóc phải thử nghiệm/duyệt bằng hình trước khi sản xuất.
- Thêm Nón vào rương, trang bị, kho, mặc/tháo, so chỉ số, phân giải, cường hóa và dữ liệu lưu theo cùng nguyên tắc chung, **nhưng chưa được tự chốt chỉ số, tên vật phẩm, bonus mốc +3/+6/+9 hoặc tỷ lệ rơi riêng của Nón**. Phải bảo toàn save cũ 6 ô.
- **Đây là thiết kế được chủ game chốt ở cấp tài liệu; code hiện tại vẫn chỉ có 6 ô.** Không ghi là đã làm.

### Cường hóa

| Mốc muốn lên | Thành công | Giữ cấp | Rớt 1 cấp | Hư hỏng | Huyền Thiết (đề xuất mới) | Nguyên liệu phụ (đề xuất) |
|---|---:|---:|---:|---:|---:|---|
| +1 / +2 | 100% | 0% | 0% | 0% | 1 / 1 | Không |
| +3 / +4 | 80% | 20% | 0% | 0% | 2 / 2 | Không |
| +5 | 50% | 40% | 10% | 0% | **4** | Không |
| +6 | 40% | 50% | 10% | 0% | **5** | Không |
| +7 | 25% | 55% | 20% | 0% | **7** | Không |
| +8 | 15% | 59% | 20% | 6% | **10** | **1 Tinh Hoa Rèn** (tên tạm) |
| +9 | 8% | 56% | 25% | 11% | **14** | **2 Tinh Hoa Rèn** (tên tạm) |

**ĐÃ CHỐT THIẾT KẾ, CHƯA SỬA CODE GAME (23/11/2026):** Tỷ lệ thành công +1/+2 = 100%; +3/+4 = 80%; **+5 = 50%; +6 = 40%; +7 = 25%; +8 = 15%; +9 = 8%**. Các cột thất bại chưa được chủ game chốt lại: bảng tạm **giữ nguyên xác suất rớt cấp và hư hỏng cũ**, phân bổ phần chênh lệch vào tỷ lệ *Giữ cấp* để mỗi dòng đủ 100%. **Đã chốt hướng tăng tiêu hao Huyền Thiết ở +5 đến +9 và thêm nguyên liệu phụ ở +8/+9. Số lượng 4/5/7/10/14 cùng tên tạm `Tinh Hoa Rèn` (1 ở +8, 2 ở +9) là ĐỀ XUẤT ĐỂ DUYỆT, KHÔNG PHẢI SỐ ĐÃ CHỐT.** Phải chốt nguồn rơi nguyên liệu phụ, tỷ lệ rơi và cân kinh tế trước khi sửa code.

Mỗi cấp tăng 4% chỉ số gốc. Sửa tốn 3 Huyền Thiết và đưa món về +0. Thưởng mốc lấy mốc cao nhất trên từng món.

| Ô | +3 | +6 | +9 |
|---|---|---|---|
| Kiếm | Đòn thường bỏ qua 5% giáp | Mở nhát C | Thêm hiệu ứng hoặc sát thương sau C |
| Y phục | +4 HP | +6 HP | +8 HP |
| Hài | Giảm hồi Lướt 3% | 4,5% | 6% |
| Hộ phù | +0,25 Nội lực/giây | +0,375 | +0,50 |
| Nhẫn/Bội ngọc | +1 điểm % chí mạng | +1,5 | +2 |
| Đai | +3 HP | +4,5 HP | +6 HP |
| Găng tay | +2% tốc độ đòn thường | +3% | +4% |


**Quy tắc chung đã chốt cho các loại vũ khí và trang bị (23/11/2026; định hướng thiết kế, chưa cập nhật code):**
- **Vũ khí:** +3 tăng **chỉ số ẩn** phù hợp lối đánh của từng loại vũ khí (ví dụ Kiếm xuyên 5% giáp như bảng); +6 **mở đòn thường C**; +9 **nâng cấp hiệu ứng, sát thương hoặc phạm vi tấn công** tùy bộ chiêu của từng loại vũ khí. Game thiết kế theo **vũ khí**, không chia class/môn phái cố định. Không ép mọi loại vũ khí dùng cùng một hiệu ứng +9.
- **Trang bị không phải vũ khí:** +3 và +6 tăng chỉ số; +9 **tăng chỉ số, hoặc nâng cấp passive/phòng ngự, hoặc cấp buff phòng ngự**, tùy món. Các con số trong bảng trên là **mốc chỉ số tham chiếu hiện có**; không tự thay bằng passive/buff mới khi chưa có thiết kế chi tiết được duyệt. Hệ Nón thứ 7 phải tuân theo cùng quy tắc, nhưng phần thưởng cụ thể chưa chốt.
- Các mức thưởng +3/+6/+9 là **mốc cường hóa**; chỉ áp dụng theo cấp đang đạt của món và nguyên tắc cộng dồn/không cộng dồn phải được định nghĩa rõ khi triển khai. Mọi thay đổi gameplay cần kiểm tra cân bằng với thẻ Tu luyện, bí tịch và trang bị.

### Hệ phẩm Hóa Thân và số lượng kỹ năng — ĐÃ CHỐT S/SS/SSS/UR (24/11/2026), CHƯA CẬP NHẬT CODE

- Định hướng mới từ chủ game: **C chỉ dùng làm phôi Hóa Thân**; các phẩm chiến đấu/sưu tầm chính là **A, S, SS, SSS, UR**. **B không thuộc thang phẩm mới được đề xuất.** Chưa chốt cách chuyển dữ liệu C hiện có (Thổ Địa đang là C và đánh được), không xóa Hóa Thân đang chạy trước khi có phương án chuyển hồ sơ.
- **S:** đúng **2 kỹ năng chủ động + 1 bị động**.
- **SS:** đúng **3 kỹ năng chủ động + 1 bị động**.
- **SSS:** đúng **3 kỹ năng chủ động + 2 bị động**.
- **UR:** đúng **4 kỹ năng chủ động + 2 hoặc 3 bị động** (tùy từng Hóa Thân, chưa chốt tiêu chí chọn 2 hay 3).
- **Đòn đánh thường tách riêng**, không tính vào số kỹ năng trên. **Phẩm A chưa được chủ game chốt số kỹ năng**. Vị trí của **tuyệt kỹ** (có tính là một chủ động hay là chiêu riêng) **chưa chốt**, không tự mở thêm ô kỹ năng trước khi xác định.
- Danh sách dự kiến 50 Hóa Thân (20 A / 13 S / 9 SS / 5 SSS / 3 UR) là **phương án để duyệt**, không phải danh sách đã khóa. Chủ game đang cân nhắc bổ sung thần thú và thần linh **Sơn Hải Kinh** như Ứng Long, Chúc Long, Tây Vương Mẫu, Hình Thiên, Đế Tuấn; phẩm và số lượng thực tế sẽ chốt sau.
- **Chưa được tự sửa gameplay:** `GODS` trong `game/index.html` hiện mới có Ngộ Không (SSS), Na Tra (SS), Bát Giới (S), Thổ Địa (C). Các bộ đang chạy có thể chưa khớp số kỹ năng mới, cần lập bảng thiếu/thừa và phương án cập nhật sau khi chủ game giao task.

## 3. Các hệ thống để sau

| Tính năng | Quy tắc đã bàn | Phần còn cần quyết định |
|---|---|---|
| Raid 3–4 người | Ai đủ điều kiện tranh loot có xác suất ngang nhau. Cần có mặt trong map khi boss chết và đóng góp ít nhất 15% máu tối đa của boss theo bản chốt lưu lại. Sát thương cao hơn ngưỡng hoặc sống lâu hơn không tăng xác suất. | Kiểm tra khả năng đáp ứng của vai trò hỗ trợ và cách tính đóng góp. Chốt bảng loot khi có dữ liệu solo. |
| Cứu đồng đội | Lại gần người gục để hiện nút Cứu. Bấm cứu và đứng yên 5 giây; hủy nếu di chuyển, ra chiêu hoặc nhận sát thương. | Bán kính, trạng thái khi vừa được cứu, giới hạn số lần và xử lý mất kết nối. |
| Đấu giá | Có đường bán món lệch giới hoặc khác vũ khí nhận từ rương. | Luật giao dịch, phí, phạm vi món được giao dịch và xác nhận số dư trên máy chủ. |
| PvP | Lực chiến dùng để vào nội dung và xét ghép trận. | Cân riêng sau khi có dữ liệu Kiếm +6/+9 đánh boss solo. |
| Bang Hội | Có ô trong sảnh. | Tính năng online để sau, chưa có máy chủ. |
| Chiêu Mộ chính thức và event cuối tuần | Chiêu Mộ mở Hóa Thân; trùng đổi mảnh. Event cuối tuần để sau. | Tỷ lệ và lịch chính thức. |
| Ý tưởng chưa chốt | Đàn cầu phúc, thành tựu, nhiệm vụ ngày, bảng xếp hạng, set đồ, thêm boss và cốt truyện. Lò Rèn thử đòn là đề xuất để duyệt. | Chỉ đưa vào sprint khi chủ game chọn. |

## 4. Thứ tự làm tiếp và cách nghiệm thu

1. **Loại các tư thế Kiếm A–B–C cũ khỏi kế hoạch sản xuất** (không xóa code hiện tại). Phác thảo bộ combo mới theo Master nam/nữ để chủ game duyệt; KHÔNG dùng demo `demo/nhat_c/` hay logic nhát C Lướt Trảm cũ làm chuẩn cho animation mới.
2. Sau khi được duyệt mới triển khai animation/VFX A–B–C mới, kiểm tra +0/+3/+6/+9, hướng chém, đúng tay cầm và socket, đồng bộ điểm chạm/hitbox và nối đòn; giữ chức năng các kỹ năng khác không bị ảnh hưởng. Đồng thời chốt số lượng Huyền Thiết mới +5 đến +9, vật liệu phụ +8/+9 và nguồn kiếm nguyên liệu trước khi sửa hệ cường hóa.
3. Chạy lại luồng tạo nhân vật → sảnh → ải → nghỉ → checkpoint → boss → rương → cường hóa. Khi triển khai: kiểm lưu/nhận rương chờ nếu thiếu thể lực, không mất thưởng và không nhận trùng; kiểm Nón thứ 7 (Ẩn/Hiện không mất chỉ số, hoạt ảnh nam/nữ, save cũ). Test HUD máu thấp, mô tả kỹ năng/thuốc, Vạn Kiếm ngắm vùng, hướng dẫn lần đầu, Liên kích và xoay ngang. Dùng một lượt hồ sơ mới và một lượt hồ sơ cũ.
4. Cân vòng solo trước. Sau đó mới triển khai tính năng cần tài khoản, máy chủ, sổ giao dịch, Raid/PvP và bảng rơi chính thức.

Hồ sơ cũ ghi kết quả kiểm thử tại thời điểm từng chặng. Tình trạng trong tài liệu này dựa trên code bản đóng gói và hồ sơ bàn giao; những tư thế A–B–C và demo Lướt Trảm cũ chỉ là lịch sử, đã bị loại khỏi phương án sản xuất mới. Safari iPhone thật, cân bằng dài hạn và combo Kiếm mới vẫn cần kiểm thử trực tiếp.
