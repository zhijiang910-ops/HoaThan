# Prompt gửi ChatGPT: 5 mini-boss Âm Giới (đồng bộ phong cách master)

**Cách dùng:** mở một cuộc trò chuyện ChatGPT mới, đính kèm 2 ảnh: `gui_chatgpt_minoboss/master_mau_hacvo_bachvo_madien_quysai.png` (các hình đã vào game, đây là chuẩn phong cách) và ảnh `nguon/tham_chieu/minoboss_phacthao_mau.png` (tông màu gợi ý). Dán nguyên văn phần dưới. Làm MỖI LẦN MỘT CON để chất lượng đồng đều.

---

## PROMPT (dán từ đây)

Bạn là họa sĩ pixel art cho game hành động chibi tên "Khử Tà Diệt Ma" (chủ đề âm phủ, khử tà). Tôi cần 5 mini-boss, **đúng phong cách các hình mẫu tôi đính kèm** (Hắc Vô Thường, Bạch Vô Thường, Mã Diện, Quỷ Sai). Chúng đã nằm trong game, hình mới phải đứng cạnh chúng mà không lệch phong cách.

### 1. Phong cách bắt buộc (đo từ hình đã có trong game)
- Pixel art thật, nhìn nghiêng/chếch 3/4 sang trái hoặc phải đều được (tôi sẽ lật), **đứng thẳng, hai chân chạm đất, nền trong suốt**.
- Tỉ lệ chibi: đầu to, thân ngắn, tay chân ngắn vừa phải, nhưng nhìn oai, có phong thái "ma tướng" chứ không dễ thương.
- **Viền ngoài đen mảnh 1 pixel** bao toàn bộ hình; bên trong KHÔNG viền dày.
- Màu dịu, hơi xỉn, tô bóng ít nhưng có chiều sâu: mỗi chất liệu (da, giáp, vải, kim loại) dùng **4–5 tông** từ tối đến sáng, không chói, không bão hòa mạnh, không gradient mượt, không hiệu ứng phát sáng mờ.
- Tổng số màu khoảng **80–110 màu** (các hình mẫu: 75–112 màu). Không khử răng cưa (anti-alias), không nhòe, không đổ bóng nền, không chữ, không khung.
- Có đồ vật nhỏ cho thấy chi tiết (xích, chuông, xương, dây, cờ...), giống hình mẫu.
- Không chồng hiệu ứng khói, lửa, hào quang lớn bao quanh (tôi thêm VFX riêng sau). Một chút lửa/sương nhỏ gắn vào hình thì được.

### 2. Kích thước
- **Chiều cao nhân vật 130–145 px** (Quỷ Sai thường cao 106 px, trùm cao 140–165 px; mini-boss nằm giữa). Chiều rộng tối đa khoảng 150 px.
- Khung ảnh cuối cùng: **canvas 192×192 px**, nhân vật đứng chính giữa, chân cách đáy 6–8 px, nền trong suốt (PNG RGBA).

