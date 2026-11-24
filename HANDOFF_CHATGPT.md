# HANDOFF_CHATGPT.md — Bàn giao dự án Tây Du Sinh Tồn

> Cập nhật: 24/11/2026. Mục tiêu: cho ChatGPT, Codex hoặc Claude tiếp quản **đúng tiến độ, không phải làm lại**, không nhầm thiết kế với tính năng đã chạy. Tài liệu này là **bản chỉ mục bàn giao**, không thay thế việc đọc code và các file gốc.
>
> **Repo riêng tư:** `zhijiang910-ops/HoaThan`  
> **Nhánh đang làm:** `claude/relaxed-heisenberg-72j521`  
> **Không tự merge `main`, không tạo PR hoặc thay đổi code/asset nếu không được giao.**  
> **Phạm vi riêng:** Tây Du Sinh Tồn (webgame sinh tồn pixel art) — **không được trộn với dự án Tu Tiên MMORPG 2D khác của chủ game**.

## A. Thứ tự đọc và nguyên tắc đối chiếu

1. `CLAUDE.md`: chuẩn kỹ thuật hiện tại, workflow PixelLab, các giới hạn/QA và trạng thái giao việc gần nhất từ Claude.
2. `game/index.html` cùng `game/assets/`: **nguồn xác nhận hành vi thực sự đã chạy**. Game dùng HTML/CSS/JS Canvas 2D, ưu tiên màn hình điện thoại xoay ngang; lưu hồ sơ bằng localStorage.
3. `TONG_HOP_TINH_NANG.md`: bảng quyết định gameplay/kinh tế và trạng thái Đang chạy / Đã chốt nhưng chưa triển khai / Đề xuất.
4. `BAT_DAU_CLAUDE.md`, `tai_lieu/`, `demo/`, `cong_cu/claude/`: lịch sử, quy trình sản xuất, thử nghiệm; nhiều chi tiết đã lỗi thời.
5. Chính file bàn giao này: danh sách mâu thuẫn, những quyết định mới và thiết kế cốt truyện đang bàn.

**Khi có khác biệt:** code xác định cái đang chạy; quyết định **mới hơn, rõ ràng của chủ game** xác định cái phải làm tiếp. Không âm thầm khôi phục ý tưởng bị loại chỉ vì tài liệu cũ còn ghi. Nếu thiếu dữ liệu hoặc còn xung đột, ghi "cần đối chiếu/duyệt" thay vì tự đoán.

### Quy tắc làm việc bắt buộc
- Chủ game nói tiếng Việt, xưng "tao/mày". Báo trước thay đổi nếu chưa được giao trực tiếp; không tự thay các phần đã duyệt.
- Hình/animation/VFX: phác thảo để duyệt trước; dùng PixelLab hoặc asset được phép, không chắp vá frame, không tự vẽ VFX bằng code, không thay đổi thiết kế master.
- Kiểm từng frame theo master, tay/chân/vũ khí/sockets/hướng và đúng động tác; không squash/stretch, không hitstop, không tự đổi màu. Báo bằng video/ảnh và kết quả QA thật.
- Giữ repo **private**. Không commit API key, token, mật khẩu; không đưa bí mật vào handoff, issue hoặc log.
- Không nói đã PASS khi chưa chạy game/kiểm thử. Không ghi một ý tưởng thành "đã triển khai".

## B. Hiện trạng kiểm tra trên GitHub (24/11/2026)

