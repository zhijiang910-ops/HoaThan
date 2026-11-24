# Khử Tà Diệt Ma 驅邪滅魔: tóm tắt tiến độ (24/11)

Dán file này vào đầu cuộc trò chuyện mới. Chi tiết đầy đủ nằm ở `CLAUDE.md`. Khi mâu thuẫn, `CLAUDE.md` và code game là bản đúng.

## Game là gì
Game hành động sinh tồn pixel art, một file `game/index.html` cùng `game/assets/`, vẽ bằng canvas, chạy trên trình duyệt, ưu tiên điện thoại xoay ngang. Chủ game nói tiếng Việt, xưng "tao/mày". Trả lời bằng tiếng Việt.

Game vốn là bản Tây Du, đang chuyển chủ đề sang **khử tà diệt ma** (Âm Giới). Gameplay giữ nguyên, chỉ đổi bối cảnh, tên và phong cách chiêu.

## Đã làm xong
- Bộ Kiếm (Mao Sơn Phái) đầy đủ: đánh thường A/B/C, Q, F, X, C, nội tại Linh Kiếm Hộ Pháp. Có vũ khí dạng lớp riêng, aura cường hóa, bộ đồ Huyền Giáp.
- Thần tướng (Ngộ Không, Na Tra, Bát Giới, Thổ Địa): người chơi tự bấm kỹ năng. Ngộ Không đã làm kỹ chuỗi đòn và animation.
- Hệ thống: tối đa Lv200 và 12 phẩm (mở đến Lv70 và 7 phẩm), cường hóa, Tàng Bảo Các, rương Boss, tạo nhân vật có avatar, Luyện Công, Vượt Ải theo sao.
- **2 map:** Hoang Thôn Nghĩa Địa (làng bỏ hoang phía tây, nghĩa địa phía đông, hàng đèn lồng ở giữa) và Cổ Miếu Hoang (một tượng Phật lớn ở chính điện, lư hương, sư tử đá, đèn đá dọc lối đi). Bố cục map xếp tay, không còn rải ngẫu nhiên. 4 map cũ đã xóa.
- **Quái Âm Giới thay quái Tây Du:** Vong Hồn, Ma Trơi, Âm Binh (có animation PixelLab), Oan Hồn Xạ, Địa Ngục Khuyển, Quỷ Sai. Boss ải vẫn là Ngưu Ma Vương.
- **Âm Giới 18 tầng: dữ liệu và cấu hình đã có** (7 map, 12 boss/mini-boss, quái theo chặng, bậc kích cỡ quái thường < Tinh Anh < mini-boss < trùm), chưa nối vào luồng chơi. Hình 7 trùm đã có: Ngưu Đầu, Mã Diện (PixelLab), Hắc/Bạch Vô Thường (thiết kế ChatGPT, PixelLab chuyển nét pixel), Mạnh Bà, Phán Quan, Diêm Vương (ChatGPT). Brief và master để nhờ ChatGPT vẽ: `nguon/master_amgioi/`.
- Bản chơi thử: https://claude.ai/artifact/66MCZmMfKMjwuYrknQjNU1 (riêng tư, chủ game tự mở Share).
- Code mới nhất ở nhánh `claude/youthful-fermat-6hovsq`.

## Việc còn dở
1. **Hoạt động Âm Giới** chưa nối vào luồng chơi (chỉ có dữ liệu `AM_*`, `amFloor(n)`): 18 tầng địa ngục, 1/3/5 sao, 2 lượt mỗi ngày, chết là thua. Boss mốc: Ngưu Đầu và Mã Diện (tầng 3), Hắc Vô Thường (6), Bạch Vô Thường (9), Mạnh Bà (12), Phán Quan (15), Diêm Vương (18). Phần thưởng chưa chốt.
2. **Boss Âm Giới:** cả 7 trùm đã có hình riêng; còn thiếu hình riêng cho 5 mini-boss (đang dùng hình Quỷ Sai/Ngưu Ma Vương) và 6 quái thường mới.
3. **6 môn phái:** 5 phái đã chơi được (chọn ở màn tạo nhân vật), mỗi phái có cây vũ khí riêng và bộ chiêu Q/F/X dùng VFX gói Wuxia: Mao Sơn (Kiếm), Trảm Yêu Môn (Đao, Xích Diễm), Phục Ma Tự (Trượng, Kim Cương Tự), Huyền Linh Các (Quạt, Bách Hoa Cốc), Truy Hồn Cốc (Cung, U Minh Giáo). **Thiên Cương Môn (Quyền) chưa có bộ chiêu**, vẫn khóa. Số liệu các phái mới là tạm, chưa cân bằng; động tác đánh riêng của từng vũ khí chủ game tự làm.
4. **Đổi chữ theo chủ đề** còn dở: mô tả kỹ năng, thần tướng, quái sự kiện, cốt truyện, tên màn, vật phẩm.
5. **Cân bằng sát thương** để sau. Không tự chỉnh số khi chủ game chưa ra lệnh.
6. Tiến độ sao đang dùng chung giữa các map, chưa tách. Chưa thử trên iPhone thật. Chưa đo hiệu năng Vạn Kiếm trên máy yếu.

## Luật làm việc của chủ game (bắt buộc)
1. Muốn sửa gì phải báo trước, chờ duyệt rồi mới làm. Ngoại lệ: chủ game ra lệnh trực tiếp.
2. Giữ đúng phong cách đồ họa master: chibi đầu to thân ngắn, viền đen mảnh, màu dịu, tô bóng ít.
3. Hình nhân vật và VFX tạo bằng PixelLab hoặc lấy từ gói asset đã mua. Không vẽ VFX bằng code, không ghép hay vá frame. Không co giãn, bóp méo frame nhân vật.
4. **PixelLab (tốn tiền) chỉ dùng khi thật sự cần.** Làm trước bằng cách rẻ: dùng lại asset, chỉnh timing hoặc vị trí, thử trong game. Trước khi gọi phải nói rõ vì sao và dự kiến bao nhiêu lượt.
5. Báo đúng sự thật, kể cả lỗi. Gửi ảnh hoặc video kiểm tra khi xong mỗi phần.
6. Không tạo PR nếu chủ game không yêu cầu. Không ghi tên model vào commit hay code.
7. Repo riêng tư, có asset mua giấy phép. Không công khai repo hay link game.
