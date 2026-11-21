# Tây Du Sinh Tồn · Bàn giao toàn dự án

Dùng **game/index.html** và **game/assets/** làm bản nền. Đây là bản có yêu cầu xoay ngang điện thoại và các thay đổi solo đã ghép tới trước demo nhát C mới. Game chạy trên trình duyệt và dùng localStorage. Giải nén toàn bộ, mở thư mục gói rồi chạy `python -m http.server 8000 --directory game`. Mở http://localhost:8000 để chơi.

| Tệp hoặc thư mục | Công dụng |
|---|---|
| `TONG_HOP_TINH_NANG.md` | Tình trạng từng hệ thống, quy tắc đã chốt, số thử đang dùng và việc còn lại. Đọc trước khi sửa. |
| `tai_lieu/ANIMATION_KIEM_6.md` | Bàn giao riêng cho nhát C, vị trí code và cách dựng lại clip. Lệnh trong tài liệu chạy từ thư mục gốc của gói. |
| `demo/TDST_PhaThe_Kiem6_LuotChem.mp4` | So sánh A–B với A–B–C dạng lướt chém. Đây là demo nữ để duyệt. |
| `demo/lunge.py` và `demo/render.py` | Mã dựng clip, dùng chung tài nguyên trong game. Dựng lại cần Python, Pillow, FFmpeg và font DejaVu Sans. |
| `demo/video_tham_chieu/` | Các clip thử trước về A–B, tư thế đứng, Vạn Kiếm và các phương án nhát C. |
| `tai_lieu/ban_cu/` | Hồ sơ bàn giao qua các chặng, gồm mô tả kỹ thuật, lịch sử và kết quả kiểm thử đã ghi nhận. Thông số cũ có thể khác bản game hiện tại. |

Việc đang giao tiếp cho Claude là làm nhát C ở +6 đủ khác A–B về cả chuyển động lẫn công dụng. Xuất MP4 với cùng nhân vật và cùng cụm mục tiêu để chủ game duyệt. Chỉ tích hợp sau khi chủ game đồng ý. Phần Liên kích đã được Claude xử lý, giữ để kiểm thử hồi quy. Các hệ thống online nằm sau vòng chơi solo.

Khi gặp chênh lệch, dùng code game để xác định hành vi đang chạy, dùng tài liệu tổng hợp để xác định thiết kế đích. Các số thử, asset tạm và ý tưởng chưa duyệt có thể thay đổi.


## Cập nhật 22/11 (Claude) · đọc phần này trước

Bản nền vẫn là `game/index.html` + `game/assets/` (bản có yêu cầu xoay ngang), cộng thêm 2 thay đổi đã chạy thử:

1. **Kiếm nhân vật nam dài thêm ~30%** (theo yêu cầu chủ game). `game/assets/hero_nam.png` đã thay bằng sheet mới: mỗi ô frame thêm lề 12 px để mũi kiếm không bị cắt. `CHM.hero_nam` trong `index.html` đổi thành `w:131,h:138,ax:57,ay:119,pad:12`, toạ độ frame xếp lưới 16 cột. Avatar HUD cộng `M.pad` khi cắt mặt (`fr[1]+4+(M.pad||0)`). Công cụ dựng lại ở `cong_cu/kiem_nam/`: `python ext.py 0.30` đọc `hero_nam_goc.png` + `meta_goc.json`, xuất `hero_nam_long.png/.json` và ảnh so sánh. Đổi `0.30` để chỉnh độ dài; điểm chuôi/mũi từng frame nằm trong bảng `B`.
2. **Chặn tự thu phóng trên iPhone** khi chạm vào vùng chơi: `touch-action:none` cho `html, body, #cv`, chặn `touchstart/move/end` trên canvas, `gesture*`, `dblclick`, chụm hai ngón và chạm đúp ở chỗ không phải nút (ngay sau `cv.addEventListener('pointerup',joyEnd)…`). Joystick, Lướt và nút HUD vẫn hoạt động. Chưa xác nhận trên iPhone thật.

**Nhát C Kiếm +6 · Lướt Trảm: demo chờ duyệt, CHƯA ghép vào game.**
- Clip: `demo/nhat_c/TDST_NhatC_Kiem6_LuotTram_NamNu.mp4` (nam + nữ, cùng cụm 3 quái; tốc độ thật → quay chậm ×0,35 → so tắt/bật hiệu ứng).
- Dựng từ frame sprite thật, chỉ dùng scale/skew/translate/alpha nên canvas làm y hệt được. Dựng lại: `python demo/nhat_c/frames.py` rồi `python demo/nhat_c/c6.py out.mp4` (không tham số: ra `check.jpg`).
- Nhịp đề xuất: Lấy đà 0,18 s (co người sy .86, ngả sau, kéo lùi 12 px, ánh lóe kiếm) → Lướt chém 0,15 s (ease-out, skew +.30, dư ảnh 3 lớp, vệt chém) → Trượt dừng 0,14 s (bụi) → Thu thế 0,30 s. Frame dùng: nữ `attack1 → attack3 → attack5 → attack6/7 → idle`; nam `run0 → run3 → attack2[6] → attack2[7], attack[7] → idle` (xem `POSE` trong `c6.py`).
- Công dụng đề xuất: xuyên hàng, mỗi mục tiêu trúng đúng 1 lần, 15 sát thương (bằng `heavy` hiện tại), gắn Phá Thế 3 s, đổi vị trí. Khi ghép: tầm lướt ~160, dừng khi gặp địa hình, vẫn nhận sát thương, Lướt hủy được giai đoạn lấy đà, giữ Truy Phong (`lunge`), +9 vẫn bắn kiếm khí sau C. Điểm sửa: `startSwordCut`, `finishSwordCut`, `heroFrame/drawHeroFrame`.
- **Lỗi có sẵn trong game:** nhát B của nữ dùng anim `attack2` = động tác chưởng, không có kiếm (`P.swordGuard`/`P.avAlt` chọn `attack2`). Demo tạm dùng `attack[4..7]` cho B nữ. Sửa khi ghép C.

**Kiểm thử đã chạy trên bản này** (Playwright + Chrome, 844×390): vào sảnh → ải bằng hồ sơ nam, không lỗi JS; chạm liên tục vào nhân vật không đổi `visualViewport.scale`; joystick cảm ứng di chuyển được; nút Tạm dừng bấm được. Chưa chạy lại toàn bộ luồng solo trên bản nền này.

**Lưu ý giấy phép:** không công khai gói hay link game (asset cấm phân phối lại). Artifact game cũ đang để công khai, nên chuyển về riêng tư.


## Cập nhật 21/11 · Nhát C Lướt Trảm ĐÃ GHÉP vào game

Theo yêu cầu chủ game, nhát C Kiếm +6 trong `game/index.html` đã đổi từ chém quét sang Lướt Trảm theo demo `demo/nhat_c/`.

- Nhịp: Lấy đà 0,18 s (co người, ngả sau, lùi 8, ánh lóe kiếm) → Lướt chém 0,15 s (ease-out, tầm 160, skew .30, dư ảnh 3 lớp, vệt chém) → Trượt dừng 0,14 s (thêm 11, bụi) → Thu thế 0,30 s. Số chỉnh trong `CUT_C`.
- Frame lấy từ sheet gốc trước `setSwordPoses` (anim `cutC`): nữ `attack1 → attack3 → attack5 → attack6, attack7, idle0`; nam `run0 → run3 → attack2[6] → attack2[7], attack[7], idle0`.
- Công dụng: xuyên hàng, mỗi mục tiêu (kể cả vật phá được) trúng đúng 1 lần, 15 sát thương, gắn Phá Thế 3 s (có dấu hình thoi + vòng đếm trên đầu quái), đổi vị trí. Dừng khi chạm địa hình/mép ải, không miễn thương.
- Hủy: Lướt hủy được lúc lấy đà và lúc thu thế; trong pha lướt + trượt thì khóa. Chạy hoặc chiêu bấm tay cắt được thu thế. Truy Phong (`lunge`) giữ nguyên; +9 bắn kiếm khí khi vào pha trượt.
- Code: `startCutC`, `updCutC`, `drawCutC`, `endCutC`, `cutCPose`, `cutCDist` (ngay trên `VAN_KIEM`); fx `ctrail`, `ccut` trong `drawFx`.
- Lỗi "B nữ là chưởng" ghi ở trên thực ra đã được `setSwordPoses` xử lý trong game (B nữ dùng frame kiếm), nên không sửa thêm.
- Kiểm thử (Playwright, 1280×720): nam và nữ, 3 quái thẳng hàng → trúng 3/3, mỗi con ~15–16, dấu Phá Thế 3 s, chuỗi quay về A; Lướt lúc lấy đà hủy được, lúc lướt chém bị khóa; không lỗi JS.
