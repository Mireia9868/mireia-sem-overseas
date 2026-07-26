#!/usr/bin/env python3
"""Generate the English overseas SEM blog site."""

import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- CDN URLs (international) ----
BOOTSTRAP_CSS = "https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css"
BOOTSTRAP_JS = "https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.min.js"
JQUERY_JS = "https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"
NPROGRESS_JS = "https://cdn.jsdelivr.net/npm/nprogress@0.2.0/nprogress.min.js"
NPROGRESS_CSS = "https://cdn.jsdelivr.net/npm/nprogress@0.2.0/nprogress.min.css"
TYPED_JS = "https://cdn.jsdelivr.net/npm/typed.js@2.0.12/lib/typed.min.js"
FANCYBOX_CSS = "https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css"
FANCYBOX_JS = "https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js"
MARKDOWN_CSS = "https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown.min.css"
HINT_CSS = "https://cdn.jsdelivr.net/npm/hint.css@2.7.0/hint.min.css"
ANCHOR_JS = "https://cdn.jsdelivr.net/npm/anchor-js@4.3.1/anchor.min.js"
MERMAID_JS = "https://cdn.jsdelivr.net/npm/mermaid@8.13.5/dist/mermaid.min.js"

# ---- Site config ----
SITE_TITLE = "Mireia SEM Blog"
SITE_SUBTITLE = "Data-driven insights for cross-border digital advertising."
SITE_AUTHOR = "Mireia"
SITE_DESC = "Professional insights on Google Ads, Bing Ads, Facebook Ads, conversion tracking, and cross-border e-commerce marketing."

