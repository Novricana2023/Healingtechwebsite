"""Production SEO: meta, favicons, JSON-LD, performance hints, accessibility — all HTML pages."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://healingtechinitiative.org"
LOGO = f"{BASE}/img/official-logo.png"
OG_IMAGE = f"{BASE}/img/og-social.jpg"

ORG = {
    "@type": "NGO",
    "@id": f"{BASE}/#organization",
    "name": "HealingTech Initiative",
    "url": BASE,
    "logo": {"@type": "ImageObject", "url": LOGO, "width": 512, "height": 512},
    "image": OG_IMAGE,
    "description": "Technology-driven social impact organization leveraging innovation to improve the lives of children, youth, and underserved communities across Africa.",
    "email": "info@healingtechinitiative.org",
    "telephone": "+265997774972",
    "slogan": "Support · Empower · Elevate",
    "areaServed": ["Malawi", "Kenya", "Africa"],
    "sameAs": [
        "https://www.facebook.com/profile.php?id=61564442654149",
        "https://www.linkedin.com/company/the-healingtech-initiative/",
    ],
}

PAGES = {
    "index.html": {
        "path": "/",
        "title": "HealingTech Initiative | Support · Empower · Elevate",
        "description": "HealingTech Initiative — technology-driven social impact across Malawi and Kenya. Digital skills, innovation, inclusive support, and wellbeing for youth and children.",
        "index": True,
        "website": True,
        "breadcrumbs": [],
        "preload": "img/carousel-1.jpg",
    },
    "about.html": {
        "path": "/about",
        "title": "About Us | HealingTech Initiative",
        "description": "Our founder story, mission, and journey empowering children and youth across Africa through technology, education, and social innovation.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("About", "/about")],
    },
    "programs.html": {
        "path": "/programs",
        "title": "Programs & Initiatives | HealingTech Initiative",
        "description": "Ongoing and upcoming HealingTech programmes — Future Coders, digital inclusion, AI literacy, and community empowerment across Malawi and Kenya.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Programs", "/programs")],
    },
    "resources.html": {
        "path": "/resources",
        "title": "Resources | HealingTech Initiative",
        "description": "Guides, tools, and resources from HealingTech Initiative for partners, volunteers, and communities building digital opportunity in Africa.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Resources", "/resources")],
    },
    "contact.html": {
        "path": "/contact",
        "title": "Contact | HealingTech Initiative",
        "description": "Contact HealingTech Initiative for partnerships, volunteering, donations, and general enquiries. Lilongwe, Malawi & Nairobi, Kenya.",
        "index": True,
        "page_type": "ContactPage",
        "breadcrumbs": [("Home", "/"), ("Contact", "/contact")],
    },
    "focus-areas.html": {
        "path": "/focus-areas",
        "title": "Focus Areas | HealingTech Initiative",
        "description": "HealingTech focus areas: technology, AI, education, digital skills, healthcare access, inclusion, and community empowerment for youth in Africa.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Focus Areas", "/focus-areas")],
    },
    "why-healingtech.html": {
        "path": "/why-healingtech",
        "title": "Why HealingTech Matters | The Challenge We Are Solving",
        "description": "Evidence-based data on Malawi's digital divide, youth unemployment, education gaps, and mental health — and how HealingTech Initiative responds with technology and compassionate support.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Why HealingTech Matters", "/why-healingtech")],
    },
    "impact.html": {
        "path": "/impact",
        "title": "Impact | HealingTech Initiative",
        "description": "HealingTech Initiative impact — communities reached, programmes delivered, and measurable change across Malawi, Kenya, and Africa.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Impact", "/impact")],
    },
    "Partners.html": {
        "path": "/Partners",
        "title": "Partners | HealingTech Initiative",
        "description": "Partner with HealingTech Initiative to expand digital skills, innovation, and inclusive support for youth and children across Africa.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Partners", "/Partners")],
    },
    "donate.html": {
        "path": "/donate",
        "title": "Donate | HealingTech Initiative",
        "description": "Support HealingTech Initiative — your contribution helps deliver digital skills, inclusion programmes, and wellbeing support for youth in Africa.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Donate", "/donate")],
    },
    "volunteer.html": {
        "path": "/volunteer",
        "title": "Volunteer | HealingTech Initiative",
        "description": "Volunteer with HealingTech Initiative. Mentor youth, support programmes, and help bridge the digital divide in Malawi, Kenya, and beyond.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Volunteer", "/volunteer")],
    },
    "blog.html": {
        "path": "/blog",
        "title": "News & Stories | HealingTech Initiative",
        "description": "News, stories, and updates from HealingTech Initiative — technology for social good across Malawi, Kenya, and Africa.",
        "index": True,
        "page_type": "Blog",
        "breadcrumbs": [("Home", "/"), ("News & Stories", "/blog")],
    },
    "team.html": {
        "path": "/team",
        "title": "Our Team | HealingTech Initiative",
        "description": "Meet the leaders driving HealingTech Initiative — youth empowerment, innovation, and social impact across Malawi and Kenya.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Our Team", "/team")],
    },
    "event.html": {
        "path": "/event",
        "title": "Our Projects | HealingTech Initiative",
        "description": "HealingTech community projects including Clear Sight Initiative and Mathari Mentorship — real impact in Malawi and Kenya.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Our Projects", "/event")],
    },
    "initiative.html": {
        "path": "/initiative",
        "title": "HealingTech Initiative | Programs & Impact",
        "description": "Learn about HealingTech Initiative programmes, mission, and technology-driven social impact across Africa.",
        "index": True,
        "breadcrumbs": [("Home", "/"), ("Initiative", "/initiative")],
    },
    "faq.html": {
        "path": "/faq",
        "title": "FAQ | HealingTech Initiative",
        "description": "Frequently asked questions about HealingTech Initiative, our programmes, partnerships, and how to get involved.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("FAQ", "/faq")],
    },
    "technology.html": {
        "path": "/technology",
        "title": "Technology | HealingTech Labs",
        "description": "Technology capabilities from HealingTech Labs — software engineering partner to the HealingTech Initiative.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("Technology", "/technology")],
    },
    "solutions.html": {
        "path": "/solutions",
        "title": "Solutions | HealingTech Labs",
        "description": "Enterprise and community technology solutions from HealingTech Labs.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("Solutions", "/solutions")],
    },
    "products.html": {
        "path": "/products",
        "title": "Products | HealingTech Labs",
        "description": "Products and innovation from HealingTech Labs — technology for social good.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("Products", "/products")],
    },
    "portfolio.html": {
        "path": "/portfolio",
        "title": "Portfolio | HealingTech Labs",
        "description": "Portfolio of work from HealingTech Labs.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("Portfolio", "/portfolio")],
    },
    "industries.html": {
        "path": "/industries",
        "title": "Industries | HealingTech Labs",
        "description": "Industries served by HealingTech Labs technology services.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("Industries", "/industries")],
    },
    "service.html": {
        "path": "/service",
        "title": "Services | HealingTech Labs",
        "description": "Technology services from HealingTech Labs.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("Services", "/service")],
    },
    "careers.html": {
        "path": "/careers",
        "title": "Careers | HealingTech Labs",
        "description": "Career opportunities at HealingTech Labs.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("Careers", "/careers")],
    },
    "ai-assistant.html": {
        "path": "/ai-assistant",
        "title": "AI Assistant | HealingTech Initiative",
        "description": "HealingTech Initiative AI assistant — get answers about our programmes and mission.",
        "index": False,
        "breadcrumbs": [("Home", "/"), ("AI Assistant", "/ai-assistant")],
    },
    "single.html": {
        "path": "/single",
        "title": "Article | HealingTech Initiative",
        "description": "HealingTech Initiative news and stories — technology for social good across Africa.",
        "index": False,
        "page_type": "Article",
        "breadcrumbs": [("Home", "/"), ("News", "/blog"), ("Article", "/single")],
    },
}

SKIP_LINK = '<a href="#main-content" class="skip-link">Skip to main content</a>'

HEAD_END_MARKERS = (
    "<!-- Google Font",
    "<link href=\"https://fonts.googleapis.com",
    "<!-- CSS Libraries",
    "<link href=\"https://stackpath.bootstrapcdn.com",
    "<link href=\"css/style.css",
)


def favicon_block():
    return """    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#e8943a">
    <meta name="theme-color" content="#e8943a">
    <meta name="msapplication-TileColor" content="#1a2744">
    <meta name="msapplication-TileImage" content="/mstile-144x144.png">"""


def perf_hints(preload=None):
    hints = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://stackpath.bootstrapcdn.com">
    <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">"""
    if preload:
        hints += f'\n    <link rel="preload" href="{preload}" as="image" fetchpriority="high">'
    return hints


