# Tây Du Sinh Tồn: danh sách tính năng (đã có / chưa có)

Tài liệu để bàn thêm ý tưởng. Cập nhật ngày 21/11/2026.

## Game là gì

- Webgame survivors nhìn từ trên xuống, nhân vật tự đánh, phong cách pixel art Wuxia, tông tối viền vàng đồng.
- Chạy trên trình duyệt, điện thoại phải xoay ngang. Toàn bộ nằm trong một file HTML (canvas 2D, JS thuần).
- Cảm hứng gameplay: 群侠传：幸存者.

## Ràng buộc khi đề xuất

- Giữ tông tối, viền vàng đồng, pixel Wuxia. **Không** phong cách thủy mặc, **không** ô đồ nền sáng kiểu mobile, **không** chuyển sang cuộn ngang.
- Chỉ dùng tài nguyên có giấy phép rõ ràng. Sprite động hiện chỉ có: nam/nữ chính, 4 loại quái (nón lá, hắc y, nữ áo hồng, hổ). Nhân vật mới chủ yếu là ảnh đứng yên (dùng làm NPC).
- Đồ họa mới phải vẽ bằng code pixel hoặc lấy từ gói có giấy phép thương mại.

---

## ĐÃ CÓ

### Vòng chơi
- Mỗi màn có 5 đợt, đợt 5 là trùm Ngưu Ma Vương. Hạ trùm thì ra rương, rồi vào Thương hội, rồi lên màn sau. Quái mạnh dần theo màn.
- Thanh tiến độ đợt chỉ tăng khi hạ quái. Đồng hồ đếm thời gian đã đánh.
- Xong đợt: game chậm lại, hiện dải băng hoàn thành, đồ tự bay về người, rồi mở bảng chọn: Tu luyện (thẻ nâng cấp), Kết toán, Võ học, Tiệm thuốc.
- 4 bản đồ chọn được: Hỏa Diệm Sơn, Tuyết Sơn, Sơn Lâm, Trấn. Có 2 độ khó: Thường và Khó.
- Có chọn giới tính, vũ khí và thần tướng mang theo.

### Chiến đấu
- Mỗi vũ khí có 3 chiêu chủ động, 1 tuyệt kỹ và 2 nội tại. Có nút Lướt.
- **Hóa Thân:** đủ 100 nộ thì biến thành thần tướng (Tôn Ngộ Không, Trư Bát Giới, Na Tra), có hào quang khí vàng.
- Quái: Tiểu yêu, Hỏa yêu (tự nổ), Yêu binh cận chiến, Yêu binh tầm xa, Lang yêu (lao tới), tinh anh Hỏa Tướng, trùm Ngưu Ma Vương.
- Có Hạ gục và Liên kích kiểu clip.

### Đồ rơi và vật phẩm
- Quái rơi: kinh nghiệm (thoi tím), máu (thoi đỏ, hồi 2%), mana (thoi xanh, hồi 4%), tiền.
- **Bình thuốc:** Khí Huyết (hồi 40%) và Nội Lực (hồi 50%). Mua ở Tiệm thuốc hoặc nhặt được, giữ vĩnh viễn, tối đa 9 bình mỗi loại, uống bằng phím 1 / 2.
- **Đan dược** (buff tạm thời):
  - Hộ Thể Đan: giải độc, choáng, chậm và miễn nhiễm 60 giây.
  - Cuồng Huyết Đan: +25% sát thương trong 45 giây.
- **Bình, thùng, rương phá được** (ít, tối đa 5 cái trên sân):
  - Rơi máu, mana, bình thuốc, đan dược, trang bị (tối đa 2 món mỗi đợt).
  - Tỉ lệ ra trang bị: vò 1,5%, bình 1,8%, thùng 2,5%, chồng thùng 4,5%, rương 10%.
  - Phẩm trang bị: Phàm 77%, Linh 18%, Bảo 3,8%, Tiên 0,76%, Thần 0,16%, Thánh 0,03%, Hỗn Độn 0,005%.
  - Có bẫy (5–15%): khói độc, mê hồn hương (chậm), thuốc nổ (choáng).

### Trang bị và phát triển lâu dài
- 7 phẩm: Phàm, Linh, Bảo, Tiên, Thần, Thánh, Hỗn Độn. 5 ô: Vũ khí, Y phục, Hộ phù, Hài, Bội ngọc.
- Trang bị có **cấp**, theo cấp nhân vật lúc nhận được. Cấp càng cao chỉ số càng cao.
- Kho đồ lưu vĩnh viễn, phân giải đồ lấy Tiên ngọc.
- **Bí tịch** (6 cuốn, mỗi cuốn tối đa 5 tầng, cộng chỉ số vĩnh viễn): Dịch Cân Kinh (máu), Kim Chung Tráo (giáp), Thái Cực Kiếm Phổ (sát thương), Bát Quái Bộ Pháp (thân pháp, né), Ngũ Cầm Hí (hồi máu), Thanh Tâm Quyết (giảm hồi chiêu, hồi nội lực).
- **Thương hội** sau mỗi màn: bày 4 món, có nút làm mới (đắt dần), mua xong mặc ngay được.

