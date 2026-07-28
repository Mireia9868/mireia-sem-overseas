#!/usr/bin/env python3
"""
Regenerate homepage, archives, categories, tags pages with all 53 articles.
Remove Hexo footer from all HTML files.
Rewrite About page.
Uses string replacement (not .format) to avoid brace conflicts.
"""

import os, re, glob, html, shutil
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- 1. Gather all article metadata ---

import sys
sys.path.insert(0, BASE_DIR)
from articles_data_batch1 import ARTICLES_BATCH1
from articles_data_batch2 import ARTICLES_BATCH2

ALL_ARTICLES = []

for a in ARTICLES_BATCH1 + ARTICLES_BATCH2:
    ALL_ARTICLES.append({
        'slug': a['slug'],
        'date': a['date'],
        'title': a['title'],
        'category': a.get('category', 'Uncategorized'),
        'subcategory': a.get('subcategory', ''),
        'tags': a.get('tags', []),
        'excerpt': a.get('excerpt', ''),
        'url': f"/{a['date'].replace('-', '/')}/{a['slug']}/"
    })

existing_slugs = set(a['slug'] for a in ALL_ARTICLES)

for html_file in sorted(glob.glob(os.path.join(BASE_DIR, '2024/**/index.html'), recursive=True)):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'/(\d{4})/(\d{2})/(\d{2})/([^/]+)/index.html', html_file)
    if not m:
        continue
    year, month, day, slug = m.groups()
    date = f'{year}-{month}-{day}'
    if slug in existing_slugs:
        continue
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else slug
    cat_match = re.search(r'class="category-chain-item">([^<]+)</a>', content)
    category = cat_match.group(1) if cat_match else 'Uncategorized'
    tags = list(set(re.findall(r'/tags/([^/]+)/"', content)))
    desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
    excerpt = desc_match.group(1) if desc_match else ''
    ALL_ARTICLES.append({
        'slug': slug, 'date': date, 'title': title,
        'category': category, 'subcategory': '', 'tags': tags,
        'excerpt': excerpt, 'url': f"/{date.replace('-', '/')}/{slug}/"
    })

ALL_ARTICLES.sort(key=lambda x: x['date'], reverse=True)
print(f"Total articles: {len(ALL_ARTICLES)}")

# --- 2. Common HTML blocks ---

HEAD = """<!DOCTYPE html>
<html lang="en" data-default-color-scheme=auto>

<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="GIdO_iD4VCjnetTm8q99G5TLiGSH9HdRoItNgPjZmP8" />
  <link rel="apple-touch-icon" sizes="76x76" href="/img/Mireia%20Sem_transparent.png">
  <link rel="icon" href="/img/Mireia%20Sem_transparent.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="theme-color" content="#2f4154">
  <meta name="author" content="Mireia">
  <meta name="keywords" content="SEM, Google Ads, Bing Ads, Facebook Ads, cross-border e-commerce, conversion tracking, digital advertising">
  <meta name="description" content="__DESC__">
  <meta property="og:type" content="website">
  <meta property="og:title" content="__OG_TITLE__">
  <meta property="og:site_name" content="Mireia SEM Blog">
  <meta property="og:locale" content="en_US">
  <meta property="article:author" content="Mireia">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="referrer" content="no-referrer-when-downgrade">
  <title>__TITLE__</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" />
  <link rel="stylesheet" href="//at.alicdn.com/t/font_1749284_hj8rtnfg7um.css">
  <link rel="stylesheet" href="//at.alicdn.com/t/font_1736178_lbnruvf0jn.css">
  <link rel="stylesheet" href="/css/main.css" />
  <link id="highlight-css" rel="stylesheet" href="/css/highlight.css" />
  <link id="highlight-css-dark" rel="stylesheet" href="/css/highlight-dark.css" />
  <script id="fluid-configs">
    var Fluid = window.Fluid || {};
    Fluid.ctx = Object.assign({}, Fluid.ctx)
    var CONFIG = {"hostname":"mireiasem.com","root":"/","version":"1.9.3","typing":{"enable":true,"typeSpeed":70,"cursorChar":"_","loop":false,"scope":[]},"anchorjs":{"enable":true,"element":"h1,h2,h3,h4,h5,h6","placement":"left","visible":"hover","icon":""},"progressbar":{"enable":true,"height_px":3,"color":"#29d","options":{"showSpinner":false,"trickleSpeed":100}},"code_language":{"enable":true,"default":"TEXT"},"copy_btn":true,"image_caption":{"enable":true},"image_zoom":{"enable":true,"img_url_replace":["",""]},"toc":{"enable":true,"placement":"right","headingSelector":"h1,h2,h3,h4,h5,h6","collapseDepth":0},"lazyload":{"enable":true,"loading_img":"/img/loading.gif","onlypost":false,"offset_factor":2},"web_analytics":{"enable":false,"follow_dnt":true,"baidu":null,"google":null,"gtag":null,"tencent":{"sid":null,"cid":null},"woyaola":null,"cnzz":null,"leancloud":{"app_id":null,"app_key":null,"server_url":null,"path":"window.location.pathname","ignore_local":false}},"search_path":"/local-search.xml"};
    if (CONFIG.web_analytics.follow_dnt) {
      var dntVal = navigator.doNotTrack || window.doNotTrack || navigator.msDoNotTrack;
      Fluid.ctx.dnt = dntVal && (dntVal.startsWith('1') || dntVal.startsWith('yes') || dntVal.startsWith('on'));
    }
  </script>
  <script src="/js/utils.js"></script>
  <script src="/js/color-schema.js"></script>
<meta name="google-adsense-account" content="ca-pub-2269516311541291">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2269516311541291"
     crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.css">
</head>"""