| Nhóm | Đang có trong repo / code | Giới hạn cần nhớ |
|---|---|---|
| Nền game | `game/index.html`, `game/assets/`, browser Canvas 2D, UI di động xoay ngang | Cần QA trên Safari iPhone thật |
| Nhân vật | Nam/nữ; tạo hồ sơ; lớp vũ khí và socket; sprite trang phục Huyền Giáp | Không coi mọi ngoại hình và vũ khí là hoàn tất |
| Kiếm | Combo A/B và đòn C ở +6 trong code; bộ Q **Huyết Ảnh Trảm**, F **Thiên Xu Kiếm Trận**, X **Vạn Kiếm Quy Tông**, tự động **Hồi Phong Quy Sao** | Bộ **tư thế A–B–C cũ đã bị chủ game loại khỏi kế hoạch sản xuất mới**, nhưng không được tự xóa combo đang chạy |
| Vũ khí khác | Có tài nguyên/thử nghiệm Thương và Song Quyền; `WEAPONS` vẫn chứa cả bộ cũ theo tiến độ thử | Thương/Song Quyền chưa có animation đánh hoàn chỉnh; Song Quyền chưa thành kit `WEAPONS` hoàn chỉnh |
| Thế giới | Bốn môi trường trong `MAPS`: Cổ Trấn, Sơn Lâm, Tuyết Sơn, Hỏa Diệm Sơn; có quái thường, một số tinh anh, Ngưu Ma Vương | Không nhầm với 34 map cốt truyện: đó là **phương án thiết kế**, chưa sản xuất |
| Chơi solo | Lộ trình/ải, nhiệm vụ trong trận, nghỉ giữa ải, checkpoint, kèo phụ, sao ★1–★5, rương Boss, tu luyện thẻ | Các nâng cấp trong mục C chưa được đồng bộ code |
| Phát triển dài hạn | `LV_MAX=200`, `LV_OPEN=70`; 12 phẩm thiết kế, 7 phẩm mở trong bản thử; 6 ô trang bị, cường hóa tới +9 đang mở | +12 là khả năng thiết kế về sau, chưa mở; ô Nón thứ 7 chưa có trong code |
| Hóa Thân | Hệ Nộ, Hóa Thân; Tôn Ngộ Không và dữ liệu/thử nghiệm thần tướng khác | Không tuyên bố mọi thần tướng đều có sprite/animation đạt chuẩn |
| Online | Chưa có nền tảng máy chủ hoàn chỉnh cho Raid, PvP, đấu giá, bang hội | Để sau vòng solo |

**Mốc cấp/phẩm thực tế trong `CLAUDE.md` và code:** 1, 7, 14, 22, 32, 43, 56, 71, 90, 113, 140, 170. Không tự thay các mốc này bằng khoảng đều 10 cấp.

**Lưu ý lớn về tài liệu cũ:** `TONG_HOP_TINH_NANG.md` còn mô tả một số kỹ năng Kiếm đã lỗi thời (ví dụ Kiếm Khí Trảm, Hoành Tảo, Kiếm Ảnh, Kiếm Tâm). Đối với trạng thái code Kiếm hiện hành, ưu tiên `CLAUDE.md` và kiểm tra `WEAPONS.kiem` trong `game/index.html`. Không khôi phục những chiêu đã bỏ khi chỉnh tài liệu.

## C. Thiết kế ĐÃ CHỐT nhưng CHƯA triển khai đầy đủ

### C1. Rương Boss và quyền nhận thưởng — ĐÃ TRIỂN KHAI (24/11, Codex + Claude)
- **Trạng thái code:** hạ Boss gọi `recordBossVictory()`: ghi hoàn thành ải/mở sao và lưu rương chờ `save.bossChest` (thưởng roll sẵn, một rương duy nhất). Nhận tại màn rương hoặc nút "Rương Boss chờ nhận" ở sảnh (`claimChest`), trừ 15 thể lực lúc nhận, xóa rương ngay để không nhận trùng. Đã bỏ nút "Bỏ qua". Đang có rương chờ mà hạ Boss lần nữa: sao vẫn mở nhưng thưởng mới không cộng dồn (có báo trên màn hình và ở sảnh). Checkpoint `cp.chestDone` = đã hạ Boss nhưng chưa kết toán: bấm "Tiếp tục" hoặc "Vượt Ải" ở sảnh sẽ kết toán ải đó (Tiên ngọc, số lần thắng, EXP) trước. Đã QA bằng Playwright; chưa thử trên Safari iPhone thật và đoạn Boss chết → rương rơi → mở trong trận.
- **Yêu cầu thiết kế gốc (giữ để đối chiếu):**
- Hạ Boss hoàn thành ải/mở sao ngay cả khi thiếu thể lực. Mở rương tốn **15 thể lực** khi **nhận thưởng**.
- Thiếu thể lực: lưu **một quyền nhận rương chờ hợp lệ**, đủ thể lực nhận sau mà **không đánh lại Boss**. Không để nút Bỏ qua làm mất quyền nhận; chống nhận trùng và farm tài nguyên vô hạn.
- Giữ bảng `CHEST_T` đang có: 4 Huyền Thiết chắc chắn, lượt dược liệu, vật phẩm/bí tịch theo sao; tỷ lệ bí tịch ★1..★5 = **6/8/10/12/15%**. Thưởng đầu tách thưởng farm.
- Công dụng của bí tịch trùng cần phát triển sau, chưa chốt công thức.