### Nhiệm vụ và sự kiện giữa đợt
- **Bảng nhiệm vụ** luôn có 3 nhiệm vụ: hạ quái, tinh anh, đập bình, liên kích, trụ không trúng đòn, Hóa Thân, xong đợt, đạt cấp. Xong thì cộng tiền và thay nhiệm vụ mới.
- **Kỳ ngộ** khoảng 70–110 giây xuất hiện một lần, có mũi tên chỉ đường:
  - 62% là **NPC thử thách**: hạ N quái trong 25 giây, không trúng đòn 15 giây, hoặc hạ yêu vật "Truy nã". Ở Tuyết Sơn có thêm 4 NPC riêng. Đợt trùm có Thổ Địa thách hạ trùm mà máu không dưới 30%.
  - 20% là **Thương Nhân Thần Bí**: bán bình thuốc nửa giá, đan dược và 1 trang bị giá rẻ.
  - 18% là **kẻ cướp** (từ đợt 2): tự đuổi theo người chơi. 50% bị cướp ngay (mất tiền hoặc bình thuốc), 50% bị lôi vào map ẩn.
- **Map ẩn:**
  - **Sơn Trại**: đánh sơn tặc (cầm đao, cung thủ), sau đó Thủ Lĩnh Sơn Tặc ra mặt.
  - **Hổ Huyệt**: đánh bầy hổ, sau đó Hổ Vương ra mặt.
  - Hạ trùm ra rương báu: luôn có tiền và đan dược. Trang bị có tỉ lệ (50–55%), cấp từ cấp nhân vật đến +9. Bí tịch có tỉ lệ (8–12%).
  - Xong thì trở lại đúng chỗ cũ trong đợt đang đánh.

### Giao diện
- Trái trên: chân dung, tên, cấp, thanh kinh nghiệm (tím), hàng icon trạng thái (buff và debuff có đếm giờ).
- Dưới chân dung: ô tiền và bảng nhiệm vụ thu gọn được.
- Giữa trên: thanh tiến độ đợt (vàng, chia 10 ô) và đồng hồ.
- Phải trên: nút tạm dừng, số Hạ gục và Liên kích.
- Giữa đáy: 3 thanh Nộ, Nội lực, Khí huyết với icon pixel. Hai bên là nút Lướt và Hóa Thân.
- Phải dưới: bảng kỹ năng chữ Hán, 2 ô bình thuốc.
- Tạm dừng có thống kê trận và cài đặt: âm thanh, âm lượng, rung màn hình, hiện số sát thương, giảm hiệu ứng.

---

## CHƯA CÓ (đã ghi nhận, chưa làm)

- Quái thường gây độc, choáng, chậm khi đánh trúng. Hệ thống trạng thái đã có sẵn, chỉ chưa gắn vào quái.
- Đàn cầu phúc (buff 30 giây giữa trận).
- Thử thách cuối tuần.
- Thêm động tác cho nhân vật chính: lướt, trúng đòn, ngã, vạt áo bay khi chạy (cần vẽ sprite).
- Dựng lại Tuyết Sơn thành sân đá có bậc thang.
- Cân bằng: đồ Hỗn Độn, giá Thương hội, độ mạnh của cấp trang bị.
- Bí tịch mới chỉ cộng chỉ số. Chưa có bí tịch mở chiêu mới hoặc thay đổi cách đánh.
- Chưa có hệ thống bộ trang bị (mặc đủ bộ được thưởng thêm).
- Chưa có cường hóa hoặc ghép đồ.
- Chưa có thành tựu, bảng xếp hạng, nhiệm vụ ngày.
- Chưa có cốt truyện hay đoạn hội thoại giữa các màn.
- Chưa có thêm trùm khác ngoài Ngưu Ma Vương.

---

## Câu hỏi muốn bàn thêm

1. Nên thêm loại sự kiện giữa đợt nào nữa cho đa dạng?
2. Bí tịch nên có thêm hiệu ứng gì ngoài cộng chỉ số?
3. Nên làm cường hóa, ghép đồ hay bộ trang bị trước?
4. Mỗi màn nên có trùm riêng không, và lấy nhân vật Tây Du nào?
5. Có cần thêm phần thưởng để người chơi muốn chơi lại nhiều lần không?