def make_nav(home_link=""):
    return f"""<div class="header-inner" style="height: __HEIGHT__;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="{home_link}">
      <strong>Mireia Sem Blog</strong>
    </a>
    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item">
              <a class="nav-link" href="{home_link}">
                <i class="iconfont icon-home-fill"></i>
                Home
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/archives/">
                <i class="iconfont icon-archive-fill"></i>
                Archives
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/categories/">
                <i class="iconfont icon-category-fill"></i>
                Categories
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/tags/">
                <i class="iconfont icon-tags-fill"></i>
                Tags
              </a>
            </li>
          <li class="nav-item"><a class="nav-link" href="/privacy-policy/"><i class="iconfont icon-user-fill"></i> Privacy</a></li>
          <li class="nav-item"><a class="nav-link" href="/contact/"><i class="iconfont icon-user-fill"></i> Contact</a></li>
          <li class="nav-item" id="search-btn">
            <a class="nav-link" target="_self" href="javascript:;" data-toggle="modal" data-target="#modalSearch" aria-label="Search">
              &nbsp;<i class="iconfont icon-search"></i>&nbsp;
            </a>
          </li>
          <li class="nav-item" id="color-toggle-btn">
            <a class="nav-link" target="_self" href="javascript:;" aria-label="Color Toggle">&nbsp;<i
                class="iconfont icon-dark" id="color-toggle-icon"></i>&nbsp;</a>
          </li>
      </ul>
    </div>
  </div>
</nav>"""

BANNER = """
<div id="banner" class="banner" parallax=true
     style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2">
            <span id="subtitle" data-typed-text="__BANNER_TEXT__"></span>
        </div>
      </div>
__SCROLL_DOWN__
    </div>
  </div>
</div>

</div>"""

FOOTER = """  <footer>
    <div class="footer-inner">
    <div class="footer-content">
       <span>Mireia SEM Blog</span>
    </div>
    <div class="footer-links" style="margin-top: 8px; font-size: 14px;">
      <a href="/privacy-policy/">Privacy Policy</a> &middot;
      <a href="/contact/">Contact</a> &middot;
      <a href="/sitemap.xml">Sitemap</a>
    </div>
    <div class="statistics">
      <span id="busuanzi_container_site_pv" style="display: none">
        Views:
        <span id="busuanzi_value_site_pv"></span>
      </span>
      <span id="busuanzi_container_site_uv" style="display: none">
        Visitors:
        <span id="busuanzi_value_site_uv"></span>
      </span>
    </div>
    </div>
  </footer>"""

SCRIPTS = """  <!-- Scripts -->
  <script src="https://cdn.jsdelivr.net/npm/nprogress@0.2.0/nprogress.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/nprogress@0.2.0/nprogress.min.css" />
  <script>
    NProgress.configure({"showSpinner":false,"trickleSpeed":100})
    NProgress.start()
    window.addEventListener('load', function() {
      NProgress.done();
    })
  </script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.min.js"></script>
<script src="/js/events.js"></script>
<script src="/js/plugins.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12/lib/typed.min.js"></script>
  <script>
    (function (window, document) {
      var typing = Fluid.plugins.typing;
      var subtitle = document.getElementById('subtitle');
      if (!subtitle || !typing) {
        return;
      }
      var text = subtitle.getAttribute('data-typed-text');
        typing(text);
    })(window, document);
  </script>
    <script src="/js/img-lazyload.js"></script>
  <script src="/js/local-search.js"></script>
  <script defer src="https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<!-- the boot of the theme, keep it at the bottom -->
<script src="/js/boot.js"></script>
  <noscript>
    <div class="noscript-warning">Blog works best with JavaScript enabled</div>
  </noscript>
<script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js" data-cfasync="false"></script>
<script>
window.addEventListener('load', function() {
  window.cookieconsent.initialise({
    palette: {
      popup: { background: '#2f4154' },
      button: { background: '#2563eb', text: '#ffffff' }
    },
    content: {
      message: 'This website uses cookies to ensure you get the best experience on our website.',
      dismiss: 'Got it!',
      link: 'Learn more',
      href: '/privacy-policy/'
    },
    position: 'bottom'
  });
});
</script>
</body>
</html>"""

