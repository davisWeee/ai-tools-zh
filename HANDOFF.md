# HANDOFF — ai-tools-zh（opp-41 工具导航站）

- Repo: https://github.com/davisWeee/ai-tools-zh
- Pages: https://davisweee.github.io/ai-tools-zh/ （source: main /docs）
- 本地目录: workspace/experiments/opp-41-tool-mirror/site/
- 生成: `python3 build.py` 重新生成 README.md 与 docs/*.html（事实数据在 build.py 的 TOOLS，核对日期 2026-11-14，来自 gh api）
- 统计: GoatCounter 站点 venture-xinghe（与 xinghe-cinema.surge.sh 共用），页面浏览路径前缀 `ai-tools-zh/`，外链点击事件 `ai-tools-zh/click/<host>`。

## 待填占位符（网盘夸克链接）
{{QUARK_LINK_PDFMATHTRANSLATE}} {{QUARK_LINK_BUZZ}} {{QUARK_LINK_SMARTSUB}} {{QUARK_LINK_VIDEOLINGO}} {{QUARK_LINK_COMIC_TRANSLATE}}
填法：写 links.json（`{"BUZZ":"https://pan.quark.cn/s/..."}`），`python3 fill_links.py links.json`，然后 git commit/push。
注意：build.py 会重新生成占位符；填完链接后不要再跑 build.py（或先把链接写进 build.py）。
未填时，页面点击占位链接会提示"整理中，请用官方 GitHub"。

## 注意事项
- 整合包由另一 agent 在 experiments/opp-41-tool-mirror/packs/ 准备；上传网盘前保留各项目 LICENSE（PDFMathTranslate 为 AGPL-3.0，再分发需遵守源码公开义务）。
- VideoLingo 官方 Release 无附件，页面已注明需源码包 + OneKeyStart.bat。
- 未写任何收益相关表述。
- 后续：到 Google Search Console / Bing 提交 sitemap（docs/sitemap.xml）；GitHub 仓库可补 topics。
