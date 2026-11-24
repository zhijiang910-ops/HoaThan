# MASTER ÂM GIỚI: brief tạo hình cho ChatGPT

Dùng cho game pixel art **Khử Tà Diệt Ma 驅邪滅魔** (đánh 18 tầng địa ngục). Cần vẽ **boss, Tinh Anh và quái mới**. Đây là bản đặc tả để mày đưa ChatGPT, kèm ảnh `THAM_CHIEU_PHONG_CACH.png` (sprite thật của game, ChatGPT phải bám đúng phong cách này).

## 1. Prompt gốc (dán vào ChatGPT, đính kèm ảnh tham chiếu)

> Draw ONE game character sprite in pixel art, matching exactly the style of the attached reference image.
> Style rules (must follow): chibi proportions, big head and short body; thin dark outline (about 1 px, near-black); muted, desaturated palette; little shading (2 to 3 tones per colour, no glossy highlights, no glow, no gradients); hard pixel edges, no anti-aliasing, no blur; dark gloomy Chinese underworld mood.
> Pose: standing idle, **side view facing right**, full body visible, weapon or prop held in front hand, feet at the bottom of the image.
> Output: transparent PNG background, single character centred, no ground, no shadow, no text, no frame, no extra characters. Size: [KÍCH THƯỚC Ở MỤC 3] pixels.
> Character: [DÁN MÔ TẢ TỪ MỤC 3]

Gợi ý: yêu cầu ChatGPT làm **một con mỗi lần** và gửi kèm ảnh tham chiếu mỗi lần để khỏi lệch phong cách.

## 2. Luật phong cách (chủ game đã chốt)
- Chibi đầu to thân ngắn, viền đen mảnh, màu dịu, tô bóng ít. KHÔNG vẽ dáng người thật cao 7–8 đầu, KHÔNG màu chói, KHÔNG tương phản gắt (chủ game từng chê "như bị trúng độc").
- Nhìn nghiêng sang phải, cùng tỉ lệ với các sprite trong ảnh tham chiếu.
- Chất liệu cổ trang Á Đông, không hiện đại.
- Nền trong suốt, mép pixel cứng.

## 3. Danh sách cần vẽ

Kích thước canvas gợi ý: trùm 192×192 px, Tinh Anh 160×160 px, quái thường 128×128 px (nhân vật chiếm khoảng 80% chiều cao khung).

### A. Trùm (7 con; ảnh mẫu dáng và phong cách chuẩn: `HAC_VO_THUONG_master.png`, đã duyệt)
| Tầng | Tên | Mô tả hình |
|---|---|---|
| 3 | **Ngưu Đầu** | Người đầu trâu/bò: đầu bò đen có hai sừng cong lớn, mũi có khuyên, thân người vạm vỡ, giáp da đen, cầm chĩa ba hoặc búa. Cặp với Mã Diện. (Chủ game KHÔNG duyệt dùng hình Ngưu Ma Vương, nhìn không ra nét Ngưu Đầu.) |
| 3 | **Mã Diện** | (Hình hổ hiện chỉ là tạm.) Người đầu ngựa: đầu ngựa nâu, bờm đen, tai dựng, áo giáp da nâu, cầm đinh ba hoặc chùy. Cặp với Ngưu Đầu (cùng cao to, cùng bộ giáp sơ sài). |
| 6 | **Hắc Vô Thường** | Áo dài đen, mũ ống cao đen có chữ trắng ở mặt mũ, lưỡi đỏ dài thè xuống ngực, dải trắng ngang hông, tay cầm gậy khóc tang hoặc phất trần. Mặt trắng nhợt, mắt đen. |
| 9 | **Bạch Vô Thường** | Áo dài trắng, mũ ống cao trắng có chữ đen, lưỡi đỏ dài, tay cầm quạt hoặc phướn trắng. Mặt trắng nhợt. Cặp đối xứng với Hắc Vô Thường (cùng dáng). |
| 12 | **Mạnh Bà** | Bà lão còng lưng nhẹ, tóc bạc búi, áo vải xám xanh rách, tay cầm muôi lớn múc canh, bên cạnh hoặc sau lưng có vạc canh nhỏ bốc khói xanh nhạt. Vẻ mặt hiền nhưng đáng sợ. |
| 15 | **Phán Quan** | Quan âm phủ: áo bào đỏ thẫm, mũ quan cánh chuồn đen, râu đen, mặt đỏ sẫm, một tay cầm bút lớn (phán quan bút), tay kia cầm sổ sinh tử. Dáng uy nghiêm. |
| 18 | **Diêm Vương** | Vua âm phủ: mũ miện có tấm miện phẳng và dải châu rủ, long bào đỏ đen có hoa văn vàng nhạt, mặt đỏ, râu dài, một tay cầm hốt hoặc trượng. Lớn nhất, đứng uy nghi. |

