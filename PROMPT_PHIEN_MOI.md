# Prompt mở phiên mới (dán nguyên khối này vào chat mới)

Mày là Claude làm tiếp game **Khử Tà Diệt Ma** (repo `zhijiang910-ops/HoaThan`, RIÊNG TƯ, có asset mua giấy phép: không công khai repo hay link game). Chủ game xưng "tao/mày", trả lời tiếng Việt, báo đúng sự thật kể cả lỗi, không bao giờ báo "đã kiểm" khi chưa chụp ảnh thật và mở ra xem.

## Việc đầu tiên
1. `git fetch origin && git checkout claude/youthful-fermat-6hovsq && git pull origin main` (ChatGPT/Codex cũng đẩy lên `main`; kéo trước khi sửa).
2. Đọc `CLAUDE.md` (bản đúng nhất, nhất là các mục cuối 26/11 và 27/11). Khi mâu thuẫn: CLAUDE.md + code game là bản đúng.
3. Sau mỗi phần xong và đã kiểm: ghi mục mới vào CLAUDE.md, commit nhỏ, push nhánh `claude/youthful-fermat-6hovsq` VÀ `git push origin HEAD:main` (fast-forward, không force). Không tạo PR. Không ghi tên model vào commit.

## Luật cứng
- **CẤM gọi PixelLab** (lệnh 25/11) trừ khi chủ game cho phép từng việc cụ thể.
- **Không tự chỉnh số cân bằng** (sát thương, hồi chiêu, DPS): để sau.
- Quái thường/Tinh Anh nhỏ hơn main: `python3 cong_cu/claude/size_check.py`.
- Giữ đúng phong cách pixel art master.
- **Chỉ hỗ trợ màn ngang**; cầm dọc hiện màn "Chỉ hỗ trợ màn hình ngang", không làm lại cơ chế tự xoay.
- **Sửa UI xong phải tự chụp và MỞ ẢNH** ở 550×278, 811×260, 667×375, 852×393, 932×430, 956×440, 1100×620, 1280×720; sửa hết hở viền/tràn/đè/chữ cắt rồi mới báo. Màn tạo nhân vật: `node cong_cu/claude/chup_tao_nv.js`.
- Thêm ảnh mới: `python3 cong_cu/claude/png_palette.py` rồi `bash cong_cu/claude/pack_check.sh` (ngân sách mở game 6,1 MB, đang rất sát).
- Báo trước khi sửa thứ chủ game chưa ra lệnh.

## Kiểm thử
- Playwright + Chromium có sẵn. Thư viện `cong_cu/claude/rec_lib.js` (đồng hồ ảo `__step`, `L.open(ROOT,{w,h,mobile,dsf})`), `TDST.GG()` lấy G, vào Âm Giới bằng `amStartRun()`; sau `#amGo` chờ ~1,5 s thật rồi mới `__step`. Script cũ có đường dẫn `/home/user/HoaThan` cần sửa nếu khác.
- Chromium headless KHÔNG có GPU: số FPS không đại diện máy thật. Đo thời gian thật dùng đồng hồ thật, không dùng `__step` (dưới đồng hồ ảo mọi số ms = 0).
- Mở game qua http server (`cd game && python3 -m http.server 8123`), không mở `file://` (hỏng nhuộm màu).

## Trạng thái lúc chuyển phiên (27/11)
HEAD = `414672e` trên cả nhánh và `main`, cây sạch.

