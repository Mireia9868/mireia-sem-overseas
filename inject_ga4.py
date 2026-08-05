#!/usr/bin/env python3
"""Inject GA4 tracking code into all HTML files on mireiasem.com."""

import os
import re

GA4_SNIPPET = """  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0FRC1RXQLV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-0FRC1RXQLV');
  </script>
"""

GA4_ID = "G-0FRC1RXQLV"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

html_files = []
for root, dirs, files in os.walk(BASE_DIR):
    # Skip .git and hidden dirs
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML files")

injected = 0
skipped = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has this GA4 ID
    if GA4_ID in content:
        print(f"  SKIP (already present): {os.path.relpath(filepath, BASE_DIR)}")
        skipped += 1
        continue

    # Inject before </head>
    if '</head>' in content:
        new_content = content.replace('</head>', GA4_SNIPPET + '\n</head>', 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  DONE: {os.path.relpath(filepath, BASE_DIR)}")
        injected += 1
    else:
        print(f"  WARN: no </head> found in {os.path.relpath(filepath, BASE_DIR)}")

print(f"\nSummary: {injected} injected, {skipped} already present, {len(html_files)} total")
