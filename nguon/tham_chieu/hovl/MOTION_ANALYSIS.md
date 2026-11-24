# Phân tích video Hovl (quay màn hình trang ArtStation "Game VFX: Sword slash", 24/11/2026)
Nguồn: `nguon/tham_chieu/video/06_hovl_artstation_quay_man_hinh.mov` (chủ game quay 08:24, 512×1112, 30 fps, 15,1 s). Đây là bản quay màn hình **cùng nguồn** mà các ảnh COMPARE/guide của ChatGPT dựa vào: mốc giây trong ảnh guide (5,00–7,80 s) là giờ của VIDEO QUAY, không phải timeline gốc của đòn.

## Trang có 4 khối, chạy độc lập
| Khối | Vị trí trong khung quay (khi dừng cuộn 4,0–9,7 s) | Nội dung |
|---|---|---|
| GIF 1 | x22–489, y155–507 | Người nộm xám đánh kiếm **kèm VFX**, lặp **43 khung quay = 1,43 s** |
| GIF 2 | x22–489, y543–872 | **Chỉ VFX** nhiều kiểu chém, chu kỳ dài (**≈110 khung = 3,67 s**), khác nhịp GIF 1 |
| Ảnh 3 | bên dưới | Hình tĩnh người nộm + vệt cung lớn (không động) |
| Ảnh 4 | bên dưới | Hình tĩnh cảnh game + vệt chém dọc + tia trúng đất (không động) |
Không dùng mốc giây của video quay làm timeline đòn; phải cắt riêng từng GIF.

## GIF 1: chuyển động thật (1 chu kỳ 1,43 s, ms tính từ đầu chu kỳ)
Ảnh: `GIF1_nguoi_nom_danh_kiem_1chu_ky.png` (từng khung quay 33 ms, có nhãn). Video chậm x3: `GIF1_cham_x3.mp4`.
| Khoảng | Chuyển động |
|---|---|
| 0–230 ms | **Khuỵu thấp**, thân nghiêng, kiếm kéo sau/hông (tích lực) |
| 267–433 ms | Đứng dậy dần, kiếm dựng thẳng bên người |
| 467–567 ms | **Kiếm duỗi ngang trước mặt**, tay xa duỗi thẳng (nhát mở rộng, nằm ngang) |
| 600–867 ms | Kéo kiếm về thấp bên hông, vặn thân (chuyển thế) |
| 900–967 ms | **Giơ kiếm cao** chếch lên sau lưng (lấy đà lớn nhất) |
| 1000–1067 ms | **Vung kiếm xuống** chéo từ cao xuống thấp, thân đổ về trước |
| **1100–1267 ms** | **Điểm chạm + VFX**: lưỡi cong sáng xuất hiện sát đất cạnh mũi kiếm, mở rộng thành **một cung elip nằm ngang quanh chân**, nhiều đường streak mảnh bên trong, tia lửa bay dọc đường chém |
| 1300–1433 ms | VFX tan nhanh (1 khung mờ), thu thế, về tư thế khuỵu thấp đầu chu kỳ |
=> Cả chu kỳ là **một đòn lớn có đường kiếm đi: thấp-ra-sau → ngang trước → hông → cao → chém xuống**, kết bằng elip VFX; không phải ba đòn tách rời như ảnh guide ChatGPT.

## GIF 2: các kiểu VFX (ms trong chu kỳ quay đầu, 33 ms/khung)
Ảnh: `GIF2_chi_VFX_chu_ky.png`.
| Khoảng | VFX |
|---|---|
| 0–300 ms | Cung dọc mỏng "(" mũi nhọn phía trên, tia lửa nhỏ, tan còn đốm sáng + bụi sát đất |
| 767–933 ms | **Lưỡi liềm nằm ngang bay lên từ trái thấp sang phải**, lõi trắng, viền xanh điện, vài tia lửa mảnh |
| 1167–1333 ms | Quầng sáng tụ, rồi **cung elip ngang nhiều lớp streak** + tia lửa dọc mặt đất (giống VFX ở GIF 1) |
| 1567–1833 ms+ | **Lưỡi liềm lớn từ trên rơi xuống** thành cung dọc, **điểm trúng trắng chói + tia lửa tỏa** |
Đặc điểm chung: đầu cung nhọn, thân dày, đuôi thuôn, lõi trắng-viền xanh điện, nhiều đường streak bên trong, sáng đỉnh rồi tắt rất nhanh (3–5 khung).

## Hệ quả cho combo của game
1. Elip kết ở GIF 1 là **cung nằm ngang một lần, nhiều streak, đầu nhọn**, thấp sát chân. Elip PixelLab `k5c_*` hiện tại (vòng đều hiện nguyên) chưa giống.
2. Đường kiếm Hovl: tích lực thấp → giơ cao → chém xuống. Key pose C của tao nên bám chuỗi này; A/B nên lấy từ các VFX còn lại của GIF 2 (cung dọc từ trên xuống có tia trúng, lưỡi liềm ngang bay lên).
3. Nhịp: chạm ở khoảng **77%** chu kỳ (1100/1433 ms); VFX sống ~170–250 ms rồi thu thế.
4. Thân người nộm 3D nhìn từ trên xuống (camera chéo); nhân vật game nhìn nghiêng, nên chỉ lấy ngôn ngữ chuyển động, không sao chép tư thế từng khung.