# ---- Article data ----
ARTICLES = [
    {
        "slug": "microsoft-advertising-editor-bulk-editing-guide",
        "date": "2024-10-30",
        "date_iso": "2024-10-30T13:29:00+08:00",
        "title": "Microsoft Advertising Editor: The Ultimate Bulk Editing Tool",
        "excerpt": "Microsoft Advertising Editor is a powerful desktop tool that lets you bulk download, edit, and upload your ad campaigns offline. Learn how to streamline campaign management with bulk import/export, make offline changes before pushing live, and dramatically speed up your Bing Ads workflow.",
        "category": "Tools & Tips > Account Optimization > Microsoft Advertising Editor",
        "category_path": "/categories/Tools-Tips/",
        "tags": ["Tools", "Account Optimization", "Microsoft Advertising Editor"],
        "content": """<h2 id="what-is-microsoft-advertising-editor">What is Microsoft Advertising Editor?</h2>
<p>Microsoft Advertising Editor (formerly Bing Ads Editor) is a free desktop application that allows advertisers to manage their Bing Ads campaigns in bulk. You can download your entire account structure, make changes offline, and then upload everything at once — saving enormous time compared to making changes one by one in the web interface.</p>

<h2 id="key-features">Key Features</h2>
<ul>
<li><strong>Bulk Import &amp; Export:</strong> Download your entire account or specific campaigns as a local file, make changes in the editor, and push updates in one click.</li>
<li><strong>Offline Editing:</strong> All changes are made locally. Nothing syncs to your live account until you click "Post Changes" — giving you a safe sandbox to experiment.</li>
<li><strong>Bulk Keyword Management:</strong> Add, edit, or pause thousands of keywords at once using copy-paste or CSV import.</li>
<li><strong>Ad Copy Variations:</strong> Create and test multiple ad variations across campaigns simultaneously.</li>
<li><strong>Bid &amp; Budget Adjustments:</strong> Adjust bids and budgets at scale with bulk edit tools.</li>
</ul>

<h2 id="download-and-install">Download &amp; Installation</h2>
<p>Download Microsoft Advertising Editor from the official page:</p>
<p><a href="https://about.ads.microsoft.com/en-us/solutions/tools/editor" target="_blank" rel="noopener">https://about.ads.microsoft.com/en-us/solutions/tools/editor</a></p>
<p>The tool is available for both Windows and Mac. Sign in with your Microsoft Advertising credentials to get started.</p>

<h2 id="workflow-example-bulk-import">Workflow Example: Bulk Import</h2>
<ol>
<li><strong>Download your account:</strong> Open the Editor, sign in, and select "Download" to pull your current campaign structure locally.</li>
<li><strong>Make your changes:</strong> Use the left panel to navigate campaigns, ad groups, keywords, and ads. Edit any field directly — changes are highlighted in the interface.</li>
<li><strong>Review pending changes:</strong> Click "Changes" in the left panel to review all modifications before posting. You can filter by entity type (campaigns, ad groups, keywords, ads).</li>
<li><strong>Post changes:</strong> Once satisfied, click "Post Changes" to sync everything to your live account. The tool will show a progress bar and confirm when complete.</li>
</ol>

<div class="note-tip">
<p><strong>Pro Tip:</strong> Always review your pending changes before posting. The Editor makes it easy to spot mistakes — like a misplaced decimal in a bid — before they affect your live campaigns.</p>
</div>

<h2 id="best-practices">Best Practices</h2>
<ul>
<li><strong>Use CSV import for large-scale changes:</strong> Export your current structure as CSV, make changes in Excel/Google Sheets, and re-import for maximum efficiency.</li>
<li><strong>Keep a backup before major edits:</strong> Download a fresh copy before making structural changes, so you can reference the original state if needed.</li>
<li><strong>Leverage multiple accounts:</strong> If you manage multiple Bing Ads accounts, you can switch between them in the same Editor instance.</li>
<li><strong>Schedule posts during low-traffic periods:</strong> For large uploads, post during off-peak hours to minimize disruption to active campaigns.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>Microsoft Advertising Editor is an essential tool for any serious Bing Ads advertiser managing more than a handful of campaigns. The ability to make bulk changes offline, review before posting, and dramatically reduce manual work makes it indispensable for efficient account management at scale.</p>""",
    },
    {
        "slug": "bing-ads-account-registration-guide",
        "date": "2024-10-30",
        "date_iso": "2024-10-30T00:04:00+08:00",
        "title": "Bing Ads Account Registration: Complete Setup Guide",
        "excerpt": "Step-by-step guide to registering and setting up Bing Ads (Microsoft Advertising) accounts. Learn how to create a new customer, set up your account, link manager accounts, and complete the invitation process for multi-account management.",
        "category": "Ad Channels > Campaign Setup > Bing Ads",
        "category_path": "/categories/Ad-Channels/",
        "tags": ["Bing Ads", "Ad Campaigns", "Account Setup"],
        "content": """<h2 id="overview">Overview</h2>
<p>Setting up a Microsoft Advertising (Bing Ads) account correctly from the start saves time and avoids common pitfalls. This guide walks through the complete registration process, from creating your first account to linking multiple accounts under a manager structure.</p>

<h2 id="step-1-create-a-new-account">Step 1: Create a New Account</h2>
<p>Visit <a href="https://ads.microsoft.com" target="_blank" rel="noopener">ads.microsoft.com</a> and sign up using your email address. You can use any email provider — Gmail, Outlook, or a business email.</p>

<h2 id="step-2-create-a-customer-and-account">Step 2: Create a Customer &amp; Account</h2>
<p>After signing in, you'll need to create a "Customer" entity, which is the top-level organizational unit in Microsoft Advertising. Under each Customer, you can create one or more advertising accounts.</p>
<ol>
<li>Click "Create account" in the dashboard</li>
<li>Fill in your business name, timezone, and currency</li>
<li>Select your primary business location</li>
</ol>

<h2 id="step-3-confirmation">Step 3: Account Confirmation</h2>
<p>Once created, you'll see a confirmation page with your Customer ID and Account ID. Save these numbers — you'll need them for support requests and API integrations.</p>

<h2 id="step-4-link-accounts-manager">Step 4: Link Accounts to a Manager Account</h2>
<p>If you're managing multiple accounts (e.g., for different clients or markets), you'll want to set up a Manager Account:</p>
<ol>
<li>In your Manager Account, go to "Account settings" → "Link accounts"</li>
<li>Enter the Account ID you want to link</li>
<li>Click "Send invitation"</li>
</ol>

<h2 id="step-5-accept-invitation">Step 5: Accept the Invitation</h2>
<p>The invited account will receive an email notification. Log into the invited account:</p>
<ol>
<li>Go to "Account settings" → "Account access"</li>
<li>Find the pending invitation from the Manager Account</li>
<li>Click "Accept" to complete the linking</li>
</ol>

<div class="note-tip">
<p><strong>Important:</strong> The Manager Account only gains access after the invitation is accepted from the client account side. This two-step confirmation ensures account security.</p>
</div>

<h2 id="step-6-verification-complete">Step 6: Verification &amp; Setup Complete</h2>
<p>Once the invitation is accepted, the account will appear in your Manager Account's dashboard. You can now manage campaigns, billing, and settings across all linked accounts from a single interface.</p>

<h2 id="common-issues">Common Issues &amp; Solutions</h2>
<ul>
<li><strong>Invitation not received:</strong> Check spam/junk folders. If still missing, resend from the Manager Account.</li>
<li><strong>Cannot create account in certain countries:</strong> Microsoft Advertising is not available in all markets. Check the <a href="https://help.ads.microsoft.com/#apex/ads/en/56804/2" target="_blank" rel="noopener">list of available markets</a>.</li>
<li><strong>Currency mismatch:</strong> Choose your currency carefully — it cannot be changed after account creation. If you need a different currency, create a new account.</li>
</ul>

<h2 id="next-steps">Next Steps After Setup</h2>
<ol>
<li>Set up billing (credit card or invoice payments)</li>
<li>Import campaigns from Google Ads using the import tool</li>
<li>Install the UET tag for conversion tracking</li>
<li>Set up campaign structure (campaigns → ad groups → keywords → ads)</li>
</ol>""",
    },
    {
        "slug": "shopify-plus-bing-uet-tag-deployment",
        "date": "2024-10-30",
        "date_iso": "2024-10-30T00:04:00+08:00",
        "title": "Shopify Plus & Bing UET Tag Deployment Guide",
        "excerpt": "After Shopify Plus updated its checkout, the old additional scripts section no longer accepts custom code — breaking conversion tracking for Google, Facebook, and Bing. Here's the complete solution for deploying Bing UET tags on Shopify Plus with the new checkout architecture.",
        "category": "Conversion Tracking > Code Integration > Bing Ads",
        "category_path": "/categories/Conversion-Tracking/",
        "tags": ["Bing Ads", "UET Tag", "Event Tracking", "Shopify Plus"],
        "content": """<h2 id="background">Background: The Shopify Plus Checkout Update</h2>
<p>Shopify Plus updated its checkout flow, and the old "Additional Scripts" section in checkout settings no longer accepts custom code. This directly impacts marketing channels — Google Ads, Facebook Ads, and Bing Ads all lose their conversion tracking capabilities if you relied on the old method.</p>
<p>If your Shopify Plus store previously had tracking codes installed in the checkout additional scripts area, those codes have stopped firing. Below is the updated solution for Bing UET tag deployment.</p>

<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Shopify Plus account with admin access</li>
<li>Microsoft Advertising account with UET tag created</li>
<li>Your UET Tag ID (found in Microsoft Advertising → Tools → UET tags)</li>
</ul>

<h2 id="step-1-base-uett-tag">Step 1: Install the Base UET Tag</h2>
<p><em>This step assumes you already have the UET tracking code from your Microsoft Advertising account.</em></p>
<p>The base UET tag needs to be installed on <strong>all pages</strong> of your Shopify store. In Shopify admin:</p>
<ol>
<li>Go to <strong>Online Store → Themes → Actions → Edit Code</strong></li>
<li>Open <code>layout/theme.liquid</code></li>
<li>In the <code>&lt;head&gt;</code> section, paste your UET tag script:</li>
</ol>
<pre><code class="language-html">&lt;script&gt;(function(w,d,t,r,u){var f,n,i;w[u]=w[u]||[],f=function(){var o={ti:"YOUR_TAG_ID"};o.q=w[u],w[u]=new UET(o),w[u].push("pageLoad")},n=d.createElement(t),n.src=r,n.async=1,n.onload=n.onreadystatechange=function(){var s=this.readyState;s&&s!=="loaded"&&s!=="complete"||(f(),n.onload=n.onreadystatechange=null)},i=d.getElementsByTagName(t)[0],i.parentNode.insertBefore(n,i)})(window,document,"script","//bat.bing.com/bat.js","uetq");&lt;/script&gt;</code></pre>
<p>Replace <code>YOUR_TAG_ID</code> with your actual UET Tag ID.</p>

<h2 id="step-2-conversion-events">Step 2: Set Up Conversion Events via Shopify Webhooks</h2>
<p>With the new Shopify Plus checkout, you need to use <strong>Shopify Webhooks</strong> or the <strong>Shopify Customer Events</strong> API to fire conversion events:</p>
<ol>
<li>Go to <strong>Settings → Customer events</strong> in Shopify admin</li>
<li>Click "Add custom pixel"</li>
<li>Name it "Bing UET Conversion"</li>
<li>Paste the following code:</li>
</ol>
<pre><code class="language-javascript">// Track purchase events for Bing UET
analytics.subscribe("checkout_completed", (event) => {
  window.uetq = window.uetq || [];
  window.uetq.push({
    'ec': 'purchase',
    'ea': 'checkout_completed',
    'el': event.data?.checkout?.order?.id || '',
    'ev': event.data?.checkout?.subtotalPrice?.amount || 0
  });
});</code></pre>

<h2 id="step-3-verify-installation">Step 3: Verify the Installation</h2>
<p>Use the <strong>Microsoft Advertising UET Tag Helper</strong> Chrome extension to verify your tag is firing correctly:</p>
<ol>
<li>Install the <a href="https://chrome.google.com/webstore/detail/microsoft-advertising-uet" target="_blank" rel="noopener">UET Tag Helper</a> extension</li>
<li>Navigate to your Shopify store and complete a test purchase</li>
<li>Check the extension to confirm both the page load and conversion events are tracked</li>
</ol>

<div class="note-warning">
<p><strong>Important:</strong> The conversion event will only fire on the "Thank You" / order confirmation page. Make sure your webhook/pixel fires after the order is completed, not during checkout.</p>
</div>

<h2 id="step-4-define-conversion-goals">Step 4: Define Conversion Goals in Microsoft Advertising</h2>
<p>After the UET tag is verified, set up conversion goals:</p>
<ol>
<li>In Microsoft Advertising, go to <strong>Tools → Conversion goals</strong></li>
<li>Create a new goal of type "Event" or "Destination URL"</li>
<li>Map it to the UET event you configured (e.g., <code>purchase</code> event)</li>
<li>Set the conversion value to match your order subtotal</li>
</ol>

<h2 id="troubleshooting">Troubleshooting Common Issues</h2>
<ul>
<li><strong>Tag not firing on checkout pages:</strong> This is the core issue with the Shopify Plus update. Use the Customer Events API method described above — do not try to add scripts directly to checkout.</li>
<li><strong>Conversion value showing as 0:</strong> Check that your event data object includes the price amount. Use <code>event.data?.checkout?.subtotalPrice?.amount</code> to capture the value.</li>
<li><strong>UET Tag Helper shows no activity:</strong> Ensure the base tag is in <code>theme.liquid</code> and loads on all pages. Clear your browser cache and try again.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>The Shopify Plus checkout update disrupted tracking for many advertisers, but the Customer Events API provides a robust solution. By combining the base UET tag in <code>theme.liquid</code> with event-based tracking through custom pixels, you can restore full conversion tracking for Bing Ads — and the same approach works for Google Ads and Facebook Pixel.</p>""",
    },
    {
        "slug": "google-ads-compromised-sites-ad-disapproval",
        "date": "2024-09-21",
        "date_iso": "2024-09-21T22:56:00+08:00",
        "title": "Google Ads: Resolving \"Compromised Sites\" Ad Disapprovals",
        "excerpt": "Google's \"Abuse of the ad network\" policy was updated in 2023, splitting malware policies into three separate categories. If your ads are being disapproved for \"compromised sites,\" here's how to identify the issue, fix it, and request a review.",
        "category": "Channel Policies > Policy Updates & Solutions > Google Ads",
        "category_path": "/categories/Channel-Policies/",
        "tags": ["Google Ads", "Ad Campaigns", "Channel Policies", "Ad Disapproval"],
        "content": """<h2 id="policy-background">Policy Background</h2>
<p>In May 2023, Google Ads updated its "malware or unwanted software" policy, splitting it into three separate policies:</p>
<ol>
<li><strong>Malware policy</strong> — targets software designed to harm or exploit systems</li>
<li><strong>Compromised sites policy</strong> — targets sites that have been hacked or infected</li>
<li><strong>Unwanted software policy</strong> — targets deceptive or harmful software downloads</li>
</ol>
<p>Reference: <a href="https://support.google.com/adspolicy/answer/13334531" target="_blank" rel="noopener">Google Ads Policy — Abuse of the ad network</a></p>

<h2 id="what-is-a-compromised-site">What is a "Compromised Site"?</h2>
<p>A compromised site is one where a third party has injected malicious code without the site owner's knowledge. Common examples include:</p>
<ul>
<li>Injected JavaScript that redirects visitors to phishing pages</li>
<li>Hidden iframes loading malware downloads</li>
<li>SEO spam injections (pharmaceutical, gambling links inserted into pages)</li>
<li>Backdoor scripts that give attackers ongoing access</li>
</ul>
<p>Google detects these issues through its Safe Browsing system and will disapprove any ads pointing to compromised URLs.</p>

<h2 id="how-to-diagnose">How to Diagnose the Issue</h2>
<ol>
<li><strong>Check Google Search Console:</strong> Go to <strong>Security &amp; Manual Actions → Security Issues</strong>. If your site is flagged, Google will show the type of compromise detected.</li>
<li><strong>Scan with Google Safe Browsing:</strong> Visit <a href="https://transparencyreport.google.com/safe-browsing/search" target="_blank" rel="noopener">Google Safe Browsing Transparency Report</a> and enter your URL.</li>
<li><strong>Use Sucuri SiteCheck:</strong> <a href="https://sitecheck.sucuri.net/" target="_blank" rel="noopener">sitecheck.sucuri.net</a> provides a free scan that identifies known malware and blacklisting status.</li>
<li><strong>Check ad disapproval reason in Google Ads:</strong> In your Google Ads account, hover over the disapproved ad's status to see the specific policy violation.</li>
</ol>

<h2 id="fixing-the-compromise">Step-by-Step Fix</h2>

<h3 id="step-1-isolate-and-identify">Step 1: Isolate and Identify the Malicious Code</h3>
<ol>
<li>Put your site into maintenance mode if possible</li>
<li>Check recently modified files (sort by date in your file manager or use SSH: <code>find . -mtime -7 -name "*.php"</code>)</li>
<li>Look for suspicious patterns: <code>eval(base64_decode</code>, <code>str_rot13</code>, <code>gzinflate</code>, unexpected <code>&lt;iframe&gt;</code> tags, or <code>&lt;script&gt;</code> tags pointing to unknown domains</li>
</ol>

<h3 id="step-2-remove-malicious-code">Step 2: Remove the Malicious Code</h3>
<ol>
<li>Delete injected files and code blocks</li>
<li>Restore from a known-good backup if the infection is widespread</li>
<li>Update all CMS, plugins, and themes to their latest versions</li>
<li>Change all passwords (admin, FTP, database, hosting control panel)</li>
</ol>

<h3 id="step-3-patch-vulnerabilities">Step 3: Patch the Underlying Vulnerability</h3>
<ul>
<li><strong>If using WordPress:</strong> Update all plugins and themes, remove unused ones, install a security plugin (Wordfence, Sucuri)</li>
<li><strong>If using Shopify:</strong> Review installed apps, remove any suspicious ones, check theme code for injections</li>
<li><strong>If custom-built:</strong> Audit input validation, SQL injection vulnerabilities, and file upload handlers</li>
</ul>

<h3 id="step-4-request-review">Step 4: Request a Review</h3>
<ol>
<li>In <strong>Google Search Console → Security Issues</strong>, click "Request Review"</li>
<li>Explain what was compromised, how you fixed it, and what steps you've taken to prevent recurrence</li>
<li>Submit the review request — Google typically processes it within 72 hours</li>
</ol>
<p>Once Search Console clears the flag, your Google Ads disapprovals should resolve automatically. If they don't, contact Google Ads support directly.</p>

<div class="note-tip">
<p><strong>Pro Tip:</strong> Always set up Google Search Console email alerts for security issues. Early detection means fewer days of ads being disapproved.</p>
</div>

<h2 id="prevention">Prevention Best Practices</h2>
<ul>
<li>Keep all software (CMS, plugins, themes) updated to the latest versions</li>
<li>Use strong, unique passwords and enable two-factor authentication</li>
<li>Install a Web Application Firewall (WAF) like Cloudflare or Sucuri</li>
<li>Regularly back up your site to a separate location</li>
<li>Monitor your site with Google Search Console and Sucuri</li>
<li>Limit file upload capabilities and use SFTP instead of FTP</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>Compromised site disapprovals can be stressful, but they follow a predictable pattern: diagnose → clean → patch → request review. The key is speed — the faster you identify and remove the malicious code, the sooner your ads resume serving. Invest in prevention to avoid repeat incidents.</p>""",
    },
    {
        "slug": "google-ads-uac-campaign-strategy",
        "date": "2024-09-21",
        "date_iso": "2024-09-21T22:56:00+08:00",
        "title": "Google Ads Universal App Campaign (UAC) Strategy Guide",
        "excerpt": "UAC leverages Google's machine learning to automate app install and engagement campaigns across Search, Play, YouTube, and Display. Learn how to structure your campaigns, set tCPA/tROAS targets, optimize creative assets, and scale effectively.",
        "category": "Ad Channels > Campaign Setup > Google Ads",
        "category_path": "/categories/Ad-Channels/",
        "tags": ["Google Ads", "Ad Campaigns", "Universal App Campaign"],
        "content": """<h2 id="what-is-uac">What is a Universal App Campaign (UAC)?</h2>
<p>Introduced in 2015, Universal App Campaigns (now called <strong>Google App Campaigns</strong>) use Google's machine learning to automatically optimize app install and engagement ads across Google's entire inventory — including Search, Google Play, YouTube, and the Display Network.</p>
<p>Instead of manually setting bids, targeting, and placements, you provide creative assets and a target CPA (tCPA) or target ROAS (tROAS), and Google's algorithm handles the rest.</p>

<h2 id="campaign-types">App Campaign Types</h2>
<table>
<thead><tr><th>Type</th><th>Goal</th><th>Best For</th></tr></thead>
<tbody>
<tr><td>App Installs</td><td>Drive new app installs</td><td>New apps, growth-phase apps</td></tr>
<tr><td>App Engagement</td><td>Re-engage existing users</td><td>Mature apps with retention goals</td></tr>
<tr><td>App Pre-registration</td><td>Build anticipation before launch</td><td>Games, major app launches</td></tr>
</tbody>
</table>

<h2 id="campaign-setup">Campaign Setup Best Practices</h2>

<h3 id="1-target-cpa-setting">1. Setting Your Target CPA (tCPA)</h3>
<p>Your tCPA is the most important setting — it tells Google's algorithm how much you're willing to pay for one install. Best practices:</p>
<ul>
<li><strong>Start with your historical CPA</strong> from other channels as a baseline</li>
<li><strong>Don't set tCPA too low initially</strong> — a very low target will starve the algorithm of data. Start 20-30% above your actual target and gradually lower it</li>
<li><strong>Give the algorithm 7-14 days</strong> to learn before making changes. Each significant adjustment resets the learning phase</li>
</ul>

<h3 id="2-creative-assets">2. Creative Assets</h3>
<p>Google App Campaigns automatically generate ad combinations from your assets. Provide as many as possible:</p>
<ul>
<li><strong>Text headlines:</strong> 20-30 characters, provide at least 5 distinct headlines</li>
<li><strong>Text descriptions:</strong> Up to 90 characters, provide at least 5</li>
<li><strong>Images:</strong> Landscape (1200×628), portrait (1200×1500), and square (1200×1200). Provide multiple variations</li>
<li><strong>Video:</strong> At least one landscape and one portrait video. YouTube-compatible format (MP4, MOV)</li>
<li><strong>HTML5 playable ads:</strong> Optional but highly effective for games</li>
</ul>

<div class="note-tip">
<p><strong>Creative is the #1 lever in App Campaigns.</strong> Since you can't control targeting or placements, the quality and diversity of your creative assets determines performance. Refresh assets every 2-4 weeks to combat creative fatigue.</p>
</div>

<h3 id="3-budget">3. Budget Setting</h3>
<ul>
<li>Set your daily budget to at least <strong>50× your tCPA</strong> to give the algorithm enough data to optimize</li>
<li>For new campaigns, Google recommends a minimum budget of <strong>$250-500/day</strong> for the first 2 weeks</li>
<li>Once the campaign stabilizes, you can adjust the budget down while monitoring performance</li>
</ul>

<h2 id="optimization-strategy">Optimization Strategy</h2>

<h3 id="phase-1-learning">Phase 1: Learning (Days 1-14)</h3>
<ul>
<li>Don't make changes — let the algorithm learn</li>
<li>Monitor install volume and CPI trends</li>
<li>Check that creative assets are serving across all placements</li>
</ul>

<h3 id="phase-2-optimization">Phase 2: Optimization (Weeks 3-6)</h3>
<ul>
<li>Review asset performance report — pause underperforming assets</li>
<li>Add new creative variations to replace fatigued ones</li>
<li>Gradually lower tCPA by 10-15% at a time, waiting 5-7 days between changes</li>
<li>If using tROAS, ensure your in-app conversion values are accurately tracked</li>
</ul>

<h3 id="phase-3-scaling">Phase 3: Scaling (Week 7+)</h3>
<ul>
<li>Increase budget by 20% at a time, no more than once per week</li>
<li>Consider splitting campaigns by country or OS if scaling beyond $10K/day</li>
<li>Test App Engagement campaigns for re-engaging high-value users</li>
<li>Layer in custom audiences and similar audiences if available</li>
</ul>

<h2 id="common-mistakes">Common Mistakes to Avoid</h2>
<ol>
<li><strong>Setting tCPA too low from the start:</strong> This kills the campaign before it has a chance to learn</li>
<li><strong>Making frequent changes during learning phase:</strong> Each change resets the algorithm's optimization</li>
<li><strong>Insufficient creative assets:</strong> Fewer assets = fewer ad combinations = limited reach</li>
<li><strong>Not tracking post-install events:</strong> Without event tracking, you can't use tROAS or optimize for high-value users</li>
<li><strong>Ignoring asset performance reports:</strong> Regularly review and refresh creative to maintain performance</li>
</ol>

<h2 id="conclusion">Conclusion</h2>
<p>Google App Campaigns are powerful but require patience and a data-driven approach. The algorithm rewards advertisers who provide high-quality creative assets, set realistic targets, and resist the urge to micro-manage. Follow the phased approach above, and you'll be well-positioned to scale your app installs profitably.</p>""",
    },
    {
        "slug": "google-ads-offline-conversion-upload",
        "date": "2024-09-21",
        "date_iso": "2024-09-21T00:04:00+08:00",
        "title": "Google Ads: Offline Conversion Data Upload Guide",
        "excerpt": "For B2B and high-consideration purchases, online conversions don't tell the full story. Learn how to use GCLID and offline conversion upload to feed your CRM data back into Google Ads, enabling smarter bidding based on actual business outcomes.",
        "category": "Conversion Tracking > Offline Data > Google Ads",
        "category_path": "/categories/Conversion-Tracking/",
        "tags": ["Google Ads", "Conversion Tracking", "Offline Conversions"],
        "content": """<h2 id="why-offline-conversions">Why Offline Conversion Upload?</h2>
<p>Many businesses — especially B2B, real estate, and high-consideration purchases — generate leads online but close deals offline (via phone calls, in-person meetings, or CRM-tracked sales). Standard Google Ads conversion tracking only captures the initial online action (form submission, call), not the actual revenue.</p>
<p><strong>Offline conversion upload</strong> bridges this gap by sending CRM-tracked conversion data back to Google Ads using the GCLID (Google Click ID). This enables:</p>
<ul>
<li>Bidding based on actual sales, not just leads</li>
<li>Target ROAS (tROAS) bidding using real revenue data</li>
<li>Smarter algorithm optimization toward high-value conversions</li>
</ul>

<h2 id="setup-overview">Setup Overview</h2>
<p>The process has three main components:</p>
<ol>
<li><strong>Enable auto-tagging</strong> to capture GCLID on every ad click</li>
<li><strong>Pass GCLID to your CRM</strong> alongside lead data</li>
<li><strong>Upload conversion data</strong> back to Google Ads with the GCLID</li>
</ol>

<h2 id="step-1-enable-auto-tagging">Step 1: Enable Auto-Tagging to Capture GCLID</h2>
<p>Auto-tagging automatically appends a GCLID parameter to every ad click URL. Without it, you cannot link offline conversions back to specific ad clicks.</p>
<ol>
<li>In Google Ads, go to <strong>Settings → Account settings</strong></li>
<li>Check "Auto-tagging" → toggle to <strong>Enabled</strong></li>
<li>Save changes</li>
</ol>

<div class="note-warning">
<p><strong>Important:</strong> UTM parameters alone are not sufficient for offline conversion upload. UTM can track keyword-level data, but only GCLID can uniquely identify each click and link it to a conversion event. You must use auto-tagging + GCLID.</p>
</div>

<h2 id="step-2-capture-gclid">Step 2: Capture GCLID in Your Lead Forms</h2>
<p>When a user clicks your ad and lands on your site, the GCLID is in the URL. You need to capture it and store it with the lead data:</p>
<ol>
<li>Add a hidden field to your lead forms to store the GCLID</li>
<li>Use JavaScript to extract the GCLID from the URL and populate the hidden field</li>
</ol>
<pre><code class="language-javascript">// Extract GCLID from URL and populate hidden form field
function getGclid() {
  var w = window.location.search.substring(1);
  var params = w.split('&');
  for (var i = 0; i < params.length; i++) {
    var pair = params[i].split('=');
    if (pair[0] === 'gclid') {
      return decodeURIComponent(pair[1]);
    }
  }
  return '';
}
// Set on page load
document.addEventListener('DOMContentLoaded', function() {
  var gclidField = document.getElementById('gclid_field');
  if (gclidField) {
    gclidField.value = getGclid();
  }
});</code></pre>
<p>Store the GCLID in your CRM alongside the lead record (e.g., as a custom field on the lead/contact object in Salesforce, HubSpot, etc.)</p>

<h2 id="step-3-create-conversion-actions">Step 3: Create Conversion Actions in Google Ads</h2>
<ol>
<li>Go to <strong>Tools → Conversions → New conversion action</strong></li>
<li>Select "Import → Other data sources or CRMs"</li>
<li>Choose "Track conversions from clicks" (uses GCLID)</li>
<li>Name your conversion (e.g., "Qualified Lead," "Closed Deal")</li>
<li>Set category, value, and count settings</li>
<li>Repeat for each conversion stage you want to track (lead → qualified → closed)</li>
</ol>

<h2 id="step-4-upload-conversions">Step 4: Upload Conversion Data</h2>
<p>There are two methods for uploading offline conversions:</p>

<h3 id="method-a-manual-csv-upload">Method A: Manual CSV Upload</h3>
<p>For small volumes or testing:</p>
<ol>
<li>Prepare a CSV with columns: <code>Google Click ID</code>, <code>Conversion Name</code>, <code>Conversion Time</code>, <code>Conversion Value</code>, <code>Conversion Currency</code></li>
<li>Go to <strong>Tools → Conversions → Uploads</strong></li>
<li>Click "Upload" and select your CSV file</li>
<li>Review the upload status for errors</li>
</ol>

<h3 id="method-b-api-upload">Method B: Google Ads API (Automated)</h3>
<p>For production use, automate uploads via the Google Ads API:</p>
<pre><code class="language-python"># Pseudocode for Google Ads API offline conversion upload
from google.ads.googleads.client import GoogleAdsClient

client = GoogleAdsClient.load_from_storage()
conversion_upload_service = client.get_service("ConversionUploadService")

conversion_action = client.get_service("ConversionActionService")
conversion_action_resource = conversion_action.conversion_action_path(
    customer_id, conversion_action_id
)

click_conversion = client.get_type("ClickConversion")
click_conversion.gclid = "EAIaIQobChMI..."
click_conversion.conversion_action = conversion_action_resource
click_conversion.conversion_date_time = "2024-09-20 14:32:05+08:00"
click_conversion.conversion_value = 1500.0
click_conversion.currency_code = "USD"

request = client.get_type("UploadClickConversionsRequest")
request.customer_id = customer_id
request.conversions = [click_conversion]

response = conversion_upload_service.upload_click_conversions(request=request)</code></pre>

<h2 id="best-practices">Best Practices</h2>
<ul>
<li><strong>Upload within 90 days:</strong> Google only accepts GCLID conversions within 90 days of the click</li>
<li><strong>Use consistent naming:</strong> Match your CRM stage names with Google Ads conversion action names for easy mapping</li>
<li><strong>Track multiple stages:</strong> Create separate conversion actions for "Lead," "Qualified," "Opportunity," and "Closed" to give the algorithm rich signal</li>
<li><strong>Include conversion value:</strong> Revenue data enables tROAS bidding, which is far more effective than tCPA for revenue-focused campaigns</li>
<li><strong>Upload frequently:</strong> Daily uploads provide the freshest signal. Weekly is the minimum for effective optimization</li>
</ul>

<h2 id="common-issues">Common Issues</h2>
<ul>
<li><strong>"GCLID not found" errors:</strong> The GCLID may be expired (90-day limit exceeded) or malformed. Check your CRM data quality.</li>
<li><strong>Conversions not appearing in reports:</strong> Allow 3-12 hours for uploaded conversions to appear in Google Ads reports. Attribution lag settings may also delay reporting.</li>
<li><strong>Low match rate:</strong> If many leads have empty GCLID fields, review your form implementation — ensure the hidden field is populated before form submission.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>Offline conversion upload transforms Google Ads from a lead-generation tool into a revenue-optimization platform. By feeding real business outcomes back to the algorithm, you enable smarter bidding that focuses on quality — not just quantity. The setup requires coordination between marketing and CRM teams, but the performance gains are well worth the effort.</p>""",
    },
    {
        "slug": "google-consent-mode-v2-updates",
        "date": "2024-07-18",
        "date_iso": "2024-07-18T00:19:00+08:00",
        "title": "Google Consent Mode v2: What Advertisers Need to Know",
        "excerpt": "With GDPR and evolving privacy regulations, Google's Consent Mode has become essential. Version 2 introduces new parameters for ad user data and ad personalization. Learn how to implement it and recover up to 70% of lost conversion data through modeling.",
        "category": "Channel Policies > Policy Updates & Solutions > Google Ads",
        "category_path": "/categories/Channel-Policies/",
        "tags": ["Policy & News", "Ad Campaigns", "Channel Policies", "Google Ads"],
        "content": """<h2 id="background">Background: Why Consent Mode Matters</h2>
<p>The EU's General Data Protection Regulation (GDPR) and similar privacy laws worldwide have made consent management a critical requirement for digital advertising. When users decline cookie consent, traditional tracking methods fail — creating gaps in conversion data.</p>
<p>Google's <strong>Consent Mode</strong> addresses this by adjusting how Google tags behave based on user consent status. When consent is denied, Google uses <strong>modeled conversions</strong> to estimate the missing data — recovering up to 70% of lost conversion signals.</p>

<h2 id="what-is-consent-mode">What is Consent Mode?</h2>
<p>Consent Mode is a framework that allows advertisers to indicate whether users have consented to cookies for analytics and advertising purposes. Based on this signal, Google tags adjust their behavior:</p>
<ul>
<li><strong>Consent granted:</strong> Normal tracking — full cookie-based measurement</li>
<li><strong>Consent denied:</strong> Cookieless measurement — Google uses aggregated, modeled data to estimate conversions and user behavior</li>
</ul>

<h2 id="whats-new-in-v2">What's New in Consent Mode v2</h2>
<p>Version 2 introduces two new consent parameters:</p>
<table>
<thead><tr><th>Parameter</th><th>Purpose</th><th>Default</th></tr></thead>
<tbody>
<tr><td><code>ad_user_data</code></td><td>Indicates whether user data can be sent to Google for advertising</td><td>'not set'</td></tr>
<tr><td><code>ad_personalization</code></td><td>Indicates whether data can be used for personalized advertising</td><td>'not set'</td></tr>
</tbody>
</table>
<p>These join the existing v1 parameters:</p>
<ul>
<li><code>ad_storage</code> — enables storage of advertising cookies</li>
<li><code>analytics_storage</code> — enables storage of analytics cookies</li>
<li><code>functionality_storage</code> — enables storage for site functionality</li>
<li><code>personalization_storage</code> — enables storage for personalization</li>
<li><code>security_storage</code> — enables storage for security</li>
</ul>

<h2 id="implementation">Implementation Guide</h2>

<h3 id="option-1-consent-management-platform">Option 1: Using a Consent Management Platform (CMP)</h3>
<p>The easiest approach is to use a Google-certified CMP that integrates natively with Consent Mode:</p>
<ul>
<li>Cookiebot, OneTrust, TrustArc, Usercentrics, Didomi, etc.</li>
<li>Configure your CMP to send consent signals to the Google Data Layer</li>
<li>The CMP automatically sets the Consent Mode parameters based on user choices</li>
</ul>

<h3 id="option-2-manual-implementation">Option 2: Manual Implementation</h3>
<p>If you're not using a CMP, you can implement Consent Mode directly:</p>

<p><strong>Step 1: Set default consent state (before tags load):</strong></p>
<pre><code class="language-html">&lt;!-- Set default consent to denied before any Google tags --&gt;
&lt;script&gt;
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }

  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'wait_for_update': 500
  });
&lt;/script&gt;</code></pre>

<p><strong>Step 2: Update consent when user makes a choice:</strong></p>
<pre><code class="language-javascript">// When user grants consent
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted'
});

// Or update specific parameters based on user choices
// e.g., user consents to analytics but not personalization
gtag('consent', 'update', {
  'analytics_storage': 'granted',
  'ad_storage': 'granted',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied'
});</code></pre>

<div class="note-tip">
<p><strong>Key Principle:</strong> Always set defaults to 'denied' <em>before</em> any Google tags load. Then update to 'granted' after the user consents. This ensures compliance — you never set non-essential cookies before consent is given.</p>
</div>

<h2 id="modeled-conversions">How Modeled Conversions Work</h2>
<p>When consent is denied, Google uses machine learning to model conversions based on:</p>
<ul>
<li>Aggregated data from consenting users with similar behavior patterns</li>
<li>Historical conversion data from your account</li>
<li>Browser and device signals</li>
<li>Time and geographic patterns</li>
</ul>
<p>Google reports that modeled conversions can recover up to <strong>70% of the data lost</strong> when users deny consent. This varies by industry and traffic volume — accounts with more historical data get better modeling results.</p>

<h2 id="impact-on-ads">Impact on Google Ads Performance</h2>
<ul>
<li><strong>Bidding optimization:</strong> Smart Bidding strategies (tCPA, tROAS, Maximize Conversions) rely on conversion data. Without Consent Mode, denied-consent users create data gaps that degrade bidding performance.</li>
<li><strong>Audience targeting:</strong> When ad_personalization is denied, users are excluded from remarketing lists and similar audiences.</li>
<li><strong>Conversion reporting:</strong> Modeled conversions appear in your Google Ads reports alongside observed conversions, giving a more complete picture.</li>
</ul>

<h2 id="verification">Verification &amp; Monitoring</h2>
<ol>
<li>Use the <strong>Google Tag Assistant</strong> Chrome extension to verify consent signals are firing correctly</li>
<li>Check <strong>Google Ads → Conversions</strong> to see if modeled conversions appear alongside observed ones</li>
<li>Monitor conversion volume trends — a sudden drop may indicate a consent implementation issue</li>
</ol>

<h2 id="conclusion">Conclusion</h2>
<p>Consent Mode v2 is no longer optional — it's a requirement for running Google Ads in regions with privacy regulations. Proper implementation ensures you remain compliant while maximizing data recovery through modeled conversions. If you haven't upgraded from v1 yet, do so immediately — Google now requires v2 for European Economic Area (EEA) traffic.</p>""",
    },
    {
        "slug": "gcs-high-touch-payment-method-updates",
        "date": "2024-06-21",
        "date_iso": "2024-06-21T01:00:00+08:00",
        "title": "Google Ads: GCS High Touch Client Payment Method Updates",
        "excerpt": "Starting May 2024, Google Cloud Service (GCS) High Touch advertisers face new payment restrictions: monthly invoicing or direct debit only — no credit cards, debit cards, or e-wallets. Here's what this means and how to prepare.",
        "category": "Channel Policies > Policy Updates & Solutions > Google Ads",
        "category_path": "/categories/Channel-Policies/",
        "tags": ["Google Ads", "Policy & News", "Channel Policies"],
        "content": """<h2 id="background">Background</h2>
<p>Effective May 1, 2024, Google updated payment options for advertisers receiving <strong>GCS (Google Cloud Service) High Touch</strong> support. These advertisers — typically large-scale accounts with dedicated Google account teams — are now limited to:</p>
<ol>
<li><strong>Monthly invoicing</strong> (net-30 or net-60 terms)</li>
<li><strong>Direct debit / bank transfer</strong> (available only in the US and select EMEA countries)</li>
</ol>
<p><strong>No longer supported:</strong> Credit cards, debit cards, or e-wallets (Google Pay, Alipay, etc.)</p>

<h2 id="who-is-affected">Who is Affected?</h2>
<p>This policy affects accounts that Google classifies as "GCS High Touch" — typically determined by:</p>
<ul>
<li>Monthly ad spend exceeding a threshold (varies by region)</li>
<li>Account history and support level</li>
<li>Direct relationship with a Google account team</li>
</ul>
<p>Many self-service advertisers in Hong Kong or those using virtual credit cards for payment are gradually being reclassified into this category as their accounts grow.</p>

<h2 id="how-youll-be-notified">How You'll Be Notified</h2>
<p>When your account is reclassified, you'll receive an email from Google that includes:</p>
<ul>
<li>Your account ID and Customer ID</li>
<li>The effective date of the payment change</li>
<li>Instructions for setting up the new payment method</li>
<li>A deadline by which you must transition (typically 30-60 days)</li>
</ul>

<h2 id="impact-on-advertisers">Impact on Advertisers</h2>
<table>
<thead><tr><th>Aspect</th><th>Before</th><th>After (GCS High Touch)</th></tr></thead>
<tbody>
<tr><td>Payment Method</td><td>Credit card, debit card, e-wallet</td><td>Monthly invoice or direct debit only</td></tr>
<tr><td>Billing Cycle</td><td>Automatic charges per threshold or monthly</td><td>Monthly invoice (net-30/60)</td></tr>
<tr><td>Credit Check</td><td>Not required</td><td>Credit check required for invoicing</td></tr>
<tr><td>Setup Time</td><td>Instant</td><td>2-4 weeks for credit check &amp; approval</td></tr>
</tbody>
</table>

<h2 id="how-to-prepare">How to Prepare</h2>

<h3 id="step-1-check-your-status">Step 1: Check Your Account Status</h3>
<ol>
<li>Log into Google Ads → <strong>Billing → Payment methods</strong></li>
<li>Check if you see a notice about payment method changes</li>
<li>Look for the "Account type" — if it says "High Touch" or "GCS," you're affected</li>
</ol>

<h3 id="step-2-apply-for-monthly-invoicing">Step 2: Apply for Monthly Invoicing</h3>
<ol>
<li>Go to <strong>Billing → Payments → Payment methods</strong></li>
<li>Click "Add payment method" → "Monthly invoicing"</li>
<li>Complete the credit application form (requires business registration documents, financial statements)</li>
<li>Google will conduct a credit check — this takes 2-4 weeks</li>
</ol>

<h3 id="step-3-transition-plan">Step 3: Plan the Transition</h3>
<ul>
<li><strong>Don't wait until the deadline:</strong> Start the invoicing application immediately after receiving the notification — the credit check takes weeks</li>
<li><strong>Maintain a backup funding source:</strong> Keep a valid payment method active during the transition to avoid campaign disruption</li>
<li><strong>Communicate with your finance team:</strong> Monthly invoicing changes your cash flow — ensure your finance department is prepared for net-30/60 terms</li>
</ul>

<div class="note-warning">
<p><strong>Warning:</strong> If you don't set up an approved payment method by the deadline, Google will pause your campaigns. Don't risk losing ad serving — start the transition immediately upon receiving notification.</p>
</div>

<h2 id="alternative-options">Alternative Options</h2>
<p>If monthly invoicing isn't viable for your business:</p>
<ul>
<li><strong>Direct debit (US/EMEA only):</strong> Set up automatic bank transfers. Available in select countries.</li>
<li><strong>Third-party payment agencies:</strong> Some agencies offer payment intermediary services where they pay Google on your behalf via invoice and bill you separately. This adds a service fee but can bridge the gap.</li>
<li><strong>Account restructuring:</strong> In some cases, splitting spend across multiple smaller accounts can keep them below the GCS High Touch threshold — but this is a short-term workaround, not a long-term solution.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>The GCS High Touch payment update is a sign that your Google Ads account has grown to a significant scale — which is good news. But the transition requires proactive planning, especially for businesses accustomed to credit card payments. Start the invoicing application early, keep your finance team in the loop, and ensure a smooth transition to avoid any disruption to your campaigns.</p>""",
    },
    {
        "slug": "facebook-ads-business-page-optimization",
        "date": "2024-05-17",
        "date_iso": "2024-05-17T00:04:00+08:00",
        "title": "Facebook Ads: Business Page Optimization Complete Guide",
        "excerpt": "A well-optimized Facebook Business Page is the foundation of successful Facebook advertising. Learn how to update your profile picture, cover photo, page name, About section, and call-to-action button — and why only admins can make these changes.",
        "category": "Ad Channels > Campaign Setup > Facebook Ads",
        "category_path": "/categories/Ad-Channels/",
        "tags": ["Facebook Ads", "Page Optimization"],
        "content": """<h2 id="why-page-optimization-matters">Why Page Optimization Matters</h2>
<p>Your Facebook Business Page is the public face of your brand on Facebook. Before users see your ads, they often check your page — and a poorly optimized page can undermine even the best ad campaigns. Key reasons to optimize:</p>
<ul>
<li><strong>First impressions:</strong> A professional page with proper branding builds trust</li>
<li><strong>Ad quality signals:</strong> Facebook's algorithm considers page quality when serving ads</li>
<li><strong>Organic reach:</strong> Well-optimized pages get better organic distribution</li>
<li><strong>Conversion trust:</strong> Users who click your ad and land on an unprofessional page are less likely to convert</li>
</ul>

<div class="note-warning">
<p><strong>Important:</strong> Only <strong>Admins</strong> can modify a Facebook Business Page. If you don't see the edit options described below, check your page role — you may be an "Editor" or "Analyst" instead of "Admin."</p>
</div>

<h2 id="update-profile-picture">How to Update Your Profile Picture</h2>
<ol>
<li>Log into <a href="https://www.facebook.com" target="_blank" rel="noopener">facebook.com</a> and click on <strong>"Pages"</strong> in the left menu</li>
<li>Select your Business Page from the list</li>
<li>Click on the profile picture → <strong>"Update"</strong></li>
<li>Choose "Upload Photo" and select your brand logo</li>
<li>Adjust the crop and positioning, then click "Save"</li>
</ol>
<p><strong>Best practices for profile pictures:</strong></p>
<ul>
<li>Use your brand logo — keep it simple and recognizable</li>
<li>Recommended size: 320×320 pixels (square)</li>
<li>Ensure it's visible at small sizes (it appears as a tiny circle in comments and ads)</li>
</ul>

<h2 id="update-cover-photo">How to Update Your Cover Photo</h2>
<ol>
<li>On your Business Page, hover over the cover photo area</li>
<li>Click <strong>"Edit Cover"</strong></li>
<li>Choose "Upload Photo" or select from existing photos</li>
<li>Drag to reposition and click "Save"</li>
</ol>
<p><strong>Best practices for cover photos:</strong></p>
<ul>
<li>Recommended size: 820×312 pixels (displays as 640×360 on mobile — keep key content centered)</li>
<li>Use a high-quality brand image, product showcase, or promotional graphic</li>
<li>Avoid placing text in the bottom-left corner (it's covered by the profile picture and page name)</li>
<li>Update seasonally or for promotions to keep the page fresh</li>
</ul>

<h2 id="update-page-name">How to Update Your Page Name</h2>
<ol>
<li>Log into Facebook and click your profile picture (top-right)</li>
<li>Click <strong>"See all Profiles"</strong> and select your Business Page</li>
<li>Click <strong>"Settings"</strong> (gear icon) in the left menu</li>
<li>Go to <strong>"Page Setup" → "Name"</strong></li>
<li>Enter the new name and click "Review Change"</li>
</ol>

<div class="note-warning">
<p><strong>Note:</strong> Facebook may review name changes, especially for pages with large followings. If your page has more than 200 likes, the name change may require Facebook's approval. You can only change your page name once every 7 days.</p>
</div>

<h2 id="optimize-about-section">Optimizing the About Section</h2>
<p>The About section is critical for SEO and user trust. Make sure to complete:</p>
<ul>
<li><strong>Category:</strong> Choose the most relevant category for your business</li>
<li><strong>Description:</strong> 1-2 sentences describing what your business does</li>
<li><strong>Website:</strong> Link to your landing page or e-commerce site</li>
<li><strong>Contact info:</strong> Email, phone number, and physical address (if applicable)</li>
<li><strong>Hours:</strong> Business operating hours (for local businesses)</li>
<li><strong>Founded:</strong> Year your business was established (adds credibility)</li>
</ul>

<h2 id="call-to-action-button">Set Up the Call-to-Action Button</h2>
<p>The CTA button appears prominently below your cover photo:</p>
<ol>
<li>Click <strong>"Add a Button"</strong> below your cover photo</li>
<li>Select the action type: "Shop Now," "Contact Us," "Sign Up," "Book Now," etc.</li>
<li>Enter the destination URL</li>
<li>Click "Finish" to save</li>
</ol>
<p>Choose a CTA that aligns with your ad objectives — if you're running conversion campaigns, "Shop Now" is ideal. For lead gen, use "Sign Up" or "Contact Us."</p>

<h2 id="page-verification">Page Verification</p>
<p>(Content continues with verification steps...)</p>

<h2 id="conclusion">Conclusion</h2>
<p>Facebook Business Page optimization is a foundational step that should be completed before launching any ad campaigns. A polished, professional page with complete information improves ad performance, builds trust, and increases conversion rates. Remember: only admins can make these changes — ensure you have the right access level before starting.</p>""",
    },
    {
        "slug": "woocommerce-facebook-pixel-integration",
        "date": "2024-05-17",
        "date_iso": "2024-05-17T00:04:00+08:00",
        "title": "WooCommerce & Facebook Pixel Integration Guide",
        "excerpt": "Complete guide to integrating Facebook Pixel with your WooCommerce store. Learn how to create the pixel in Business Manager, install the base code, set up standard events (ViewContent, AddToCart, Purchase), and verify everything with the Pixel Helper.",
        "category": "Conversion Tracking > Code Integration > Facebook Ads",
        "category_path": "/categories/Conversion-Tracking/",
        "tags": ["Facebook Ads", "Conversion Tracking", "WooCommerce"],
        "content": """<h2 id="overview">Overview</h2>
<p>Facebook Pixel is essential for tracking conversions from your Facebook and Instagram ad campaigns. For WooCommerce stores, proper pixel integration enables:</p>
<ul>
<li>Conversion tracking (purchases, add-to-cart, etc.)</li>
<li>Audience building (remarketing to website visitors)</li>
<li>Lookalike audience creation</li>
<li>Conversion-optimized bidding (oCPM)</li>
<li>Dynamic product ads (retargeting with specific products)</li>
</ul>

<h2 id="step-1-create-pixel">Step 1: Create the Facebook Pixel</h2>
<p>You need a Facebook Business Manager account to create a pixel:</p>
<ol>
<li>Go to <a href="https://business.facebook.com" target="_blank" rel="noopener">business.facebook.com</a> → <strong>Events Manager</strong></li>
<li>Click "Connect Data Source" → "Web" → "Facebook Pixel"</li>
<li>Name your pixel (e.g., "StoreName — Main Pixel")</li>
<li>Enter your website URL</li>
<li>Click "Continue" — you'll receive your <strong>Pixel ID</strong> (a 15-16 digit number)</li>
</ol>
<p>Save your Pixel ID — you'll need it for the installation steps below.</p>

<h2 id="step-2-install-base-code">Step 2: Install the Base Pixel Code</h2>
<p>You have three options for installing the base pixel code on WooCommerce:</p>

<h3 id="option-a-plugin">Option A: Using a Plugin (Recommended)</h3>
<p>The easiest method for non-developers:</p>
<ol>
<li>Install the <strong>"PixelYourSite"</strong> or <strong>"Facebook for WooCommerce"</strong> plugin</li>
<li>Go to the plugin settings</li>
<li>Enter your Facebook Pixel ID</li>
<li>The plugin automatically installs the base code and fires standard events on all pages</li>
</ol>

<h3 id="option-b-manual-code">Option B: Manual Code Installation</h3>
<p>For full control over what fires where:</p>
<ol>
<li>In WordPress admin, go to <strong>Appearance → Theme Editor</strong></li>
<li>Open <code>header.php</code> (or use a header injection plugin)</li>
<li>Paste the Facebook Pixel base code right after the <code>&lt;head&gt;</code> tag:</li>
</ol>
<pre><code class="language-html">&lt;!-- Meta Pixel Code --&gt;
&lt;script&gt;
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
&lt;/script&gt;
&lt;noscript&gt;&lt;img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&amp;ev=PageView&amp;noscript=1"
/&gt;&lt;/noscript&gt;
&lt;!-- End Meta Pixel Code --&gt;</code></pre>

<h3 id="option-c-google-tag-manager">Option C: Google Tag Manager</h3>
<p>If you already use GTM, add the pixel as a custom HTML tag with an "All Pages" trigger. This gives you centralized tag management.</p>

<h2 id="step-3-standard-events">Step 3: Set Up Standard Events</h2>
<p>For WooCommerce, the most important standard events are:</p>
<table>
<thead><tr><th>Event</th><th>When to Fire</th><th>Key Parameters</th></tr></thead>
<tbody>
<tr><td><code>ViewContent</code></td><td>Product detail page</td><td>content_ids, content_type, value, currency</td></tr>
<tr><td><code>AddToCart</code></td><td>When item added to cart</td><td>content_ids, content_type, value, currency</td></tr>
<tr><td><code>InitiateCheckout</code></td><td>Checkout page load</td><td>content_ids, num_items, value, currency</td></tr>
<tr><td><code>Purchase</code></td><td>Order confirmation page</td><td>content_ids, content_type, value, currency</td></tr>
</tbody>
</table>

<h3 id="purchase-event-code">Purchase Event Code (for order confirmation page)</h3>
<pre><code class="language-html">&lt;script&gt;
fbq('track', 'Purchase', {
  content_ids: ['product_1', 'product_2'],  // Product IDs
  content_type: 'product',
  value: 99.50,                              // Total order value
  currency: 'USD'
});
&lt;/script&gt;</code></pre>

<div class="note-tip">
<p><strong>Pro Tip:</strong> The Purchase event with value and currency is the most critical — it powers conversion-optimized bidding and ROAS reporting. Make sure the value matches the actual order total including shipping and tax.</p>
</div>

<h2 id="step-4-advanced-matching">Step 4: Enable Advanced Matching (Optional but Recommended)</h2>
<p>Advanced Matching sends hashed customer data (email, phone, name) with pixel events, improving match rates for custom and lookalike audiences:</p>
<pre><code class="language-javascript">fbq('init', 'YOUR_PIXEL_ID', {
  em: 'hashed_email',       // SHA-256 hashed email
  ph: 'hashed_phone',       // SHA-256 hashed phone
  fn: 'hashed_first_name',  // SHA-256 hashed first name
  ln: 'hashed_last_name'    // SHA-256 hashed last name
});</code></pre>

<h2 id="step-5-verify">Step 5: Verify with Pixel Helper</h2>
<ol>
<li>Install the <a href="https://chrome.google.com/webstore/detail/meta-pixel-helper" target="_blank" rel="noopener">Meta Pixel Helper</a> Chrome extension</li>
<li>Navigate to your WooCommerce store</li>
<li>Visit each key page: product page, cart, checkout, order confirmation</li>
<li>Click the Pixel Helper icon to verify each event fires correctly</li>
<li>Check that event parameters (especially value and currency) are populated</li>
</ol>

<h2 id="step-6-capi">Step 6: Set Up Conversions API (CAPI)</h2>
<p>The Conversions API supplements the pixel by sending data server-side, improving data reliability (especially with iOS privacy restrictions and ad blockers):</p>
<ol>
<li>Use the <strong>"Facebook for WooCommerce"</strong> plugin — it includes CAPI integration</li>
<li>Or implement via the <a href="https://developers.facebook.com/docs/marketing-api/conversions-api" target="_blank" rel="noopener">Conversions API</a> directly</li>
<li>Pair the pixel (client-side) with CAPI (server-side) for maximum data quality</li>
</ol>

<h2 id="troubleshooting">Troubleshooting</h2>
<ul>
<li><strong>Pixel not firing:</strong> Check that the pixel ID is correct and the code is in the <code>&lt;head&gt;</code> section. Clear cache plugins.</li>
<li><strong>Purchase event not firing:</strong> Ensure the code is on the Thank You / order confirmation page only. In WooCommerce, this is typically <code>thankyou.php</code> or the order-received endpoint.</li>
<li><strong>Value showing as 0:</strong> Make sure you're passing the dynamic order total, not a hardcoded value.</li>
<li><strong>Duplicate events:</strong> If using both a plugin and manual code, you'll get double-firing. Choose one method only.</li>
</ul>

<h2 id="conclusion">Conclusion</h2>
<p>Proper Facebook Pixel integration on WooCommerce unlocks the full power of Meta advertising — from conversion tracking to audience building to dynamic product ads. Use the "Facebook for WooCommerce" plugin for the quickest setup, or implement manually for maximum control. Don't forget to add the Conversions API for maximum data reliability in the post-iOS 14.5 era.</p>""",
    },
]

