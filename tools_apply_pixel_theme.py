#!/usr/bin/env python3
"""Apply the Pixel Overworld theme shell to the remaining legacy pages of mireiasem.com.

Reads each legacy Fluid-theme page, extracts its <head> SEO metadata and its
markdown-body content, then rebuilds the page with the same pixel shell used by
the 57 already-converted pages (index / articles / contact). Idempotent: pages
that already carry data-design="pixel" are skipped.

Usage:
    python3 tools_apply_pixel_theme.py           # convert
    python3 tools_apply_pixel_theme.py --check   # report status only
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECK_ONLY = '--check' in sys.argv

PIXEL_HEAD = '''<link rel="stylesheet" href="/pixel/fonts.css">
<link rel="stylesheet" href="/pixel/style.css">
<link rel="stylesheet" href="/pixel/game.css">
<link rel="stylesheet" href="/pixel/production.css">
<script src="/pixel/site.js" defer></script>'''

BRAND = '''<a class="brand" href="/"><img class="brand-star" src="/pixel/mireia-star.png" width="28" height="28" alt="">Mireia SEM</a>
<nav class="site-nav" aria-label="Main navigation"><a href="/#articles">Articles</a><a href="/archives/">Archive</a> <a href="/tools/">Tools</a><a href="/contact/">Contact</a></nav>'''

FOOTER = '''<footer class="site-footer shell"><span>&copy; Mireia SEM</span>
<nav aria-label="Site information"><a href="/about/">About</a><a href="/privacy-policy/">Privacy Policy</a><a href="/terms/">Terms</a><a href="/contact/">Contact</a><a href="/sitemap.xml">Sitemap</a></nav></footer>'''

COOKIE = '''<script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js" data-cfasync="false"></script><script>
window.addEventListener('load', function() {
  window.cookieconsent.initialise({
    palette: {
      popup: { background: '#1d1b30', text: '#f7f3fb', link: '#d7f984' },
      button: { background: '#d7f984', text: '#151524' }
    },
    content: {
      message: 'This website uses cookies for analytics and advertising. See our Privacy Policy for details.',
      dismiss: 'Got it!',
      link: 'Learn more',
      href: '/privacy-policy/'
    }
  });
});
</script>'''

ART_ALTS = {
    'folio-strategy.webp': 'Pixel-art large golden compass with a pointing needle on a floating rock tile, with a tiny flag and signpost.',
    'folio-measurement.webp': 'Pixel-art golden crystal data screen showing a rising chart with cyan data points, on a floating rock tile.',
    'folio-google.webp': 'Pixel-art golden search bar with a four-point star on a floating rock tile, with a tiny flag and treasure chest.',
    'folio-meta.webp': 'Pixel-art golden speech bubble with three dots and small chat bubbles around it, on a floating rock tile.',
    'folio-microsoft.webp': 'Pixel-art glowing cyan-blue portal with a golden symbol inside, on a floating rock tile with a tiny flag.',
    'folio-policy.webp': 'Pixel-art golden gear with a glowing keyhole and cyan energy, on a floating rock tile with a tiny flag.',
}

# page path -> (data-page, kicker, h1, art file)
PAGES = {
    'about/index.html': ('about', 'About the Blog', 'About Mireia SEM', 'folio-strategy.webp'),
    'archives/index.html': ('archives', 'The Library', 'Article Archive', 'folio-google.webp'),
    'categories/index.html': ('categories', 'The Library', 'Categories', 'folio-meta.webp'),
    'tags/index.html': ('tags', 'The Library', 'All Topics', 'folio-microsoft.webp'),
    'privacy-policy/index.html': ('legal', 'The Rulebook', 'Privacy Policy', 'folio-policy.webp'),
    'terms/index.html': ('legal', 'The Rulebook', 'Terms of Service', 'folio-policy.webp'),
    '404.html': ('notfound', 'Off the Map', 'Page Not Found', 'folio-strategy.webp'),
}

# Legacy Fluid head noise: drop these entirely (multiline blocks included).
NOISE = [
    r'<link[^>]*?(?:bootstrap\.min\.css|at\.alicdn\.com|/css/main\.css|highlight(?:-dark)?\.css|github-markdown|hint\.min\.css|fancybox\.min\.css|nprogress)[^>]*>',
    r'<script\s+id="fluid-configs">.*?</script>',
    r'<script\s+src="/js/[^"]+"></script>',
    r'<script>\s*NProgress\b.*?</script>',
]
NOISE_RE = re.compile('|'.join(f'(?:{p})' for p in NOISE), re.S | re.I)


def extract_head_meta(head: str) -> str:
    cleaned = NOISE_RE.sub('', head)
    # align theme-color with the pixel palette
    cleaned = re.sub(r'(<meta name="theme-color" content=")[^"]*(")', r'\g<1>#151426\g<2>', cleaned)
    lines = [ln.rstrip() for ln in cleaned.splitlines()]
    lines = [ln for ln in lines if ln.strip()]
    return '\n'.join(lines)


def extract_body_content(html: str, path: str) -> str:
    m = re.search(r'<div class="markdown-body[^"]*">', html)
    if not m:
        raise ValueError(f'no markdown-body in {path}')
    start = m.end()
    depth = 1
    for tag in re.finditer(r'<div\b|</div>', html[start:]):
        depth += -1 if tag.group() == '</div>' else 1
        if depth == 0:
            return html[start:start + tag.start()].strip()
    raise ValueError(f'unbalanced markdown-body in {path}')


def build_page(path: str, meta: str, body_content: str) -> str:
    page, kicker, h1, art = PAGES[path]
    art_alt = ART_ALTS[art]
    meta = re.sub(r'\s*</head>\s*$', '', meta).strip()

    if page == 'notfound':
        hero = f'''<section class="article-hero shell"><div>
<p class="kicker"><span class="pixel-star" aria-hidden="true"></span>{kicker}</p>
<h1 id="article-title">{h1}</h1>
<p class="article-deck">The page you're looking for doesn't exist. It may have been moved or deleted.</p>
<a class="button game-button" href="/">Back to Home</a>
</div></section>'''
    else:
        hero = f'''<section class="article-hero shell game-article-hero"><div>
<a class="text-link" href="/#articles">All articles</a>
<p class="kicker"><span class="pixel-star" aria-hidden="true"></span>{kicker}</p>
<h1 id="article-title">{h1}</h1>
</div><div class="pixel-scene article-scene"><img src="/pixel/{art}" width="900" height="600" alt="{art_alt}" fetchpriority="high"></div></section>'''

    content_class = 'article-body listing-body' if page in ('archives', 'categories', 'tags') else 'article-body'
    # The 404 hero already carries the full message + CTA; skip the redundant body block.
    if page == 'notfound':
        body_block = ''
    else:
        body_block = f'''<div class="reading-layout single-column shell"><article class="{content_class}" id="article-body"><div class="markdown-body">
{body_content}
</div></article></div>'''
    # These pages have no TOC aside, so use a centered single-column variant of reading-layout.
    return f'''<!doctype html>
<html lang="en">
<head>
{meta}

{PIXEL_HEAD}
</head>
<body data-design="pixel" data-page="{page}">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header shell">
{BRAND}
</header>
<main id="main">
{hero}
{body_block}</main>
{FOOTER}
{COOKIE}
</body>
</html>
'''


def process(path: str) -> bool:
    f = ROOT / path
    html = f.read_text(encoding='utf-8')
    if 'data-design="pixel"' in html:
        return False
    head_match = re.search(r'<head>(.*?)</head>', html, re.S)
    if not head_match:
        raise ValueError(f'no head in {path}')
    meta = extract_head_meta(head_match.group(1))
    body_content = extract_body_content(html, path)
    f.write_text(build_page(path, meta, body_content), encoding='utf-8')
    return True


def main():
    changed = []
    for path in PAGES:
        f = ROOT / path
        html = f.read_text(encoding='utf-8')
        is_pixel = 'data-design="pixel"' in html
        if CHECK_ONLY:
            print(('OK   ' if is_pixel else 'TODO ') + path)
        else:
            did = process(path)
            print(('DONE ' if did else 'SKIP ') + path)
            if did:
                changed.append(path)
    if not CHECK_ONLY:
        print(f'\nConverted {len(changed)} page(s).')


if __name__ == '__main__':
    main()