def breadcrumb_ld(page_meta):
    crumbs = page_meta.get("breadcrumbs") or []
    if not crumbs:
        return None
    items = []
    for i, (name, path) in enumerate(crumbs):
        items.append(
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": BASE + path,
            }
        )
    return {
        "@type": "BreadcrumbList",
        "@id": BASE + page_meta["path"] + "#breadcrumb",
        "itemListElement": items,
    }


def json_ld(page_meta, filename):
    url = BASE + page_meta["path"]
    page_type = page_meta.get("page_type", "WebPage")
    page_node = {
        "@type": page_type,
        "@id": url + "#webpage",
        "url": url,
        "name": page_meta["title"],
        "description": page_meta["description"],
        "isPartOf": {"@id": f"{BASE}/#website"},
        "about": {"@id": f"{BASE}/#organization"},
        "inLanguage": "en",
    }
    if page_type == "ContactPage":
        page_node["mainEntity"] = {"@id": f"{BASE}/#organization"}
    if page_type == "Article":
        page_node.update(
            {
                "headline": page_meta["title"].split("|")[0].strip(),
                "author": {"@id": f"{BASE}/#organization"},
                "publisher": {"@id": f"{BASE}/#organization"},
                "image": OG_IMAGE,
                "datePublished": "2025-01-01",
                "dateModified": "2026-07-01",
            }
        )
    if page_type == "Blog":
        page_node["@type"] = "CollectionPage"
        page_node["about"] = {"@type": "Blog", "name": "HealingTech News & Stories"}

    graphs = [page_node, dict(ORG)]
    if page_meta.get("website"):
        graphs.append(
            {
                "@type": "WebSite",
                "@id": f"{BASE}/#website",
                "url": BASE,
                "name": "HealingTech Initiative",
                "description": ORG["description"],
                "publisher": {"@id": f"{BASE}/#organization"},
                "inLanguage": "en",
                "potentialAction": {
                    "@type": "SearchAction",
                    "target": f"{BASE}/resources?q={{search_term_string}}",
                    "query-input": "required name=search_term_string",
                },
            }
        )
    bc = breadcrumb_ld(page_meta)
    if bc:
        graphs.append(bc)
    payload = {"@context": "https://schema.org", "@graph": graphs}
    return "    <script type=\"application/ld+json\">\n    " + json.dumps(payload, separators=(",", ":")) + "\n    </script>"