### C2. Trang bị Nón — ô thứ 7
- Thêm **Nón** độc lập, nâng từ 6 lên **7 ô**; không thay ô nào.
- Nút **Ẩn/Hiện Nón**: khi ẩn chỉ tắt lớp hình trên nhân vật, **vẫn mặc và nhận toàn bộ chỉ số/cường hóa/buff**.
- Lưu lựa chọn hiển thị theo hồ sơ; mặc định hiện; phù hợp sprite nam/nữ, tóc, trang phục và animation; QA save 6 ô cũ.
- Tên, chỉ số, bonus mốc và trọng số rơi riêng của Nón **chưa chốt**.

### C3. Cường hóa và phần thưởng mốc
- **Tỷ lệ thành công chốt:** +1/+2: **100%**; +3/+4: **80%**; +5 **50%**; +6 **40%**; +7 **25%**; +8 **15%**; +9 **8%**. Chưa sửa code theo bảng mới.
- Phân bổ còn lại (giữ cấp/rớt cấp/hư hỏng) trong tài liệu là **giả định tạm**; người dùng chưa duyệt lại tỷ lệ thất bại.
- **Vũ khí** +3 chỉ số ẩn riêng; +6 mở đòn đánh thường **C**; +9 tăng hiệu ứng, sát thương **hoặc** tầm đánh tùy **loại vũ khí**.
- **Trang bị khác vũ khí** +3/+6 tăng chỉ số; +9 tăng chỉ số **hoặc** nội tại/buff phòng ngự theo món. Bảng HP/tốc đánh/hồi mana hiện có là baseline chỉ số, không tự thay đổi.
- Đã chốt **hướng** tăng Huyền Thiết mốc +5 đến +9, thêm nguyên liệu phụ tại +8/+9; **CHƯA duyệt số lượng cuối cùng**. Đề xuất ghi trong `TONG_HOP_TINH_NANG.md`: +5=4, +6=5, +7=7, +8=10 kèm 1 "Tinh Hoa Rèn" (tên tạm), +9=14 kèm 2 đơn vị. Cần chốt tên, nguồn rơi, tỷ lệ và kinh tế trước khi code.

### C4. Định hướng vũ khí và animation
- Sáu loại vũ khí ưu tiên giai đoạn đầu: **Kiếm, Thương, Song Quyền, Phù Chú, Quạt (phóng ám khí), Cung**. **Không phân class/môn phái**; vũ khí quyết định cách đánh, kỹ năng. Những loại Đao/Côn/Đinh Ba... và mục nhập legacy trong code không thay danh sách ưu tiên.
- **Quạt** phóng phi châm/phi đao/ám khí, **không phải phong thuật/gió**.
- **Loại các tư thế chém Kiếm A–B–C phiên bản cũ** và demo C Lướt Trảm cũ khỏi kế hoạch art. Chưa chốt bộ tư thế thay thế. **Không được tự xóa game logic combo hoặc các phần liên quan kỹ năng đang dùng**.
- Thương/Song Quyền cần thực hiện bộ đòn đánh đạt chuẩn riêng. Tuân thủ bước trình bày concept → duyệt → tạo → kiểm frame → test ingame.

### C5. Các đầu việc sản xuất khác
- Trang phục/sprite set khác, hiệu ứng bộ 2/4/6 món và dáng vũ khí: đọc `CLAUDE.md`; phân biệt đề xuất và hạng mục đã duyệt chi tiết.
- Không tự sản xuất/chi tiền PixelLab khi chưa có mẫu, giới hạn và xác nhận phù hợp.