# ---- Category data ----
CATEGORIES = [
    {"name": "Ad Channels", "description": "Google Ads, Bing Ads, Facebook Ads campaign setup and optimization", "count": 4},
    {"name": "Conversion Tracking", "description": "Pixel deployment, UET tags, offline conversion upload, code integration", "count": 3},
    {"name": "Channel Policies", "description": "Platform policy updates, ad disapproval solutions, compliance", "count": 3},
    {"name": "Tools & Tips", "description": "Advertising tools, account optimization, workflow efficiency", "count": 1},
]

# ---- Tag data ----
ALL_TAGS = {}
for article in ARTICLES:
    for tag in article["tags"]:
        ALL_TAGS[tag] = ALL_TAGS.get(tag, 0) + 1


def get_head(title, description, extra_css="", extra_head=""):
    """Generate HTML head section."""
    return f"""<!DOCTYPE html>
<html lang="en" data-default-color-scheme=auto>

<head>
  <meta charset="UTF-8">
  <link rel="apple-touch-icon" sizes="76x76" href="/img/Mireia%20Sem_transparent.png">
  <link rel="icon" href="/img/Mireia%20Sem_transparent.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">

  <meta name="theme-color" content="#2f4154">
  <meta name="author" content="{SITE_AUTHOR}">
  <meta name="keywords" content="SEM, Google Ads, Bing Ads, Facebook Ads, cross-border e-commerce, conversion tracking, digital advertising">
  <meta name="description" content="{description}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:site_name" content="{SITE_TITLE}">
  <meta property="og:locale" content="en_US">
  <meta property="article:author" content="{SITE_AUTHOR}">
  <meta name="twitter:card" content="summary_large_image">

  <meta name="referrer" content="no-referrer-when-downgrade">

  <title>{title}</title>

  <link rel="stylesheet" href="{BOOTSTRAP_CSS}" />
  {extra_css}
  <link rel="stylesheet" href="//at.alicdn.com/t/font_1749284_hj8rtnfg7um.css">
  <link rel="stylesheet" href="//at.alicdn.com/t/font_1736178_lbnruvf0jn.css">
  <link rel="stylesheet" href="/css/main.css" />
  <link id="highlight-css" rel="stylesheet" href="/css/highlight.css" />
  <link id="highlight-css-dark" rel="stylesheet" href="/css/highlight-dark.css" />

  <script id="fluid-configs">
    var Fluid = window.Fluid || {{}};
    Fluid.ctx = Object.assign({{}}, Fluid.ctx)
    var CONFIG = {{"hostname":"mireiasem.com","root":"/","version":"1.9.3","typing":{{"enable":true,"typeSpeed":70,"cursorChar":"_","loop":false,"scope":[]}},"anchorjs":{{"enable":true,"element":"h1,h2,h3,h4,h5,h6","placement":"left","visible":"hover","icon":""}},"progressbar":{{"enable":true,"height_px":3,"color":"#29d","options":{{"showSpinner":false,"trickleSpeed":100}}}},"code_language":{{"enable":true,"default":"TEXT"}},"copy_btn":true,"image_caption":{{"enable":true}},"image_zoom":{{"enable":true,"img_url_replace":["",""]}},"toc":{{"enable":true,"placement":"right","headingSelector":"h1,h2,h3,h4,h5,h6","collapseDepth":0}},"lazyload":{{"enable":true,"loading_img":"/img/loading.gif","onlypost":false,"offset_factor":2}},"web_analytics":{{"enable":false,"follow_dnt":true,"baidu":null,"google":null,"gtag":null,"tencent":{{"sid":null,"cid":null}},"woyaola":null,"cnzz":null,"leancloud":{{"app_id":null,"app_key":null,"server_url":null,"path":"window.location.pathname","ignore_local":false}}}},"search_path":"/local-search.xml"}};

    if (CONFIG.web_analytics.follow_dnt) {{
      var dntVal = navigator.doNotTrack || window.doNotTrack || navigator.msDoNotTrack;
      Fluid.ctx.dnt = dntVal && (dntVal.startsWith('1') || dntVal.startsWith('yes') || dntVal.startsWith('on'));
    }}
  </script>
  <script src="/js/utils.js"></script>
  <script src="/js/color-schema.js"></script>
  {extra_head}
</head>"""


