# PROMPT CẬP NHẬT CHO CLAUDE — MÔN PHÁI THIÊN CƯƠNG MÔN (QUYỀN) — TÁCH BIỆT HOÀN TOÀN KHỎI BÁT QUÁI CỦA MAO SƠN

Trong game có 6 môn phái (Mao Sơn dùng Kiếm mới giữ biểu tượng Bát Quái Âm Dương, còn phái Quyền Cước này là **Thiên Cương Môn** mang biểu tượng **Tinh Luân Bắc Đẩu Thất Tinh — Kim Cang Bạch Hổ**).
Tôi gửi kèm gói ZIP cập nhật toàn bộ tài nguyên đã xóa sạch Bát Quái và thay bằng bộ nhận diện **Thiên Cương Tinh Luân**:
- `assets/vfx/vfx_f_thien_cuong_tinh_luan.png`: Bánh xe răng cưa Dương Hỏa + 7 ngôi sao Bắc Đẩu + đầu Hổ Phù vuông 1:1 tâm đối xứng cho chiêu F.
- `assets/icons/icon_f_thien_cuong_dap_tinh_cuoc.png` (và đè luôn vào `icon_f_bat_quai_chan_dia_cuoc.png`) + `icon_r_quy_mon_tran_nguc_an.png`: Icon F và R mới mang ấn Thiên Cương.
- `assets/vfx/vfx_r_giant_exorcist_palm.png`: Bàn tay chụp 5 ngón từ cổng trời xuống khắc ấn Kim Cang Tinh Mang.
- `assets/vfx/vfx_r_bagua_crater_decal.png` (và `vfx_r_tinh_ban_crater_decal.png`): Hố đá rạn nứt khắc bánh xe sao Thiên Cương.
- `assets/vfx/vfx_passive_chu_sa_mark.png`: Dấu Chưởng Ấn Chu Sa viền bánh răng sao Thiên Cương.

Hãy chép đè bộ ảnh này vào thư mục `assets/` và thực thi chính xác 4 mục dưới đây (giữ nguyên Đánh thường, nút Lướt và chiêu E đang chạy đẹp):

---

## 1. ĐỔI TÊN & MÔ TẢ CHIÊU F SANG "THIÊN CƯƠNG ĐẠP TINH CƯỚC"
- Tên hiển thị chiêu F: **Thiên Cương Đạp Tinh Cước**
- Nội dung mô tả Popup: `"Giậm cước kích nổ Tinh Luân Bắc Đẩu dưới đất, làm choáng mọi quái trước mặt và thiêu đốt âm khí."`
- Cập nhật lại ảnh icon trên HUD cho Ô 2 (F), Ô 4 (R) và dấu Ấn trên đầu quái từ bộ file mới.

---

## 2. HIỆU ỨNG CHIÊU F — NỔ BUNG "THIÊN CƯƠNG TINH LUÂN" TỪ NHỎ THÀNH LỚN & XOÁY THU ẤN (XÓA BỎ VÒNG TRÒN VẼ CODE)
**TUYỆT ĐỐI KHÔNG vẽ vòng tròn `ctx.arc` bằng code nữa!** Dùng tấm `assets/vfx/vfx_f_thien_cuong_tinh_luan.png` vẽ ở `Ground Decal Layer` (trên nền gạch đá của map, DƯỚI chân quái và nhân vật) với phép ép phối cảnh mặt đất 2.5D (`ctx.scale(1, 0.58)`):

