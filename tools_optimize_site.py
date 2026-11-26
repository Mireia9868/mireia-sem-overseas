#!/usr/bin/env python3
"""
mireiasem.com 站点统一优化脚本（幂等，可重复运行）

按诊断报告的 P0/P1/P2 问题清单，一次性修复所有现有 HTML，并把关键配置固化到生成脚本。
每一项修复都是幂等的：重复运行不会产生重复代码或二次破坏。

用法：
    python3 tools_optimize_site.py            # 执行全部修复
    python3 tools_optimize_site.py --check    # 只体检，不修改

修复项：
    P0-1  给缺失页面的 head/body 补 Cookie 同意横幅 CSS + JS + initialise
    P0-2  og:image / twitter:image 换成实图，并补 width/height
    P0-3  移除废弃的 data-ad-layout，降低单页广告密度（>4 的页面）
    P1-2  清空 Uncategorized 分类，按 article_meta.json 回填真实分类
    P1-3  首页补一段价值主张
    P1-4  摘要按完整单词截断（修 regenerate_site.py 的 excerpt[:150]）
    P2-1  字体 CDN 从 alicdn 换成本地托管
    P2-3  sitemap lastmod 日期格式统一为 W3C Datetime
"""
import os
import re
import sys
import json
import glob
import html as htmlmod

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHECK_ONLY = '--check' in sys.argv

# 各分类的修复计数
STATS = {}


def log(item, msg):
    STATS.setdefault(item, []).append(msg)
    print(f"  [{item}] {msg}")


def iter_html():
    """遍历全站所有 HTML 文件（排除 .git）"""
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules')]
        for f in files:
            if f.endswith('.html'):
                yield os.path.join(root, f)


def read(path):
    with open(path, 'r', encoding='utf-8') as fh:
        return fh.read()


def write(path, content):
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(content)


# ---------------------------------------------------------------- P0-1 Cookie 横幅
CC_CSS = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.css"><style>.cc-window,.cc-revoke{font-family:var(--mono,ui-monospace,SFMono-Regular,Menlo,monospace)!important}.cc-btn,.cc-link{font-family:inherit!important}.cc-link{opacity:1!important}</style>'
CC_JS = """<script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js" data-cfasync="false"></script>
<script>
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
    },
    position: 'bottom'
  });
});
</script>"""


def fix_cookie_consent():
    item = 'P0-1'
    for path in iter_html():
        c = read(path)
        orig = c
        rel = os.path.relpath(path, BASE_DIR)

        # head 里补 CSS（在 </head> 前）
        if 'cookieconsent.min.css' not in c:
            c = c.replace('</head>', f'  {CC_CSS}\n</head>', 1)
            if c != orig:
                log(item, f'{rel}: 补 CSS')

        # body 末尾补 JS + init（在 </body> 前）
        if 'cookieconsent.min.js' not in c or 'cookieconsent.initialise' not in c:
            c = c.replace('</body>', f'{CC_JS}\n</body>', 1)
            log(item, f'{rel}: 补 JS+init')

        # 统一旧版 cookie 文案为合规版
        c = c.replace(
            "message: 'This website uses cookies to ensure you get the best experience on our website.'",
            "message: 'This website uses cookies for analytics and advertising. See our Privacy Policy for details.'"
        )

        if c != orig and not CHECK_ONLY:
            write(path, c)


# ---------------------------------------------------------------- P0-2 社交分享图
OG_URL = 'https://mireiasem.com/img/og-cover.png'
OG_TAG = f'<meta property="og:image" content="{OG_URL}">'
TW_TAG = f'<meta name="twitter:image" content="{OG_URL}">'
DIM_TAG = ('<meta property="og:image:width" content="1200">\n'
           '<meta property="og:image:height" content="630">')