def get_nav():
    """Generate navigation bar."""
    return """  <header>

<div class="header-inner" style="height: 100vh;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="/">
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
              <a class="nav-link" href="/">
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
            <li class="nav-item">
              <a class="nav-link" href="/about/">
                <i class="iconfont icon-user-fill"></i>
                About
              </a>
            </li>
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


def get_banner(subtitle=SITE_SUBTITLE, banner_height="100vh"):
    """Generate banner section."""
    return f"""<div id="banner" class="banner" parallax=true
     style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2">
            <span id="subtitle" data-typed-text="{subtitle}"></span>
        </div>
      </div>
        <div class="scroll-down-bar">
          <i class="iconfont icon-arrowdown"></i>
        </div>
    </div>
  </div>
</div>

</div>

  </header>"""


def get_footer():
    """Generate footer."""
    return """  <footer>
    <div class="footer-inner">

    <div class="footer-content">
       <a href="https://hexo.io" target="_blank" rel="nofollow noopener"><span>Hexo</span></a> <i class="iconfont icon-love"></i> <a href="https://github.com/fluid-dev/hexo-theme-fluid" target="_blank" rel="nofollow noopener"><span>Fluid</span></a>
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


def get_scripts(extra_scripts=""):
    """Generate script includes."""
    return f"""  <!-- Scripts -->

  <script src="{NPROGRESS_JS}"></script>
  <link rel="stylesheet" href="{NPROGRESS_CSS}" />

  <script>
    NProgress.configure({{"showSpinner":false,"trickleSpeed":100}})
    NProgress.start()
    window.addEventListener('load', function() {{
      NProgress.done();
    }})
  </script>


<script src="{JQUERY_JS}"></script>
<script src="{BOOTSTRAP_JS}"></script>
<script src="/js/events.js"></script>
<script src="/js/plugins.js"></script>

  <script src="{TYPED_JS}"></script>
  <script>
    (function (window, document) {{
      var typing = Fluid.plugins.typing;
      var subtitle = document.getElementById('subtitle');
      if (!subtitle || !typing) {{
        return;
      }}
      var text = subtitle.getAttribute('data-typed-text');
        typing(text);
    }})(window, document);
  </script>

    <script src="/js/img-lazyload.js"></script>

  <script src="/js/local-search.js"></script>

  <script defer src="https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>

{extra_scripts}

<!-- the boot of the theme, keep it at the bottom -->
<script src="/js/boot.js"></script>

  <noscript>
    <div class="noscript-warning">Blog works best with JavaScript enabled</div>
  </noscript>
</body>
</html>"""