- Tâm đặt tại vị trí dậm cước trước mặt nhân vật `(cx, cy)`, bán kính chuẩn `baseRadius = 130` (đường kính ngang `260px`).
- **Diễn hoạt 3 giai đoạn (tổng `3.0s`):**
  1. **Nổ Bung Từ Nhỏ Thành Lớn Lúc Dậm Chân (`0.0s -> 0.22s`):**
     - Bánh xe Tinh Luân chính bung cực nhanh từ `scale = 0.12 -> 1.15` trong `0.15s` đầu (`Cubic Ease-Out`), nảy đàn hồi về `1.00` trong `0.07s` kế tiếp (`alpha = 0.95`), vừa bung vừa xoay nhanh `0.5 rad`.
     - **Sóng Dư Chấn Tinh Luân (thay vòng tròn cũ):** Trong `0.0s -> 0.35s`, vẽ thêm 1 bản sao thứ hai của chính `vfx_f_thien_cuong_tinh_luan.png` với `globalCompositeOperation = 'lighter'`, phóng to từ `scale = 0.65 -> 1.65` và giảm `alpha` từ `0.70 -> 0.0`.
  2. **Xoay Răng Cưa Thiêu Đốt Âm Khí (`0.22s -> 2.65s`):**
     - Giữ `scale = 1.0 + 0.03 * Math.sin(elapsed * 10)`, `alpha = 0.92`, cho bánh xe răng cưa xoay tròn liên tục trên mặt đất (`angle += dt * 1.1`) như cối xay nghiền tà khí!
  3. **Thu Ấn Từ Lớn Hóa Nhỏ (`2.65s -> 3.00s`):**
     - Xoáy nhanh dần (`angle += dt * 5.0`), thu sập từ `scale = 1.0 -> 0.08` (`Cubic Ease-In`) và giảm `alpha` về `0.0`.

```js
function drawGroundTinhLuan(ctx, img, cx, cy, baseRadius, scale, angleRad, alpha, additive = false) {
  if (alpha <= 0.01 || scale <= 0.02) return;
  const r = baseRadius * scale;
  ctx.save();
  ctx.globalAlpha = alpha;
  if (additive) ctx.globalCompositeOperation = 'lighter';
  ctx.translate(cx, cy);
  ctx.scale(1, 0.58); // Ép phối cảnh mặt đất 2.5D TRƯỚC khi xoay để bánh xe răng cưa xoay đúng mặt phẳng sàn!
  ctx.rotate(angleRad);
  ctx.drawImage(img, -r, -r, r * 2, r * 2);
  ctx.restore();
}
```

---

## 3. SỢI HỒNG TUYẾN PHÍM Q ("PHƯỢC HỒN CƯƠNG QUYỀN") — XÓA 2 VẠCH THẲNG ĐƠ MỌC TỪ ĐẦU GỐI
Xóa đoạn `lineTo` 2 vạch thẳng cũ. Vẽ dải Hồng Tuyến xoắn kép nằm **DƯỚI** sprite `vfx_q_fist_projectile.png`:
- Đầu dây: `headX = bullet.x - dir * (bulletWidth * 0.28)`, `headY = bullet.y`.
- Tay nhân vật lúc đấm: `handX = player.x + dir * 18`, `handY = player.y - playerVisualHeight * 0.56`.
- Khi `progress <= 0.30`: nối từ `(handX, handY)`. Khi `progress > 0.30`: tách khỏi người, lướt theo sau đạn với chiều dài đuôi tối đa `175px`.