SEARCH_MODAL = """            <a id="scroll-top-button" aria-label="TOP" href="#" role="button">
        <i class="iconfont icon-arrowup" aria-hidden="true"></i>
      </a>
            <div class="modal fade" id="modalSearch" tabindex="-1" role="dialog" aria-labelledby="ModalLabel"
     aria-hidden="true">
  <div class="modal-dialog modal-dialog-scrollable modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header text-center">
        <h4 class="modal-title w-100 font-weight-bold">Search</h4>
        <button type="button" id="local-search-close" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body mx-3">
        <div class="md-form mb-5">
          <input type="text" id="local-search-input" class="form-control validate">
          <label data-error="x" data-success="v" for="local-search-input">Keyword</label>
        </div>
        <div class="list-group" id="local-search-result"></div>
      </div>
    </div>
  </div>
</div>"""

def build_page(desc, og_title, title, height, home_link, banner_text, scroll_down, body_content):
    """Build a complete HTML page using string replacement."""
    page = HEAD.replace('__DESC__', desc).replace('__OG_TITLE__', og_title).replace('__TITLE__', title)
    page += '\n\n<body>\n\n  <header>\n\n'
    nav = make_nav(home_link).replace('__HEIGHT__', height)
    page += nav + '\n'
    sd = f'        <div class="scroll-down-bar">\n          <i class="iconfont icon-arrowdown"></i>\n        </div>' if scroll_down else ''
    banner = BANNER.replace('__BANNER_TEXT__', banner_text).replace('__SCROLL_DOWN__', sd)
    page += banner
    page += '  </header>\n  <main>\n'
    page += body_content
    page += '\n'
    page += SEARCH_MODAL + '\n'
    page += '  </main>\n\n'
    page += FOOTER + '\n'
    page += SCRIPTS + '\n'
    return page

# --- 3. Generate Homepage ---

def generate_homepage():
    cards = []
    for a in ALL_ARTICLES:
        cat_slug = a['category'].replace(' ', '-')
        tag_parts = ' '.join(f'<a href="/tags/{t.replace(" ", "-").replace("&", "&")}/">#{html.escape(t)}</a>' for t in a['tags'])
        card = f"""  <div class="row mx-auto index-card">
    <article class="col-12 col-md-12 mx-auto index-info">
      <h1 class="index-header">
        <a href="{a['url']}" target="_self">
          {html.escape(a['title'])}
        </a>
      </h1>
      <a class="index-excerpt index-excerpt__noimg" href="{a['url']}" target="_self">
        <div>
          {html.escape(a['excerpt'][:150])}...
        </div>
      </a>
      <div class="index-btm post-metas">
          <div class="post-meta mr-3">
            <i class="iconfont icon-date"></i>
            <time datetime="{a['date']}" pubdate>
              {a['date']}
            </time>
          </div>
          <div class="post-meta mr-3 d-flex align-items-center">
            <i class="iconfont icon-category"></i>
<span class="category-chains">
      <span class="category-chain">
        <a href="/categories/{cat_slug}/" class="category-chain-item">{html.escape(a['category'])}</a>
      </span>
</span>
          </div>
          <div class="post-meta">
            <i class="iconfont icon-tags"></i>
              {tag_parts}
          </div>
      </div>
    </article>
  </div>"""
        cards.append(card)
    
    body = f"""      <div class="container nopadding-x-md">
        <div id="board"
          style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">

{chr(10).join(cards)}

              </div>
            </div>
          </div>
        </div>
      </div>"""
    
    page = build_page(
        desc="Professional insights on Google Ads, Bing Ads, Facebook Ads, conversion tracking, and cross-border e-commerce marketing.",
        og_title="Mireia SEM Blog",
        title="Mireia SEM Blog",
        height="100vh",
        home_link="",
        banner_text="Data-driven insights for cross-border digital advertising.",
        scroll_down=True,
        body_content=body
    )
    
    with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"  Homepage: {len(ALL_ARTICLES)} articles")