def get_search_modal():
    """Generate search modal."""
    return """      <div class="modal fade" id="modalSearch" tabindex="-1" role="dialog" aria-labelledby="ModalLabel"
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


def get_scroll_top():
    """Generate scroll top button."""
    return """      <a id="scroll-top-button" aria-label="TOP" href="#" role="button">
        <i class="iconfont icon-arrowup" aria-hidden="true"></i>
      </a>"""


def generate_index():
    """Generate the homepage."""
    article_cards = ""
    for article in ARTICLES:
        date_display = article["date"]
        url = f"/{article['date'].replace('-', '/')}/{article['slug']}/"
        tags_html = " ".join([f'<a href="/tags/{tag.replace(" ", "-")}/">#{tag}</a>' for tag in article["tags"]])
        category_parts = article["category"].split(" > ")
        category_chain = ""
        for i, part in enumerate(category_parts):
            if i > 0:
                category_chain += '<span>&gt;</span>'
            category_chain += f'<a href="/categories/{category_parts[0].replace(" ", "-")}/" class="category-chain-item">{part}</a>'

        article_cards += f"""
  <div class="row mx-auto index-card">
    <article class="col-12 col-md-12 mx-auto index-info">
      <h1 class="index-header">
        <a href="{url}" target="_self">
          {article['title']}
        </a>
      </h1>
      <a class="index-excerpt index-excerpt__noimg" href="{url}" target="_self">
        <div>
          {article['excerpt']}
        </div>
      </a>
      <div class="index-btm post-metas">
          <div class="post-meta mr-3">
            <i class="iconfont icon-date"></i>
            <time datetime="{article['date']}" pubdate>
              {date_display}
            </time>
          </div>
          <div class="post-meta mr-3 d-flex align-items-center">
            <i class="iconfont icon-category"></i>
