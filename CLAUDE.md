# Tây Du Sinh Tồn · bàn giao cho Claude (đọc trước khi làm)

Game hành động sinh tồn pixel art một file (`game/index.html` + `game/assets/`), canvas, chạy trên trình duyệt, ưu tiên điện thoại xoay ngang. Chủ game nói tiếng Việt, xưng "tao/mày"; trả lời bằng tiếng Việt.

Repo này để **riêng tư** và có chứa asset mua có giấy phép (`game/assets/`, `nguon/pack_wuxia/`). Chủ game đã đồng ý lưu ở đây và chịu trách nhiệm. Không công khai repo hay link game.

Lịch sử cũ hơn: `BAT_DAU_CLAUDE.md`, `TONG_HOP_TINH_NANG.md`, `tai_lieu/`. Khi mâu thuẫn, file này và code game là bản đúng.

## Luật làm việc của chủ game (bắt buộc)
1. **Cái gì muốn sửa phải báo trước.** Đề xuất, chờ duyệt rồi mới làm. Ngoại lệ: chủ game ra lệnh trực tiếp.
2. **Tạo bằng công cụ có sẵn, không chắp vá.** Hình nhân vật, VFX tạo bằng PixelLab (skeleton animation, VFX creator) hoặc lấy từ gói asset đã mua. Không vẽ VFX bằng code; không ghép, vá frame.
3. **Phác thảo trước, duyệt rồi mới tạo trên PixelLab** (với động tác, tư thế mới).
4. **Kiểm từng frame 98–99% so với master** trước khi gửi: không dư kiếm, không mất tay chân, độ dài kiếm bằng master, trang phục giữ nguyên.
5. Không co giãn (squash/stretch) frame nhân vật, không hitstop, không tự đổi màu nhân vật.
6. Gửi video/ảnh kiểm tra khi xong mỗi phần. Báo đúng sự thật, kể cả lỗi.

## Hiện trạng game (23/11)
- **Bộ Kiếm (nam và nữ chung):**
  - Đánh thường A → B (khởi kiếm, hồi kiếm); +6 mở C Phá Thế Trảm (quét 360°, vòng elip PixelLab `k5c_*`). Vệt chém A/B/C: bộ Slashes Frostwindz (`zs1-3`), đã đổi màu theo game.
  - **Q Huyết Ảnh Trảm:** khóa mục tiêu, lướt xuyên, xoáy đỏ 6 nhát, vòng kết (VFX PixelLab `hv_*`).
  - **F Thiên Xu Kiếm Trận:** VFX gói Wuxia xuất từ Godot, `tx_in/loop/out`; id vẫn là `k2`.
  - **X Vạn Kiếm Quy Tông:** bản gốc gói Wuxia, phóng ngang (`vk_e`).
  - **Ô tự kích hoạt Hồi Phong Quy Sao** (`k3`, có sẵn từ đầu trận): 3 phi kiếm vàng (`hp_guard`) bay vòng, tự lao chém quái gần rồi về.
  - Đã bỏ Lướt Trảm, Kiếm Ảnh, Kiếm Tâm, Kiếm Ý. Code lướt `cutC` vẫn giữ vì Huyết Ảnh dùng.
- **HUD ô kỹ năng:** hàng trên 4 ô chủ động (Q, F, X + 1 trống). Hàng dưới: 2 ô chiêu tự thi triển có hồi chiêu, máu, mana, 1 ô dự phòng. Nội tại cộng chỉ số không hiện ô.
- **Cấp và phẩm:**
  - Tạm mở đến **Lv70**, 7 phẩm đầu, mỗi phẩm 10 cấp (`LV_OPEN`, `TIER_OPEN`).
  - **Cấp tối đa CHƯA chốt.** Đừng tính theo mốc 120; chủ game có thể để tối đa 200. Số phẩm sau Lv70 cũng chưa chốt.
  - 5 phẩm khóa đang đặt chỗ trong code (Hồng Hoang, Thái Cổ, Vô Cực, Tạo Hóa, Thiên Đạo) chỉ là tạm, không rơi ra.
  - Cường hóa tối đa +12, mở đến +9 (`FORGE_OPEN`).
- **6 ô trang bị:** Vũ khí, Y phục, Hộ phù, Hài, Nhẫn/Bội, Đai/Găng.
- Bản chơi thử (artifact của tài khoản cũ): https://claude.ai/artifact/7HgwkR1wd2kZ521bQ1oRTA. Tài khoản khác sẽ đăng link mới.

## Sở thích thẩm mỹ của chủ game (rút ra từ góp ý)
- VFX phải chau chuốt, dày, có chiều sâu. Nét mỏng, phẳng là "như đồ chơi". Vòng elip đòn C phải có độ dày đáng kể.
- Không để đòn đánh trông như nhân vật bị giật, lag hay xoay 360° bằng cách lật sprite. Cảm giác xoay để VFX lo.
- Đòn A, B, C phải liền mạch như một combo. Vệt chém phải nằm trước mặt, đúng hướng chém.
- Không dùng mảnh, hạt lạ do demo để lại (ví dụ tia trúng cọc trong bản xuất Godot bị xem là "mảnh băng").
- HUD gọn: ô kỹ năng không quá to, thanh máu và mana đủ to, không che màn hình. Joystick cố định góc trái dưới, không hiện ở chỗ chạm khác.
- Điện thoại (iPhone, Samsung): không được tự phóng to khi bấm đúp hoặc khi nhập tên. Nút không được lọt khỏi khung.
- Ngộ Không: khỉ con là con của Ngộ Không, không đeo vòng kim cô. Hình phải cổ trang, không giống võ sĩ hiện đại.
- Chủ game thích được thử ngay trong game: khi cần duyệt hiệu ứng, có thể làm tạm ô kỹ năng TEST, duyệt xong thì xóa.
- Ảnh và video tham chiếu đã gửi: `nguon/tham_chieu/` (xem README trong đó).