```js
function drawHongTuyenRibbon(ctx, tailX, tailY, headX, headY, timeSec, alphaMul = 1) {
  const dx = headX - tailX, dy = headY - tailY;
  const dist = Math.hypot(dx, dy);
  if (dist < 8) return;
  const nx = -dy / dist, ny = dx / dist, steps = 28;
  ctx.save();
  ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  for (let strand = 0; strand < 2; strand++) {
    const pts = [];
    for (let i = 0; i <= steps; i++) {
      const t = i / steps;
      const env = Math.sin(Math.PI * Math.pow(t, 0.75)) * (1 - 0.25 * t);
      const phase = timeSec * 14 - t * Math.PI * 3.2 + (strand === 1 ? 2.2 : 0);
      const wave = Math.sin(phase) * (strand === 0 ? 8.5 : 5.5) * env * (strand === 0 ? 1 : -1);
      pts.push({ x: tailX + dx * t + nx * wave, y: tailY + dy * t + ny * wave, t });
    }
    for (let i = 0; i < steps; i++) {
      const p0 = pts[i], p1 = pts[i + 1], tMid = (p0.t + p1.t) * 0.5;
      const fade = Math.min(1, tMid / 0.35) * alphaMul;
      if (fade <= 0.02) continue;
      ctx.globalCompositeOperation = 'lighter';
      ctx.strokeStyle = `rgba(255, 56, 36, ${(0.28 * fade).toFixed(3)})`;
      ctx.lineWidth = (strand === 0 ? 7.5 : 5.0) * (0.35 + 0.65 * tMid);
      ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.stroke();

      ctx.globalCompositeOperation = 'source-over';
      ctx.strokeStyle = `rgba(218, 28, 40, ${(0.92 * fade).toFixed(3)})`;
      ctx.lineWidth = (strand === 0 ? 2.8 : 1.8) * (0.4 + 0.6 * tMid);
      ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.stroke();

      if (strand === 0 && tMid > 0.2) {
        ctx.strokeStyle = `rgba(255, 212, 120, ${(0.80 * fade).toFixed(3)})`;
        ctx.lineWidth = 1.1;
        ctx.beginPath(); ctx.moveTo(p0.x, p0.y); ctx.lineTo(p1.x, p1.y); ctx.stroke();
      }
    }
    if (strand === 0) {
      for (const kt of [0.42, 0.72]) {
        const kp = pts[Math.floor(kt * steps)], kAlpha = Math.min(1, kt / 0.35) * alphaMul;
        ctx.fillStyle = `rgba(255, 218, 95, ${kAlpha.toFixed(2)})`;
        ctx.strokeStyle = `rgba(200, 24, 32, ${kAlpha.toFixed(2)})`;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(kp.x, kp.y - 3.5); ctx.lineTo(kp.x + 3.5, kp.y);
        ctx.moveTo(kp.x + 3.5, kp.y); ctx.lineTo(kp.x, kp.y + 3.5);
        ctx.lineTo(kp.x - 3.5, kp.y); ctx.closePath();
        ctx.fill(); ctx.stroke();
      }
    }
  }
  ctx.restore();
}
```

---

## 4. ĐẠI CHIÊU R ("QUỶ MÔN TRẤN NGỤC ẤN") VỚI BÀN TAY & HỐ ĐÁ THIÊN CƯƠNG MỚI
- Dùng `assets/vfx/vfx_r_giant_exorcist_palm.png` mới (`palmWidth = 360`, `palmHeight = palmWidth * (img.naturalHeight / img.naturalWidth)`, `rotation = 0`, `flipY = false`, `drawX = targetX - palmWidth / 2`).
- Điểm chạm đất cố định (`landedY`): `landedY = (targetY + 26) - palmHeight` (đặt 5 đầu ngón tay đè đúng tâm hố đá Tinh Bàn).
- 4 nhịp trong World Layer (DƯỚI lớp UI HUD):
  1. `0.0s -> 0.55s`: Hiện hố đá bánh xe sao `vfx_r_bagua_crater_decal.png` (`width = 340px`, tâm tại `(targetX, targetY)`) ở `Ground Decal Layer` hút quái vào tâm (giữ sáng tới `1.50s`).
  2. `0.55s -> 0.70s`: Bàn tay lao từ `landedY - 260` xuống `landedY` theo `Cubic Ease-In`, `alpha = 1.0`.
  3. `0.70s -> 1.15s`: Chạm đất gây sát thương + chớp sáng `0.05s` + hit-stop `3 frame`, giữ nguyên bàn tay đứng yên tại `landedY` với `alpha = 1.0` suốt `0.45s`.
  4. `1.15s -> 1.55s`: Giảm `alpha` từ `1.0 -> 0.0`, tỏa 6-8 hạt khói mềm `vfx_soft_ghost_smoke_puff.png` (`alpha <= 0.42`).
