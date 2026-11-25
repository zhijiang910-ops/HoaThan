# Prompt gửi ChatGPT: Dạ Xoa + 4 quái thường mới cho Âm Giới

**Cách dùng:** mở cuộc trò chuyện ChatGPT mới, đính kèm ảnh mẫu phong cách: `nguon/tham_chieu/tat_ca_quai_amgioi.png` (toàn bộ quái đã vào game). Dán nguyên văn phần dưới. Làm MỖI LẦN MỘT CON, chờ duyệt rồi mới con tiếp.

---

## PROMPT (dán từ đây)

Bạn là họa sĩ pixel art cho game hành động chibi tên "Khử Tà Diệt Ma" (chủ đề âm phủ, khử tà). Tôi cần **5 quái thường mới**, đứng cạnh các quái đã có trong ảnh đính kèm (Vong Hồn, Ma Trơi, Âm Binh, Oan Hồn Xạ, Địa Ngục Khuyển, Quỷ Sai) mà không lệch phong cách.

### 1. Phong cách bắt buộc (đo từ quái đã có trong game)
- Pixel art thật, nhìn nghiêng sang phải (tôi sẽ lật), **hai chân chạm đất** (hoặc lơ lửng nếu là hồn), nền trong suốt.
- Chibi: đầu to, thân ngắn, **dễ đọc ở cỡ nhỏ**, nhưng vẫn có vẻ ma quỷ hung hãn, không dễ thương.
- **Viền ngoài đen mảnh 1 px**; bên trong không viền dày.
- Màu **dịu, hơi xỉn, tông xám xanh / nâu / đỏ sẫm**, mỗi chất liệu **4–5 tông** từ tối đến sáng. **Không chói, không cyan/neon, không phát sáng mờ, không gradient mượt, không khử răng cưa.**
- Tổng số màu khoảng **55–90 màu**.
- Không hiệu ứng khói/lửa/hào quang lớn bao quanh (tôi thêm VFX riêng). Chút sương/lửa nhỏ gắn vào hình thì được.
- Không chữ, không khung, không bóng nền.

### 2. Kích thước (quan trọng)
- **Chiều cao nhân vật 100–112 px** (các quái hiện có cao 98–111 px; Ma Trơi 80 px). Chiều rộng tối đa ~110 px (trừ vũ khí dài).
- Khung cuối: **canvas 160×160 px**, nhân vật đứng giữa, chân cách đáy 6 px, PNG RGBA nền trong suốt.

### 3. Cách làm để pixel THẬT (đây là chỗ hay hỏng)
Mô hình tạo ảnh hay cho "pixel giả" (lưới không đều, hoặc ảnh nhỏ phóng đôi). **Không được thế.** Làm như sau:
1. Tạo ảnh nguồn lớn (~1024 px), pixel art rõ khối, mảng màu phẳng, viền đen gọn, không gradient.
2. Dùng Python (code interpreter) chuyển về pixel thật bằng đúng đoạn mã sau (chỉnh `SRC`, `OUT`):
```python
from PIL import Image
import numpy as np
SRC='nguon.png'; OUT='quai_160.png'
im=Image.open(SRC).convert('RGBA')
a=np.array(im); bg=a[0,0,:3].astype(int)
if a[0,0,3]>0:
    d=np.abs(a[...,:3].astype(int)-bg).sum(2); a[...,3]=np.where(d<40,0,255)
im=Image.fromarray(a.astype(np.uint8)); im=im.crop(im.getbbox())
H=106; W=round(im.width*H/im.height)
im=im.resize((W,H),Image.BOX)
al=np.array(im)[...,3]>128
rgb=Image.fromarray(np.array(im)[...,:3]).quantize(colors=72,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).convert('RGB')
out=np.dstack([np.array(rgb),(al*255).astype(np.uint8)]); im=Image.fromarray(out)
C=Image.new('RGBA',(160,160),(0,0,0,0)); C.alpha_composite(im,((160-W)//2,160-6-H)); C.save(OUT)
arr=np.array(C); m=arr[...,3]>0
print('cao',np.where(m.any(1))[0].ptp()+1,'số màu',len({tuple(p) for p in arr[m][:,:3]}))
same=tot=0
for y in range(159):
    for x in range(159):
        if m[y,x] and m[y,x+1] and m[y+1,x] and m[y+1,x+1]:
            tot+=1
            if (arr[y,x,:3]==arr[y,x+1,:3]).all() and (arr[y,x,:3]==arr[y+1,x,:3]).all() and (arr[y,x,:3]==arr[y+1,x+1,:3]).all(): same+=1
print('tỉ lệ khối 2x2 cùng màu',round(same/max(tot,1),2),'(quá 0.6 là pixel giả)')
```
3. Gửi tôi **file PNG cuối `quai_160.png`** (không phải ảnh nguồn) kèm 3 số in ra. Nếu tỉ lệ 2x2 > 0.6 hoặc số màu ngoài 45–95, làm lại.