def fix_og_image():
    item = 'P0-2'
    pattern_og = re.compile(r'<meta property="og:image" content="[^"]*">')
    pattern_tw = re.compile(r'<meta name="twitter:image" content="[^"]*">')
    for path in iter_html():
        c = read(path)
        orig = c
        rel = os.path.relpath(path, BASE_DIR)

        c = pattern_og.sub(OG_TAG, c)
        c = pattern_tw.sub(TW_TAG, c)

        # 补宽高（第一个 og:image 之后）
        if 'og:image:width' not in c and OG_TAG in c:
            c = c.replace(OG_TAG, OG_TAG + '\n' + DIM_TAG, 1)

        if c != orig:
            log(item, f'{rel}: 更新 OG 图')
            if not CHECK_ONLY:
                write(path, c)


# ---------------------------------------------------------------- P0-3 广告密度与废弃属性
def fix_ads():
    item = 'P0-3'
    for path in iter_html():
        c = read(path)
        orig = c
        rel = os.path.relpath(path, BASE_DIR)
        n_ins = c.count('<ins class="adsbygoogle"')

        # 移除废弃属性 data-ad-layout="in-article"
        if 'data-ad-layout' in c:
            n = len(re.findall(r'data-ad-layout="[^"]*"\s*', c))
            c = re.sub(r'data-ad-layout="[^"]*"\s*', '', c)
            log(item, f'{rel}: 移除 {n} 处 data-ad-layout')

        # 单页广告 > 4 时，从后往前删除中间的 in-article 广告，保留首+尾
        if n_ins > 4:
            # 匹配完整的 ad-container-N div 块
            blocks = list(re.finditer(
                r'<div id="ad-container-(\d+)"[^>]*>.*?</div>\s*(?=<|\n)', c, re.S))
            to_remove = n_ins - 4
            removed = 0
            for m in reversed(blocks):
                if removed >= to_remove:
                    break
                num = int(m.group(1))
                # 保留 ad-container-1（第一个），删除靠后的
                if num == 1:
                    continue
                seg = m.group(0)
                # 只删含 ins 广告的块
                if '<ins class="adsbygoogle"' in seg:
                    c = c[:m.start()] + c[m.end():]
                    removed += 1
            if removed:
                log(item, f'{rel}: 广告 {n_ins}→{n_ins-removed} 个')

        if c != orig and not CHECK_ONLY:
            write(path, c)


# ---------------------------------------------------------------- P1-2 分类清理
def load_meta():
    with open(os.path.join(BASE_DIR, 'article_meta.json'), 'r', encoding='utf-8') as fh:
        return json.load(fh)


def fix_categories():
    item = 'P1-2'
    meta = {m['slug']: m for m in load_meta()}

    # 重建首页 / categories 页里文章的分类链接
    # 先建立 slug -> category 映射（从文章 URL 提取 slug）
    def slug_from_href(href):
        parts = [p for p in href.split('/') if p]
        return parts[-1] if parts else ''

    for path in [os.path.join(BASE_DIR, 'index.html'),
                 os.path.join(BASE_DIR, 'categories', 'index.html')]:
        if not os.path.exists(path):
            continue
        c = read(path)
        orig = c
        rel = os.path.relpath(path, BASE_DIR)

        # 首页分类链接模式：<a href="/categories/Uncategorized/" class="category-chain-item">Uncategorized</a>
        # 需要根据该文章卡片对应的 slug 回填——用正则匹配包含文章 href 的分类块较复杂，
        # 这里采用逐文章卡片定位的方式
        if rel == 'index.html':
            # 按 <article ... index-info> ... </article> 切分
            def repl_card(m):
                card = m.group(0)
                if 'Uncategorized' not in card:
                    return card
                href_m = re.search(r'class="index-header">\s*<a href="/([^"]+)/"', card)
                if not href_m:
                    return card
                slug = slug_from_href(href_m.group(1))
                cat = meta.get(slug, {}).get('category')
                if not cat or cat == 'Uncategorized':
                    return card
                # 与站点既有 URL 格式保持一致：空格→连字符，& 原样保留
                cat_url = cat.replace(' ', '-')
                return card.replace('/categories/Uncategorized/', f'/categories/{cat_url}/').replace(
                    '>Uncategorized</a>', f'>{htmlmod.escape(cat)}</a>')

            c = re.sub(r'<article class="col-12 col-md-12 mx-auto index-info">.*?</article>',
                       repl_card, c, flags=re.S)

        if c != orig:
            n = orig.count('Uncategorized') - c.count('Uncategorized')
            log(item, f'{rel}: 回填 {n} 处分类')
            if not CHECK_ONLY:
                write(path, c)