### B. Tinh Anh (5 con, cao 160 px, tối đa 3 màu chủ đạo mỗi con để dễ phân biệt)
| Tầng | Tên | Mô tả hình |
|---|---|---|
| 4–5 | **Huyết Sát Ma Tướng** | Tướng ma giáp đỏ máu, sừng, kiếm bản rộng. |
| 7–8 | **Nghiệt Hỏa Quỷ Vương** | Quỷ ngực trần, tóc và vai bốc lửa cam, chùy lửa. |
| 10–11 | **Thiết Lao Ma Tướng** | Cai ngục giáp sắt xám, xích lớn quấn người, chìa khóa to bên hông. |
| 13–14 | **Vong Xuyên Quỷ Tướng** | Tướng ma xanh nước, rong rêu bám áo giáp, giáo ba chĩa. |
| 16–17 | **Đế Thính** | Linh thú giống sư tử/kỳ lân (dáng bốn chân hoặc đứng hai chân), lông vàng nhạt, sừng đơn, mắt sáng; hình dáng thần thú canh điện Diêm La. |

### C. Quái thường mới (6 con, 128 px)
| Chặng | Tên | Mô tả hình |
|---|---|---|
| T12–14 Vong Xuyên | **Thủy Quỷ** | Hồn ma ướt sũng, tóc rong rêu, da xanh xám, lơ lửng. |
| T7–9 Nghiệt Kính | **Kính Quỷ** | Bóng ma cầm gương đồng vỡ, áo rách, bắn xa. |
| T4–6 Bỉ Ngạn | **Câu Hồn Sứ** | Sứ giả trắng cầm xích câu hồn, mặt che vải. |
| T15–18 Diêm La | **Ngục Tốt** | Lính gác điện, giáp đen, kích dài. |
| T10–11 Uổng Tử | **Du Hồn Vạc Dầu** | Quỷ mang vạc dầu bốc khói trên lưng (tinh anh nhỏ). |
| T15–18 Diêm La | **Thiết Giáp Quỷ Sai** | Quỷ Sai khoác giáp sắt nặng, sừng, chùy gai (biến thể của Quỷ Sai có sẵn). |

## 4. Bàn giao và cách dùng ảnh ChatGPT vẽ
1. Mày gửi ảnh cho tao (PNG nền trong suốt). Tao kiểm tra: phong cách khớp master, mép pixel cứng, không bị mờ, kích thước đúng.
2. Nếu ảnh đạt: tao cắt theo khung, đưa vào `game/assets/` và khai báo hình cho quái/boss. Chuyển động ban đầu bằng code (lơ lửng, nhấp nhô) như 5 quái Âm Giới.
3. Muốn hoạt ảnh thật (đứng, chạy, đánh, trúng, ngã): đưa ảnh master này vào PixelLab `animate-with-text-v3`, khoảng 17 lượt mỗi con. Chỉ làm cho con nào cần, tao báo mày trước.
4. Nếu ChatGPT vẽ lệch phong cách (cao như người thật, màu chói, bóng mượt): bắt vẽ lại theo ảnh tham chiếu, không sửa tay.

## 5. Ghi chú
- Chữ Hán trên mũ Vô Thường: ChatGPT thường vẽ sai nét. Chấp nhận nét giả giống chữ viết, hoặc yêu cầu để mũ trơn.
- Thứ tự ưu tiên đề xuất: Hắc Vô Thường, Bạch Vô Thường, Mạnh Bà, Phán Quan, Diêm Vương, Mã Diện, rồi Tinh Anh, rồi quái thường.
- Map (7 map): chưa có brief. Nếu muốn ChatGPT vẽ vật trang trí map thì tao viết thêm brief riêng (nền đất lặp 399×399 px và vật trang trí rời).
