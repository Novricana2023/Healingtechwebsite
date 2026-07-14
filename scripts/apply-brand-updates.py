"""Apply loader, footer logo, favicon meta, and image path updates across HTML pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LOADER_OLD = re.compile(
    r'<div id="loader" class="show">\s*<div class="loader"></div>\s*</div>',
    re.DOTALL,
)
LOADER_NEW = """<div id="loader" class="show">
            <div class="loader-wrap">
                <img src="img/official-logo.png" alt="HealingTech Initiative" class="loader-logo">
                <div class="loader-bar"><span></span></div>
            </div>
        </div>"""

FOOTER_LOGO = """<div class="footer-brand reveal">
                            <a href="index.html"><img src="img/official-logo.png" alt="HealingTech Initiative" class="footer-logo"></a>
                            <p class="footer-tagline">Support · Empower · Elevate</p>
                        </div>
                        """

FAVICON_BLOCK = """<link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#e8943a">"""

IMAGE_REPLACEMENTS = {
    "img/Program1.jpeg": "img/program-coders.jpg",
    "img/Program2.jpeg": "img/program-digital-inclusion.jpg",
    "img/program 2.jpeg": "img/program-digital-inclusion.jpg",
    "https://healingtechinitiative.org/img/official-logo.png": "https://healingtechinitiative.org/img/og-social.jpg",
}

OG_TWITTER_LOGO_ONLY = re.compile(
    r'(property="og:image" content=")https://healingtechinitiative\.org/img/official-logo\.png(")',
)


def ensure_favicon_meta(content: str) -> str:
    if "/favicon.ico" in content:
        return content
    content = re.sub(
        r'<link href="img/official-logo\.png" rel="icon">',
        FAVICON_BLOCK,
        content,
        count=1,
    )
    content = re.sub(
        r'<link href="img/favicon\.ico" rel="icon">',
        FAVICON_BLOCK,
        content,
        count=1,
    )
    return content


def ensure_og_social(content: str) -> str:
    content = OG_TWITTER_LOGO_ONLY.sub(
        r"\1https://healingtechinitiative.org/img/og-social.jpg\2", content
    )
    content = content.replace(
        'name="twitter:image" content="https://healingtechinitiative.org/img/official-logo.png"',
        'name="twitter:image" content="https://healingtechinitiative.org/img/og-social.jpg"',
    )
    if 'property="og:image"' not in content and "<head>" in content:
        content = content.replace(
            "<head>",
            '<head>\n    <meta property="og:image" content="https://healingtechinitiative.org/img/og-social.jpg">',
            1,
        )
    return content


def ensure_footer_logo(content: str) -> str:
    if "footer-brand" in content:
        return content
    marker = '<div class="footer-contact">'
    if marker in content:
        return content.replace(marker, FOOTER_LOGO + marker, 1)
    compact = '<div class="footer"><div class="container copyright">'
    compact_logo = (
        '<div class="footer"><div class="container text-center pt-4">'
        + FOOTER_LOGO.strip()
        + '</div><div class="container copyright">'
    )
    if compact in content:
        return content.replace(compact, compact_logo, 1)
    return content


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = LOADER_OLD.sub(LOADER_NEW, text)
    for old, new in IMAGE_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = ensure_favicon_meta(text)
    text = ensure_og_social(text)
    text = ensure_footer_logo(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    updated = []
    for html in sorted(ROOT.glob("*.html")):
        if process_file(html):
            updated.append(html.name)
    print("Updated:", ", ".join(updated) if updated else "none")


if __name__ == "__main__":
    main()
