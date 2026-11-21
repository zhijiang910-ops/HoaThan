# Tây Du Sinh Tồn · Bàn giao animation Kiếm +6

Mở `demo/TDST_PhaThe_Kiem6_LuotChem.mp4` để xem cùng một cụm quái với chuỗi A–B và A–B–C. Clip dùng nhân vật nữ. Từ giây 3 có đoạn quay chậm.

## Bản game để sửa tiếp

`game/index.html` và `game/assets/` là bản nền có màn hình yêu cầu xoay ngang trên điện thoại. Bản này có cơ chế mở nhát C ở Kiếm +6 và vẫn dùng động tác chém quét cũ trong game. Bản lướt chém trong video đang chờ chủ game duyệt. Chỉnh và xuất demo để duyệt trước khi tích hợp. Phần Liên kích đã được sửa riêng.

Nếu cần chạy game qua HTTP, mở thư mục gói rồi chạy `python -m http.server 8000 --directory game` và mở `http://localhost:8000`.

## Hướng đang thử cho nhát C

- Giữ nhịp A–B khi kiếm dưới +6. Từ +6, C là đòn kết chuỗi có động tác hạ người, kéo kiếm ra sau, lướt chém qua cụm quái và kết ở vị trí mới.
- Mục tiêu của mốc +6 là tạo một lựa chọn chiến đấu mới. Trong bản thử, đường lướt cho phép đánh nhiều quái xếp hàng và đổi vị trí khi bị vây. Tầm lướt và lực đánh trong clip chỉ để minh họa.
- Khi được duyệt, thử tầm lướt ngắn, chặn theo địa hình, mỗi mục tiêu trúng tối đa một lần và người chơi vẫn có thể chịu sát thương trong lúc thi triển. Kiểm tra với nút Lướt và bí tịch Truy Phong Kiếm để tránh xung đột. +9 vẫn là mốc kiếm khí.
- Dùng một kiếm xuyên suốt nhát C. Kiểm tra điểm nắm, hướng mặt và tay cầm, chuyển tiếp từ B sang C, cảm giác trụ chân và về tư thế thủ. Kiểm tra cả nhân vật nam và nữ trước khi bàn giao.

## Điểm sửa trong code

Trong `game/index.html`, tìm `startSwordCut`, `finishSwordCut`, `drawHeroFrame` và `weaponForge`. `lunge` hiện có trong `startSwordCut` là điều kiện Truy Phong Kiếm. Cần giữ cơ chế đó khi thử nhát C.

`demo/lunge.py` và `demo/render.py` là mã dựng clip minh họa, dùng sprite trực tiếp từ tài nguyên game. Sửa trực tiếp các keyframe trong `demo/lunge.py` để thử tư thế và thời điểm ra đòn. Dựng lại bằng Python, Pillow và FFmpeg có H.264:

```bash
python demo/lunge.py demo/TDST_PhaThe_Kiem6_LuotChem.mp4
```
