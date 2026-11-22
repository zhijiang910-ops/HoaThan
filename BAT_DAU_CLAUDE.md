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


## Cập nhật 22/11 · Nhát C đổi theo clip tham chiếu của chủ game

Chủ game gửi clip quay màn hình (đòn đâm lướt xuyên mục tiêu) và yêu cầu nhát C làm giống. Đã đổi phần cảm giác, giữ nguyên công dụng:
- Nhịp nhanh, gắt hơn: lóe kiếm 0,13 s → đâm lướt 0,13 s → trượt 0,12 s → thu thế 0,26 s (`CUT_C`, tầm 170, trượt thêm 14). Tư thế lướt ngả mạnh hơn (skew .36).
- Lóe kiếm: quầng sáng vàng trắng ở mũi kiếm phía trước, có tia ngang.
- Lúc bắt đầu lướt phóng **tia kiếm trắng** đâm thẳng dài hơn tầm lướt (fx `cbeam`).
- **Vệt lướt vàng** dày, mờ dần về phía sau (fx `ctrail`), dư ảnh nhuộm vàng.
- Trúng: quái **trắng xóa** 0,14 s, **nổ răng cưa cam** (fx `cburst`, mục tiêu đầu to nhất), rung màn hình 4. Đẩy lùi giảm còn 12 để nhân vật xuyên hẳn qua.


## Cập nhật 22/11 (đợt 2) · Trải nghiệm, chủ game duyệt mục 1–17 (trừ 18 Trúc Cơ Đan)

- **Chạy lùi:** sheet nam xếp frame chạy ngược (chân trụ trượt về trước). Đảo lại khi nạp (`A.run.f.reverse()`), giữ frame phanh cũ. Nhịp chân theo quãng đường (`P.runPh`, `runStride` nam 10,5 / nữ 8,5). Nữ vẫn là động tác đi bộ → chờ frame chạy mới.
- **A/B:** khựng hình (`G.hitstop`, A 35 ms, B 55 ms, C 60 ms), vệt chém vẽ tay `sarc` (trắng, viền tối, B có viền vàng), vết cắt + tia lửa trên 3 mục tiêu đầu, số sát thương to dần theo liên kích (`num(...,sc)`), dồn bước khi đứng yên, B rung nhẹ. Bỏ tia xanh `imp` cho đòn thường kiếm.
- **HUD điện thoại** (khối CSS "Điện thoại ngang (22/11)"): chiêu 54–58 px, Lướt 70 px, bỏ nhãn BẤM/TỰ/NỘI/phím, Hóa Thân bên trái cụm chiêu, chữ ≥10 px. Camera điện thoại 390/470 (trước 390/600). Viền tối 1 px + vòng sáng chân nhân vật (`HERO.dark`, `heroRing`). Nền tuyết phủ tối 16%. Nhiệm vụ thu gọn mặc định trên điện thoại, tiêu đề hiện "Nhiệm vụ x/y".
- **Hướng dẫn:** bước 1, 2, 4 là dải gợi ý không dừng game (`#tut.hint`), chỉ bước Lướt còn dừng.
- **Sảnh:** ẩn Bang Hội, Chiêu Mộ (`hide:1`); ẩn "Tiếp tục ải" khi không có; `giveStarterSword()` tặng Thanh Phong Kiếm +0 (cả hồ sơ cũ chưa có vũ khí). Vượt Ải bỏ dòng ghi nguồn ở tiêu đề. Nút màn nghỉ ghi "Chọn thêm N thẻ"/"Chọn đường đi".
- **Nhịp ải:** ải 1 có thêm Yêu binh cận chiến (đường đâm đỏ), ải 2 thêm Lang yêu (đường lao). Mỗi ải thường có "Phục kích!" hai phía ở 55% mục tiêu hạ gục. Giữ Lướt ≥0,3 s khi kiếm +6 → nối Lướt Trảm vào mục tiêu gần nhất (hồi 3 s).
- **Chờ frame:** prompt trong `frame_moi/PROMPT_ChatGPT.md` (chạy nữ, nhát C, chém A/B, tranh sảnh).

