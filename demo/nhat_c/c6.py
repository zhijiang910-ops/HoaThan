"""Demo nhát C Kiếm +6 · Lướt Trảm, dựng từ frame sprite thật của game.
Mọi biến dạng (co người, nghiêng, trượt, dư ảnh) đều là scale/skew/translate/alpha,
nên canvas trong game làm y hệt được bằng drawImage + transform.
Chạy từ thư mục gốc gói: python demo/nhat_c/frames.py rồi python demo/nhat_c/c6.py out.mp4
(không tham số: xuất check.jpg). Cần Python, Pillow, FFmpeg (libx264), font DejaVu Sans.
"""
import json, math, random, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parents[2]
GAME = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / 'game'
A = GAME / 'assets'
META = json.load(open(Path(__file__).with_name('meta.json')))  # tạo bằng: python frames.py
W, H, FPS = 1280, 720, 48
PW, PH = 600, 250
FLOOR = 212
SC = 1.45
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans'
def F(n, b=False): return ImageFont.truetype(FONT + ('-Bold' if b else '') + '.ttf', n)
def clamp(x, a=0, b=1): return max(a, min(b, x))
def smooth(x): x = clamp(x); return x * x * (3 - 2 * x)
def eout(x): x = clamp(x); return 1 - (1 - x) ** 3
def lerp(a, b, u): return a + (b - a) * u

# ---------- sprite ----------
SHEETS = {g: Image.open(A / f'{g}.png').convert('RGBA') for g in META}
def frame(g, an, i):
    m = META[g]; x, y = m['anims'][an]['f'][i]
    return SHEETS[g].crop((x, y, x + m['w'], y + m['h']))

# Chọn frame cho từng thế (A/B dùng đúng anim attack/attack2 của game, trừ B nữ – xem ghi chú)
POSE = {
 'hero_nu': {
   'A': [('attack', i) for i in (0, 1, 2, 3)],
   'B': [('attack', i) for i in (4, 5, 6, 7)],      # attack2 của nữ là chưởng, không có kiếm
   'wind': ('attack', 1), 'dash': ('attack', 3), 'slide': ('attack', 5),
   'finish': [('attack', 6), ('attack', 7), ('idle', 0)], 'idle': ('idle', 0)},
 'hero_nam': {
   'A': [('attack', i) for i in (2, 3, 4, 5)],
   'B': [('attack2', i) for i in (3, 4, 5, 6)],
   'wind': ('run', 0), 'dash': ('run', 3), 'slide': ('attack2', 6),
   'finish': [('attack2', 7), ('attack', 7), ('idle', 0)], 'idle': ('idle', 0)},
}

def blit(dst, img, ax, ay, x, y, sx=1, sy=1, skew=0, alpha=1, tint=None):
    """Đặt sprite: điểm neo (ax,ay) tới (x,y); scale rồi skew quanh chân (giống ctx.transform)."""
    sx *= SC; sy *= SC
    # forward: X = x + sx*(u-ax) + skew*sy*(v-ay)*(-1) ; Y = y + sy*(v-ay)
    # skew>0 = ngả về trước (đầu đi trước chân)
    a, b, c = sx, -skew * sy, x - sx * ax + skew * sy * ay
    d, e, f = 0, sy, y - sy * ay
    det = a * e - b * d
    ia, ib = e / det, -b / det
    id_, ie = -d / det, a / det
    ic = -(ia * c + ib * f); if_ = -(id_ * c + ie * f)
    src = img
    if tint:
        al = img.getchannel('A')
        src = Image.blend(img, Image.new('RGBA', img.size, tint), .62); src.putalpha(al)
    if alpha < 1:
        src = src.copy(); src.putalpha(src.getchannel('A').point(lambda p: int(p * alpha)))
    out = src.transform(dst.size, Image.AFFINE, (ia, ib, ic, id_, ie, if_), resample=Image.NEAREST)
    dst.alpha_composite(out)

# ---------- timeline (giây, trong một vòng) ----------
X0 = 120
TG = [205, 280, 355]
DASH = 300           # px trong clip; đề xuất trong game: 160 đơn vị
A_T, B_T, C_T = 0.0, 0.30, 0.60
WIND, DASH_T, SLIDE, FIN = 0.18, 0.15, 0.14, 0.30

def seq(lst, u):
    return lst[min(len(lst) - 1, int(clamp(u) * len(lst)))]