### 3. Cách làm để pixel THẬT (quan trọng, đây là chỗ hay hỏng)
Các mô hình tạo ảnh thường cho ra "pixel giả": lưới không đều, pixel to nhỏ lẫn lộn, hoặc ảnh nhỏ phóng to gấp đôi. **Không được thế.** Làm như sau:
1. Tạo ảnh nguồn lớn (khoảng 1024 px), phong cách pixel art rõ khối, mảng màu phẳng, viền đen đậm gọn, không gradient.
2. Dùng công cụ Python của bạn (code interpreter) để chuyển về pixel thật, theo đúng đoạn mã này (chỉnh `SRC`, `OUT`):
```python
from PIL import Image
import numpy as np
SRC='nguon.png'; OUT='minoboss_192.png'
im=Image.open(SRC).convert('RGBA')
# 1) xóa nền: nếu nền chưa trong suốt, dùng màu góc ảnh làm nền rồi cắt
a=np.array(im); bg=a[0,0,:3].astype(int)
if a[0,0,3]>0:
    d=np.abs(a[...,:3].astype(int)-bg).sum(2); a[...,3]=np.where(d<40,0,255)
im=Image.fromarray(a.astype(np.uint8))
im=im.crop(im.getbbox())
# 2) thu về cao đúng 138 px, KHÔNG làm mượt: BOX trung bình rồi lượng tử hóa màu
H=138; W=round(im.width*H/im.height)
im=im.resize((W,H),Image.BOX)
al=np.array(im)[...,3]>128
rgb=Image.fromarray(np.array(im)[...,:3])
rgb=rgb.quantize(colors=96,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).convert('RGB')
out=np.array(rgb); out=np.dstack([out,(al*255).astype(np.uint8)])
im=Image.fromarray(out)
# 3) đặt vào canvas 192x192, chân cách đáy 7 px
C=Image.new('RGBA',(192,192),(0,0,0,0)); C.alpha_composite(im,((192-W)//2,192-7-H))
C.save(OUT)
# 4) tự kiểm
arr=np.array(C); m=arr[...,3]>0
print('cao',np.where(m.any(1))[0].ptp()+1,'số màu',len({tuple(p) for p in arr[m][:,:3]}))
# không được có khối 2x2 cùng màu chiếm quá nhiều (dấu hiệu phóng đôi)
same=0;tot=0
for y in range(0,191):
    for x in range(0,191):
        if m[y,x] and m[y,x+1] and m[y+1,x] and m[y+1,x+1]:
            tot+=1
            if (arr[y,x,:3]==arr[y,x+1,:3]).all() and (arr[y,x,:3]==arr[y+1,x,:3]).all() and (arr[y,x,:3]==arr[y+1,x+1,:3]).all(): same+=1
print('tỉ lệ khối 2x2 cùng màu',round(same/max(tot,1),2),'(mẫu của game khoảng 0.15–0.30; quá 0.6 là pixel giả)')
```
3. Gửi tôi **file PNG cuối `minoboss_192.png`** (không phải ảnh nguồn lớn), kèm 3 con số in ra ở bước tự kiểm. Nếu tỉ lệ 2x2 > 0.6 hoặc số màu ngoài 70–120, **làm lại** (tạo lại ảnh nguồn rõ khối hơn).

### 4. Năm mini-boss (làm từng con, chờ tôi duyệt rồi mới làm con tiếp)
1. **Huyết Sát Ma Tướng** (tầng 4–5): ma tướng cao to nhất trong 5 con, thân đỏ máu sẫm, giáp xương và sừng trâu cong, vai có gai, cầm chùy xương khổng lồ; nét hung hãn. Tông: đỏ máu, xám xương, đen.
2. **Nghiệt Hỏa Quỷ Vương** (tầng 7–8): quỷ vương lửa nghiệt, da đỏ cam sẫm, tóc là ngọn lửa **xanh lam** nhỏ, giáp đen viền lửa cam, cầm đinh ba. Tông: đen, cam, xanh lam điểm.
3. **Thiết Lao Ma Tướng** (tầng 10–11): ma tướng ngục sắt, giáp xám sắt rỉ, **xiềng xích quấn quanh người**, mặt nạ sắt có khe mắt đỏ mờ, cầm búa gông nặng. Tông: xám sắt, nâu rỉ, một chút đỏ.
4. **Vong Xuyên Quỷ Tướng** (tầng 13–14): quỷ tướng sông Vong Xuyên, da xanh lục nhạt như xác ngâm nước, rong rêu và vải ướt rách quấn người, mái chèo xương làm vũ khí. Tông: xanh nước, xanh rêu, trắng xương.
5. **Đế Thính** (tầng 16–17): thần thú canh điện Diêm La, thân **sư tử vàng sẫm** (bốn chân vẫn đứng dáng chibi chắc chắn), **một sừng**, mắt sáng, bờm viền, đeo chuông đồng và dây đỏ. Tông: vàng sẫm, nâu, đỏ, đồng.

### 5. Quy trình trả lời
Với mỗi con: (a) mô tả ngắn 2 dòng bạn sẽ vẽ, (b) tạo ảnh nguồn, (c) chạy đoạn mã ở mục 3, (d) gửi `minoboss_192.png` và số liệu tự kiểm. Đợi tôi nói "duyệt" hoặc góp ý rồi mới làm con tiếp theo.

---

## Sau khi nhận ảnh (việc của Claude, 0 lượt PixelLab nếu ảnh sạch)
1. Đo: số màu, tỉ lệ khối 2×2, độ cao (so với mẫu 140–165 px của trùm và 106 px của Quỷ Sai).
2. Sửa nhẹ bằng code: dọn pixel lẻ, làm đều viền 1 px, căn đáy, gom màu, lật hướng nếu cần.
3. Chỉ khi ảnh còn lưới lệch hoặc méo dáng mà code không sửa được thì mới tính PixelLab (khoảng 10 lượt mỗi con, báo trước cho chủ game).
4. Vào game: `ESPR.<id>=['<tên>_am',hệ số]`, `ET`/`AM_BOSSES` đã có sẵn; chuyển động ảnh tĩnh bằng code (`proc:'walk'`).
