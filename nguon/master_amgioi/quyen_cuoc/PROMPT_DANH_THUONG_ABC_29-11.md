# PROMPT NÂNG CẤP CHUỖI ĐÁNH THƯỜNG TỰ ĐỘNG A - B - C (VŨ KHÍ +6) — THIÊN CƯƠNG MÔN

Game của tôi sử dụng cơ chế **Tự động đánh (Auto-attack) khi ở gần quái** (giống dòng Action Roguelike) và có quy ước toàn game:
- **Khi Vũ khí `< +6` (mặc định):** Nhân vật chỉ đánh lặp chuỗi 2 nhịp **A (Đấm trái) -> B (Đấm phải)**.
- **Khi Vũ khí đạt `>= +6` (hoặc bật nút `+6` trong bảng Luyện Công):** Mở khóa đòn kết chuỗi thứ 3 là **C (Đòn quét chân — Thiên Cương Tảo Tinh Cước)** tạo chuỗi **A -> B -> C**.

Hiện tại cả 3 nhịp A - B - C đang vẽ chung một kiểu vệt lưỡi liềm cong giống chém kiếm, tốc độ và sát thương đều đều `1 - 1 - 1` nên nhìn bị chán và chưa thấy sức mạnh đột biến khi lên `+6`.
Tôi đã thêm 2 sprite pixel-art tách nền `.png` mới vào `assets/vfx/`:
1. `assets/vfx/vfx_ab_fist_impact.png`: Chớp xung kích nắm đấm phóng thẳng về phía bên phải (gốc lóe sáng ở mép trái, luồng lửa bắn sang phải — KHÔNG phải vệt chém cong!).
2. `assets/vfx/vfx_c_star_sweep_arc.png`: Vòng cung lửa bán nguyệt 200° hướng sang phải, bên trong vệt quét có 7 ngôi sao Bắc Đẩu phát sáng (tâm ảnh là tâm xoay quanh nhân vật).

Hãy giữ nguyên animation nhân vật (Đấm trái / Đấm phải / Quét chân) nhưng nâng cấp toàn bộ **Nhịp độ, VFX, Hitbox và Phần thưởng `+6`** của chuỗi đánh thường Thiên Cương Môn theo đúng đặc tả dưới đây:

---

## 1. TÁCH HẲN NHỊP ĐỘ "NHANH - NHANH - NẶNG" & BÁM MỤC TIÊU (MICRO-LUNGE)
- **Đòn A — Đấm Trái (`0.19s` · `50% ATK`):**
  * Nhịp khởi đầu cực nhanh gọn. Nếu người chơi không kéo mạnh joystick ngược hướng mà có quái cách hơi xa trong tầm kích hoạt, cho nhân vật nhích nhẹ `6px` về phía mục tiêu để không đấm hụt vào không khí.
  * VFX: Dùng `vfx_ab_fist_impact.png` (`scale = 0.82`, tồn tại `0.14s`), đặt gốc mép trái của ảnh ngay trước nắm đấm nhân vật (`handX, handY`), hướng theo góc mục tiêu (hoặc lật `scaleX = dir`), trượt nhanh tới trước `18px` theo `Cubic Ease-Out` rồi mờ nhanh.
- **Đòn B — Đấm Phải (`0.18s` · `65% ATK`):**
  * Tung nối sát ngay sau A tạo nhịp "one-two" giòn tay, nhích bước bám mục tiêu `10px` và đẩy khựng quái nhẹ `6px`.
  * VFX: Vẫn dùng `vfx_ab_fist_impact.png` nhưng to và rực hơn (`scale = 1.08`, nghiêng lệch nhẹ `+6°` so với đòn A để hai cú đấm không trùng khít 1 vệt, vẽ thêm 1 lớp phụ `globalCompositeOperation = 'lighter'` với `alpha = 0.45` trong `0.06s` đầu để tạo ánh chớp uy lực hơn đòn A).
  * *Tích Ấn khi `< +6`:* Nếu vũ khí chưa đạt `+6`, cứ mỗi lần hoàn thành đòn B thứ 2 (tức 2 chu kỳ A-B) thì khắc `+1 tầng Chưởng Ấn` lên mục tiêu chính.

---

## 2. BIẾN ĐÒN C (MỞ KHÓA KHI VŨ KHÍ `+6`) THÀNH CÚ NỔ DIỆN RỘNG "TẢO TINH CƯỚC"
Khi điều kiện vũ khí `+6` được bật (giữ đúng biến kiểm tra vũ khí `+6` hiện có trong code): sau đòn B sẽ nối sang đòn **C (Quét chân — `0.34s`)**:
- **Bước trượt & Hitbox diện rộng `200°`:**
  * Nhân vật lướt trượt tới `14px` theo hướng quái gần nhất.
  * Mở rộng vùng sát thương thành **hình quạt rộng `200°` bán kính `135px`** quét cả đám quái vây hai bên sườn chứ không chỉ đánh hẹp trước mặt!