def build_head(title, page_meta, filename):
    url = BASE + page_meta["path"]
    desc = page_meta["description"]
    robots = "index, follow, max-image-preview:large" if page_meta.get("index", True) else "noindex, follow"
    og_type = "article" if page_meta.get("page_type") == "Article" else "website"
    preload = page_meta.get("preload")
    analytics_comment = """    <!-- Google Analytics (GA4): replace G-XXXXXXXXXX with your Measurement ID -->
    <!-- <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script> -->
    <!-- Google Search Console: add verification meta tag below when ready -->
    <!-- <meta name="google-site-verification" content="YOUR_VERIFICATION_CODE" /> -->"""
    return f"""    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{desc}">
    <meta name="author" content="HealingTech Initiative">
    <link rel="canonical" href="{url}">
    <meta name="robots" content="{robots}">
    <meta property="og:locale" content="en_US">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="HealingTech Initiative">
    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:image:secure_url" content="{OG_IMAGE}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="HealingTech Initiative — Support, Empower, Elevate">
    <meta property="og:logo" content="{LOGO}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{OG_IMAGE}">
    <meta name="twitter:image:alt" content="HealingTech Initiative logo and tagline">
{analytics_comment}
{favicon_block()}
{perf_hints(preload)}
{json_ld(page_meta, filename)}"""


