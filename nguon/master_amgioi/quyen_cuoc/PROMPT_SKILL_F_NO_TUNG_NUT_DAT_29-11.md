# PROMPT NÂNG CẤP CHIÊU F ("THIÊN CƯƠNG ĐẠP TINH CƯỚC") — DẬM NỔ TUNG MẶT ĐẤT NỨT TOÁC DUNG NHAM & VĂNG ĐÁ TẢNG

Tôi vừa bổ sung thêm 2 sprite pixel-art tách nền `.png` mới vào `assets/vfx/` dành riêng cho chiêu F (**Thiên Cương Đạp Tinh Cước**):
1. `assets/vfx/vfx_f_earth_fissures.png`: Mạng lưới mặt đất nứt toác thành các khe dung nham đỏ-vàng xé rách ra tứ phía (ảnh vuông `1:1` tâm đối xứng).
2. `assets/vfx/vfx_f_earth_eruption.png`: Vụ nổ tung mặt đất văng các tảng đá vỡ và cột lửa xung kích hướng lên trên (cạnh đáy của ảnh là mặt đất tại tâm dậm chân).

Hiện tại chiêu F chỉ có mỗi bánh xe `vfx_f_thien_cuong_tinh_luan.png` xoay trên nền đất phẳng nên thiếu cảm giác mặt đất bị dậm nổ tung nứt toác. Hãy kết hợp cả **3 lớp (Vết Nứt Toác Mặt Đất + Vụ Nổ Đá Văng + Bánh Xe Tinh Luân)** cho chiêu F theo đúng đặc tả và hàm code dưới đây (giữ nguyên các chiêu Q, C, X và Đánh thường):

---

## 1. CHỈNH TÂM DẬM CHÂN CHUẨN NGAY GIỮA ĐÁM QUÁI TRƯỚC MẶT
- Đặt tâm chiêu F tại: `cx = player.x + facingDir * 72`, `cy = player.y - 10` (cao hơn bản cũ ~25px để nằm ngay giữa chân bầy quái trước mặt, không bị lệch thấp xuống dưới).
- Ngay khoảnh khắc dậm chân (`t = 0.0s`): kích hoạt **rung camera `5px` trong `0.14s`**, chớp trắng mục tiêu và **hit-stop `2 frame`** để cú dậm có lực chấn động ngàn cân.

---

## 2. BA LỚP HIỆU ỨNG PHỐI HỢP (THỨ TỰ VẼ TỪ DƯỚI LÊN TRÊN)

### Lớp A (Dưới cùng — `Ground Decal Layer`, dưới chân quái & nhân vật): MẶT ĐẤT NỨT TOÁC (`vfx_f_earth_fissures.png`)
- Đường kính ngang lớn hơn bánh xe Tinh Luân để các nhánh nứt xé toạc vươn dài ra ngoài rìa bánh xe: `fissureRadius = 175` (tức rộng ngang **`350px`**, ép trục dọc `0.58` chuẩn mặt đất 2.5D, **KHÔNG xoay** vết nứt đất để vết nứt bám cố định trên nền đất thật!).
- `0.0s -> 0.12s`: Xé toác cực nhanh từ `scale = 0.20 -> 1.05` rồi khựng ở `1.00` (`Cubic Ease-Out`), `alpha = 1.0`, kèm thêm 1 lớp chớp `lighter` (`alpha 0.6 -> 0.0`) trong `0.20s` đầu làm khe dung nham lóe sáng chói lòa!
- `0.12s -> 2.60s`: Bám cố định trên mặt đất với `scale = 1.0`, lửa dung nham trong khe nứt phập phồng nhẹ (`alpha = 0.88 + 0.10 * Math.sin(elapsed * 12)`).
- `2.60s -> 3.00s`: Vết nứt nguội và khép dần (`alpha` giảm từ `0.90 -> 0.0`).

### Lớp B (Đè lên trên tâm vết nứt — `Ground Decal Layer`, vẫn dưới chân quái): BÁNH XE SAO (`vfx_f_thien_cuong_tinh_luan.png`)
- Bán kính `wheelRadius = 122` (nhỏ hơn `fissureRadius = 175` để thấy rõ các khe đất nứt toác xé dài ra xung quanh rìa bánh xe!).
- `0.0s -> 0.20s`: Nổ bung từ `scale = 0.15 -> 1.12 -> 1.00`, `alpha = 0.88`.
- `0.20s -> 2.65s`: Xoay tròn nghiền âm khí (`angle += dt * 1.15`, ép `ctx.scale(1, 0.58)` trước khi `rotate`).
- `2.65s -> 3.00s`: Xoáy nhanh thu ấn từ `scale = 1.0 -> 0.08`, `alpha -> 0.0`.