def hero_state(g, t, up):
    """Trả (frame-key, dx, sx, sy, skew)."""
    p = POSE[g]
    if t < B_T: return seq(p['A'], (t - A_T) / .22), 0, 1, 1, 0
    if t < C_T: return seq(p['B'], (t - B_T) / .22), 0, 1, 1, 0
    if not up:
        if t < C_T + .30: return seq(p['A'], (t - C_T) / .22), 0, 1, 1, 0
        if t < C_T + .60: return seq(p['B'], (t - C_T - .30) / .22), 0, 1, 1, 0
        return p['idle'], 0, 1, 1, 0
    u = t - C_T
    if u < WIND:                                   # Lấy đà: hạ trọng tâm, kéo kiếm về sau
        k = smooth(u / WIND)
        return p['wind'], -12 * k, lerp(1, 1.07, k), lerp(1, .86, k), -.10 * k
    u -= WIND
    if u < DASH_T:                                 # Lướt chém
        k = eout(u / DASH_T)
        return p['dash'], lerp(-12, DASH, k), 1.12, .90, .30
    u -= DASH_T
    if u < SLIDE:                                  # Trượt dừng
        k = eout(u / SLIDE)
        return p['slide'], lerp(DASH, DASH + 16, k), lerp(1.12, 1.0, k), lerp(.90, 1, k), lerp(.30, .02, k)
    u -= SLIDE
    if u < FIN: return seq(p['finish'], u / FIN), DASH + 16, 1, 1, 0
    return p['idle'], DASH + 16, 1, 1, 0

def hero_x(g, t, up): return X0 + hero_state(g, t, up)[1]
DASH0 = C_T + WIND; DASH1 = DASH0 + DASH_T

def c_hit_time(g, tx):
    """Thời điểm thân người lướt qua mục tiêu (mỗi mục tiêu đúng 1 lần)."""
    lo, hi = DASH0, DASH1
    for _ in range(30):
        mid = (lo + hi) / 2
        if hero_x(g, mid, True) + 30 < tx: lo = mid
        else: hi = mid
    return hi

def hits(g, i, up):
    h = []
    if i == 0:
        h = [(A_T + .12, 9), (B_T + .12, 9)]
        if not up: h += [(C_T + .12, 9), (C_T + .42, 9)]
    if up: h.append((c_hit_time(g, TG[i]), 15))
    return h

# ---------- cảnh ----------
snow = Image.open(A / 'map' / 'g_snow.jpg').convert('RGB')
snow = ImageEnhance.Brightness(snow.resize((700, 700))).enhance(.56)
BG = Image.blend(snow.crop((40, 120, 40 + PW, 120 + PH)), Image.new('RGB', (PW, PH), '#293b42'), .40).convert('RGBA')
en = Image.open(A / 'daulap.png').convert('RGBA')
EN_IDLE = en.crop((0, 0, 133, 122)).transpose(Image.Transpose.FLIP_LEFT_RIGHT).resize((106, 97), Image.LANCZOS)
rnd = random.Random(7)
SPARK = [(rnd.uniform(-1, 1), rnd.uniform(-1, -.1), rnd.uniform(25, 90)) for _ in range(12)]
DUST = [(rnd.uniform(-1, .3), rnd.uniform(-.9, -.2), rnd.uniform(.6, 1.4)) for _ in range(9)]