## Đã chốt, CHƯA làm vào game (việc tiếp theo)
1. **Tách vũ khí thành lớp riêng** cho mọi động tác (nam, nữ). Đã làm thử ổn trên đòn A nam, xem `nguon/pixellab/wl/`.
   - `cong_cu/claude/unsword.py`: xóa kiếm khỏi frame theo khớp `sword_grip/tip` trong file job khung xương (`nguon/pixellab/combo5/job_*.json`).
   - Ghi "socket" (vị trí tay, góc) cho từng frame.
   - Game vẽ vũ khí đang trang bị vào tay, rồi vẽ lại nắm tay (bán kính ~3,2 px) đè lên chuôi.
   - Vũ khí: mỗi cây 1 ảnh PixelLab (pixflux, nằm ngang, mũi sang phải). Ví dụ: `wl/gen/red1, red2, big1m, big2`.
2. **Aura vũ khí theo cường hóa** (đã có VFX PixelLab, `nguon/pixellab/aura/`):
   | Mốc | Aura | File |
   |---|---|---|
   | +3 | lục mờ | `aura3` |
   | +6 | vàng | `aura6y` |
   | +9 | tím | `aura9p` |
   | +12 | đen + sấm sét (khóa) | `aura12` |
   - Sáng tăng dần theo mốc. Dùng lớp `front`, xoay theo kiếm, kéo theo chiều dài lưỡi.
3. **Đồ theo bộ** (chủ game chọn hướng này). Mỗi bộ có trang phục riêng và kiếm đi kèm, hiệu ứng bộ mốc 2/4/6 món nên đổi lối chơi.
   - Đề xuất 4 bộ: Thanh Sam (mặc định), Huyền Giáp, Kim Lũ Y, Huyết Ma Bào. Chờ chủ game chốt danh sách và hiệu ứng.
   - Trang phục: `edit-image-pro-flash` tạo ảnh mẫu (6 lượt), sau đó `transfer-outfit-v2` mặc lên frame (3 frame/lần, 10 lượt). Mỗi bộ cho đủ động tác khoảng 170 lượt/giới tính. Bản thử Huyền Giáp: `nguon/pixellab/outfit/`.
4. Chưa có: yêu cầu cấp để mặc đồ; đồ rơi theo cấp nhân vật (hiện rơi theo ải).

## Công cụ và quy trình
- **PixelLab API v2:** `https://api.pixellab.ai/v2`, header `Authorization: Bearer <key>`. Môi trường mới phải thêm key PixelLab làm network secret cho host `api.pixellab.ai`. Không ghi key vào code; script dùng `Bearer proxy-injected`.
  - Script: `cong_cu/claude/plvfx.py` (VFX; `GAMEPACK=1` ra zip tách lớp `behind/front`; `EFFECT=<thư mục>/<tên>` để sửa tiếp hiệu ứng cũ, 4 lượt).
  - `run5.sh` + `combo5.py` + `combopose.py`: tạo động tác bằng khung xương.
  - `qc*.py`, `ruler.py`: kiểm frame.
  - `nguon/pixellab/pl_openapi.json`: danh sách API.
- **Xuất VFX gói Wuxia từ Godot ra frame:**
  - Gói cần Godot **4.7.1** (tải bản linux x86_64 trên GitHub releases của godotengine). Chạy dưới `xvfb-run` với `--rendering-driver opengl3 --write-movie <thư mục>/f.png --fixed-fps 30`. Bật `rendering/viewport/transparent_background=true` trong `project.godot`.
  - Chiêu môn phái: chép `nguon/godot_bake/Bake.gd`, `Bake.tscn` vào `nguon/pack_wuxia/Skills/Godot/`, chạy `res://Bake.tscn -- <id chiêu>`. Đặt `demo_incoming:false` và không gọi `boundary_attempt`, nếu không demo sẽ để lại tia và mảnh lạ trong hình.
  - Vạn Kiếm: chép `Drive2.gd`, `Rec2.tscn` vào `nguon/pack_wuxia/Common_VFX/`. File này xóa hẳn cọc gỗ, không chỉ giấu, để không còn tia trúng cọc.
  - Đóng sheet bằng PIL: cắt theo bbox chung, rộng ≤4096 px, ≤15 Mpx mỗi ảnh (điện thoại). Khai báo trong `SPX` (`w,h,c,n,px,py`).
- **Kiểm thử:** Playwright + Chromium có sẵn trong môi trường. `cong_cu/claude/rec_lib.js` (đồng hồ ảo `__step`); `combo_film2.js` quay combo ở Luyện Công; `hv_film.js`, `kit2.js`, `run_hp.js` thử chiêu.
- **VFX trong game:** fx `{k:'sp',s:<tên SPX>,x,y,sc,fx:hướng,T,gr:lớp sau,follow:1}`. Ảnh để ở `game/assets/vfx/`.
- Nhân vật: `game/assets/hero_nam.png`, `hero_nu.png`, ô 160×128. Frame PixelLab 128 canvas đặt lệch dx=16.

## Git
- Làm trên nhánh `claude/relaxed-heisenberg-72j521`, push lên nhánh đó.
- Không tạo PR nếu chủ game không yêu cầu.
- Không ghi tên model vào commit.