## D. Thiết kế cốt truyện & nhiệm vụ ĐANG THẢO LUẬN — CHƯA DUYỆT ĐỂ CODE

**Nguồn cảm hứng đã được chủ game nêu rõ:** *Tây Du Ký*, *Phong Thần Diễn Nghĩa*, *Sơn Hải Kinh* và các thần thoại Trung Hoa khác. Không chỉ kể lại Tây Du; kết hợp thành một vũ trụ thần/yêu/tiên/dị thú, với phân biệt nguyên tác và nhân vật do game tạo.

**Khung đang bàn:** 34 map chính, 200 stage, Lv1–200. Map thường **5 stage**; map **5/10/15/20/25/30** có **10 stage** (6 map mốc). Tổng: 28×5 + 6×10 = **200 stage**. Các map 5/10/15/20/25/30 là mốc cốt truyện có thể gắn Mini Boss stage 5 + Đại Boss stage 10. Phân chia 12 map đầu/70 stage (Lv1–70), 10 map tiếp/60 stage (Lv71–130), 7 map/40 stage (Lv131–170), 5 map/30 stage (Lv171–200) mới chỉ là **đề xuất phân phối**, không phải tiến trình đã code. Độ khó ★1–★5 lặp lại map để thử thách/farm, tránh khóa truyện chính sau ★1 (đề xuất).

**Phác thảo thế giới "Thiên Mệnh – Vạn Giới Đại Kiếp":** Phong Thần Bảng/đại trận bị xáo trộn, Sơn Hải dị thú và yêu vương thức tỉnh, người chơi mang Thiên Mệnh Ấn có thể Hóa Thân. Đối thủ dự kiến: Vô Tướng Ma Chủ, muốn thu gom sáu phong ấn; tới map 29 có cú đảo chiều rằng Ma Chủ đang lợi dụng người chơi hợp nhất phong ấn. **Tên truyện, phản diện, twist đều chưa được chủ game chốt để sản xuất.**

**Phân bố map đang bàn (34 map, chưa khóa):**
- **Chương I, map 1–12:** 1 Cổ Trấn; 2 Sơn Lâm; 3 Hắc Phong Sơn; 4 Hoàng Phong Lĩnh; 5 Bạch Cốt Lĩnh [10]; 6 Bảo Tượng Quốc; 7 Bình Đỉnh Sơn; 8 Ô Kê Quốc; 9 Xa Trì Quốc; 10 Hỏa Vân Động [10]; 11 Tuyết Sơn; 12 Hỏa Diệm Sơn.
- **Chương II, map 13–22:** 13 Thanh Khâu Sơn; 14 Độc Chướng Sơn; 15 Đại Hoang Tây Cảnh [10]; 16 Thao Thiết Cổ Vực; 17 Khoa Phụ Cổ Đạo; 18 Tương Liễu Trạch; 19 Tinh Vệ Hải; 20 Hình Thiên Chiến Địa [10]; 21 Côn Lôn Bí Cảnh; 22 Chúc Long U Cảnh.
- **Chương III, map 23–29:** 23 Triều Ca Ảo Cảnh; 24 Tây Kỳ Cổ Chiến Trường; 25 Thập Tuyệt Trận [10]; 26 Cửu Khúc Hoàng Hà Trận; 27 Kim Ngao Đảo; 28 Ngọc Hư Di Tích; 29 Phong Thần Đài.
- **Chương IV, map 30–34:** 30 Nam Thiên Môn [10]; 31 Vạn Yêu Cổ Vực; 32 Lăng Tiêu Bảo Điện; 33 Linh Sơn Tàn Cảnh; 34 Vô Tướng Ma Vực.

