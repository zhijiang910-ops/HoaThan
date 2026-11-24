# Xuất lại Vạn Kiếm (đã chạy 24/11/2026)
1. Tải Godot 4.7.1 linux x86_64 (GitHub releases). Chép `nguon/pack_wuxia/Common_VFX` + `nguon/godot_bake/{Drive2.gd,Rec2.tscn}` ra thư mục tạm; thêm `viewport/transparent_background=true` vào mục `[rendering]` của `project.godot`.
2. Đổi `const WANJIAN_COUNT=36` trong `Shared/TrainingCore.gd` (đã dùng 16).
3. `xvfb-run -a godot --headless --path . --import` (BẮT BUỘC, không import thì khung trống), rồi
   `xvfb-run -a -s "-screen 0 1280x900x24" godot --path . --rendering-driver opengl3 --write-movie <out>/f.png --fixed-fps 30 res://Rec2.tscn`.
4. Khung k (0..45) của sheet = khung quay thứ `int(15+2.5*k)`, cắt cửa sổ góc trái-trên (442,365), rộng 838, cao 316 (khớp sheet cũ sai khác 0). Xếp 4 cột, 12 hàng → 3352×3792.