<span class="category-chains">
      <span class="category-chain">
        {category_chain}
      </span>
</span>
          </div>
          <div class="post-meta">
            <i class="iconfont icon-tags"></i>
              {tags_html}
          </div>
      </div>
    </article>
  </div>"""

    html = get_head(SITE_TITLE, SITE_DESC) + "\n\n<body>\n\n" + get_nav() + "\n\n" + get_banner() + f"""
  <main>
      <div class="container nopadding-x-md">
        <div id="board"
          style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
{article_cards}
              </div>
            </div>
          </div>
        </div>
      </div>

      {get_scroll_top()}

      {get_search_modal()}

  </main>

{get_footer()}

{get_scripts()}
"""
    return html


def generate_about():
    """Generate the about page."""
    extra_css = f"""  <link rel="stylesheet" href="{MARKDOWN_CSS}" />
  <link rel="stylesheet" href="{HINT_CSS}" />
  <link rel="stylesheet" href="{FANCYBOX_CSS}" />"""

    html = get_head(f"About - {SITE_TITLE}", "About Mireia - SEM specialist and cross-border advertising optimizer.", extra_css=extra_css) + f"""

<body>

  <header>

<div class="header-inner" style="height: 60vh;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="/">
      <strong>Mireia Sem Blog</strong>
    </a>
    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item"><a class="nav-link" href="/"><i class="iconfont icon-home-fill"></i> Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/archives/"><i class="iconfont icon-archive-fill"></i> Archives</a></li>
            <li class="nav-item"><a class="nav-link" href="/categories/"><i class="iconfont icon-category-fill"></i> Categories</a></li>
            <li class="nav-item"><a class="nav-link" href="/tags/"><i class="iconfont icon-tags-fill"></i> Tags</a></li>
            <li class="nav-item"><a class="nav-link" href="/about/"><i class="iconfont icon-user-fill"></i> About</a></li>
          <li class="nav-item" id="search-btn"><a class="nav-link" target="_self" href="javascript:;" data-toggle="modal" data-target="#modalSearch" aria-label="Search">&nbsp;<i class="iconfont icon-search"></i>&nbsp;</a></li>
          <li class="nav-item" id="color-toggle-btn"><a class="nav-link" target="_self" href="javascript:;" aria-label="Color Toggle">&nbsp;<i class="iconfont icon-dark" id="color-toggle-icon"></i>&nbsp;</a></li>
      </ul>
    </div>
  </div>
