# Phân tích video tham chiếu combo Kiếm A–B–C (24/11/2026)

Chưa sửa animation game. Mọi thứ dưới đây chỉ là phân tích để chủ game duyệt.

## 1. Phân loại nguồn
| Nguồn | Là gì | Dùng làm gì |
|---|---|---|
| `tham_chieu/anh/17_SWORD_COMBO_KEYFRAME_GUIDE_uu_tien.png` | Bảng keyframe chủ game gửi: A1–A7, B1–B7, C1–C12 + timing, ghi "Based on Hovl Clip (Pose & VFX)" | **Chuẩn ưu tiên cao nhất** cho combo mới |
| `video/03_vo_thuat_3_don.mov` (576×1024, 8,3 s, 30 fps, h264, giải mã được) | Người thật cầm đao dài, bài đao pháp nhiều thế, **không có VFX**, camera đổi góc liên tục | Tham khảo cách dồn trọng tâm chân, hông, vai. **Không khớp cấu trúc 7/7/12 của guide** |
| `video/02_master_don_danh.mov` (1024×576, 53,6 s, 30 fps, h264, giải mã được) | Game 3D Ngộ Không (côn vàng) trên nền tuyết, VFX lửa/vàng/đá vụn dày, không phải kiếm | Tham khảo độ dày VFX, nhịp bùng nổ. **Không phải clip pose hay VFX của guide** |
| Sprite master nam/nữ | `nguon/pixellab/pl/xt_nam_first.png`, `xd_nu_first.png` (128 canvas, mặt hướng đông, kiếm cầm tay xa) | Nền để dựng key pose |

**Thiếu:** clip "Hovl" của guide (cả clip pose lẫn clip VFX xanh điện) **không có trong repo**. Tên "02_master_don_danh" không khớp nội dung (là Ngộ Không 3D). Cần chủ game gửi hai clip này nếu muốn tái hiện 98–99%.

## 2. Video 03 (đao pháp) theo mốc thời gian
Contact sheet: `frames/v03_tongquan_6fps_1/2.png`, chi tiết 15 fps: `frames/v03_chitiet_*`. Video chậm x3 có timestamp: `v03_cham_x3.mp4`.
| Mốc | Chuyển động |
|---|---|
| 0,0–1,0 s | Đứng thẳng, đao gác vai, chuẩn bị |
| 1,0–2,3 s | Bước chân ra, nâng đao lên, hạ thấp vào tấn rộng, đao ngang trước ngực |
| 2,3–3,5 s | Tấn rộng, đao kéo ngang qua mặt rồi nâng cao qua đầu (tụ lực) |
| 3,5–4,3 s | Nhún bật, hạ xuống tấn thấp, đao rút ra sau, sát đất |
| 4,5–5,0 s | Lao tới, hất đao từ thấp lên |
| 5,0–6,2 s | Xoay người, nâng đao sau lưng, bổ từ trên xuống (6,17 s) |
| 6,5–7,5 s | Bước dài, đao kéo thấp sát đất phía trước, hất lên |
| 7,5–8,3 s | Thu thế, đao dựng đứng |
Đúc kết dùng được: chân luôn rộng và thấp lúc ra đòn, hông và vai dẫn trước kiếm, đường kiếm đi từ thấp-ra-sau → cao → chém xuống/ngang, thu đòn bằng việc dựng kiếm. Không có điểm chạm hay VFX để đo.

## 3. Video 02 (Ngộ Không 3D)
Contact sheet: `frames/v02_tongquan_2fps_1..4.png`, `frames/v02_chitiet_2-10s_4fps_1.png`. Video chậm x3: `v02_4.5-8.5s_cham_x3.mp4`.
- 2,0–4,0 s: tụ lực, hào quang vàng bùng ra quanh người.
- 4,5–5,0 s: nhảy chém, vệt vàng dài chéo ngang màn hình.
- 5,0–6,5 s: bùng nổ đỏ/cam, tia lửa dày phủ cả màn.
- 7,0–8,0 s: vụ nổ vàng rồi bụi đá vụn bay lên.
- Từ 9 s: vệt trắng-vàng cong, tia lửa nhỏ.
Dùng làm tham chiếu **độ dày, nhiều lớp, tia lửa**, không phải đường kiếm hay tư thế. Màu vàng/đỏ khác với tông xanh điện của guide.

## 4. Guide keyframe (chuẩn ưu tiên)
| Đòn | Số khung | Thời lượng guide | Mô tả (từ ảnh) |
|---|---|---|---|
| A · Diagonal Downward Slash | 7 (A1–A7) | 5,00–5,96 s ≈ 0,96 s | A1 chuẩn bị, A2 nâng/tụ, A3 chém xuống (vệt xanh), A4 điểm chạm lớn nhất, A5 theo đà, A6 hồi, A7 sẵn sàng nối |
| B · Sweeping Slash (follow-up) | 7 (B1–B7) | 5,84–6,56 s ≈ 0,72 s | B1 bắt đầu từ cuối A, B2 kéo kiếm về, B3 bắt đầu quét, B4 quét, B5 điểm chạm (quét rộng), B6 theo đà, B7 hồi |
| C · Finisher, Elliptical Sweep | 12 (C1–C12) | 6,56–6,78+ s, ghi ≈ 1,12 s | C1 tụ, C2 nâng, C3 hạ, C4 chém xuống, C5 mở rộng, C6–C8 elip trước/hông/sau, C9–C10 mờ dần, C11 hồi, C12 kết |
| Tổng | 26 | ≈ 2,80 s | |

**Điểm cần chủ game quyết** (guide không khớp nhau):
1. Mốc C ghi 12 khung cách nhau 0,02 s (6,56–6,78 s) nhưng mô tả ≈ 1,12 s. Hai số này không thể cùng đúng.
2. Thời lượng A = 0,96 s dài hơn nhiều nhịp đánh thường hiện tại trong game (`P.atkT=0.22`, C khoảng 0,5 s). Cần chọn: giữ nguyên số khung và rút ngắn thời gian, hay đổi tốc độ đánh.
3. A là chém chéo từ trên xuống, B là quét ngang rộng, C là chém xuống rồi quét elip một vòng. Guide dặn "một vòng elip duy nhất, không thêm VFX sau khi elip bắt đầu tan". Yêu cầu của chủ game cũng dặn không xoay nhân vật giả. Vòng elip do VFX lo, thân nhân vật không lật.
4. Vệt xanh điện/trắng trong guide đổi tông so với vệt `zs1-3` hiện có trong game. Cần chốt dùng lại vệt cũ hay VFX mới từ PixelLab.

## 5. Bước tiếp theo (chờ duyệt)
Dựng bảng key pose A/B/C trên sprite master nam và nữ theo guide (chuẩn bị, ra đòn, điểm chạm, thu kiếm, mốc chuyển tiếp). Chưa gọi PixelLab, chưa thay animation trong game.