## Cập nhật 22/11 (đợt 3)
- **A/B chọn lại frame theo logic ra đòn** (`setSwordPoses`): nam A `2,3,3,4,5,5,5,7` (giơ cao → khụy bổ xuống → dứt đòn → thủ), B `6,6,6,14,14,12,13,13` (kéo sau hông → chém ngang → hất lên); nữ A `1,0,0,3,4,5,5,5` (vung qua đầu → bổ chéo xuống), B `5,5,4,6,7,7,7,6` (từ thấp hất lên). Frame chạm địch là ô thứ 4. Thêm chuyển động thân khi đánh (`tf` trong `drawPlayer`): 0–35% ngả sau co người, 35–55% đổ người về trước, sau đó trả về.
- **Nữ cắt bớt dải lụa** (giữ màu gốc): `cong_cu/nu_lua/nu_edit.py <hero_nu_goc_lua.png> <out.png> goc 5`. Bản gốc còn lụa lưu ở `game/assets/hero_nu_goc_lua.png`. Script chỉ cắt điểm xanh lụa (b−r ≥ 38) nằm xa thân váy quá 5 px, vá lỗ tóc, xóa cụm vụn < 40 điểm. Bảng master nữ cần dựng lại theo sheet mới.

## Cập nhật 22/11 (đợt 4) · Đồng bộ toàn bộ theo gói Wuxia Pixel Assets Vol.2 (bản trả phí, Integrated)

Chủ game đã mua gói Integrated (19,99 USD) và giao: giữ toàn bộ Wuxia, đồng bộ phong cách, tự quyết. **Không đưa asset của gói lên git** (giấy phép cấm đăng file gốc/đã sửa công khai); `game/assets/` đã nằm trong `.gitignore`.

- **Nhân vật chính đổi sang nhân vật Wuxia** cầm kiếm nhất quán khi đứng, đi, chém (sửa vụ "chạy cất kiếm, đứng lại cầm kiếm"):
  - Nam = Huyền Tiêu Kiếm Tông · Nam đệ tử (玄霄剑宗-男弟子): A = attack, B = attack_secondary.
  - Nữ = Xích Diễm Đao Môn · Nữ đệ tử (赤焰刀门-女弟子): chỉ có 1 bộ đòn → A = attack, B = đâm thẳng ghép từ attack `[2,2,1,6,6,6,7,7]`.
  - Sheet dựng bằng `cong_cu/wuxia_sheet.py <04_Integrated> "<tên>" <id> <ra>`, meta dán vào `Object.assign(CHM,{hero_nam,hero_nu})`. Bỏ `setSwordPoses`, đảo frame chạy, cắt lụa và kéo dài kiếm cũ (không còn áp dụng). Chạy = walk 8 frame, `runStride` 13. Avatar HUD dùng `meta.face`.
  - Nhát C dùng: nam `attack2[2] → attack2[6] → attack[5] → attack[7] → idle`, nữ `attack[2] → attack[6] → attack[4] → attack[7] → idle`.
- **Trùm ải 5** tạm dùng sprite Tượng Quỷ Chiến Sĩ Nanh Xám (`quytuong`, ESPR boss ×1,45) thay Ngưu Ma Vương vẽ bằng code.
- **Hóa Thân, phân thân Ngộ Không, Hỏa yêu** (vẽ bằng code, Wuxia không có) được vẽ qua `pixWrap` ở 1 điểm ảnh = 1 đơn vị rồi phóng lên cho cùng mật độ pixel. Tạm thời, chờ sprite PixelLab (prompt trong `pixellab/PROMPT_PIXELLAB.md` của gói gửi chủ game).
- **Icon trang bị**: `gear.png` thêm 2 hàng icon Items_64 của Wuxia cho phẩm Phàm/Linh/Bảo và ô Đai/Găng (`cong_cu/gear_build.py`), phẩm Tiên trở lên giữ icon pháp bảo cũ. `GCELL` cập nhật, `.cxwb .gi` background-size 1000% 500%.
- Vật phá được, vệt chém, hiệu ứng Như Lai/Thái Cực/Vạn Kiếm, nền đất và 13 âm thanh vốn đã là Wuxia (đối chiếu hash), giữ nguyên.
- Giữ asset ngoài Wuxia: 14 NPC HOANTDZ (chân dung hội thoại), bình thuốc, tranh núi mực, nét mực, hào quang Hóa Thân, Google Fonts.
