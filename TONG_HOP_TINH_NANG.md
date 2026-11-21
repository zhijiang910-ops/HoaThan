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
| Rương boss và tiến trình | Mở tốn 15 thể lực. Hết thể lực vẫn có thể hoàn thành và mở sao theo chế độ tập ải. Có nguyên liệu chắc chắn và roll bí tịch/trang bị theo sao. Nhận thưởng rương đầu mở Truy Phong Kiếm. | Phẩm đá và kinh tế cuối cùng còn chờ cân. Lực chiến dùng để chuẩn bị cho nội dung về sau. |
| Trang bị và kho | Có sáu ô, so/mặc món, phân giải lấy Tiên ngọc, hàng chờ đồ mới khi kho 120 món đầy, bảo vệ đồ đang mặc. Các phẩm từ Phàm tới Hỗn Độn. | Sáu ô gồm Vũ khí, Y phục, Hài, Hộ phù, Nhẫn/Bội ngọc, Đai/Găng tay. Đai ưu tiên sinh tồn, Găng ưu tiên tấn công. Cần asset icon Đai/Găng. |
| Cường hóa | Có +0 đến +9, rủi ro rớt cấp từ khi thử lên +5, hư hỏng khi thử lên +8/+9. Món hỏng được giữ, tự tháo và sửa về +0. Có đọc đồ cũ và báo lần đầu đạt mốc. | Vũ khí là ô mở đòn; các ô khác cộng chỉ số ở +3/+6/+9. Bỏ bể mất món vĩnh viễn. Chừa phẩm đá và kinh tế chính thức để bàn tiếp. Giữ sự tò mò bằng cách che nội dung mốc chưa mở. |
| Đòn thường Kiếm | A–B trong lúc di chuyển. +3 xuyên 5% giáp cho đòn thường. +6 mở C chém quét trong bản game; dấu Phá Thế hỗ trợ nhát thường kế và giúp phá Cương Khí. +9 thêm kiếm khí ngắn. | Demo C Lướt Trảm nam + nữ (`demo/nhat_c/`) chờ duyệt. Lỗi: nhát B nữ đang dùng anim chưởng (`attack2`). Làm rõ hạ trọng tâm, một kiếm nhất quán, đúng tay cầm, nhát ra có lực và về thế mượt. Nâng +6 nên mở cách đánh có ích. Giữ nhát C gắn combo; +9 giữ vai trò riêng. |
| Kỹ năng Kiếm | Kiếm Khí Trảm (Q), Hoành Tảo (F), Vạn Kiếm Quy Tông (X) chủ động. Vạn Kiếm chọn vùng đặt mưa kiếm. Kiếm Ảnh là ba kiếm tự xoay quanh người, có vòng hồi. Có nội tại Kiếm Tâm. | Chủ động nhìn rõ nút dùng. Tự kích hoạt hiển thị vòng hồi riêng. Bấm xem chú thích thuốc và kỹ năng, gồm sát thương đơn/diện, hiệu ứng, hồi chiêu, nội lực và số lượng thuốc tùy mục. |
| Lướt và bí tịch | Có Lướt và hủy nhát đang lấy đà. Có bí tịch cộng chỉ số vĩnh viễn và biến thể Truy Phong Kiếm, Hồi Phong. Truy Phong dùng được từ +0 và biến đổi nhát đầu sau Lướt. Hồi Phong ảnh hưởng Hoành Tảo sau Lướt. Chọn một bí tịch Lướt mang theo. | Tối đa một ô bí tịch chủ động ở giai đoạn thử, chưa xác nhận ô riêng trong bản đóng gói. Ưu tiên thay đổi cách dùng một chiêu; có thể thử tăng tốc ngắn hoặc thêm dư ảnh Lướt. Dịch chuyển xuyên địa hình và nhiều biến thể đồng thời để sau. |
| Luyện đan | Tinh anh và boss cho đường lấy Tuyết Sâm/Băng Tâm Liên. Có Cuồng Huyết Đan dùng tạm trong ải và Trúc Cơ Đan vĩnh viễn giới hạn trong bản thử. Có Hộ Thể Đan giải trạng thái. | Định hướng bản đầu ưu tiên đan dùng trong ải. Trúc Cơ Đan hiện vẫn tồn tại trong code (+20 HP/viên, một lượt dùng mở theo mỗi sao đã vượt, tối đa 5). Để chủ game chốt phần thử này trước khi mở rộng; bỏ hướng làm nhiều đan cộng vĩnh viễn nhiều chỉ số. |
| Hóa Thân và Chiêu Mộ | Có Hóa Thân dùng Nộ, vòng Nộ trong nút Hóa Thân. Có Chiêu Mộ local để thử thần tướng và đổi mảnh từ bản trùng. | Chiêu Mộ chính thức để sau solo. Bản thử bắt đầu với Tôn Ngộ Không; giá, tỷ lệ và đổi mảnh còn để cân trước khi mở online. |
| HUD và cảnh báo | Avatar hiển thị, viền nút Hóa Thân lục giác. Khí huyết và Nội lực ở dưới, EXP tím và tiến độ đợt vàng. Hạ gục và Liên kích riêng. Quái thường ẩn HP, tinh anh có HP trên đầu, boss có thanh riêng trên cùng. | Máu dưới 30% có trạng thái cảnh báo; vừa xuống dưới 20% nháy viền 2 giây rồi giữ đỏ nhẹ. Kiểm tra đọc được máu khi đông quái và trên màn nhỏ. |
| Liên kích | Có đếm tụt dần khi ngừng đánh, lớp màu đen đi qua chữ số và thưởng theo mốc. Bản hiện tại giữ 2,2 giây rồi tụt trong 2,4 giây. | Mốc 25 tích Nộ nhanh hơn 5%, 100 thêm 4 điểm phần trăm chí mạng, 300 thêm 5% sát thương. Thưởng mất theo mốc khi tụt. Đây là phần Claude đã sửa, ưu tiên giữ hành vi hiện tại. |
| Hướng dẫn lần đầu | Có luồng đi, đánh, Lướt và nối đòn. Ghi nhận để lần sau không lặp. Tạm dừng khi chờ xác nhận, có spotlight vào nút Lướt ở bước tương ứng. | Giữ nguyên tắc chỉ hiện ở lần đầu và chiếu đúng ô cần thao tác. Mở rộng có chọn lọc cho Hóa Thân, thuốc, nghỉ giữa ải và rèn nếu bổ sung hướng dẫn mới. |
| Màn hình điện thoại | Có chặn dọc, hiện yêu cầu xoay ngang và dừng chạy trận khi đang dọc. Chặn tự thu phóng khi chạm/chạm đúp/chụm ngón trên vùng chơi (22/11). | Xác nhận trên iPhone/Safari thật và trường hợp mở link trong app chat. |
| Hiệu ứng và chuyển động | Có bản A–B sửa tư thế, nối thế kiếm, idle ổn định và Vạn Kiếm ngắm vùng. Có video thử nhát C. | Soi đổi hướng khi vừa di chuyển vừa đánh, tay cầm, frame dư kiếm, tóc bị giật khi thoát đòn, nhịp tiếp xúc và hiệu ứng trúng. Xuất clip tốc độ thật và quay chậm để duyệt trước khi ghép C mới. |