# --- 4. Generate Archives ---

def generate_archives():
    by_year = defaultdict(list)
    for a in ALL_ARTICLES:
        by_year[a['date'][:4]].append(a)
    
    parts = []
    for year in sorted(by_year.keys(), reverse=True):
        articles = sorted(by_year[year], key=lambda x: x['date'], reverse=True)
        items = [f'<li class="archive-item"><span class="archive-date">{a["date"]}</span><a href="{a["url"]}">{html.escape(a["title"])}</a></li>' for a in articles]
        parts.append(f'<div class="archive-timeline">\n<h2 class="archive-year">{year}</h2>\n<ul class="archive-list">\n{chr(10).join(items)}\n</ul>\n</div>')
    
    body = f"""      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
                <div class="markdown-body">

{chr(10).join(parts)}

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>"""
    
    page = build_page(
        desc="All articles organized by date.",
        og_title="Archives - Mireia SEM Blog",
        title="Archives - Mireia SEM Blog",
        height="60vh",
        home_link="../",
        banner_text="Archives",
        scroll_down=False,
        body_content=body
    )
    
    with open(os.path.join(BASE_DIR, 'archives/index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"  Archives: {len(ALL_ARTICLES)} articles in {len(by_year)} years")

# --- 5. Generate Categories ---

def generate_categories():
    by_cat = defaultdict(list)
    for a in ALL_ARTICLES:
        by_cat[a['category']].append(a)
    
    cat_descs = {
        'Ad Channels': 'Google Ads, Bing Ads, Facebook Ads campaign setup and optimization',
        'Conversion Tracking': 'Pixel deployment, UET tags, offline conversion upload, code integration',
        'Channel Policies': 'Platform policy updates, ad disapproval solutions, compliance',
        'Tools & Tips': 'Advertising tools, account optimization, workflow efficiency',
        'Industry Insights': 'Market analysis, industry trends, data-driven insights',
        'Data & Analytics': 'Web analytics, data tools, measurement strategies',
    }
    
    parts = []
    for cat in sorted(by_cat.keys()):
        articles = by_cat[cat]
        cat_slug = cat.replace(' ', '-')
        desc = cat_descs.get(cat, f'{len(articles)} articles')
        parts.append(f'<div class="category-item"><h3><a href="/categories/{cat_slug}/">{html.escape(cat)}</a> <span class="category-count">({len(articles)})</span></h3><p>{html.escape(desc)}</p></div>')
    
    body = f"""      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
                <div class="markdown-body">
<div class="category-list">
{chr(10).join(parts)}
</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>"""
    
    page = build_page(
        desc="Browse articles by category.",
        og_title="Categories - Mireia SEM Blog",
        title="Categories - Mireia SEM Blog",
        height="60vh",
        home_link="../",
        banner_text="Categories",
        scroll_down=False,
        body_content=body
    )
    
    with open(os.path.join(BASE_DIR, 'categories/index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"  Categories: {len(by_cat)} categories")

# --- 6. Generate Tags ---

def generate_tags():
    by_tag = defaultdict(int)
    for a in ALL_ARTICLES:
        for tag in a['tags']:
            by_tag[tag] += 1
    
    max_count = max(by_tag.values()) if by_tag else 1
    parts = []
    for tag in sorted(by_tag.keys()):
        count = by_tag[tag]
        tag_slug = tag.replace(' ', '-')
        font_size = 14 + int((count / max_count) * 15)
        parts.append(f'<a href="/tags/{tag_slug}/" class="tag-item" style="font-size: {font_size}px;">#{html.escape(tag)} <span class="tag-count">({count})</span></a>')
    
    body = f"""      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
                <div class="markdown-body">
<div class="tag-cloud">
{chr(10).join(parts)}
</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>"""
    
    page = build_page(
        desc="Browse articles by tag.",
        og_title="Tags - Mireia SEM Blog",
        title="Tags - Mireia SEM Blog",
        height="60vh",
        home_link="../",
        banner_text="Tags",
        scroll_down=False,
        body_content=body
    )
    
    with open(os.path.join(BASE_DIR, 'tags/index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"  Tags: {len(by_tag)} tags")

# --- 7. Generate About page ---

def generate_about():
    content = """<div class="markdown-body">
<h2 id="about-this-blog">About This Blog</h2>
<p><strong>Mireia SEM</strong> is a professional digital advertising resource focused on practical, hands-on guides for cross-border e-commerce marketing. We cover the platforms and tools that matter most to performance marketers:</p>
<ul>
<li><strong>Google Ads:</strong> Search, Display, Shopping, App Campaigns (UAC), Performance Max, automated bidding</li>
<li><strong>Microsoft Advertising (Bing Ads):</strong> Search, Shopping, audience targeting, UET tag deployment</li>
<li><strong>Facebook / Meta Ads:</strong> Conversion campaigns, dynamic product ads, pixel integration</li>
<li><strong>Conversion Tracking:</strong> Pixel deployment, UET tags, offline conversion upload, GA4, Consent Mode v2</li>
<li><strong>E-commerce Integration:</strong> Shopify, WooCommerce, Shopline, custom platform tracking setups</li>
</ul>

<h2 id="what-youll-find-here">What You'll Find Here</h2>
<p>Every article on this site is based on real campaign experience and testing, not theoretical fluff. We document:</p>
<ul>
<li>Step-by-step setup guides for ad accounts, conversion tracking, and platform integrations</li>
<li>Policy updates and compliance solutions (Google Ads disapprovals, Bing Ads policies, etc.)</li>
<li>Bidding strategies, optimization techniques, and performance benchmarking</li>
<li>API integrations for automation and bulk management</li>
<li>Platform updates and new feature walkthroughs</li>
</ul>

<h2 id="our-approach">Our Approach</h2>
<p>We believe in <strong>data-driven marketing</strong>. Every recommendation comes from testing on live campaigns with real budgets. Whether it's a bidding strategy, a tracking setup, or a policy workaround, if we haven't seen it work, we won't write about it.</p>

<h2 id="stay-connected">Stay Connected</h2>
<p>Have a question, spotted an error, or want to discuss a specific topic? We'd love to hear from you:</p>
<ul>
<li><strong>Contact:</strong> <a href="/contact/">Reach out via our contact page</a></li>
<li><strong>Sitemap:</strong> <a href="/sitemap.xml">View all articles</a></li>
<li><strong>Search:</strong> Use the search bar above to find specific topics</li>
</ul>

<p>Whether you're a fellow advertiser, a brand looking for marketing insights, or just someone interested in SEM, welcome. Let's grow together in the world of cross-border digital advertising.</p>
</div>"""
    
    body = f"""      <div class="container nopadding-x-md">
        <div id="board"
          style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">

{content}

              </div>
            </div>
          </div>
        </div>
      </div>"""
    
    page = build_page(
        desc="About Mireia SEM - Professional digital advertising insights and guides.",
        og_title="About - Mireia SEM Blog",
        title="About - Mireia SEM Blog",
        height="60vh",
        home_link="../",
        banner_text="About",
        scroll_down=False,
        body_content=body
    )
    
    # Add markdown CSS
    page = page.replace(
        '</head>',
        '  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown.min.css" />\n  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/hint.css@2.7.0/hint.min.css" />\n  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css" />\n</head>'
    )
    
    with open(os.path.join(BASE_DIR, 'about/index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print("  About: rewritten (professional, no personal info)")

# --- 8. Remove Hexo footer + About nav from ALL HTML files ---

def remove_hexo_footer_all():
    old_footer = '<a href="https://hexo.io" target="_blank" rel="nofollow noopener"><span>Hexo</span></a> <i class="iconfont icon-love"></i> <a href="https://github.com/fluid-dev/hexo-theme-fluid" target="_blank" rel="nofollow noopener"><span>Fluid</span></a>'
    new_footer = '<span>Mireia SEM Blog</span>'
    
    about_nav1 = '<li class="nav-item">\n              <a class="nav-link" href="/about/">\n                <i class="iconfont icon-user-fill"></i>\n                About\n              </a>\n            </li>'
    about_nav2 = '<li class="nav-item"><a class="nav-link" href="/about/"><i class="iconfont icon-user-fill"></i> About</a></li>'
    
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', 'css', 'js', 'img')]
        for fname in files:
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            original = content
            if old_footer in content:
                content = content.replace(old_footer, new_footer)
            if about_nav1 in content:
                content = content.replace(about_nav1, '')
            if about_nav2 in content:
                content = content.replace(about_nav2, '')
            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
    
    print(f"  Footer/Nav: updated {count} files")

# --- 9. Main ---

print("Generating listing pages...")
generate_homepage()
generate_archives()
generate_categories()
generate_tags()
generate_about()

print("\nRemoving Hexo footer + About nav from all pages...")
remove_hexo_footer_all()

print("\nDone!")
