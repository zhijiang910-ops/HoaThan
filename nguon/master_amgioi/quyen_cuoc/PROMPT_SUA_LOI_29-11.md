# PROMPT THỰC THI CHO CLAUDE — SỬA DỨT ĐIỂM SỢI HỒNG TUYẾN (Q), MẤT HÌNH CHIÊU F & BÀN TAY ĐẠI CHIÊU R

Tôi gửi kèm gói cập nhật này gồm file `assets/vfx/vfx_r_giant_exorcist_palm.png` mới (cánh tay thò ra từ cổng không gian đỏ ở đỉnh ảnh, 5 ngón tay chụp thẳng xuống mặt đất ở đáy ảnh) cùng thư mục `assets/` chuẩn.
*(Lưu ý dự phòng: Nếu ảnh bàn tay mới được đính kèm dưới dạng `.jpg` nền đen thay vì `.png` đã tách nền, hãy tự động chuyển nền đen sang trong suốt bằng offscreen canvas với điều kiện pixel rìa ngoài `Math.max(r, g, b) < 22` -> `alpha = 0` và bỏ 8% lề đen xung quanh).*

Trong bản hiện tại: Đánh thường, dấu Ấn Chu Sa trên đầu cọc, nút Lướt và 4 ô Icon HUD đã đẹp chuẩn (GIỮ NGUYÊN KHÔNG SỬA CÁC PHẦN ĐÓ).
Hãy thực thi chính xác 3 mục sửa lỗi dưới đây:

---

## 1. LÀM LẠI SỢI CHỈ ĐỎ PHÍM Q ("PHƯỢC HỒN CƯƠNG QUYỀN") — XÓA 2 VẠCH THẲNG ĐƠ MỌC TỪ ĐẦU GỐI
Hiện tại khi bắn phím Q: đang vẽ 2 đường thẳng `lineTo` song song cứng đơ từ đầu gối nhân vật, đè lên trên lá bùa vàng của đạn, và khi nhân vật đã thu tay đứng im 2 vạch đỏ vẫn chĩa từ đầu gối ra mép màn hình.

Hãy **XÓA BỎ HOÀN TOÀN** đoạn vẽ 2 đường thẳng cũ và thay bằng **Dải Hồng Tuyến Xoắn Kép 3 Lớp Ánh Sáng**:
1. **Thứ tự vẽ:** Bắt buộc gọi hàm vẽ Hồng Tuyến **TRƯỚC (nằm DƯỚI)** lệnh `drawImage` của viên đạn `vfx_q_fist_projectile.png` để đầu dây chui gọn vào cổ tay nắm đấm.
2. **Tọa độ đầu & đuôi tự thu rút (không dính chết vào chân/đầu gối):**
   - Đầu dây gắn vào cổ tay sau của đạn: `headX = bullet.x - dir * (bulletWidth * 0.28)`, `headY = bullet.y`.
   - Vị trí tay nhân vật lúc đấm (ngang ngực/vai): `handX = player.x + dir * 18`, `handY = player.y - playerVisualHeight * 0.56`.
   - Giai đoạn đầu (`progress` từ `0.0 -> 0.30`): đuôi dây đặt tại `(handX, handY)`.
   - Giai đoạn sau (`progress > 0.30`, khi nhân vật đã hạ tay): đuôi dây **tách khỏi người và lướt theo sau đạn**, giữ chiều dài tối đa `175px` (`tailX = headX - dir * Math.min(distFromHand, 175)`) và mờ dần về `0` ở chóp đuôi.
3. **Hàm vẽ Canvas 2D chuẩn (copy nguyên hàm này vào code):**

