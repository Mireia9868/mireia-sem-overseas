#!/usr/bin/env python3
"""
Generate per-tag and per-category archive pages for mireiasem.com.

The site links to /tags/<slug>/ and /categories/<slug>/ from every article,
the homepage, and the tag/category clouds, but those child pages never
existed — all of them landed on 404.html. This script creates them using
the current pixel-theme template, so internal links resolve and GA4 stops
recording 404 pageviews.

Data source: article_meta.json (55 articles, authoritative).
Template source: the pixel-theme head/header/footer in tags/index.html.

Idempotent: re-running overwrites generated child pages with identical
content. It never touches existing top-level pages or article pages.

Usage:
    python3 generate_tag_category_pages.py           # generate pages
    python3 generate_tag_category_pages.py --check    # report coverage only
"""

import os, re, sys, json, html as H
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHECK_ONLY = '--check' in sys.argv
SITE = 'https://mireiasem.com'

CAT_DESC = {
    'Ad-Channels': 'Google Ads, Bing Ads, Facebook Ads campaign setup and optimization guides.',
    'Channel-Policies': 'Platform policy updates, ad disapproval solutions, and compliance walkthroughs.',
    'Conversion-Tracking': 'Pixel deployment, UET tags, offline conversion upload, and code integration.',
    'Tools-&-Tips': 'Advertising tools, account optimization, and workflow efficiency tips.',
    'SEM': 'Search engine marketing strategy, keyword research, and account structure best practices.',
    'Campaign-Optimization': 'Campaign optimization techniques, bidding strategies, and performance tuning.',
    'Uncategorized': 'Assorted search engine marketing guides and reference articles.',
}


def slugify(s):
    """Match the site's URL convention: spaces -> hyphens, & preserved."""
    return s.replace(' ', '-')


def load_articles():
    meta = json.load(open(os.path.join(BASE_DIR, 'article_meta.json'), encoding='utf-8'))
    articles = []
    for a in meta:
        url = f"/{a['date'].replace('-', '/')}/{a['slug']}/"
        articles.append({
            'title': a['title'],
            'url': url,
            'date': a['date'],
            'excerpt': a.get('excerpt', ''),
            'category': a.get('category', ''),
            'subcategory': a.get('subcategory', ''),
            'tags': a.get('tags', []),
        })
    articles.sort(key=lambda x: x['date'], reverse=True)
    return articles


def build_indexes(articles):
    by_tag = defaultdict(list)
    by_cat = defaultdict(list)
    tag_display = {}
    cat_display = {}
    for a in articles:
        for t in a['tags']:
            s = slugify(t)
            by_tag[s].append(a)
            # Prefer the natural-word display form (#Google Ads) over the
            # legacy hyphenated form (#Google-Ads) when both exist.
            if s not in tag_display or ('-' not in t):
                tag_display[s] = t
        if a['category']:
            s = slugify(a['category'])
            by_cat[s].append(a)
            cat_display[s] = a['category']
        if a['subcategory']:
            s = slugify(a['subcategory'])
            by_cat[s].append(a)
            cat_display.setdefault(s, a['subcategory'])
    # Historical category link still present in categories/index.html and one article.
    cat_display.setdefault('Uncategorized', 'Uncategorized')
    return by_tag, by_cat, tag_display, cat_display


def referenced_slugs():
    """Collect every tag/category slug actually linked anywhere in the site."""
    tags, cats = set(), set()
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules')]
        for f in files:
            if not f.endswith('.html'):
                continue
            c = open(os.path.join(root, f), encoding='utf-8', errors='ignore').read()
            for m in re.finditer(r'href="/tags/([^/]+)/"', c):
                tags.add(m.group(1))
            for m in re.finditer(r'href="/categories/([^/]+)/"', c):
                cats.add(m.group(1))
    return tags, cats


# --- pixel-theme template, copied from tags/index.html ---

TEMPLATE_HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
  <meta name="google-site-verification" content="GIdO_iD4VCjnetTm8q99G5TLiGSH9HdRoItNgPjZmP8" />
  <link rel="apple-touch-icon" sizes="76x76" href="/img/Mireia%20Sem_transparent.png">
  <link rel="icon" href="/img/Mireia%20Sem_transparent.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="theme-color" content="#151426">
  <meta name="author" content="Mireia">
  <meta name="keywords" content="SEM, Google Ads, Bing Ads, Facebook Ads, cross-border e-commerce, conversion tracking, digital advertising">
  <meta name="description" content="__DESC__">
<meta name="twitter:card" content="summary_large_image">
  <meta name="referrer" content="no-referrer-when-downgrade">
  <title>__TITLE__</title>
<meta name="google-adsense-account" content="ca-pub-2269516311541291">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2269516311541291"
     crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.css"><style>.cc-window,.cc-revoke{font-family:var(--mono,ui-monospace,SFMono-Regular,Menlo,monospace)!important}.cc-btn,.cc-link{font-family:inherit!important}.cc-link{opacity:1!important}</style>
  <!-- SEO Optimization -->
  <link rel="canonical" href="__CANONICAL__">
<meta property="og:type" content="website">
<meta property="og:url" content="__CANONICAL__">
<meta property="og:title" content="__OG_TITLE__">
<meta property="og:description" content="__DESC__">
<meta property="og:image" content="https://mireiasem.com/img/og-cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="__OG_TITLE__">
<meta name="twitter:title" content="__OG_TITLE__">
<meta name="twitter:description" content="__DESC__">
<meta name="twitter:image" content="https://mireiasem.com/img/og-cover.png">
<meta property="og:site_name" content="Mireia SEM Blog">
<meta property="og:locale" content="en_US">
<meta property="article:author" content="Mireia">
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0FRC1RXQLV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-0FRC1RXQLV');
  </script>