def panel(g, t, up, vfx=True):
    v = BG.copy(); d = ImageDraw.Draw(v, 'RGBA')
    d.line((20, FLOOR + 3, PW - 20, FLOOR + 3), fill='#7f8f8b')
    key, dx, sx, sy, sk = hero_state(g, t, up)
    hx = X0 + dx
    # vệt đất + vệt lướt
    if up and vfx and DASH0 < t < DASH1 + .25:
        fade = 1 - smooth((t - DASH1) / .25) if t > DASH1 else 1
        x1 = hx + 18; x0 = X0 - 10 + (x1 - X0) * .15
        d.polygon([(x0, FLOOR - 50), (x1, FLOOR - 58), (x1 + 16, FLOOR - 55), (x1, FLOOR - 52), (x0, FLOOR - 46)],
                  fill=(80, 200, 230, int(130 * fade)))
        d.line((x0, FLOOR - 51, x1 + 10, FLOOR - 56), fill=(235, 255, 255, int(235 * fade)), width=2)
        d.line((x0 + 20, FLOOR + 1, x1, FLOOR + 1), fill=(150, 225, 240, int(120 * fade)), width=2)
    # quái
    hit_count = 0; marks = []
    for i, x in enumerate(TG):
        hl = [h for h in hits(g, i, up) if h[0] <= t]
        dt = t - hl[-1][0] if hl else 99
        c_hit = up and any(h[1] == 15 for h in hl)
        if c_hit: hit_count += 1
        elif not up and hl: hit_count = max(hit_count, 1)
        kb = (14 * eout(dt / .25) if c_hit else 0) + (math.sin(clamp(dt / .22) * math.pi) * 9 if dt < .22 else 0)
        ex = int(x + kb)
        d.ellipse((ex - 22, FLOOR - 4, ex + 20, FLOOR + 6), fill='#3a423f')
        img = EN_IDLE
        if dt < .22: img = img.rotate(12 * math.sin(math.pi * dt / .22), resample=Image.BICUBIC, center=(53, 85))
        if .0 < dt < .08:
            al = img.getchannel('A'); img = Image.blend(img, Image.new('RGBA', img.size, '#fff2c8'), .45); img.putalpha(al)
        v.alpha_composite(img, (ex - 53, FLOOR - 95))
        if c_hit: marks.append((ex, dt))
        # số sát thương
        for hi_, (ht, dmg) in enumerate(hl):
            q = t - ht
            if q < .55:
                fy = FLOOR - 104 - 24 * eout(q / .55)
                d.text((ex - 8 + (hi_ % 2) * 14, fy), str(dmg), font=F(20 if dmg > 9 else 16, True),
                       fill=(255, 232, 150, int(255 * (1 - smooth((q - .3) / .25)))) if dmg > 9 else
                       (225, 240, 255, int(255 * (1 - smooth((q - .3) / .25)))), stroke_width=2, stroke_fill=(20, 20, 26, 220))
        if vfx and dt < .26:
            a = int(255 * (1 - dt / .26)); cy = FLOOR - 52
            for vx, vy, pw in SPARK:
                px, py = ex + vx * pw * dt * 3, cy + vy * pw * dt * 3
                d.line((px, py, px + vx * 7, py + vy * 7), fill=(255, 220, 140, a), width=2)
            if c_hit and dt < .14:   # đường cắt ngang thân
                k = dt / .14
                d.line((ex - 46, cy + 6, ex + 46, cy - 6), fill=(235, 255, 255, int(255 * (1 - k))), width=max(1, int(5 * (1 - k))))
                d.line((ex - 52, cy + 7, ex + 52, cy - 7), fill=(90, 210, 240, int(140 * (1 - k))), width=9)
    # dấu Phá Thế (3 giây): hình thoi vàng + vòng đếm
    for ex, dt in marks:
        if dt < 3:
            cx, cy = ex, FLOOR - 152 - (6 if dt < .2 else 0)
            d.polygon([(cx, cy - 9), (cx + 7, cy), (cx, cy + 9), (cx - 7, cy)], fill='#f2c562', outline='#5a3a12')
            d.arc((cx - 13, cy - 13, cx + 13, cy + 13), -90, -90 + 360 * (1 - dt / 3), fill='#ffe3a0', width=2)
    # dư ảnh
    if up and vfx and DASH0 - .02 < t < DASH1 + .06:
        for lag, al in ((.075, .10), (.05, .16), (.025, .26)):
            k2, dx2, sx2, sy2, sk2 = hero_state(g, max(DASH0, t - lag), True)
            m = META[g]
            blit(v, frame(g, *k2), m['ax'], m['ay'], X0 + dx2, FLOOR, sx2, sy2, sk2, al, '#86e0f0')
    # bóng + nhân vật
    d = ImageDraw.Draw(v, 'RGBA')
    d.ellipse((hx - 30 * sx, FLOOR - 5, hx + 30 * sx, FLOOR + 6), fill=(18, 26, 30, 150))
    m = META[g]
    blit(v, frame(g, *key), m['ax'], m['ay'], hx, FLOOR, sx, sy, sk)
    # ánh kiếm lúc tích lực
    if up and vfx and C_T + .10 < t < DASH0 + .02:
        k = (t - C_T - .10) / (DASH0 + .02 - C_T - .10)
        cx, cy = hx - 36, FLOOR - 92 if g == 'hero_nu' else FLOOR - 40
        r = 4 + 9 * math.sin(math.pi * k)
        d.line((cx - r, cy, cx + r, cy), fill=(240, 255, 255, 230), width=2)
        d.line((cx, cy - r, cx, cy + r), fill=(240, 255, 255, 230), width=2)
    # bụi trượt
    if up and vfx and DASH1 - .02 < t < DASH1 + .45:
        q = t - DASH1 + .02
        for vx, vy, s in DUST:
            px = hx + 10 + vx * 40 * q * 3; py = FLOOR - 2 + vy * 22 * q * 3
            r = 3 + 6 * s * q * 3
            d.ellipse((px - r, py - r, px + r, py + r), fill=(205, 220, 226, int(150 * (1 - q / .47))))
    return v, hit_count