Đã xong phiên trước:
- UI 27/11: ô Thụ Lộc dùng `dtShort()` không cắt chữ; Lực chiến ở sảnh không đè số; HUD màn ≤720 px dời `#top` để không đè % kinh nghiệm.
- **Lag "như chơi tốc độ 0,25" ở Quỷ Môn Quan (chủ game chơi Chrome máy tính):** nguyên nhân là bước thời gian bị kẹp 50 ms/khung nên máy vẽ chậm thì cả game chậm theo; tải trước tài nguyên/màn loading chỉ chữa khựng lúc mới vào, KHÔNG chữa chậm suốt trận. Đã làm:
  - **Bảng đo hiệu năng** (`PERF`, `perfSet`, `perfTick`, mốc `pm0()/pm('tên')` trong `frame()`/`render()`): FPS, ms/khung, "tốc độ game xN", ms JS game vs phần trình duyệt vẽ, DPR, ZOOM, cỡ canvas, map, ms từng lớp. Bật bằng menu **Tạm dừng (II) trong trận → "Đo hiệu năng"**, hoặc thêm `?perf=1` vào link.
  - **Tùy chọn Độ nét** (`SET.res` Cao/Vừa/Thấp → DPR ≤ không giới hạn/1,5/1) trong menu Tạm dừng, áp ở `resize()`.
  - **Tự giảm tải theo thời gian:** khung trung bình >34 ms trong 2 s → `__mapLite` (tắt trang trí map); vẫn chậm thêm 2 s và Độ nét = Cao → `__resAuto=1` hạ DPR về 1 + thông báo "Máy đang chậm".
  - Đo headless: 1280×720 DPR2 ~25 FPS dù JS game ~3 ms (nặng ở trình duyệt vẽ canvas 2560×1440), DPR1 lên 60 FPS; 1920×1080 lớp `drawAmbient` ("sương/khói map", Hoàng Tuyền kiểu 'ash') ~11 ms/khung = ứng viên tối ưu.

## Việc đang làm dở (làm ngay)
Chủ game hỏi: **"sao tao không thấy cái đo hiệu năng nó nằm ở đâu"**. Hiện công tắc chỉ có trong menu Tạm dừng khi đang trong trận (và `?perf=1`).
1. Thêm "Đo hiệu năng" và "Độ nét" vào popover bánh răng ở sảnh (`footer.lbfoot`, dòng ~2009 `game/index.html`, cạnh `#lowfx3` "Giảm hiệu ứng"; nút `#lbGear` bật/tắt `.lbfoot.open`; handler `#lowfx3` ở dòng ~5159 và ~5238). Dùng chung `perfSet`/`resSync`/`SET.res`, đồng bộ trạng thái hai nơi.
2. Chụp 8 cỡ (mở popover), sửa tràn, commit, push nhánh + main, ghi CLAUDE.md.
3. **Đăng lại bản chơi thử** (phiên trước CHƯA đăng lại nên link chủ game đang mở có thể là bản cũ, không có bảng đo): chép `game/index.html` vào thư mục tạm `pub/index.html`, gọi Artifact publish với `url` = link artifact hiện tại của chủ game (hỏi lại nếu không biết; CLAUDE.md ghi `https://claude.ai/artifact/66MCZmMfKMjwuYrknQjNU1`), `root` = thư mục `game`, `files`/`overwrite_unread` = CHỈ các file assets mới/đổi. Nhắc chủ game link đang chia sẻ.
4. Trả lời chủ game chỉ đường rõ: sảnh → bánh răng → "Đo hiệu năng"; hoặc trong trận bấm II → "Đo hiệu năng"; hoặc thêm `?perf=1`. Nhờ chủ game vào Quỷ Môn Quan, bật bảng, chụp gửi.

## Việc treo (theo thứ tự chủ game duyệt: "làm theo thứ tự đi")
1. Map Âm Giới lag + vỡ nét: chủ game chọn **"nét hơn"** + màn loading tầng. Chờ số đo thật từ máy chủ game rồi tối ưu lớp nặng (ứng viên `drawAmbient`), sau đó làm nền 1:1 (chỉ Vong Xuyên có ảnh 1:1 ở `nguon/master_amgioi/vongxuyen_1to1/`, 6 map còn lại cần ChatGPT vẽ; nặng hơn ~4×, cân với ngân sách tải).
2. Icon thanh dưới sảnh: Tàng Bảo Các = rương bạc khóa đầu lâu; "cuộn giấy có mắt" chưa rõ ô nào. Cần chủ game gửi lại 2 ảnh (ảnh không còn trong phiên).
3. Chuông sảnh: ổn ở ≥667×375; ở 550×278 và 811×260 thẻ hồ sơ che chuông. Cần chủ game đồng ý đổi bố cục.
4. Lỗi nhuộm áo iPhone (mất nhân vật, chỉ còn kiếm): không tái hiện được trên Chromium; đã thêm chốt bỏ nhuộm khi đọc canvas trống; cần chủ game thử máy thật.
5. Cân bằng: làm SAU, không tự chỉnh.
6. Ảnh kiếm `kiem01..05`, `mucanh`: giữ hay xóa, chờ chủ game.