- **Phần thưởng sức mạnh rõ rệt của mốc `+6` (Power Spike):**
  * Gây **`130% ATK`** (cao gấp đôi đòn thường A/B).
  * **Khắc ngay `+1 tầng Chưởng Ấn Thiên Cương` lên TẤT CẢ quái trúng cú quét** (giúp tốc độ tích Ấn và dọn bầy quái tăng vọt ngay khi rèn lên `+6`!).
  * Gây khựng ngắn (`mini-stagger 0.20s`) ngắt đòn đánh thường của quái nhỏ xung quanh.
  * Nếu cú quét trúng từ `2` quái trở lên: kích hoạt `hit-stop 2 frame` (`~0.033s`) để cảm nhận rõ sức nặng cú gạt giò.
- **Hàm vẽ VFX Vòng Cung Sao Bắc Đẩu (`vfx_c_star_sweep_arc.png`) chuẩn phối cảnh mặt đất 2.5D:**
  * Không vẽ vệt chém mảnh cũ nữa! Vẽ `vfx_c_star_sweep_arc.png` lấy tâm tại ngang hông/gối nhân vật (`player.x, player.y - playerVisualHeight * 0.28`), ép nhẹ trục dọc `0.72` cho tiệp mặt phẳng sàn 2.5D và **xoay quét một góc `70°` cực mượt trong `0.24s`**:

```js
function drawStarSweepArc(ctx, sweepImg, cx, cy, dir, progress) {
  // progress chạy từ 0.0 -> 1.0 trong 0.24 giây
  if (progress < 0 || progress > 1) return;
  const easeOut = 1 - Math.pow(1 - progress, 3);
  const radius = 135 * (0.78 + 0.26 * easeOut); // Bung rộng từ 78% -> 104% bán kính
  // Xoay quét từ góc -0.65 rad đến +0.55 rad để vòng lửa + 7 ngôi sao Bắc Đẩu quét ngang sướng mắt
  const sweepAngle = -0.65 + 1.20 * easeOut;
  const alpha = progress < 0.2 ? (progress / 0.2) : Math.pow(1 - (progress - 0.2) / 0.8, 1.3);

  ctx.save();
  ctx.translate(cx, cy);
  ctx.scale(dir, 0.72); // dir = 1 (phải) hoặc -1 (trái); 0.72 = độ nghiêng mặt phẳng quét chân 2.5D
  ctx.rotate(sweepAngle);

  // Lớp chính sắc nét thấy rõ chòm sao Bắc Đẩu
  ctx.globalAlpha = Math.min(1, alpha * 1.05);
  ctx.drawImage(sweepImg, -radius, -radius, radius * 2, radius * 2);

  // Lớp chớp sáng đầu đòn (0.0 -> 0.35 progress)
  if (progress < 0.35) {
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = (1 - progress / 0.35) * 0.45;
    ctx.drawImage(sweepImg, -radius * 1.04, -radius * 1.04, radius * 2.08, radius * 2.08);
  }
  ctx.restore();
}
```

```js
function drawFistShockCone(ctx, fistImpactImg, handX, handY, dir, progress, baseScale = 1.0, tiltRad = 0, extraFlash = false) {
  // progress chạy từ 0.0 -> 1.0 trong 0.14 giây
  if (progress < 0 || progress > 1) return;
  const easeOut = 1 - Math.pow(1 - progress, 3);
  const w = 135 * baseScale * (0.65 + 0.45 * easeOut);
  const h = (w * fistImpactImg.naturalHeight) / fistImpactImg.naturalWidth;
  const forwardOffset = 18 * easeOut;
  const alpha = progress < 0.18 ? 1.0 : (1 - (progress - 0.18) / 0.82);

  ctx.save();
  ctx.translate(handX + dir * forwardOffset, handY);
  ctx.scale(dir, 1);
  ctx.rotate(tiltRad);
  ctx.globalAlpha = Math.max(0, alpha);
  // Gốc nổ nằm ở mép trái của ảnh (-w * 0.12), thân xung kích phóng thẳng ra trước
  ctx.drawImage(fistImpactImg, -w * 0.12, -h * 0.5, w, h);

  if (extraFlash && progress < 0.35) {
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = (1 - progress / 0.35) * 0.5;
    ctx.drawImage(fistImpactImg, -w * 0.12, -h * 0.5, w * 1.08, h * 1.08);
  }
  ctx.restore();
}
```

Hãy tích hợp 2 hàm VFX này cùng thông số sát thương / tầm quét / khắc Chưởng Ấn diện rộng ở mốc `+6` cho chuỗi đánh thường của Thiên Cương Môn (không làm ảnh hưởng 4 kỹ năng chủ động Q, F, E, R).