```js
function drawHongTuyenRibbon(ctx, tailX, tailY, headX, headY, timeSec, alphaMul = 1) {
  const dx = headX - tailX;
  const dy = headY - tailY;
  const dist = Math.hypot(dx, dy);
  if (dist < 8) return;
  const nx = -dy / dist;
  const ny = dx / dist;
  const steps = 28;

  ctx.save();
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';

  for (let strand = 0; strand < 2; strand++) {
    const pts = [];
    for (let i = 0; i <= steps; i++) {
      const t = i / steps; // 0 = chóp đuôi, 1 = cổ tay viên đạn
      const env = Math.sin(Math.PI * Math.pow(t, 0.75)) * (1 - 0.25 * t);
      const phase = timeSec * 14 - t * Math.PI * 3.2 + (strand === 1 ? 2.2 : 0);
      const amp = strand === 0 ? 8.5 : 5.5;
      const wave = Math.sin(phase) * amp * env * (strand === 0 ? 1 : -1);
      pts.push({
        x: tailX + dx * t + nx * wave,
        y: tailY + dy * t + ny * wave,
        t
      });
    }

    for (let i = 0; i < steps; i++) {
      const p0 = pts[i], p1 = pts[i + 1];
      const tMid = (p0.t + p1.t) * 0.5;
      const fade = Math.min(1, tMid / 0.35) * alphaMul;
      if (fade <= 0.02) continue;

      // Lớp 1: Hào quang đỏ cam hòa trộn sáng (Additive)
      ctx.globalCompositeOperation = 'lighter';
      ctx.strokeStyle = `rgba(255, 56, 36, ${(0.28 * fade).toFixed(3)})`;
      ctx.lineWidth = (strand === 0 ? 7.5 : 5.0) * (0.35 + 0.65 * tMid);
      ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.stroke();

      // Lớp 2: Thân tơ Chu Sa đậm
      ctx.globalCompositeOperation = 'source-over';
      ctx.strokeStyle = `rgba(218, 28, 40, ${(0.92 * fade).toFixed(3)})`;
      ctx.lineWidth = (strand === 0 ? 2.8 : 1.8) * (0.4 + 0.6 * tMid);
      ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.stroke();

      // Lớp 3: Lõi linh hỏa vàng kim tiệp màu lửa của viên đạn
      if (strand === 0 && tMid > 0.2) {
        ctx.strokeStyle = `rgba(255, 212, 120, ${(0.80 * fade).toFixed(3)})`;
        ctx.lineWidth = 1.1;
        ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.stroke();
      }
    }

    // Đính 2 nút bùa hình thoi vàng-đỏ nhỏ trôi dọc sợi chính
    if (strand === 0) {
      for (const kt of [0.42, 0.72]) {
        const kp = pts[Math.floor(kt * steps)];
        const kAlpha = Math.min(1, kt / 0.35) * alphaMul;
        ctx.fillStyle = `rgba(255, 218, 95, ${kAlpha.toFixed(2)})`;
        ctx.strokeStyle = `rgba(200, 24, 32, ${kAlpha.toFixed(2)})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(kp.x, kp.y - 3.5);
        ctx.lineTo(kp.x + 3.5, kp.y);
        ctx.lineTo(kp.x, kp.y + 3.5);
        ctx.lineTo(kp.x - 3.5, kp.y);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      }
    }
  }
  ctx.restore();
}
```
4. Khi đạn xuyên trúng từ 2 quái trở lên, vẽ thêm một sợi `drawHongTuyenRibbon` ngắn nối giữa các quái trúng đòn trong `0.25s` lúc chúng bị kéo nhích tụ lại gần nhau.

---

## 2. KHÔI PHỤC HIỆU ỨNG MẶT ĐẤT ĐANG BỊ TÀNG HÌNH CỦA CHIÊU F ("BÁT QUÁI CHẤN ĐỊA CƯỚC")
- Lỗi hiện tại: Bấm phím F có tiếng nổ, trừ Nội lực và nhảy hồi chiêu 9s nhưng mặt đất trống trơn không hiện hố Bát Quái.
- Cách sửa: Vẽ `assets/vfx/vfx_r_bagua_crater_decal.png` ở `Ground Decal Layer` (trên nền gạch đá của map, dưới chân quái và nhân vật), `width = 210px` (giữ đúng tỷ lệ ảnh), đặt tâm tại điểm giậm chân trước mặt nhân vật, `alpha = 0.9` tồn tại `3.0s`, kèm 2 vòng sóng chấn động vàng cam bung nhanh từ `20px -> 140px` trong `0.25s` đầu.

---

## 3. CẬP NHẬT ĐẠI CHIÊU R ("QUỶ MÔN TRẤN NGỤC ẤN") VỚI SPRITE BÀN TAY CHỤP XUỐNG MỚI
- Chép đè file `assets/vfx/vfx_r_giant_exorcist_palm.png` mới từ gói ZIP này vào dự án.
- Xóa đoạn code lật ngược ảnh ở frame đầu và xóa đoạn cộng dồn `y` làm bàn tay trượt tụt dần xuống đáy màn hình.
- Thiết lập chuẩn: `palmWidth = 360`, `palmHeight = palmWidth * (img.naturalHeight / img.naturalWidth)`, `rotation = 0`, `flipY = false`, `drawX = targetX - palmWidth / 2`.
- Khóa điểm chạm đất cố định (`landedY`) sao cho **cạnh đáy ảnh (5 đầu ngón tay) đặt đúng tâm hố Bát Quái cộng `26px`**:
  `landedY = (targetY + 26) - palmHeight`
- 4 nhịp diễn hoạt (toàn bộ vẽ trong World Layer, DƯỚI lớp UI HUD để không bao giờ đè lên thanh máu hay nút kỹ năng):
  1. `0.0s -> 0.55s`: Hiện hố `vfx_r_bagua_crater_decal.png` lớn (`width = 340px`, tâm tại `(targetX, targetY)`) ở `Ground Decal Layer` hút quái vào tâm. **KHÔNG tắt hố này khi bàn tay xuất hiện — giữ hố sáng liên tục tới `1.50s`!**
  2. `0.55s -> 0.70s`: Bàn tay lao từ `landedY - 260` xuống đúng `landedY` theo `Cubic Ease-In`, `alpha = 1.0`.
  3. `0.70s -> 1.15s`: Chạm đất gây sát thương + chớp sáng `0.05s` + hit-stop `3 frame`. **GIỮ NGUYÊN bàn tay đứng yên tại `landedY` với `alpha = 1.0` suốt `0.45s`**.
  4. `1.15s -> 1.55s`: Giảm `alpha` của cả bàn tay và hố Bát Quái từ `1.0 -> 0.0`, tỏa 6-8 hạt khói mềm `vfx_soft_ghost_smoke_puff.png` (`alpha <= 0.42`) quanh các đầu ngón tay.