## 2. Các thông số thử quan trọng

### Thể lực và phần thưởng

- Thể lực thường tối đa 100, hồi 1 điểm mỗi 15 phút. Điểm Tâm lúc 07:00, 14:00 và 21:00 giờ Việt Nam, cửa sổ 2 giờ, bấm bánh bao 5 lần để nhận tối đa 15 thể lực cho khung, trần điểm tâm 115.
- Rương boss tốn 15 thể lực. Bản game đóng gói cho 4 Huyền Thiết mỗi sao và có roll dược liệu. Tỷ lệ bí tịch theo sao từ ★1 đến ★5 là 6%, 8%, 10%, 12%, 15%, ngoài thưởng riêng của rương đầu. Tỷ lệ/trọng số phẩm đầy đủ ở `CHEST_T`.
- Cuồng Huyết Đan cộng 25% sát thương trong 45 giây, mang tối đa 5, luyện từ 3 Tuyết Sâm. Hộ Thể Đan giải độc/choáng/chậm và miễn trạng thái tương ứng 60 giây. Trúc Cơ Đan hiện tốn 2 Tuyết Sâm + 1 Băng Tâm Liên.

### Cường hóa

| Mốc muốn lên | Thành công | Giữ cấp | Rớt 1 cấp | Hư hỏng | Huyền Thiết |
|---|---:|---:|---:|---:|---:|
| +1 / +2 | 100% | 0% | 0% | 0% | 1 / 1 |
| +3 / +4 | 80% | 20% | 0% | 0% | 2 / 2 |
| +5 / +6 | 50% | 40% | 10% | 0% | 3 / 3 |
| +7 | 20% | 60% | 20% | 0% | 4 |
| +8 | 20% | 54% | 20% | 6% | 5 |
| +9 | 8% | 56% | 25% | 11% | 6 |