def replace_head(content, filename, page_meta):
    new_head = build_head(page_meta["title"], page_meta, filename)
    content = re.sub(
        r"\s*<script type=\"application/ld\+json\">.*?</script>",
        "",
        content,
        count=0,
        flags=re.DOTALL,
    )
    match = re.search(r"<head>\s*", content, re.IGNORECASE)
    if not match:
        return content
    start = match.end()
    end = start
    for marker in HEAD_END_MARKERS:
        pos = content.find(marker, start)
        if pos != -1 and (end == start or pos < end):
            end = pos
    if end == start:
        end = content.find("</head>", start)
    return content[:start] + "\n" + new_head + "\n\n        " + content[end:]


def add_lazy_loading(content):
    skip_patterns = (
        "brand-logo", "loader-logo", "footer-logo", "carousel-img",
        "official-logo", "about-logo", "initiative-logo", "labs-card-logo",
    )

    def repl(m):
        tag = m.group(0)
        if "loading=" in tag:
            return tag
        if any(p in tag for p in skip_patterns):
            if "fetchpriority=" not in tag and "carousel" in tag:
                return tag.replace("<img ", '<img fetchpriority="high" ', 1)
            return tag
        ins = "loading=\"lazy\" decoding=\"async\" "
        return tag.replace("<img ", "<img " + ins, 1)

    return re.sub(r"<img(?![^>]*loading=)[^>]*>", repl, content)


def inject_skip_link(content):
    if "skip-link" in content:
        return content
    return re.sub(r"(<body[^>]*>)", r"\1\n        " + SKIP_LINK, content, count=1, flags=re.I)


def inject_main_target(content, filename):
    if filename == "index.html" and '<main class="carousel"' not in content:
        content = content.replace('<div class="carousel">', '<main class="carousel" id="main-content">', 1)
        content = content.replace("<!-- Carousel End -->", "</main>\n        <!-- Carousel End -->", 1)
    elif '<main class="labs-hero-mini"' in content:
        pass
    elif '<div class="labs-hero-mini">' in content:
        content = content.replace(
            '<div class="labs-hero-mini">',
            '<div class="labs-hero-mini" id="main-content" role="main">',
            1,
        )
    elif 'class="page-header"' in content and 'id="main-content"' not in content:
        content = content.replace(
            'class="page-header"',
            'class="page-header" id="main-content" role="main"',
            1,
        )
    return content


def fix_main_closing(content):
    content = re.sub(
        r'(<main class="labs-hero-mini" id="main-content">.*?</div>)\s*</div>',
        r"\1</main>",
        content,
        flags=re.DOTALL,
    )
    return content


def fix_social_aria(content):
    content = re.sub(
        r'(<a href="https://www\.facebook\.com[^"]*")(?![^>]*aria-label)',
        r'\1 aria-label="HealingTech on Facebook"',
        content,
    )
    content = re.sub(
        r'(<a href="https://www\.linkedin\.com[^"]*")(?![^>]*aria-label)',
        r'\1 aria-label="HealingTech on LinkedIn"',
        content,
    )
    return content


