from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import io, os

SITE = 'site/assets/img'
FONTS = 'site/assets/fonts'
BG = (250, 247, 242)
INK = (27, 24, 20)
MUTED = (109, 104, 88)
ACCENT = (122, 46, 31)
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

# 1200x900 landscape covers for the pinned-chapters 4:3 frame
def cover(path, kicker, title, meta, accent=False):
    W, H = 1200, 900
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    m = 64
    d.rectangle([m, m, W - m, H - m], outline=LINE, width=2)
    f_label = font(24)
    f_title = font(76)
    f_meta = font(30)
    f_small = font(24)
    d.text((m + 28, m + 34), kicker.upper(), font=f_label, fill=ACCENT if accent else MUTED)
    d.line([(m + 28, m + 74), (m + 28 + 110, m + 74)], fill=ACCENT, width=4)
    words = title.split()
    lines, cur = [], ''
    maxw = W - 2 * (m + 28)
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if d.textlength(t, font=f_title) > maxw and cur:
            lines.append(cur); cur = wd
        else:
            cur = t
    lines.append(cur)
    y = m + 140
    for ln in lines:
        d.text((m + 28, y), ln, font=f_title, fill=INK)
        y += 88
    ym = H - m - 84
    d.line([(m + 28, ym - 18), (W - m - 28, ym - 18)], fill=LINE, width=2)
    d.text((m + 28, ym), meta, font=f_meta, fill=INK)
    d.text((m + 28, ym + 50), 'shruuspeaks@gmail.com', font=f_small, fill=MUTED)
    d.text((W - m - 28, H - m - 42), 'SG.', font=font(30), fill=ACCENT, anchor='ra')
    im.save(os.path.join(SITE, path + '-land.webp'), 'WEBP', quality=90)
    im.save(os.path.join(SITE, path + '-land.jpg'), 'JPEG', quality=90)
    print(path + '-land', im.size)

cover('cover-blog', 'Bragly.io · SEO Blog', 'Keyword research for SaaS product launches', 'Blog · 2026', accent=True)
cover('cover-landing', 'Phantom Rent A Car · Landing Page', 'Dubai car rental, written to convert', 'Landing page · 2026')
cover('cover-howto', 'ImageWith.ai · How-to Guide', 'Upscaling images with AI, step by step', 'How-to guide · 2026', accent=True)
print('done')
