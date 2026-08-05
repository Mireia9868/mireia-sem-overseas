#!/usr/bin/env python3
"""
Regenerate homepage, archives, categories, tags pages from article_meta.json
+ update sitemap.xml with new article.
Uses simple string replacement.
"""

import os, json, html
from datetime import datetime
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Load articles ---
with open(os.path.join(BASE_DIR, 'article_meta.json'), 'r') as f:
    ARTICLES = json.load(f)

# Sort by date descending
ARTICLES.sort(key=lambda a: a['date'], reverse=True)

# --- Helper: URL from slug + date ---
def article_url(a):
    d = a['date']
    return f"/{d.replace('-', '/')}/{a['slug']}/"

def article_full_url(a):
    return f"https://mireiasem.com{article_url(a)}"

# --- Helper: escape for HTML ---
def esc(s):
    return html.escape(str(s))

# ============================================================
# 1. HOMEPAGE (index.html)
# ============================================================

def gen_homepage():
    path = os.path.join(BASE_DIR, 'index.html')
    with open(path, 'r') as f:
        content = f.read()

    # Find the article cards section
    # Pattern: after banner section, before pagination
    # We'll replace everything between specific markers

    cards_html = ""
    for a in ARTICLES:
        url = article_url(a)
        cards_html += f"""        <div class="post-card">
          <a href="{url}">
            <div class="post-card-content">
              <h3 class="post-title">{esc(a['title'])}</h3>
              <p class="post-excerpt">{esc(a.get('excerpt', ''))}</p>
              <div class="post-meta">
                <span class="post-date"><i class="iconfont icon-date"></i> {esc(a['date'])}</span>
                <span class="post-category"><i class="iconfont icon-category-fill"></i> {esc(a['category'])}</span>
              </div>
            </div>
          </a>
        </div>
"""

    # Find existing cards block and replace
    # Cards are between: <div class="post-cards"> and the closing </div> before pagination
    import re
    pattern = r'(<div class="post-cards">)(.*?)(</div>\s*\n\s*<div class="pagination)'
    replacement = r'\1\n' + cards_html + r'        \3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(path, 'w') as f:
        f.write(content)
    print(f"Updated: {path}")

# ============================================================
# 2. ARCHIVES PAGE
# ============================================================

def gen_archives():
    path = os.path.join(BASE_DIR, 'archives', 'index.html')
    with open(path, 'r') as f:
        content = f.read()

    # Group by year
    by_year = defaultdict(list)
    for a in ARTICLES:
        year = a['date'][:4]
        by_year[year].append(a)

    archives_html = ""
    for year in sorted(by_year.keys(), reverse=True):
        archives_html += f'        <h2 class="archive-year">{year}</h2>\n'
        archives_html += '        <ul class="archive-list">\n'
        for a in by_year[year]:
            url = article_url(a)
            archives_html += f'          <li><span class="archive-date">{esc(a["date"])}</span> &raquo; <a href="{url}">{esc(a["title"])}</a></li>\n'
        archives_html += '        </ul>\n'

    import re
    pattern = r'(<div class="page-content">)(.*?)(<div class="post-metas|<hr>)'
    replacement = r'\1\n' + archives_html + r'\n      \3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Update total count
    content = re.sub(r'<span class="archive-count">\d+</span>', f'<span class="archive-count">{len(ARTICLES)}</span>', content)

    with open(path, 'w') as f:
        f.write(content)
    print(f"Updated: {path}")

# ============================================================
# 3. CATEGORIES PAGE
# ============================================================

def gen_categories():
    path = os.path.join(BASE_DIR, 'categories', 'index.html')
    with open(path, 'r') as f:
        content = f.read()

    by_category = defaultdict(list)
    for a in ARTICLES:
        cat = a['category']
        by_category[cat].append(a)

    cats_html = ""
    for cat in sorted(by_category.keys()):
        cats_html += f'        <h3 id="{esc(cat).replace(" ", "-")}">{esc(cat)} <span class="category-count">({len(by_category[cat])})</span></h3>\n'
        cats_html += '        <ul>\n'
        for a in by_category[cat]:
            url = article_url(a)
            cats_html += f'          <li><span class="archive-date">{esc(a["date"])}</span> &raquo; <a href="{url}">{esc(a["title"])}</a></li>\n'
        cats_html += '        </ul>\n'

    import re
    pattern = r'(<div class="page-content">)(.*?)(<div class="post-metas|<hr>)'
    replacement = r'\1\n' + cats_html + r'\n      \3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Update total count
    content = re.sub(r'<span class="category-total">\d+</span>', f'<span class="category-total">{len(ARTICLES)}</span>', content)

    with open(path, 'w') as f:
        f.write(content)
    print(f"Updated: {path}")

# ============================================================
# 4. TAGS PAGE  
# ============================================================

def gen_tags():
    path = os.path.join(BASE_DIR, 'tags', 'index.html')
    with open(path, 'r') as f:
        content = f.read()

    by_tag = defaultdict(list)
    for a in ARTICLES:
        for tag in a.get('tags', []):
            by_tag[tag].append(a)

    tags_html = ""
    for tag in sorted(by_tag.keys()):
        tags_html += f'        <h3 id="{esc(tag).replace(" ", "-")}">{esc(tag)} <span class="tag-count">({len(by_tag[tag])})</span></h3>\n'
        tags_html += '        <ul>\n'
        for a in by_tag[tag]:
            url = article_url(a)
            tags_html += f'          <li><span class="archive-date">{esc(a["date"])}</span> &raquo; <a href="{url}">{esc(a["title"])}</a></li>\n'
        tags_html += '        </ul>\n'

    import re
    pattern = r'(<div class="page-content">)(.*?)(<div class="post-metas|<hr>)'
    replacement = r'\1\n' + tags_html + r'\n      \3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Update total count
    content = re.sub(r'<span class="tag-total">\d+</span>', f'<span class="tag-total">{len(by_tag)}</span>', content)

    with open(path, 'w') as f:
        f.write(content)
    print(f"Updated: {path}")

# ============================================================
# 5. SITEMAP
# ============================================================

def gen_sitemap():
    path = os.path.join(BASE_DIR, 'sitemap.xml')
    with open(path, 'r') as f:
        content = f.read()

    # Find the last <url> entry and add new one after it
    import re

    # Build the new URL entry
    a = ARTICLES[0]  # newest article
    new_entry = f"""  <url>
    <loc>{article_full_url(a)}</loc>
    <lastmod>{a['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.80</priority>
  </url>"""

    # Insert after the first <url> block (which is the homepage)
    # Find the pattern: </url>\n  <url>
    first_url_end = content.find('</url>')
    if first_url_end > 0:
        # Find the next <url> after the first one
        next_url_start = content.find('<url>', first_url_end)
        if next_url_start > 0:
            content = content[:next_url_start] + new_entry + '\n  ' + content[next_url_start:]

    with open(path, 'w') as f:
        f.write(content)
    print(f"Updated: {path}")

# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    gen_homepage()
    gen_archives()
    gen_categories()
    gen_tags()
    gen_sitemap()
    print(f"\nDone. Updated listings with {len(ARTICLES)} articles.")