**Đề xuất cấu trúc nhiệm vụ theo map:**
- Một tuyến chính liên tục; mỗi stage có mục tiêu gameplay cụ thể, thay đổi giữa săn quái, phá trận, hộ tống/bảo vệ NPC, thu thập, giải ảo cảnh, diệt tinh anh/boss.
- Mỗi map thường 3 nhóm quái thường, 1–2 kiểu tinh anh, 1 boss cuối; map 10 stage thêm mini boss và thử thách trung gian. Quái chia họ: Yêu Tây Du, Dị thú Sơn Hải, Thần binh/Trận pháp Phong Thần, Ma/Hỗn Độn.
- Đề xuất 1–2 nhiệm vụ phụ đặc trưng/map, thưởng nhiệm vụ chính chỉ một lần; thưởng rương Boss theo thể lực riêng, không trộn lẫn.
- Tư duy UI: dùng bảng nhiệm vụ hiện có trong trận, thêm nhật ký ở sảnh về sau; thoại ngắn, có thể bỏ qua và đọc lại.
- **TẤT CẢ danh sách map, boss, tinh anh, nhiệm vụ trong những cuộc bàn gần đây là ý tưởng khung. Chưa có GDD level-by-level đủ để Claude/Codex tự tạo 34 map. Không triển khai các bản này trước khi chốt và làm thử một map mẫu.**
- Đặc biệt: game hiện dùng Ngưu Ma Vương trong tuyến thử nghiệm Tuyết Sơn; đề xuất đưa về Hỏa Diệm Sơn trong cốt truyện tương lai **chưa phải thay đổi code được chấp thuận**.

## E. Các hệ thống để sau
- Solo trước; Raid 3–4 người, PvP, bang hội, đấu giá, online account, sổ giao dịch, hoạt động hằng ngày và event để sau. Chốt luật riêng trước khi code.
- Không kéo hệ MMORPG Tu Tiên, các hệ môn phái hoặc định dạng đồ họa dự án khác sang Tây Du Sinh Tồn.

## F. Gợi ý thứ tự tiếp tục công việc (chờ chủ game xác nhận từng hạng mục)
1. **Đối chiếu repo:** đọc `CLAUDE.md`, `game/index.html`, `TONG_HOP_TINH_NANG.md`; báo cáo thay đổi mới nhất, check Git status, file chưa push, test thực tế.
2. **Khóa thiết kế đầu vào:** chốt animation Kiếm A–B–C mới; chốt cân rèn +5..+9, nguyên liệu +8/+9; chốt phạm vi hệ Nón và rương chờ.
3. **Triển khai có thứ tự, mỗi task một commit:** ưu tiên các sửa logic solo ít ảnh hưởng art (rương chờ, cân rèn sau khi duyệt), rồi Nón (UI/lưu game/ảnh nam nữ), sau đó vũ khí/animation từng bộ khi có master duyệt.
4. **GDD thế giới:** khi chủ game duyệt khung 34 map, tách từng map thành stage, quái/tinh anh/boss, quest, điều kiện mở, thưởng một lần, trạng thái save và kịch bản thoại; làm 1 map 5 stage + 1 map 10 stage mẫu trước.
5. **Regression QA:** hồ sơ cũ + mới; Kiếm +0/+3/+6/+9; rương đủ/thiếu thể lực; trang bị Nón ẩn/hiện không đổi chỉ số; checkpoint; quay lại game; thiết bị ngang/dọc; không xóa các thành phần đã duyệt.

## G. Cách bắt đầu phiên AI mới

1. Chọn đúng repo/nhánh; **không chạy trên `main` mặc định**.
2. Đọc `CLAUDE.md` → `HANDOFF_CHATGPT.md` → `TONG_HOP_TINH_NANG.md` → code liên quan.
3. Kiểm tra commit mới hơn tài liệu này (nếu có). Tất cả trạng thái "đã chạy" cần xác minh lại.
4. **Trước tiên báo cáo**: (a) đã có (b) dang dở (c) đã chốt chưa làm (d) cần duyệt (e) test được/chưa test được. Chưa sửa code nếu chưa nhận task cụ thể.
5. Khi chủ game giao task: khoanh vùng file, ghi chuẩn nghiệm thu, làm và QA, commit lên đúng nhánh, tóm tắt kết quả và tồn đọng. Không tự merge.

> **Lưu ý:** Tài liệu này được tạo từ phiên ChatGPT dựa trên repo GitHub tại thời điểm kiểm tra và các quyết định trực tiếp với chủ game; không phải chứng nhận game đã được build hoặc chạy thử trong phiên lập tài liệu. Nếu Claude còn chỉnh sửa local chưa push thì GitHub chưa phản ánh phần đó.