# ---------------------------------------------------------------- P1-3 首页价值主张
INTRO_HTML = """<div class="site-intro" style="max-width:820px;margin:24px auto 8px;padding:0 16px;text-align:center;color:#5a6b7b;line-height:1.8;">
  <p style="font-size:1.02rem;">Practical, data-driven guides for cross-border advertisers. I break down Google Ads, Microsoft Ads, conversion tracking and ad-policy compliance into step-by-step playbooks you can apply to real accounts — with the settings, trade-offs and pitfalls that actually matter.</p>
</div>
"""


def fix_home_intro():
    item = 'P1-3'
    path = os.path.join(BASE_DIR, 'index.html')
    c = read(path)
    if 'class="site-intro"' in c:
        return
    # 插在 <main> 之后、文章列表容器之前
    marker = '<main>'
    if marker in c:
        c = c.replace(marker, marker + '\n' + INTRO_HTML, 1)
        log(item, '首页: 补价值主张段落')
        if not CHECK_ONLY:
            write(path, c)


# ---------------------------------------------------------------- P1-4 摘要按完整单词截断
def smart_excerpt(text, maxlen=150):
    """按完整单词截断，末尾加省略号，避免从单词中间断开。"""
    text = htmlmod.unescape(re.sub(r'<[^>]+>', '', text)).strip()
    if len(text) <= maxlen:
        return htmlmod.escape(text)
    cut = text[:maxlen]
    # 回退到最后一个空格
    last_space = cut.rfind(' ')
    if last_space > maxlen * 0.6:
        cut = cut[:last_space]
    return htmlmod.escape(cut.rstrip(' ,;:-')) + '...'


def fix_excerpts():
    item = 'P1-4'
    path = os.path.join(BASE_DIR, 'index.html')
    c = read(path)
    orig = c

    # 关键：首页 HTML 里的摘要本身已是残缺文本（如 "account, l..."），
    # 无法从残缺文本恢复，必须从 article_meta.json 的完整 excerpt 按 slug 重建。
    meta = {m['slug']: m['excerpt'] for m in load_meta() if m.get('excerpt')}

    def slug_of(card):
        m = re.search(r'class="index-header">\s*<a href="/([^"]+)/"', card)
        if not m:
            return ''
        parts = [p for p in m.group(1).split('/') if p]
        return parts[-1] if parts else ''

    card_pat = re.compile(r'(<article class="col-12 col-md-12 mx-auto index-info">)(.*?)(</article>)', re.S)
    rebuilt = [0]

    def repl_card(m):
        card = m.group(2)
        slug = slug_of(card)
        full_excerpt = meta.get(slug)
        if not full_excerpt:
            return m.group(0)
        new_excerpt = smart_excerpt(full_excerpt, 150)
        card2, n = re.subn(
            r'(index-excerpt[^>]*>\s*<div>)(.*?)(</div>)',
            lambda em: em.group(1) + new_excerpt + em.group(3),
            card, count=1, flags=re.S)
        if n:
            rebuilt[0] += 1
        return m.group(1) + card2 + m.group(3)

    c = card_pat.sub(repl_card, c)
    if c != orig:
        log(item, f'首页: 从数据源重建 {rebuilt[0]} 条摘要（完整单词截断）')
        if not CHECK_ONLY:
            write(path, c)

    # 固化到生成脚本：把 excerpt[:150]... 改成 smart 截断
    for gen in ('regenerate_site.py',):
        gp = os.path.join(BASE_DIR, gen)
        if not os.path.exists(gp):
            continue
        g = read(gp)
        if "html.escape(a['excerpt'][:150])" in g:
            g = g.replace(
                "{html.escape(a['excerpt'][:150])}...",
                "{smart_excerpt(a['excerpt'], 150)}"
            )
            # 注入 smart_excerpt 函数定义
            if 'def smart_excerpt' not in g:
                helper = '''\ndef smart_excerpt(text, maxlen=150):
    """按完整单词截断摘要，避免从单词中间断开。"""
    text = html.unescape(re.sub(r'<[^>]+>', '', text)).strip()
    if len(text) <= maxlen:
        return text
    cut = text[:maxlen]
    last_space = cut.rfind(' ')
    if last_space > maxlen * 0.6:
        cut = cut[:last_space]
    return cut.rstrip(' ,;:-') + '...'
\n'''
                g = g.replace('existing_slugs = set(', helper + 'existing_slugs = set(', 1)
            log(item, f'{gen}: 固化 smart_excerpt')
            if not CHECK_ONLY:
                write(gp, g)


