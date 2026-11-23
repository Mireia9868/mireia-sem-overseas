# mireiasem.com 构建与发布说明

本站在 GitHub Pages 上运行，HTML 是预先生成的静态文件。本文说明如何正确新增文章和发布，避免历史上出现过的「Cookie 横幅遗漏、OG 图失效、广告属性废弃」问题。

## 核心原则

**数据源是 `article_meta.json`（55 篇文章的完整元数据）。** 新增或修改文章，先改数据源，再生成，最后跑全局优化脚本。任何直接手改 HTML 的做法都会在下次生成时被覆盖。

## 标准发布流程

### 1. 新增文章
- 在 `article_meta.json` 追加一条记录（slug / date / title / category / tags / excerpt 必填）。
- category 只能是这 5 个之一：`Ad Channels`、`Channel Policies`、`Conversion Tracking`、`Tools & Tips`、`SEM`。
- tags 统一规则：**URL 用连字符**（如 `/tags/Google-Ads/`），**显示文本用 `#` + 空格自然词**（如 `#Google Ads`）。不要混用 `#Google-Ads` 与 `#Google Ads`。
- excerpt 写完整句子（120–160 字符），**不要手动截断**——截断由脚本按完整单词处理。

### 2. 生成页面
按实际需要运行对应脚本（历史脚本职责有重叠，新增内容优先改数据源后重新生成）：
- `generate_batch_articles.py` —— 批量生成文章页
- `regenerate_site.py` —— 重建首页 / 归档 / 分类 / 标签页
- `inject_ga4.py` —— 给缺失页面补 GA4（幂等，可重复跑）

### 3. 全局优化（发布前必跑）
```bash
python3 tools_optimize_site.py
```
这是**唯一的全局 SEO / 合规配置入口**，负责统一处理：
- P0-1 Cookie 同意横幅（CSS + JS + 合规文案）
- P0-2 社交分享图 og:image / twitter:image（指向 `img/og-cover.png`）+ 宽高
- P0-3 广告单元：移除废弃的 `data-ad-layout`，单页广告数 ≤ 4
- P1-2 分类回填（按 `article_meta.json` 的 category）
- P1-4 摘要按完整单词截断
- P2-1 图标字体本地托管（`/css/fonts/`）
- P2-3 sitemap 日期格式统一

该脚本**幂等**：重复运行不会重复注入或破坏结构。可用 `--check` 只体检不修改：
```bash
python3 tools_optimize_site.py --check
```

### 4. 验证
```bash
python3 tools_optimize_site.py --check   # 应输出「发现 0 项待修」
```

### 5. 提交发布
```bash
git add -A && git commit -m "..." && git push
```
GitHub Pages 自动部署，通常 1–2 分钟生效。

## 需要人工处理的事项

- **文章配图**（P1-1）：目前 55 篇文章正文均无配图。新增文章时每篇至少补 2 张图（一张结构/流程示意图，一张产品后台真实截图），存入 `img/posts/<slug>/`，并填写描述性 `alt`。真实产品截图无法自动生成，需人工提供。
- **内容更新节奏**（P2-4）：目标每月 2 篇，优先覆盖平台政策更新、追踪配置、新广告类型等搜索意图明确的话题。

## 历史脚本说明

以下脚本为一次性修补性质，日常发布无需运行，保留仅供追溯：
`fix_adsense_issues.py`、`add_links_to_existing.py`、`update_listings.py`、`articles_data_batch1.py`、`articles_data_batch2.py`、`generate_site.py`。

> `generate_site.py` 是早期文章数据文件（约 100 KB），不是 HTML 生成器；不要把它当作主入口。