### Lớp C (Lớp không gian — `World VFX Layer`, vẽ TRÊN mặt đất/ngang thân quái lúc vừa dậm `0.0s -> 0.34s`): VỤ NỔ TUNG ĐÁ TẢNG (`vfx_f_earth_eruption.png`) + ĐÁ VỤN VẬT LÝ
- Ngay khoảnh khắc `0.0s -> 0.34s`, vẽ `vfx_f_earth_eruption.png` đặt **cạnh đáy của ảnh trùng đúng `(cx, cy + 12)`**:
  * Trong `0.0s -> 0.12s` (`p = elapsed / 0.12`): Bùng dựng đứng cực mạnh từ mặt đất lên (`scaleX = 0.45 + 0.65 * easeOut`, `scaleY = 0.30 + 0.85 * easeOut`, kích thước chuẩn `baseW = 290`, `baseH = baseW * img.naturalHeight / img.naturalWidth`, `alpha = 1.0`).
  * Trong `0.12s -> 0.34s`: Giãn rộng nhẹ tiếp từ `1.10 -> 1.25` và giảm `alpha` mượt từ `1.0 -> 0.0` để không che khuất quái sau cú nổ đầu!
- **Bắn thêm 10 - 12 mảnh đá vụn vật lý 60 FPS (`spawnRockDebris`):** Lúc `t = 0`, tạo 12 hạt đá đa giác nâu xám (`4px - 8px`, viền sáng cam lửa nhẹ) bắn văng lên từ `(cx, cy)` với vận tốc ngang `vx = random(-160, 160)`, vận tốc tung lên `vy = random(-260, -130)`, trọng lực `gravity = 780 px/s²`, nảy nhẹ 1 nhịp khi chạm mặt sàn `y >= cy + random(-25, 25)` rồi mờ đi trong `0.55s`!

---

## 3. HÀM CODE MẪU SẴN SÀNG TÍCH HỢP

```js
// 1. Vẽ vết nứt đất cố định (KHÔNG xoay, chỉ ép phối cảnh 2.5D)
function drawEarthFissures(ctx, fissureImg, cx, cy, fissureRadius, scale, alpha, flashAlpha = 0) {
  if (alpha <= 0.01 || scale <= 0.02) return;
  const r = fissureRadius * scale;
  ctx.save();
  ctx.translate(cx, cy);
  ctx.scale(1, 0.58);
  ctx.globalAlpha = alpha;
  ctx.drawImage(fissureImg, -r, -r, r * 2, r * 2);
  if (flashAlpha > 0.02) {
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = flashAlpha;
    ctx.drawImage(fissureImg, -r * 1.03, -r * 1.03, r * 2.06, r * 2.06);
  }
  ctx.restore();
}

// 2. Vẽ vụ nổ tung đất đá lúc vừa dậm chân (0.0s -> 0.34s, đáy ảnh đặt tại cy + 12)
function drawEarthEruptionBurst(ctx, eruptImg, cx, cy, elapsedSec) {
  const totalDur = 0.34;
  if (elapsedSec < 0 || elapsedSec > totalDur) return;
  const baseW = 295;
  const baseH = (baseW * eruptImg.naturalHeight) / eruptImg.naturalWidth;
  let sx, sy, alpha;
  if (elapsedSec <= 0.12) {
    const p = elapsedSec / 0.12;
    const ease = 1 - Math.pow(1 - p, 3);
    sx = 0.45 + 0.65 * ease;
    sy = 0.30 + 0.85 * ease;
    alpha = 1.0;
  } else {
    const p = (elapsedSec - 0.12) / (totalDur - 0.12);
    sx = 1.10 + 0.16 * p;
    sy = 1.15 + 0.10 * p;
    alpha = Math.pow(1 - p, 1.4);
  }
  const w = baseW * sx;
  const h = baseH * sy;
  ctx.save();
  ctx.globalAlpha = Math.max(0, alpha);
  ctx.drawImage(eruptImg, cx - w * 0.5, (cy + 12) - h, w, h);
  if (elapsedSec < 0.10) {
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = (1 - elapsedSec / 0.10) * 0.55;
    ctx.drawImage(eruptImg, cx - w * 0.52, (cy + 12) - h * 1.04, w * 1.04, h * 1.04);
  }
  ctx.restore();
}
```

Hãy cập nhật ngay hiệu ứng nổ tung nứt toác mặt đất này cho chiêu F (**Thiên Cương Đạp Tinh Cước**).