Mỗi cấp tăng 4% chỉ số gốc. Sửa tốn 3 Huyền Thiết và đưa món về +0. Thưởng mốc lấy mốc cao nhất trên từng món.

| Ô | +3 | +6 | +9 |
|---|---|---|---|
| Kiếm | Đòn thường bỏ qua 5% giáp | Mở nhát C | Thêm kiếm khí sau C |
| Y phục | +4 HP | +6 HP | +8 HP |
| Hài | Giảm hồi Lướt 3% | 4,5% | 6% |
| Hộ phù | +0,25 Nội lực/giây | +0,375 | +0,50 |
| Nhẫn/Bội ngọc | +1 điểm % chí mạng | +1,5 | +2 |
| Đai | +3 HP | +4,5 HP | +6 HP |
| Găng tay | +2% tốc độ đòn thường | +3% | +4% |

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

1. Duyệt chuyển động và công dụng nhát C. Dựng thử với nam và nữ, so cùng bố cục và cùng mục tiêu, có đoạn tắt VFX. Nhát C lướt chém là phương án demo, đoạn lướt thật và cân bằng còn phải thử.
2. Khi được duyệt, tích hợp tại `startSwordCut` và `finishSwordCut`. Kiểm tra +0/+3/+6/+9, không dư kiếm, không mất khả năng vừa đi vừa đánh. Kiểm tra Lướt hủy lấy đà và Truy Phong hoạt động đúng, mỗi mục tiêu chỉ trúng một lần trong phương án lướt. Kiểm tra cản địa hình, đổi hướng và va chạm khi bị vây.
3. Chạy lại luồng tạo nhân vật → sảnh → ải → nghỉ → checkpoint → boss → rương → cường hóa. Test HUD máu thấp, mô tả kỹ năng/thuốc, Vạn Kiếm ngắm vùng, hướng dẫn lần đầu, Liên kích và xoay ngang. Dùng một lượt hồ sơ mới và một lượt hồ sơ cũ.
4. Cân vòng solo trước. Sau đó mới triển khai tính năng cần tài khoản, máy chủ, sổ giao dịch, Raid/PvP và bảng rơi chính thức.

Hồ sơ cũ ghi kết quả kiểm thử tại thời điểm từng chặng. Tình trạng trong tài liệu này dựa trên code bản đóng gói và hồ sơ bàn giao. Safari iPhone thật, cân bằng dài hạn và cảm giác nhát C trong game vẫn cần kiểm thử trực tiếp.
