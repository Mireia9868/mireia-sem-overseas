#!/usr/bin/env python3
"""Add internal links to existing 10 articles on the site."""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
from articles_data_batch1 import ARTICLES_BATCH1
from articles_data_batch2 import ARTICLES_BATCH2
from generate_batch_articles import EXISTING_ARTICLES, find_related_articles, generate_internal_links_section, get_article_url

def main():
    all_batch = list(ARTICLES_BATCH1) + list(ARTICLES_BATCH2)
    all_articles = list(EXISTING_ARTICLES) + all_batch

    updated = 0
    for article in EXISTING_ARTICLES:
        slug = article["slug"]
        date = article["date"]
        date_parts = date.split("-")
        file_path = os.path.join(BASE_DIR, date_parts[0], date_parts[1], date_parts[2], slug, "index.html")

        if not os.path.exists(file_path):
            print(f"  SKIP (not found): {slug}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if already has Related Articles
        if "Related Articles" in content:
            print(f"  SKIP (already has links): {slug}")
            continue

        # Generate related articles section
        related_html = generate_internal_links_section(article, all_articles)

        # Insert before the closing </div> of markdown-body
        # Find the pattern: </div>\n\n                  <div class="post-metas
        # or: </div>\n\n                  <div class="post-metas my-4">
        insert_pattern = r'(</div>\s*\n\s*<div class="post-metas)'
        match = re.search(insert_pattern, content)
        if match:
            insert_pos = match.start()
            content = content[:insert_pos] + related_html + "\n\n" + content[insert_pos:]
        else:
            # Fallback: find </div> before post-metas
            post_metas_pos = content.find('class="post-metas')
            if post_metas_pos > 0:
                # Find the </div> before post-metas
                search_back = content[:post_metas_pos].rfind("</div>")
                if search_back > 0:
                    content = content[:search_back] + related_html + "\n\n" + content[search_back:]
            else:
                print(f"  ERROR (no insert point): {slug}")
                continue

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        related = find_related_articles(article, all_articles, max_results=3)
        print(f"  Updated: {slug} ({len(related)} related articles)")
        updated += 1

    print(f"\nDone: {updated} existing articles updated with internal links")

if __name__ == "__main__":
    main()
