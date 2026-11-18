from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import io, os

SITE = 'site/assets/img'
RAW = 'imagery/user-assets'
FONTS = 'site/assets/fonts'
PAPER = (241, 236, 227)   # --p-surface
BG = (250, 247, 242)      # --p-bg
INK = (27, 24, 20)        # --p-ink
MUTED = (109, 104, 88)    # --p-muted
ACCENT = (122, 46, 31)    # --p-accent
LINE = (221, 214, 200)

def woff2_to_ttf(path):
    data = open(path, 'rb').read()
    f = TTFont(io.BytesIO(data))
    buf = io.BytesIO()
    f.flavor = None
    f.save(buf)
    buf.seek(0)
    return buf

def font(size, italic=False):
    name = 'instrument-serif-italic-400.woff2' if italic else 'instrument-serif-normal-400.woff2'
    ttf = woff2_to_ttf(os.path.join(FONTS, name))
    ttf.seek(0)
    return ImageFont.truetype(ttf, size)

# ---------- portrait plates 768x960 (4:5), cutout on paperTint ----------
def plate(src, dst):
    cut = Image.open(src).convert('RGBA')
    W, H = 768, 960
    canvas = Image.new('RGBA', (W, H), PAPER + (255,))
    # fit cutout to ~80% height, keep aspect
    ch = int(H * 0.82)
    cw = int(cut.width * ch / cut.height)
    cut = cut.resize((cw, ch), Image.LANCZOS)
    x = (W - cw) // 2
    y = H - ch - int(H * 0.06)
    canvas.alpha_composite(cut, (x, y))
    rgb = canvas.convert('RGB')
    rgb.save(os.path.join(SITE, dst + '.webp'), 'WEBP', quality=88)
    print(dst, rgb.size)

plate(f'{RAW}/photo2_nobg.png', 'portrait-hero-768')
plate(f'{RAW}/photo1_nobg.png', 'portrait-about-768')

# ---------- still-desk padded to 1132x520 (was 1132x442) ----------
still = Image.open('imagery/raw/still-desk.jpg').convert('RGB')
w, h = still.size
newh = 520
pad = (newh - h) // 2
top = still.crop((0, 0, w, 8)).resize((w, pad), Image.LANCZOS)
bot = still.crop((0, h - 8, w, h)).resize((w, newh - h - pad), Image.LANCZOS)
out = Image.new('RGB', (w, newh))
out.paste(top, (0, 0)); out.paste(still, (0, pad)); out.paste(bot, (0, pad + h))
out.save(os.path.join(SITE, 'still-desk-tall.webp'), 'WEBP', quality=88)
out.save(os.path.join(SITE, 'still-desk-tall.jpg'), 'JPEG', quality=88)
print('still-desk-tall', out.size)

# ---------- cover visuals 768x960 ----------
def cover(path, kicker, title, meta, accent=False):
    W, H = 768, 960
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    m = 72
    # hairline frame
    d.rectangle([m, m, W - m, H - m], outline=LINE, width=2)
    f_label = font(26)
    f_title = font(64)
    f_meta = font(30)
    f_small = font(24)
    # kicker top
    d.text((m + 24, m + 36), kicker.upper(), font=f_label, fill=ACCENT if accent else MUTED)
    # accent rule under kicker
    d.line([(m + 24, m + 78), (m + 24 + 120, m + 78)], fill=ACCENT, width=4)
    # title, wrapped manually ~ 3 lines max
    words = title.split()
    lines, cur = [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if d.textlength(t, font=f_title) > W - 2 * (m + 24) and cur:
            lines.append(cur); cur = wd
        else:
            cur = t
    lines.append(cur)
    y = m + 150
    for ln in lines:
        d.text((m + 24, y), ln, font=f_title, fill=INK)
        y += 78
    # meta bottom
    ym = H - m - 90
    d.line([(m + 24, ym - 20), (W - m - 24, ym - 20)], fill=LINE, width=2)
    d.text((m + 24, ym), meta, font=f_meta, fill=INK)
    d.text((m + 24, ym + 52), 'shruuspeaks@gmail.com', font=f_small, fill=MUTED)
    # corner mark
    d.text((W - m - 24, H - m - 44), 'SG.', font=font(30), fill=ACCENT, anchor='ra')
    im.save(os.path.join(SITE, path + '.webp'), 'WEBP', quality=90)
    im.save(os.path.join(SITE, path + '.jpg'), 'JPEG', quality=90)
    print(path, im.size)

cover('cover-blog', 'Bragly.io · SEO Blog', 'Keyword research for SaaS product launches', 'Blog · 2026', accent=True)
cover('cover-landing', 'Phantom Rent A Car · Landing Page', 'Dubai car rental, written to convert', 'Landing page · 2026')
cover('cover-howto', 'ImageWith.ai · How-to Guide', 'Upscaling images with AI, step by step', 'How-to guide · 2026', accent=True)
print('done')

# ---------- square crop of portrait-hero plate for potential reuse ----------
p = Image.open(os.path.join(SITE, 'portrait-hero-768.webp')).convert('RGB')
s = p.crop((0, 0, 768, 768))
s.save(os.path.join(SITE, 'pic-hero-square.webp'), 'WEBP', quality=88)
print('pic-hero-square', s.size)
# square of about plate
p2 = Image.open(os.path.join(SITE, 'portrait-about-768.webp')).convert('RGB')
p2.crop((0, 0, 768, 768)).save(os.path.join(SITE, 'pic-about-square.webp'), 'WEBP', quality=88)
print('pic-about-square', (768, 768))
# desk square-ish crop
sd = Image.open(os.path.join(SITE, 'still-desk-tall.webp')).convert('RGB')
sd.crop((140, 60, 908, 780)).save(os.path.join(SITE, 'pic-desk.webp'), 'WEBP', quality=88)
print('pic-desk', (768, 720))
print('ALL DONE')
