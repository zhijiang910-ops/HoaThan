# Prompt gửi ChatGPT: thử làm "master map" Âm Giới

Đính kèm 5 ảnh trong `gui_chatgpt_map/`: 4 ảnh chụp map trong game (Vong Xuyên có sông + thuyền, Diêm La, Hoàng Tuyền, Bỉ Ngạn) và `vat_dia_phu_17_mon.png` (17 vật đã có).

## PROMPT (dán từ đây)

Tôi làm game hành động pixel art nhìn chếch từ trên xuống (góc 3/4), chủ đề âm phủ "Khử Tà Diệt Ma". Các ảnh đính kèm là map hiện tại trong game (nhân vật nhỏ ở giữa để so tỉ lệ) và 17 vật trang trí đã có. Hãy tạo **master map** theo đúng phong cách đó để tôi so sánh và chọn hướng.

**Phong cách bắt buộc:** pixel art thật, viền đen mảnh 1 px, màu dịu xỉn, tô bóng ít, không gradient mượt, không chữ, không UI, không nhân vật hay quái. Nhìn như môi trường game wuxia u tối.

**Hãy tạo cho tôi 3 thứ, lần lượt (chờ tôi duyệt từng thứ):**

1. **Một cảnh toàn map cho "Vong Xuyên & Cầu Nại Hà"** (ngang 1600×1200 px, góc nhìn như ảnh đính kèm): dòng sông xanh đen chạy ngang phía trên, cầu đá cong Nại Hà bắc qua, quán canh Mạnh Bà bên bờ, vài thuyền gỗ cũ có đèn xanh, bờ sậy và liễu rủ, đất ẩm xanh rêu, sương mỏng. Phần giữa-dưới là khoảng đất trống rộng để chiến đấu (đừng đặt vật ở giữa). Rìa map tối dần vào bóng tối.
2. **Một ô nền liền mạch (seamless tile) 256×256** cho đất của map này, để lát lặp mà không thấy đường nối, không có vật nổi bật (vết nứt, đá nhỏ, rêu nhạt).
3. **Một sheet 8 vật trang trí mới** cùng chủ đề (xương, tượng gãy, xiềng xích, bia vỡ, cây chết, vạc, đá, cờ rách), mỗi vật nền trong suốt, cách nhau đều.

**Kỹ thuật:** mỗi pixel là một ô vuông thật, không khử răng cưa, không phóng to ảnh nhỏ gấp đôi, tối đa 64 màu cho cả cảnh. Nếu bạn dùng Python, thu ảnh về đúng cỡ bằng BOX rồi lượng tử hóa màu (không dither). Sau khi xong, tự báo: số màu, kích thước, tỉ lệ khối 2×2 cùng màu (dưới 0.4 là pixel thật).

Mục đích: tôi muốn xem bạn bám phong cách ảnh mẫu tốt đến mức nào, để quyết định có nhờ bạn làm cả 7 map hay không.