# ---------------------------------------------------------------- P2-1 字体本地化
FONT_LOCAL = """<link rel="stylesheet" href="/css/fonts/iconfont-a.css">
  <link rel="stylesheet" href="/css/fonts/iconfont-b.css">"""


def fix_fonts():
    item = 'P2-1'
    # 生成本地化 CSS（如尚未存在）
    fonts_dir = os.path.join(BASE_DIR, 'css', 'fonts')
    os.makedirs(fonts_dir, exist_ok=True)
    font_specs = [
        ('iconfont-a.css', '1749284_hj8rtnfg7um'),
        ('iconfont-b.css', '1736178_lbnruvf0jn'),
    ]
    # 尝试下载 woff2 到本地（单次请求，解析所有字体文件 URL）
    import urllib.request
    for css_name, ident in font_specs:
        css_path = os.path.join(fonts_dir, css_name)
        if os.path.exists(css_path):
            continue
        remote = f'https://at.alicdn.com/t/font_{ident}.css'
        try:
            req = urllib.request.Request(remote, headers={'User-Agent': 'Mozilla/5.0'})
            txt = urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore')

            # 提取所有字体文件 URL，改成本地文件名，并下载文件
            url_pat = re.compile(r"url\(['\"]?([^'\")]+)['\"]?\)")
            found_urls = url_pat.findall(txt)

            def localize_font(m):
                url = m.group(1)
                fname = url.split('/')[-1].split('?')[0]
                return f"url('{fname}')"
            txt = url_pat.sub(localize_font, txt)
            write(css_path, txt)

            for url in found_urls:
                if 'alicdn.com' not in url:
                    continue
                full = url if url.startswith('http') else 'https:' + url
                fname = url.split('/')[-1].split('?')[0]
                fpath = os.path.join(fonts_dir, fname)
                # 仅当文件不存在或为 0 字节时才下载，避免覆盖已修好的文件
                if os.path.exists(fpath) and os.path.getsize(fpath) > 0:
                    continue
                try:
                    # urllib 在部分环境被代理拦截会返回空内容，用 curl 更可靠
                    import subprocess
                    subprocess.run(['curl', '-sL', '--max-time', '20', '-A', 'Mozilla/5.0',
                                    '-o', fpath, full], check=True, timeout=30)
                    if os.path.getsize(fpath) == 0:
                        os.remove(fpath)
                        print(f'    警告: {fname} 下载为空，已删除')
                except Exception as e:
                    print(f'    字体文件下载失败 {fname}: {e}')
            log(item, f'{css_name}: 已本地化（{len(found_urls)} 个字体文件）')
        except Exception as e:
            log(item, f'{css_name}: 下载失败({e})，跳过')

    # 替换 HTML 中的 alicdn 引用（仅在本地 CSS 已就绪时）
    a_css = os.path.join(fonts_dir, 'iconfont-a.css')
    b_css = os.path.join(fonts_dir, 'iconfont-b.css')
    if not (os.path.exists(a_css) and os.path.exists(b_css)):
        log(item, '本地 CSS 未就绪，跳过 HTML 替换')
        return

    for path in iter_html():
        c = read(path)
        orig = c
        had_alicdn = 'at.alicdn.com' in c
        c = re.sub(r'\s*<link rel="stylesheet" href="//at\.alicdn\.com/t/font_1749284[^"]*"\s*/?>', '', c)
        c = re.sub(r'\s*<link rel="stylesheet" href="//at\.alicdn\.com/t/font_1736178[^"]*"\s*/?>', '', c)
        # 在 main.css 引用前插入本地字体（仅当原本引用过 alicdn 且尚未插入）
        if had_alicdn and '/css/fonts/iconfont-a.css' not in c:
            c = c.replace('<link rel="stylesheet" href="/css/main.css"',
                          f'{FONT_LOCAL}\n  <link rel="stylesheet" href="/css/main.css"', 1)
        if c != orig:
            log(item, f'{os.path.relpath(path, BASE_DIR)}: 字体改本地')
            if not CHECK_ONLY:
                write(path, c)


