"""Generate favicons, OG cover, Safari mask icon, and PWA icons from official logo."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "img"
LOGO_PATH = IMG / "official-logo.png"
NAVY = (26, 39, 68)
ORANGE = (232, 148, 58)
TEAL = (45, 143, 168)
WHITE = (255, 255, 255)


def load_logo():
    return Image.open(LOGO_PATH).convert("RGBA")


def fit_logo(size, padding=0.12, bg=NAVY):
    logo = load_logo()
    w, h = logo.size
    side = int(size * (1 - padding * 2))
    scale = min(side / w, side / h)
    nw, nh = int(w * scale), int(h * scale)
    resized = logo.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (*bg, 255))
    x = (size - nw) // 2
    y = (size - nh) // 2
    canvas.paste(resized, (x, y), resized)
    return canvas.convert("RGB")


def save_png_sizes():
    sizes = [
        (16, ROOT / "favicon-16x16.png"),
        (32, ROOT / "favicon-32x32.png"),
        (48, ROOT / "favicon-48x48.png"),
        (180, IMG / "apple-touch-icon.png"),
        (192, IMG / "icon-192.png"),
        (192, ROOT / "android-chrome-192x192.png"),
        (512, IMG / "icon-512.png"),
        (512, ROOT / "android-chrome-512x512.png"),
        (144, ROOT / "mstile-144x144.png"),
    ]
    for size, path in sizes:
        fit_logo(size).save(path, optimize=True)
    ico_images = [fit_logo(s) for s in (16, 32, 48)]
    ico_images[0].save(
        ROOT / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=ico_images[1:],
    )


def build_mask_icon():
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="96" fill="#000"/>
  <circle cx="256" cy="256" r="200" fill="#000"/>
  <path fill="#000" d="M148 168h52v144h-52V168zm82 0h52l56 96 56-96h52v144h-48V248l-52 88h-8l-52-88v64h-48V168z"/>
</svg>"""
    (ROOT / "safari-pinned-tab.svg").write_text(svg, encoding="utf-8")


def draw_text_centered(draw, text, y, font, fill=WHITE, width=1200):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, y), text, font=font, fill=fill)


def build_og_social():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), NAVY)
    draw = ImageDraw.Draw(img)
    for i in range(h):
        t = i / h
        r = int(NAVY[0] + (TEAL[0] - NAVY[0]) * t * 0.45)
        g = int(NAVY[1] + (TEAL[1] - NAVY[1]) * t * 0.45)
        b = int(NAVY[2] + (TEAL[2] - NAVY[2]) * t * 0.45)
        draw.line([(0, i), (w, i)], fill=(r, g, b))
    draw.ellipse([780, -100, 1220, 340], fill=(232, 148, 58, 30))
    draw.ellipse([-120, 380, 380, 720], fill=(45, 143, 168, 25))
    for x in range(0, w, 80):
        draw.line([(x, 0), (x + 120, h)], fill=(45, 143, 168, 18), width=1)
    logo = load_logo()
    lw = 400
    scale = lw / logo.width
    lh = int(logo.height * scale)
    logo_r = logo.resize((lw, lh), Image.Resampling.LANCZOS)
    img_rgba = img.convert("RGBA")
    img_rgba.paste(logo_r, ((w - lw) // 2, 72), logo_r)
    draw = ImageDraw.Draw(img_rgba)
    try:
        font_lg = ImageFont.truetype("arialbd.ttf", 44)
        font_md = ImageFont.truetype("arial.ttf", 30)
        font_sm = ImageFont.truetype("arial.ttf", 24)
    except OSError:
        try:
            font_lg = ImageFont.truetype("arial.ttf", 44)
            font_md = ImageFont.truetype("arial.ttf", 30)
            font_sm = ImageFont.truetype("arial.ttf", 24)
        except OSError:
            font_lg = font_md = font_sm = ImageFont.load_default()
    draw_text_centered(draw, "HealingTech Initiative", 72 + lh + 32, font_lg, ORANGE, w)
    draw_text_centered(draw, "Support · Empower · Elevate", 72 + lh + 92, font_md, (230, 235, 245), w)
    draw_text_centered(
        draw,
        "Technology-driven social impact across Malawi, Kenya & Africa",
        72 + lh + 142,
        font_sm,
        (175, 188, 210),
        w,
    )
    bar_y = h - 48
    draw.rectangle([0, bar_y, w, h], fill=(232, 148, 58))
    draw_text_centered(draw, "healingtechinitiative.org", bar_y + 12, font_sm, NAVY, w)
    img_rgba.convert("RGB").save(IMG / "og-social.jpg", quality=90, optimize=True)


def build_page_header():
    w, h = 1920, 600
    img = Image.new("RGB", (w, h), NAVY)
    draw = ImageDraw.Draw(img)
    for i in range(h):
        t = i / h
        c = (int(26 + 30 * t), int(39 + 50 * t), int(68 + 40 * t))
        draw.line([(0, i), (w, i)], fill=c)
    logo = load_logo()
    mark_w = 140
    scale = mark_w / logo.width
    mark_h = int(logo.height * scale)
    mark = logo.resize((mark_w, mark_h), Image.Resampling.LANCZOS)
    img_rgba = img.convert("RGBA")
    img_rgba.paste(mark, (w - mark_w - 48, h - mark_h - 40), mark)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(overlay).rectangle([0, 0, w, h], fill=(26, 39, 68, 100))
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img_rgba.convert("RGB").save(IMG / "page-header.jpg", quality=85, optimize=True)


def write_manifest():
    manifest = {
        "id": "/",
        "name": "HealingTech Initiative",
        "short_name": "HealingTech",
        "description": "Support · Empower · Elevate — technology for healing, empowerment, and opportunity across Africa.",
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "orientation": "portrait-primary",
        "background_color": "#1a2744",
        "theme_color": "#e8943a",
        "lang": "en",
        "categories": ["education", "social", "nonprofit"],
        "icons": [
            {"src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
            {"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        ],
    }
    import json
    (ROOT / "site.webmanifest").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    save_png_sizes()
    build_mask_icon()
    build_og_social()
    build_page_header()
    write_manifest()
    print("Brand assets built: favicons, OG image, mask-icon, manifest.")