</nav>


<div id="banner" class="banner" parallax=true
     style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2">
            <span id="subtitle" data-typed-text="About Me"></span>
        </div>
      </div>
    </div>
  </div>
</div>

</div>

  </header>

  <main>
      <div class="container nopadding-x-md">
        <div id="board"
          style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">

<div class="markdown-body">
<h2 id="about-me">About Me</h2>
<p>Hi, I'm <strong>Mireia</strong> — a digital advertising optimizer specializing in cross-border e-commerce marketing. Based in Beijing, I work with global brands to maximize their ROI across major advertising platforms.</p>

<p>My core expertise covers:</p>
<ul>
<li><strong>Google Ads:</strong> Search, Display, Shopping, App Campaigns (UAC), Performance Max</li>
<li><strong>Bing Ads (Microsoft Advertising):</strong> Search, Shopping, audience targeting</li>
<li><strong>Facebook / Meta Ads:</strong> Conversion campaigns, dynamic product ads, audience building</li>
<li><strong>Conversion Tracking:</strong> Pixel deployment, UET tags, offline conversion upload, GA4 integration</li>
<li><strong>E-commerce Integration:</strong> Shopify, WooCommerce, custom platform tracking setups</li>
<li><strong>AI Search &amp; GEO:</strong> Generative Engine Optimization for energy storage and B2B brands</li>
</ul>

<h2 id="about-this-blog">About This Blog</h2>
<p>This site documents my hands-on experience in digital advertising — practical guides, policy updates, troubleshooting solutions, and data-driven insights from real campaigns. If you find the content helpful, that makes it all worthwhile.</p>

<p>If you spot any errors or have questions, feel free to reach out:</p>
<ul>
<li><strong>Email:</strong> hello@mireiasem.com</li>
<li><strong>WeChat:</strong> Scan the QR code below</li>
</ul>

<p><img src="/img/wechat-qcode.jpeg" alt="WeChat QR Code" style="max-width: 200px; border-radius: 8px;" /></p>

<h2 id="site-notes">Site Notes</h2>
<ul>
<li><strong>Content:</strong> All articles are based on real campaign experience and testing — not theoretical fluff.</li>
<li><strong>Updates:</strong> I post whenever I encounter new platform policies, tools, or optimization strategies worth sharing.</li>
<li><strong>Loading:</strong> This site is hosted overseas. If you experience slow loading, try using a VPN or switching networks.</li>
</ul>

<h2 id="connect">Connect</h2>
<p>Whether you're a fellow advertiser, a brand looking for marketing support, or just someone interested in SEM — I'm always happy to connect. Let's grow together in the world of cross-border digital advertising.</p>
</div>

              </div>
            </div>
          </div>
        </div>
      </div>

      {get_scroll_top()}
      {get_search_modal()}

  </main>

{get_footer()}
{get_scripts(extra_scripts=f'<script src="{FANCYBOX_JS}"></script>')}
"""
    return html


def generate_archives():
    """Generate the archives page."""
    # Group articles by year
    by_year = {}
    for article in ARTICLES:
        year = article["date"][:4]
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(article)

    archive_html = ""
    for year in sorted(by_year.keys(), reverse=True):
        archive_html += f'\n<div class="archive-timeline">\n<h2 class="archive-year">{year}</h2>\n<ul class="archive-list">\n'
        for article in sorted(by_year[year], key=lambda x: x["date"], reverse=True):
            url = f"/{article['date'].replace('-', '/')}/{article['slug']}/"
            date_display = article["date"]
            archive_html += f'<li class="archive-item"><span class="archive-date">{date_display}</span><a href="{url}">{article["title"]}</a></li>\n'
        archive_html += '</ul>\n</div>\n'

    html = get_head(f"Archives - {SITE_TITLE}", "All articles organized by date.") + f"""

<body>

  <header>
<div class="header-inner" style="height: 60vh;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="/"><strong>Mireia Sem Blog</strong></a>
    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item"><a class="nav-link" href="/"><i class="iconfont icon-home-fill"></i> Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/archives/"><i class="iconfont icon-archive-fill"></i> Archives</a></li>
            <li class="nav-item"><a class="nav-link" href="/categories/"><i class="iconfont icon-category-fill"></i> Categories</a></li>
            <li class="nav-item"><a class="nav-link" href="/tags/"><i class="iconfont icon-tags-fill"></i> Tags</a></li>
            <li class="nav-item"><a class="nav-link" href="/about/"><i class="iconfont icon-user-fill"></i> About</a></li>
          <li class="nav-item" id="search-btn"><a class="nav-link" target="_self" href="javascript:;" data-toggle="modal" data-target="#modalSearch" aria-label="Search">&nbsp;<i class="iconfont icon-search"></i>&nbsp;</a></li>
          <li class="nav-item" id="color-toggle-btn"><a class="nav-link" target="_self" href="javascript:;" aria-label="Color Toggle">&nbsp;<i class="iconfont icon-dark" id="color-toggle-icon"></i>&nbsp;</a></li>
      </ul>
    </div>
  </div>
</nav>
<div id="banner" class="banner" parallax=true style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2"><span id="subtitle" data-typed-text="Archives"></span></div>
      </div>
    </div>
  </div>
</div>
</div>
  </header>

  <main>
      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
                <div class="markdown-body">
{archive_html}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {get_scroll_top()}
      {get_search_modal()}
  </main>

{get_footer()}
{get_scripts()}
"""
    return html


def generate_categories():
    """Generate the categories page."""
    cat_html = '<div class="category-list">\n'
    for cat in CATEGORIES:
        cat_html += f'<div class="category-item"><h3><a href="/categories/{cat["name"].replace(" ", "-")}/">{cat["name"]}</a> <span class="category-count">({cat["count"]})</span></h3><p>{cat["description"]}</p></div>\n'
    cat_html += '</div>'

    html = get_head(f"Categories - {SITE_TITLE}", "Browse articles by category.") + f"""

<body>
  <header>
<div class="header-inner" style="height: 60vh;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="/"><strong>Mireia Sem Blog</strong></a>
    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item"><a class="nav-link" href="/"><i class="iconfont icon-home-fill"></i> Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/archives/"><i class="iconfont icon-archive-fill"></i> Archives</a></li>
            <li class="nav-item"><a class="nav-link" href="/categories/"><i class="iconfont icon-category-fill"></i> Categories</a></li>
            <li class="nav-item"><a class="nav-link" href="/tags/"><i class="iconfont icon-tags-fill"></i> Tags</a></li>
            <li class="nav-item"><a class="nav-link" href="/about/"><i class="iconfont icon-user-fill"></i> About</a></li>
          <li class="nav-item" id="search-btn"><a class="nav-link" target="_self" href="javascript:;" data-toggle="modal" data-target="#modalSearch" aria-label="Search">&nbsp;<i class="iconfont icon-search"></i>&nbsp;</a></li>
          <li class="nav-item" id="color-toggle-btn"><a class="nav-link" target="_self" href="javascript:;" aria-label="Color Toggle">&nbsp;<i class="iconfont icon-dark" id="color-toggle-icon"></i>&nbsp;</a></li>
      </ul>
    </div>
  </div>