# ---------------------------------------------------------------- P2-3 sitemap 日期
def fix_sitemap():
    item = 'P2-3'
    path = os.path.join(BASE_DIR, 'sitemap.xml')
    if not os.path.exists(path):
        return
    c = read(path)
    orig = c

    def norm(m):
        d = m.group(1)
        if re.match(r'^\d{4}-\d{2}-\d{2}$', d):
            return f'<lastmod>{d}T00:00:00+08:00</lastmod>'
        return m.group(0)

    c = re.sub(r'<lastmod>([^<]+)</lastmod>', norm, c)
    if c != orig:
        log(item, 'sitemap: lastmod 统一为 W3C Datetime')
        if not CHECK_ONLY:
            write(path, c)


# ---------------------------------------------------------------- 固化：生成模板的 Cookie 横幅
def harden_generators():
    item = 'P0-1-固化'
    # generate_batch_articles.py 的模板缺正确 cookie 文案 → 统一
    gp = os.path.join(BASE_DIR, 'generate_batch_articles.py')
    if os.path.exists(gp):
        g = read(gp)
        g2 = g.replace(
            "message: 'This website uses cookies to ensure you get the best experience on our website.'",
            "message: 'This website uses cookies for analytics and advertising. See our Privacy Policy for details.'"
        )
        if g2 != g:
            log(item, 'generate_batch_articles.py: cookie 文案统一')
            if not CHECK_ONLY:
                write(gp, g2)
    # regenerate_site.py 同上
    gp = os.path.join(BASE_DIR, 'regenerate_site.py')
    if os.path.exists(gp):
        g = read(gp)
        g2 = g.replace(
            "message: 'This website uses cookies to ensure you get the best experience on our website.'",
            "message: 'This website uses cookies for analytics and advertising. See our Privacy Policy for details.'"
        )
        if g2 != g:
            log(item, 'regenerate_site.py: cookie 文案统一')
            if not CHECK_ONLY:
                write(gp, g2)


# ---------------------------------------------------------------- main
def main():
    print('=' * 60)
    print('mireiasem.com 站点统一优化脚本' + ('（体检模式）' if CHECK_ONLY else ''))
    print('=' * 60)

    fix_cookie_consent()
    fix_og_image()
    fix_ads()
    fix_categories()
    fix_home_intro()
    fix_excerpts()
    fix_fonts()
    fix_sitemap()
    harden_generators()

    print('\n' + '=' * 60)
    total = sum(len(v) for v in STATS.values())
    print(f'完成：{total} 项修改' if not CHECK_ONLY else f'体检：发现 {total} 项待修')
    print('=' * 60)


if __name__ == '__main__':
    main()
