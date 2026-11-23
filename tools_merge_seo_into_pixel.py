#!/usr/bin/env python3
"""
把上一会话的 SEO 优化合并进像素风版本（幂等，可重复运行）。

只修改 HTML 的 <head> 与合规脚本，不触碰像素风 <body> 视觉层。
刻意跳过两项与像素风冲突的优化：
  - P1-3 首页 site-intro（像素风首页已有 hero）
  - P2-1 alicdn 字体本地化替换（像素风页面已无 alicdn 引用，走 /pixel/fonts.css）

用法：
    python3 tools_merge_seo_into_pixel.py            # 执行合并
    python3 tools_merge_seo_into_pixel.py --check    # 只体检
"""
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHECK_ONLY = '--check' in sys.argv

OG_URL = 'https://mireiasem.com/img/og-cover.png'
OG_TAG = f'<meta property="og:image" content="{OG_URL}">'
TW_TAG = f'<meta name="twitter:image" content="{OG_URL}">'
DIM_TAG = ('<meta property="og:image:width" content="1200">\n'
           '<meta property="og:image:height" content="630">')
CC_CSS = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.css">'
CC_JS = """<script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js" data-cfasync="false"></script>
<script>
window.addEventListener('load', function() {
  window.cookieconsent.initialise({
    palette: {
      popup: { background: '#2f4154' },
      button: { background: '#2563eb', text: '#ffffff' }
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


def iter_html():
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules')]
        for f in files:
            if f.endswith('.html'):
                yield os.path.join(root, f)


def patch(path):
    c = open(path, encoding='utf-8').read()
    orig = c
    rel = os.path.relpath(path, BASE_DIR)
    changes = []

    # P0-2 社交分享图：og/twitter image 统一到 og-cover.png，并补 1200x630
    c2 = re.sub(r'<meta property="og:image" content="[^"]*">', OG_TAG, c)
    c2 = re.sub(r'<meta name="twitter:image" content="[^"]*">', TW_TAG, c2)
    if c2 != c:
        changes.append('OG图替换')
        c = c2
    if OG_TAG in c and 'og:image:width' not in c:
        c = c.replace(OG_TAG, OG_TAG + '\n' + DIM_TAG, 1)
        changes.append('补OG宽高')

    # P0-3 移除废弃广告属性（像素风 body 结构原样保留，只删属性）
    if 'data-ad-layout' in c:
        n = len(re.findall(r'data-ad-layout="[^"]*"\s*', c))
        c = re.sub(r'data-ad-layout="[^"]*"\s*', '', c)
        changes.append(f'移除{n}处data-ad-layout')

    # P0-1 Cookie 合规：补 CSS（head）与 JS+init（body 末尾，不破坏像素风结构）
    if 'cookieconsent.min.css' not in c and '</head>' in c:
        c = c.replace('</head>', f'  {CC_CSS}\n</head>', 1)
        changes.append('补cookie CSS')
    if 'cookieconsent.initialise' not in c and '</body>' in c:
        c = c.replace('</body>', CC_JS + '\n</body>', 1)
        changes.append('补cookie JS')

    # 统一旧版 cookie 文案（兜底）
    c = c.replace(
        "message: 'This website uses cookies to ensure you get the best experience on our website.'",
        "message: 'This website uses cookies for analytics and advertising. See our Privacy Policy for details.'"
    )

    # 内部规划文档：补 noindex（保持其浅色视觉，仅 SEO 配置）
    if rel == 'content-plan-mireiasem.html' and 'noindex' not in c:
        noindex = ('<meta name="googlebot" content="noindex, nofollow">\n'
                   '<meta name="robots" content="noindex, nofollow, noarchive">\n')
        c = c.replace('<head>', '<head>\n' + noindex, 1)
        changes.append('补noindex')

    if changes:
        print(f'  {rel}: {", ".join(changes)}')
        if c != orig and not CHECK_ONLY:
            open(path, 'w', encoding='utf-8').write(c)
    return len(changes)


def main():
    print('=' * 60)
    print('SEO 优化合并到像素风版本' + ('（体检模式）' if CHECK_ONLY else ''))
    print('=' * 60)
    n = 0
    for p in iter_html():
        n += patch(p)
    print('\n' + '=' * 60)
    print(f'{"体检发现" if CHECK_ONLY else "完成"} {n} 项变更')
    print('=' * 60)


if __name__ == '__main__':
    main()
