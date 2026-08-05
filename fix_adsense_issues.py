#!/usr/bin/env python3
"""
Batch update all HTML files in mireiasem.com:
1. Update footer links to add About and Terms
2. Update cookie consent message to mention advertising cookies
3. Update sitemap.xml to include /terms/
"""
import os
import re

BASE_DIR = "/Users/mireia/mireia-sem-overseas"

# Old footer links pattern (matches both compact and whitespace-heavy variants)
OLD_FOOTER = re.compile(
    r'(<div class="footer-links"[^>]*>\s*)'
    r'<a href="/privacy-policy/">Privacy Policy</a>\s*&middot;\s*'
    r'<a href="/contact/">Contact</a>\s*&middot;\s*'
    r'<a href="/sitemap\.xml">Sitemap</a>\s*'
    r'(</div>)',
    re.DOTALL
)

NEW_FOOTER = r'''\1<a href="/about/">About</a> &middot;
      <a href="/privacy-policy/">Privacy Policy</a> &middot;
      <a href="/terms/">Terms</a> &middot;
      <a href="/contact/">Contact</a> &middot;
      <a href="/sitemap.xml">Sitemap</a>
    \2'''

# Old cookie consent message
OLD_CC_MSG = "message: 'This website uses cookies to ensure you get the best experience on our website.'"
NEW_CC_MSG = "message: 'This website uses cookies for analytics and advertising. See our Privacy Policy for details.'"

updated_count = 0
skipped_count = 0
error_count = 0

for root, dirs, files in os.walk(BASE_DIR):
    # Skip .git directory
    if '.git' in root:
        continue
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content
            changes = []

            # 1. Update footer links
            new_content, footer_count = OLD_FOOTER.subn(NEW_FOOTER, content)
            if footer_count > 0:
                changes.append(f"footer({footer_count})")
                content = new_content

            # 2. Update cookie consent message
            if OLD_CC_MSG in content:
                content = content.replace(OLD_CC_MSG, NEW_CC_MSG)
                changes.append("cookie_msg")

            # Skip the terms/index.html we just created (already has correct values)
            rel_path = os.path.relpath(fpath, BASE_DIR)
            if rel_path == "terms/index.html":
                skipped_count += 1
                continue

            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_count += 1
                print(f"  UPDATED: {rel_path} [{', '.join(changes)}]")
            else:
                skipped_count += 1
        except Exception as e:
            error_count += 1
            print(f"  ERROR: {os.path.relpath(fpath, BASE_DIR)} - {e}")

print(f"\nSummary: {updated_count} updated, {skipped_count} skipped, {error_count} errors")

# Now update sitemap.xml
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
try:
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap = f.read()

    if '/terms/' not in sitemap:
        # Find the last </urlset> and insert before it
        terms_entry = """  <url>
    <loc>https://mireiasem.com/terms/</loc>
    <lastmod>2026-08-05T00:00:00+08:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>"""
        sitemap = sitemap.replace('</urlset>', terms_entry)
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap)
        print("sitemap.xml: added /terms/ entry")
    else:
        print("sitemap.xml: /terms/ already present")
except Exception as e:
    print(f"sitemap.xml ERROR: {e}")
