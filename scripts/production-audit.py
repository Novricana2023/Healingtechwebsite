"""Production QA audit: links, images, SEO meta, accessibility."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = list(ROOT.glob("*.html"))
WARNINGS = []
ERRORS = []


def warn(msg):
    WARNINGS.append(msg)


def err(msg):
    ERRORS.append(msg)


def audit_file(path: Path):
    text = path.read_text(encoding="utf-8")
    name = path.name

    if "<title>" not in text:
        err(f"{name}: missing <title>")
    if 'name="description"' not in text:
        err(f"{name}: missing meta description")
    if 'rel="canonical"' not in text:
        err(f"{name}: missing canonical URL")
    if "application/ld+json" not in text:
        warn(f"{name}: missing JSON-LD")
    if 'rel="icon"' not in text or "favicon.ico" not in text:
        err(f"{name}: missing favicon")
    if "og:image" not in text:
        err(f"{name}: missing Open Graph image")
    if 'lang="en"' not in text:
        warn(f"{name}: missing lang=en on html")

    for m in re.finditer(r'<img([^>]*)>', text, re.I):
        attrs = m.group(1)
        if "alt=" not in attrs:
            err(f"{name}: img missing alt - {m.group(0)[:80]}")
        elif re.search(r'alt\s*=\s*""', attrs):
            err(f"{name}: empty alt text")

    for m in re.finditer(r'href="([^"#][^"]*)"', text):
        href = m.group(1)
        if href.startswith(("http", "mailto:", "tel:", "javascript:")):
            continue
        target = ROOT / href.split("?")[0].split("#")[0]
        if not target.exists() and not href.startswith("/"):
            err(f"{name}: broken link -> {href}")

    for m in re.finditer(r'src="([^"]+)"', text):
        src = m.group(1)
        if src.startswith(("http", "data:", "//")):
            continue
        target = ROOT / src.split("?")[0]
        if not target.exists():
            err(f"{name}: broken image/script -> {src}")


def audit_assets():
    required = [
        "favicon.ico", "favicon-16x16.png", "favicon-32x32.png", "favicon-48x48.png",
        "safari-pinned-tab.svg", "site.webmanifest", "sitemap.xml", "robots.txt",
        "android-chrome-192x192.png", "android-chrome-512x512.png",
        "img/official-logo.png", "img/og-social.jpg", "img/apple-touch-icon.png",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            err(f"Missing asset: {rel}")


def main():
    audit_assets()
    for f in sorted(HTML):
        audit_file(f)
    print(f"Audited {len(HTML)} HTML pages")
    if WARNINGS:
        print(f"\nWarnings ({len(WARNINGS)}):")
        for w in WARNINGS:
            print("  WARN:", w)
    if ERRORS:
        print(f"\nErrors ({len(ERRORS)}):")
        for e in ERRORS:
            print("  ERR:", e)
        sys.exit(1)
    print("\nProduction audit passed.")


if __name__ == "__main__":
    main()