### 4. Năm quái (làm từng con)
1. **Dạ Xoa** (夜叉): quỷ canh gác âm phủ, da **xanh lục xám hoặc xanh chàm xỉn**, tóc đỏ sẫm dựng, hai nanh dưới nhô lên, tai nhọn, mắt vàng đục, thân trên trần cơ bắp quấn xích và dải vải rách, váy da thú, **cầm xoa ba chạc (đinh ba nhỏ) bằng sắt rỉ**. Dáng khom, hung dữ, nhanh nhẹn. Tông: xanh lục xám, đỏ sẫm, sắt rỉ.
2. **Cương Thi** (殭屍): xác chết nhảy, mặc quan phục Thanh (áo xanh đen, mũ quan) bạc màu, **lá bùa vàng chữ đỏ dán trán**, da xám xanh, **hai tay duỗi thẳng phía trước**, móng dài, dáng đứng cứng. Tông: xanh đen, xám, vàng bùa.
3. **Chỉ Trát Nhân** (紙紮人): người giấy cúng âm phủ, thân giấy trắng ngà nhàu, má hồng tròn, mắt chấm đen, áo giấy đỏ-vàng, **tay cầm một đèn lồng giấy nhỏ**, vài chỗ rách để lộ khung tre bên trong. Cười gượng, rợn. Tông: trắng ngà, đỏ, vàng, nâu tre.
4. **Thủy Quỷ** (水鬼): hồn chết đuối, da xanh xám trương phềnh, tóc ướt dính rong rêu, rong rêu và vải ướt quấn người, hốc mắt tối, bước lê, **nhỏ nước**. Tông: xanh rêu, xám xanh, nâu ướt.
5. **Điếu Tử Quỷ** (吊死鬼): hồn treo cổ, thân dài mảnh hơi lơ lửng, **lưỡi đỏ dài thè ra**, tóc đen dài rủ che nửa mặt, áo tang trắng rách, **đoạn dây thừng đứt quấn quanh cổ buông xuống**. Tông: trắng xám, đen, đỏ sẫm (lưỡi), nâu (dây).

### 5. Quy trình trả lời
Với mỗi con: (a) mô tả ngắn 2 dòng bạn sẽ vẽ, (b) tạo ảnh nguồn, (c) chạy đoạn mã mục 3, (d) gửi `quai_160.png` + 3 số tự kiểm. Đợi tôi "duyệt" hoặc góp ý rồi mới làm con tiếp.

---

## Sau khi nhận ảnh (việc của Claude, 0 lượt PixelLab nếu ảnh sạch)
1. Đo số màu, tỉ lệ khối 2×2, độ cao; sửa nhẹ bằng code (pixel lẻ, viền 1 px, căn đáy, lật hướng).
2. Vào game: `game/assets/<id>_am.png`, khai báo `CHM` (trước vòng tạo `CH`, `proc:'walk'` hoặc `'hover'`), thêm `ESPR`/loại quái mới trong `ET` và pool của chặng Âm Giới (`AM_ZONES`), hệ số hiển thị chọn để cao ngang quái cũ.
3. Chỉ khi lưới còn lệch mà code không sửa được mới tính PixelLab (~10 lượt/con, báo trước).