def optimize_scripts(content, filename):
    if filename == "index.html":
        content = content.replace('<script src="lib/parallax/parallax.min.js"></script>\n', "")
        content = content.replace('<script src="lib/counterup/counterup.min.js"></script>\n', "")
    defer_libs = (
        "lib/easing/easing.min.js",
        "lib/owlcarousel/owl.carousel.min.js",
        "lib/waypoints/waypoints.min.js",
        "lib/parallax/parallax.min.js",
        "lib/counterup/counterup.min.js",
        "js/main.js",
        "js/reveal.js",
        "js/challenge-stats.js",
        "js/faq.js",
        "js/ai-assistant.js",
    )
    for lib in defer_libs:
        content = content.replace(f'<script src="{lib}">', f'<script defer src="{lib}">')
    return content


def fix_missing_alts(content):
    alt_map = {
        "single.jpg": "HealingTech Initiative article feature image",
        "user.jpg": "Community member profile photo",
        "post-1.jpg": "HealingTech news and stories",
        "post-2.jpg": "HealingTech programme update",
        "post-3.jpg": "HealingTech community impact story",
        "post-4.jpg": "HealingTech youth empowerment story",
        "post-5.jpg": "HealingTech digital skills story",
        "blog-1.jpg": "HealingTech blog post thumbnail",
        "blog-2.jpg": "HealingTech blog post thumbnail",
        "blog-3.jpg": "HealingTech blog post thumbnail",
    }

    def repl(m):
        tag = m.group(0)
        if "alt=" in tag:
            return tag
        src_m = re.search(r'src="([^"]+)"', tag)
        if not src_m:
            return tag
        fname = Path(src_m.group(1)).name
        alt = alt_map.get(fname, f"HealingTech Initiative — {fname.replace('-', ' ').split('.')[0]}")
        return tag.replace("<img ", f'<img alt="{alt}" ', 1)

    return re.sub(r"<img(?![^>]*alt=)[^>]*>", repl, content)


def ensure_lang(content):
    content = re.sub(r'\s+lang="en"(?=\s+lang="en")', "", content)
    return re.sub(r"<html[^>]*>", '<html lang="en">', content, count=1, flags=re.I)


def process_file(path: Path) -> bool:
    meta = PAGES.get(path.name)
    if not meta:
        return False
    original = path.read_text(encoding="utf-8")
    updated = replace_head(original, path.name, meta)
    updated = add_lazy_loading(updated)
    updated = inject_skip_link(updated)
    updated = inject_main_target(updated, path.name)
    updated = fix_main_closing(updated)
    updated = fix_social_aria(updated)
    updated = fix_missing_alts(updated)
    updated = optimize_scripts(updated, path.name)
    updated = ensure_lang(updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def write_sitemap():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for name, meta in sorted(PAGES.items(), key=lambda x: x[1]["path"]):
        if not meta.get("index", True):
            continue
        pri = "1.0" if meta["path"] == "/" else "0.8"
        freq = "weekly" if name in ("index.html", "programs.html", "blog.html") else "monthly"
        lines.append(
            f"  <url><loc>{BASE}{meta['path']}</loc><changefreq>{freq}</changefreq><priority>{pri}</priority></url>"
        )
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_robots():
    disallow = [
        "/single", "/faq", "/technology", "/solutions", "/products",
        "/portfolio", "/industries", "/service", "/careers", "/ai-assistant",
    ]
    lines = ["User-agent: *", "Allow: /", ""]
    for d in disallow:
        lines.append(f"Disallow: {d}")
    lines.extend(["", f"Sitemap: {BASE}/sitemap.xml", ""])
    (ROOT / "robots.txt").write_text("\n".join(lines), encoding="utf-8")


def main():
    updated = []
    for name in PAGES:
        p = ROOT / name
        if p.exists() and process_file(p):
            updated.append(name)
    write_sitemap()
    write_robots()
    print("SEO updated:", ", ".join(updated) if updated else "none")


if __name__ == "__main__":
    main()