<link rel="stylesheet" href="/pixel/fonts.css">
<link rel="stylesheet" href="/pixel/style.css">
<link rel="stylesheet" href="/pixel/game.css">
<link rel="stylesheet" href="/pixel/production.css">
<script src="/pixel/site.js" defer></script>
</head>
<body data-design="pixel" data-page="listing">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header shell">
<a class="brand" href="/"><img class="brand-star" src="/pixel/mireia-star.png" width="28" height="28" alt="">Mireia SEM</a>
<nav class="site-nav" aria-label="Main navigation"><a href="/#articles">Articles</a><a href="/archives/">Archive</a> <a href="/tools/">Tools</a><a href="/contact/">Contact</a></nav>
</header>
<main id="main">
<section class="article-hero shell game-article-hero"><div>
<a class="text-link" href="__BACK_LINK__">__BACK_TEXT__</a>
<p class="kicker"><span class="pixel-star" aria-hidden="true"></span>__KICKER__</p>
<h1 id="article-title">__H1__</h1>
</div><div class="pixel-scene article-scene"><img src="/pixel/folio-google.webp" width="900" height="600" alt="Pixel-art golden search bar with a four-point star on a floating rock tile, with a tiny flag and treasure chest." fetchpriority="high"></div></section>
<div class="reading-layout single-column shell"><article class="article-body listing-body" id="article-body"><div class="markdown-body">
<div class="archive-timeline">
__ITEMS__
</div>
</div></article></div></main>
<footer class="site-footer shell"><span>&copy; Mireia SEM</span>
<nav aria-label="Site information"><a href="/about/">About</a><a href="/privacy-policy/">Privacy Policy</a><a href="/terms/">Terms</a><a href="/contact/">Contact</a><a href="/sitemap.xml">Sitemap</a></nav></footer>
<script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js" data-cfasync="false"></script><script>
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
</script>
</body>
</html>
'''


def build_page(kind, slug, display, articles, back_link, back_text, kicker):
    url = f'{SITE}/{kind}/{slug}/'
    if kind == 'tags':
        desc = f'Explore {len(articles)} article{"s" if len(articles) != 1 else ""} tagged #{display} on Mireia SEM Blog — practical Google Ads, Bing Ads, and conversion tracking guides.'
        og_title = f'#{display}'
        h1 = f'#{display}'
        title = f'#{display} - Mireia SEM Blog'
    else:
        desc = CAT_DESC.get(slug, f'Browse {len(articles)} articles in the {display} category on Mireia SEM Blog.')
        og_title = display
        h1 = display
        title = f'{display} - Mireia SEM Blog'

    if articles:
        items = '\n'.join(
            f'<li class="archive-item"><span class="archive-date">{a["date"]}</span>'
            f'<a href="{a["url"]}">{H.escape(a["title"])}</a></li>'
            for a in articles
        )
    else:
        items = '<li class="archive-item">No articles in this topic yet.</li>'

    page = (TEMPLATE_HEAD
            .replace('__DESC__', H.escape(desc, quote=True))
            .replace('__TITLE__', H.escape(title))
            .replace('__CANONICAL__', url)
            .replace('__OG_TITLE__', H.escape(og_title, quote=True))
            .replace('__BACK_LINK__', back_link)
            .replace('__BACK_TEXT__', back_text)
            .replace('__KICKER__', kicker)
            .replace('__H1__', H.escape(h1))
            .replace('__ITEMS__', items))
    return page


def main():
    articles = load_articles()
    by_tag, by_cat, tag_display, cat_display = build_indexes(articles)
    ref_tags, ref_cats = referenced_slugs()

    # Generate every referenced slug; fall back to data-derived slugs so
    # future articles also get pages even before links are regenerated.
    all_tags = sorted(ref_tags | set(by_tag.keys()))
    all_cats = sorted(ref_cats | set(by_cat.keys()))

    print(f'Articles: {len(articles)}')
    print(f'Tag pages: {len(all_tags)} ({len(ref_tags)} referenced)')
    print(f'Category pages: {len(all_cats)} ({len(ref_cats)} referenced)')

    if CHECK_ONLY:
        missing_tags = [s for s in ref_tags if not os.path.exists(os.path.join(BASE_DIR, 'tags', s, 'index.html'))]
        missing_cats = [s for s in ref_cats if not os.path.exists(os.path.join(BASE_DIR, 'categories', s, 'index.html'))]
        print(f'Missing tag pages: {len(missing_tags)}')
        print(f'Missing category pages: {len(missing_cats)}')
        return

    created = 0
    for s in all_tags:
        d = os.path.join(BASE_DIR, 'tags', s)
        os.makedirs(d, exist_ok=True)
        page = build_page('tags', s, tag_display.get(s, s.replace('-', ' ')),
                          by_tag.get(s, []), '/tags/', 'All topics', 'Topic')
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(page)
        created += 1

    for s in all_cats:
        d = os.path.join(BASE_DIR, 'categories', s)
        os.makedirs(d, exist_ok=True)
        page = build_page('categories', s, cat_display.get(s, s.replace('-', ' ')),
                          by_cat.get(s, []), '/categories/', 'All categories', 'Collection')
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(page)
        created += 1

    print(f'Written {created} pages.')


if __name__ == '__main__':
    main()