</nav>
<div id="banner" class="banner" parallax=true style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2"><span id="subtitle" data-typed-text="Categories"></span></div>
      </div>
    </div>
  </div>
</div>
</div>
  </header>
  <main>
      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
                <div class="markdown-body">
{cat_html}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {get_scroll_top()}
      {get_search_modal()}
  </main>
{get_footer()}
{get_scripts()}
"""
    return html


def generate_tags():
    """Generate the tags page."""
    tag_html = '<div class="tag-cloud">\n'
    for tag, count in sorted(ALL_TAGS.items(), key=lambda x: x[0]):
        font_size = 14 + count * 3
        tag_html += f'<a href="/tags/{tag.replace(" ", "-")}/" class="tag-item" style="font-size: {font_size}px;">#{tag} <span class="tag-count">({count})</span></a>\n'
    tag_html += '</div>'

    html = get_head(f"Tags - {SITE_TITLE}", "Browse articles by tag.") + f"""

<body>
  <header>
<div class="header-inner" style="height: 60vh;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="/"><strong>Mireia Sem Blog</strong></a>
    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item"><a class="nav-link" href="/"><i class="iconfont icon-home-fill"></i> Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/archives/"><i class="iconfont icon-archive-fill"></i> Archives</a></li>
            <li class="nav-item"><a class="nav-link" href="/categories/"><i class="iconfont icon-category-fill"></i> Categories</a></li>
            <li class="nav-item"><a class="nav-link" href="/tags/"><i class="iconfont icon-tags-fill"></i> Tags</a></li>
            <li class="nav-item"><a class="nav-link" href="/about/"><i class="iconfont icon-user-fill"></i> About</a></li>
          <li class="nav-item" id="search-btn"><a class="nav-link" target="_self" href="javascript:;" data-toggle="modal" data-target="#modalSearch" aria-label="Search">&nbsp;<i class="iconfont icon-search"></i>&nbsp;</a></li>
          <li class="nav-item" id="color-toggle-btn"><a class="nav-link" target="_self" href="javascript:;" aria-label="Color Toggle">&nbsp;<i class="iconfont icon-dark" id="color-toggle-icon"></i>&nbsp;</a></li>
      </ul>
    </div>
  </div>
</nav>
<div id="banner" class="banner" parallax=true style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2"><span id="subtitle" data-typed-text="Tags"></span></div>
      </div>
    </div>
  </div>
</div>
</div>
  </header>
  <main>
      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
                <div class="markdown-body">
{tag_html}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {get_scroll_top()}
      {get_search_modal()}
  </main>
{get_footer()}
{get_scripts()}
"""
    return html


def generate_article(article):
    """Generate an individual article page."""
    extra_css = f"""  <link rel="stylesheet" href="{MARKDOWN_CSS}" />
  <link rel="stylesheet" href="{HINT_CSS}" />
  <link rel="stylesheet" href="{FANCYBOX_CSS}" />"""

    url = f"/{article['date'].replace('-', '/')}/{article['slug']}/"
    tags_html = " ".join([f'<a href="/tags/{tag.replace(" ", "-")}/">#{tag}</a>' for tag in article["tags"]])

    # Build TOC from content h2 headings
    toc_items = ""
    import re
    headings = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', article["content"])
    for hid, htext in headings:
        toc_items += f'<li><a href="#{hid}">{htext}</a></li>\n'

    html = get_head(f"{article['title']} - {SITE_TITLE}", article["excerpt"], extra_css=extra_css) + f"""

<body>
  <header>
<div class="header-inner" style="height: 60vh;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="/"><strong>Mireia Sem Blog</strong></a>
    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item"><a class="nav-link" href="/"><i class="iconfont icon-home-fill"></i> Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/archives/"><i class="iconfont icon-archive-fill"></i> Archives</a></li>
            <li class="nav-item"><a class="nav-link" href="/categories/"><i class="iconfont icon-category-fill"></i> Categories</a></li>
            <li class="nav-item"><a class="nav-link" href="/tags/"><i class="iconfont icon-tags-fill"></i> Tags</a></li>
            <li class="nav-item"><a class="nav-link" href="/about/"><i class="iconfont icon-user-fill"></i> About</a></li>
          <li class="nav-item" id="search-btn"><a class="nav-link" target="_self" href="javascript:;" data-toggle="modal" data-target="#modalSearch" aria-label="Search">&nbsp;<i class="iconfont icon-search"></i>&nbsp;</a></li>
          <li class="nav-item" id="color-toggle-btn"><a class="nav-link" target="_self" href="javascript:;" aria-label="Color Toggle">&nbsp;<i class="iconfont icon-dark" id="color-toggle-icon"></i>&nbsp;</a></li>
      </ul>
    </div>
  </div>
</nav>
<div id="banner" class="banner" parallax=true style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2"><span id="subtitle" data-typed-text="{article['title']}"></span></div>
      </div>
    </div>
  </div>
</div>
</div>
  </header>

  <main>
      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">

              <div class="col-12 col-md-9 m-auto">
                <div class="page-content">
                  <div class="markdown-body">
{article['content']}
                  </div>

                  <div class="post-metas my-4">
                    <div class="post-meta mr-3">
                      <i class="iconfont icon-date"></i>
                      <time datetime="{article['date']}">{article['date']}</time>
                    </div>
                    <div class="post-meta">
                      <i class="iconfont icon-tags"></i>
                      {tags_html}
                    </div>
                  </div>

                  <hr>
                  <div class="post-nav">
                    <a href="/" class="post-nav-item">&larr; Back to Home</a>
                  </div>
                </div>
              </div>

              <div class="col-12 col-md-3 d-none d-lg-block">
                <div class="post-toc" id="toc">
                  <h4>Table of Contents</h4>
                  <ul>
{toc_items}
                  </ul>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
      {get_scroll_top()}
      {get_search_modal()}
  </main>

{get_footer()}
{get_scripts(extra_scripts=f'<script src="{FANCYBOX_JS}"></script>\n  <script src="{ANCHOR_JS}"></script>\n  <script>anchors.add("h2,h3,h4");</script>')}
"""
    return html


def generate_404():
    """Generate the 404 page."""
    html = get_head(f"404 - {SITE_TITLE}", "Page not found.") + f"""

<body>
  <header>
<div class="header-inner" style="height: 60vh;">
  <nav id="navbar" class="navbar fixed-top  navbar-expand-lg navbar-dark scrolling-navbar">
  <div class="container">
    <a class="navbar-brand" href="/"><strong>Mireia Sem Blog</strong></a>
    <button id="navbar-toggler-btn" class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <div class="animated-icon"><span></span><span></span><span></span></div>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item"><a class="nav-link" href="/"><i class="iconfont icon-home-fill"></i> Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/archives/"><i class="iconfont icon-archive-fill"></i> Archives</a></li>
            <li class="nav-item"><a class="nav-link" href="/categories/"><i class="iconfont icon-category-fill"></i> Categories</a></li>
            <li class="nav-item"><a class="nav-link" href="/tags/"><i class="iconfont icon-tags-fill"></i> Tags</a></li>
            <li class="nav-item"><a class="nav-link" href="/about/"><i class="iconfont icon-user-fill"></i> About</a></li>
          <li class="nav-item" id="color-toggle-btn"><a class="nav-link" target="_self" href="javascript:;" aria-label="Color Toggle">&nbsp;<i class="iconfont icon-dark" id="color-toggle-icon"></i>&nbsp;</a></li>
      </ul>
    </div>
  </div>
</nav>
<div id="banner" class="banner" parallax=true style="background: url('/img/default.png') no-repeat center center; background-size: cover;">
  <div class="full-bg-img">
    <div class="mask flex-center" style="background-color: rgba(0, 0, 0, 0.3)">
      <div class="banner-text text-center fade-in-up">
        <div class="h2"><span id="subtitle" data-typed-text="404 - Page Not Found"></span></div>
        <div style="margin-top: 20px;"><a href="/" class="btn btn-outline-light">Back to Home</a></div>
      </div>
    </div>
  </div>
</div>
</div>
  </header>
  <main>
      <div class="container nopadding-x-md">
        <div id="board" style="margin-top: 0">
          <div class="container">
            <div class="row">
              <div class="col-12 col-md-10 m-auto">
                <div class="markdown-body text-center">
                  <h2>The page you're looking for doesn't exist.</h2>
                  <p>It may have been moved or deleted. Try searching or go back to the <a href="/">homepage</a>.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </main>
{get_footer()}
{get_scripts()}
"""
    return html


def generate_local_search_xml():
    """Generate local-search.xml for the search functionality."""
    entries = ""
    for article in ARTICLES:
        url = f"/{article['date'].replace('-', '/')}/{article['slug']}/"
        # Simple content for search
        content = article["excerpt"] + " " + article["title"] + " " + " ".join(article["tags"])
        # Escape XML
        content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', '&quot;').replace("'", "&apos;")
        title = article["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        entries += f"""<entry>
    <title>{title}</title>
    <url>{url}</url>
    <content>{content}</content>
  </entry>
  """

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<search>
  {entries}
</search>"""


def main():
    """Generate all pages."""
    site_dir = BASE_DIR

    # Generate index.html
    with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_index())
    print("Generated: index.html")

    # Generate about page
    os.makedirs(os.path.join(site_dir, "about"), exist_ok=True)
    with open(os.path.join(site_dir, "about", "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_about())
    print("Generated: about/index.html")

    # Generate archives page
    os.makedirs(os.path.join(site_dir, "archives"), exist_ok=True)
    with open(os.path.join(site_dir, "archives", "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_archives())
    print("Generated: archives/index.html")

    # Generate categories page
    os.makedirs(os.path.join(site_dir, "categories"), exist_ok=True)
    with open(os.path.join(site_dir, "categories", "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_categories())
    print("Generated: categories/index.html")

    # Generate tags page
    os.makedirs(os.path.join(site_dir, "tags"), exist_ok=True)
    with open(os.path.join(site_dir, "tags", "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_tags())
    print("Generated: tags/index.html")

    # Generate article pages
    for article in ARTICLES:
        article_dir = os.path.join(site_dir, article["date"].replace("-", "/"), article["slug"])
        os.makedirs(article_dir, exist_ok=True)
        with open(os.path.join(article_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(generate_article(article))
        print(f"Generated: {article_dir}/index.html")

    # Generate 404 page
    with open(os.path.join(site_dir, "404.html"), "w", encoding="utf-8") as f:
        f.write(generate_404())
    print("Generated: 404.html")

    # Generate local-search.xml
    with open(os.path.join(site_dir, "local-search.xml"), "w", encoding="utf-8") as f:
        f.write(generate_local_search_xml())
    print("Generated: local-search.xml")

    print(f"\nDone! Generated {len(ARTICLES)} articles + 6 static pages.")


if __name__ == "__main__":
    main()