# ---------- khung ----------
BASE = Image.new('RGB', (W, H), '#121c22')
def frame_img(t, rate, mode, phase_t):
    im = BASE.copy(); d = ImageDraw.Draw(im)
    d.text((30, 18), 'Nhát C · Kiếm +6 · Lướt Trảm', font=F(30, True), fill='#f5dfab')
    d.text((560, 30), 'Demo chờ duyệt · dựng từ frame sprite trong game', font=F(17), fill='#9fb2b6')
    if mode == 'cmp': heads = [('DƯỚI +6 · chuỗi A–B', '#d6dfdc'), ('KIẾM +6 · chuỗi A–B–C', '#9fe9ef')]
    else: heads = [('KIẾM +6 · tắt hiệu ứng', '#d6dfdc'), ('KIẾM +6 · bật hiệu ứng', '#9fe9ef')]
    for c, (h, col) in enumerate(heads): d.text((30 + c * 620, 70), h, font=F(19, True), fill=col)
    for r, (g, name) in enumerate((('hero_nu', 'Nữ'), ('hero_nam', 'Nam'))):
        y = 100 + r * 272
        for c in range(2):
            up = c == 1 or mode == 'vfx'
            vfx = not (mode == 'vfx' and c == 0)
            p, n = panel(g, t, up, vfx)
            x = 30 + c * 620
            im.paste(p.convert('RGB'), (x, y))
            d.rectangle((x - 1, y - 1, x + PW, y + PH), outline='#4a5d62')
            d.rounded_rectangle((x + 8, y + 8, x + 58, y + 32), 5, fill='#17242a')
            d.text((x + 17, y + 11), name, font=F(15, True), fill='#e8eeee')
            if t > C_T + .05:
                txt = f'Trúng {n}/3 mục tiêu' + (' · mỗi mục tiêu 1 lần · đánh dấu Phá Thế' if up else ' · chỉ mục tiêu gần')
                d.text((x + 70, y + 12), txt, font=F(14, True), fill='#bfeff3' if up else '#d5dcdc')
    d.line((30, 652, 1250, 652), fill='#41555c')
    d.text((30, 668), rate, font=F(20, True), fill='#f7dfab')
    phases = ['A', 'B', 'Lấy đà', 'Lướt chém', 'Trượt dừng', 'Thu thế']
    bounds = [0, B_T, C_T, DASH0, DASH1, DASH1 + SLIDE, 9]
    ph = max(i for i in range(6) if phase_t >= bounds[i])
    for i, txt in enumerate(phases):
        x = 330 + i * 152
        on = i == ph
        d.rounded_rectangle((x, 668, x + 136, 673), 2, fill='#e9ca8a' if on else '#45595e')
        d.text((x, 682), txt, font=F(15, on), fill='#f7e2b8' if on else '#8fa3a8')
    return im

def timeline():
    out = []
    CYC = 1.85
    for rep in range(2):
        for n in range(int(CYC * FPS)): out.append((n / FPS, 'Tốc độ thật', 'cmp'))
    sl = .35
    for n in range(int((1.55 - .50) / sl * FPS)): out.append((.50 + n / FPS * sl, 'Quay chậm ×0,35', 'cmp'))
    for n in range(int((1.55 - .50) / sl * FPS)): out.append((.50 + n / FPS * sl, 'Quay chậm ×0,35 · so hiệu ứng', 'vfx'))
    for n in range(int(CYC * FPS)): out.append((n / FPS, 'Tốc độ thật · so hiệu ứng', 'vfx'))
    return out

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == 'check':
        picks = [.10, .72, .86, .90, 1.00, 1.30]
        sheet = Image.new('RGB', (1280, 1080))
        for i, t in enumerate(picks):
            sheet.paste(frame_img(t, f't={t}', 'cmp', t).resize((640, 360)), (i % 2 * 640, i // 2 * 360))
        sheet.save(Path(__file__).with_name('check.jpg'), quality=92)
    else:
        cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pixel_format', 'rgb24', '-video_size', f'{W}x{H}',
               '-framerate', str(FPS), '-i', '-', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
               '-pix_fmt', 'yuv420p', '-movflags', '+faststart', sys.argv[1]]
        with subprocess.Popen(cmd, stdin=subprocess.PIPE) as pr:
            for t, rate, mode in timeline():
                pr.stdin.write(frame_img(t, rate, mode, t).tobytes())
            pr.stdin.close(); sys.exit(pr.wait())
