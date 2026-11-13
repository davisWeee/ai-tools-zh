#!/usr/bin/env python3
"""Generate README.md + docs/*.html. Facts verified via `gh api` on 2026-11-14."""
import html, os
GC = "https://venture-xinghe.goatcounter.com/count"   # same GoatCounter site as xinghe-cinema.surge.sh
VERIFIED = "2026-11-14"
REPO = "https://github.com/davisWeee/ai-tools-zh"
SITE = "https://davisweee.github.io/ai-tools-zh/"

TOOLS = [
 dict(slug="pdfmathtranslate", name="PDFMathTranslate (pdf2zh)", token="PDFMATHTRANSLATE",
  repo="PDFMathTranslate/PDFMathTranslate", stars="38,408", lic="AGPL-3.0", ver="v1.9.11", date="2025-07-11",
  home="https://pdf2zh.com",
  what="保留公式与排版的 PDF 论文全文双语翻译，支持 Google / DeepL / Ollama / OpenAI 等翻译服务，提供命令行、图形界面、Docker。",
  who="读英文论文的学生、科研人员；需要把整本 PDF 翻成中文又不想破坏公式和图表的人。",
  steps=["到官方 Releases 下载 Windows 压缩包（如 pdf2zh-v1.9.11-win64.zip）解压；或安装 Python 3.11–3.12 后执行 <code>pip install pdf2zh</code>。",
         "运行 <code>pdf2zh -i</code> 打开网页界面（默认 7860 端口），上传 PDF。",
         "选择翻译服务并填写所需 API Key（用免费服务则无需），点击翻译，得到中英双语 PDF。"],
  kw="PDFMathTranslate pdf2zh PDF翻译 论文翻译 保留公式排版 下载 整合包 使用教程",
  note="该项目使用 AGPL-3.0 协议：若你再分发或提供网络服务，需遵守其源码公开义务。"),
 dict(slug="buzz", name="Buzz", token="BUZZ",
  repo="chidiwilliams/buzz", stars="22,739", lic="MIT", ver="v1.4.5", date="2026-08-23",
  home="https://chidiwilliams.github.io/buzz",
  what="基于 OpenAI Whisper 的本地音视频转写与翻译桌面软件，离线运行，音视频文件不必上传到云端。",
  who="需要给会议录音、网课、播客、视频生成文字稿或字幕的普通用户。",
  steps=["到官方 Releases 下载对应系统安装包（Windows 的 .exe、macOS 的 .dmg），安装并打开。",
         "首次使用时选择并下载 Whisper 模型（模型越大越准确也越慢），导入音频或视频文件。",
         "选择语言与任务（转写 / 翻译），开始处理，完成后导出 SRT、VTT 或 TXT。"],
  kw="Buzz Whisper 音频转文字 视频字幕 离线语音识别 下载 整合包 使用教程",
  note=""),
 dict(slug="smartsub", name="SmartSub（妙幕）", token="SMARTSUB",
  repo="buxuku/SmartSub", stars="6,028", lic="MIT", ver="v3.12.2", date="2026-11-05",
  home="https://smartsub.linxiaodong.com/",
  what="视频转字幕、字幕翻译、字幕烧录一站式桌面工具，用本地 Whisper / FunASR 等模型离线识别，支持批量处理。",
  who="做视频字幕、搬运翻译、需要批量处理视频的创作者；想要中文界面桌面工具的用户。",
  steps=["到官方 Releases 下载对应系统安装包（Windows .exe、macOS .dmg、Linux AppImage/.deb）并安装。",
         "在软件内选择语音识别模型，并在翻译设置里选择翻译服务、填写 API 信息。",
         "拖入视频，选择源语言与目标语言，开始处理，导出字幕文件或烧录进视频。"],
  kw="SmartSub 妙幕 视频转字幕 字幕翻译 批量 下载 整合包 使用教程",
  note=""),
 dict(slug="videolingo", name="VideoLingo", token="VIDEOLINGO",
  repo="Huanshere/VideoLingo", stars="19,240", lic="Apache-2.0", ver="v3.2.0", date="2026-11-13",
  home="https://docs.videolingo.io",
  what="一键全自动的视频字幕切割、翻译、对齐，并可选配音的 AI 字幕工具，Streamlit 网页界面操作。",
  who="想把外语视频做成中文字幕或配音版本的创作者；愿意折腾一点环境配置的进阶用户。",
  steps=["Windows：下载官方仓库源码包，解压后双击 <code>OneKeyStart.bat</code>，首次运行会自动安装 uv、Python、依赖与 FFmpeg（需联网）。也可用 Docker 部署。",
         "浏览器打开 Streamlit 页面，在侧边栏填写大模型 API 与语音识别、目标语言等设置。",
         "上传或粘贴视频链接，一键运行，得到字幕（及可选配音）视频。"],
  kw="VideoLingo 视频翻译 字幕组 AI配音 一键字幕 下载 整合包 使用教程",
  note="官方 Releases 未提供预编译安装包（经 API 核对，该版本无附件），需通过源码包运行，对网络和硬件要求较高，详见官方 README。"),
 dict(slug="comic-translate", name="comic-translate", token="COMIC_TRANSLATE",
  repo="ogkalu2/comic-translate", stars="3,008", lic="Apache-2.0", ver="v3.0.3", date="2026-11-09",
  home="https://comic-translate.com",
  what="漫画 / 条漫翻译桌面软件，自动检测文字气泡、识别、翻译并回填，支持图片、PDF、EPUB、CBR、CBZ 等格式。",
  who="想看生肉漫画的读者、汉化与嵌字爱好者。",
  steps=["到官方 Releases 下载安装包（Windows 为 ct-3.0.3-win-setup.exe，macOS 为 ct-3.0.3-mac.dmg）并安装。",
         "在设置里选择源语言、目标语言以及翻译服务（填写对应 API Key）。",
         "导入漫画图片或压缩包，运行自动翻译，检查并微调后导出。"],
  kw="comic-translate 漫画翻译 manga 生肉 自动嵌字 下载 整合包 使用教程",
  note=""),
]

FAQ = [
 ("GitHub 下载太慢 / 打不开怎么办？",
  "优先使用本站每个工具页上的网盘链接（整合包上线后填入）；也可以换网络环境、使用下载工具续传。无论从哪里下载，建议与官方 Releases 页面的文件名和大小对照。"),
 ("怎么配置翻译 API？",
  "在对应软件的「翻译 / 服务设置」里选择服务商，填入 API Key（部分需要填写 Base URL 与模型名），保存后用一小段文本测试。OpenAI 兼容接口通常只需 Base URL + Key + 模型名三项。API Key 属于个人密钥，不要发给他人，也不要提交到公开仓库。"),
 ("免费翻译服务怎么选？",
  "三类思路：①软件内置的 Google / Bing 等免费网页接口，不用 Key 但可能限速、不稳定；②本地模型（如 Ollama），不花钱但吃显存和内存；③各大模型平台的免费额度或低价模型，额度和政策以平台官网当前说明为准。论文、术语多的内容建议用大模型，日常字幕用免费接口即可。"),
 ("常见报错有哪些？",
  "①Connection / Timeout：网络或代理问题，检查网络并重试；②401 / 403：API Key 填错或无权限；③429：请求过快或额度用完，降低并发或换服务；④找不到 FFmpeg：安装 FFmpeg 并加入 PATH（VideoLingo 一键脚本会自动安装）；⑤CUDA / 显存不足：换小模型或改用 CPU；⑥macOS 提示无法验证开发者：在「系统设置 → 隐私与安全性」中选择仍要打开。仍无法解决请到对应项目的 GitHub Issues 搜索原文。"),
 ("如何更新到新版本？",
  "桌面软件（Buzz、SmartSub、comic-translate）：下载新版安装包覆盖安装，设置一般会保留；pip 安装的 PDFMathTranslate：<code>pip install -U pdf2zh</code>；VideoLingo：重新下载源码包或在仓库目录执行 <code>git pull</code>。本站「最新版本」数据核对日期见各页，请以官方 Releases 为准。"),
]

CSS = ("body{font:16px/1.7 -apple-system,'PingFang SC','Microsoft YaHei',sans-serif;max-width:860px;margin:0 auto;padding:16px;color:#222}"
 "a{color:#0b63ce}h1{font-size:1.6em}h2{margin-top:1.6em;border-left:4px solid #0b63ce;padding-left:8px}"
 "table{border-collapse:collapse;width:100%}td,th{border:1px solid #ddd;padding:6px 8px;text-align:left}"
 ".dl{display:block;padding:10px 12px;background:#f2f7ff;border:1px dashed #0b63ce;border-radius:6px;word-break:break-all}"
 "code{background:#f4f4f4;padding:1px 4px;border-radius:3px}footer{margin-top:2em;color:#666;font-size:.9em;border-top:1px solid #ddd;padding-top:1em}"
 "details{margin:.6em 0}summary{cursor:pointer;font-weight:600}")

SNIP = """<script>(function(){var B='%s',P='ai-tools-zh';
function ping(p,t,r){new Image().src=B+'?p='+encodeURIComponent(p)+(t?'&e=true&t='+encodeURIComponent(t):'')+'&r='+encodeURIComponent(r||'')+'&rnd='+Math.random();}
var path=location.pathname.replace(/\\/$/,'')||'/';ping(P+path,'',document.referrer);
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'';
if(h.indexOf('{{')===0){e.preventDefault();alert('该整合包网盘链接整理中，请先使用「官方 GitHub」链接下载。');return;}
if(/^https?:\\/\\//.test(h)&&h.indexOf(location.host)<0){var host=h.replace(/^https?:\\/\\//,'').split('/').slice(0,3).join('/');ping(P+'/click/'+host,'click '+host,path);}},true);})();</script>""" % GC

def page(title, desc, kw, body, canon):
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="keywords" content="{html.escape(kw)}">
<link rel="canonical" href="{SITE}{canon}">
<style>{CSS}</style></head><body>
<nav><a href="index.html">首页</a> · <a href="{REPO}">GitHub 仓库</a></nav>
{body}
<footer><p>非官方镜像 / 使用指南（unofficial mirror/guide）；所有软件的权利归原作者所有，本站不是任何一个项目的作者或官方站点。见 <a href="{REPO}/blob/main/NOTICE">NOTICE</a>。</p>
<p>数据核对日期：{VERIFIED}（来自 GitHub API）。</p></footer>
{SNIP}</body></html>"""

def tool_page(t):
    gh = f"https://github.com/{t['repo']}"
    ph = "{{QUARK_LINK_%s}}" % t["token"]
    steps = "".join(f"<li>{s}</li>" for s in t["steps"])
    note = f"<p><strong>注意：</strong>{t['note']}</p>" if t["note"] else ""
    body = f"""<h1>{html.escape(t['name'])} 下载 整合包 使用教程</h1>
<p>{t['what']}</p>
<table><tr><th>适合人群</th><td>{t['who']}</td></tr>
<tr><th>GitHub Stars</th><td>{t['stars']}（{VERIFIED} 核对）</td></tr>
<tr><th>开源协议</th><td>{t['lic']}</td></tr>
<tr><th>最新版本</th><td>{t['ver']}（发布于 {t['date']}）</td></tr>
<tr><th>官方网站</th><td><a href="{t['home']}" rel="noopener">{t['home']}</a></td></tr></table>
{note}
<h2>三步上手</h2><ol>{steps}</ol>
<h2>下载</h2>
<p>网盘整合包（国内网络友好）：</p>
<a class="dl" href="{ph}">{ph}</a>
<p>官方 GitHub（始终以此为准）：<a href="{gh}/releases/latest" rel="noopener">{gh}/releases/latest</a> · 项目主页 <a href="{gh}" rel="noopener">{gh}</a></p>
<h2>常见问题</h2>
<p>下载慢、API 配置、免费翻译选择、常见报错、更新方法见 <a href="index.html#faq">首页 FAQ</a>。</p>"""
    return page(f"{t['name']} 下载 整合包 使用教程｜AI 翻译/字幕工具中文导航",
                f"{t['name']} 中文使用教程与下载：{t['what']}", t["kw"], body, f"{t['slug']}.html")

def index():
    rows = "".join(f"<tr><td><a href=\"{t['slug']}.html\">{html.escape(t['name'])}</a></td><td>{t['what']}</td><td>{t['stars']}</td><td>{t['lic']}</td><td>{t['ver']}</td></tr>" for t in TOOLS)
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    body = f"""<h1>AI 翻译 / 字幕工具中文整合包导航</h1>
<p>收录热门开源的 PDF 论文翻译、语音转字幕、视频翻译、漫画翻译工具，提供中文使用教程、官方 GitHub 链接和（准备中的）网盘整合包入口。</p>
<table><tr><th>工具</th><th>简介</th><th>Stars</th><th>协议</th><th>最新版</th></tr>{rows}</table>
<p>数据核对日期 {VERIFIED}，来自 GitHub API。</p>
<h2 id="faq">常见问题 FAQ</h2>{faq}"""
    return page("AI 翻译/字幕工具中文整合包导航｜PDF翻译 视频字幕 漫画翻译 下载 使用教程",
                "AI 翻译与字幕开源工具中文导航：PDFMathTranslate、Buzz、SmartSub、VideoLingo、comic-translate 下载、整合包、使用教程与 FAQ。",
                "AI翻译工具 字幕工具 整合包 下载 使用教程 PDF翻译 视频翻译 漫画翻译 Whisper", body, "")

def readme():
    out = ["# AI 翻译/字幕工具中文整合包导航\n",
           f"> 非官方镜像 / 使用指南（unofficial mirror/guide）；所有权利归原作者所有，详见 [NOTICE](NOTICE)。\n",
           f"站点：{SITE}　·　数据核对日期：{VERIFIED}（GitHub API）\n",
           "## 工具列表\n"]
    for t in TOOLS:
        gh = f"https://github.com/{t['repo']}"
        out.append(f"### {t['name']}\n")
        out.append(f"- **是什么**：{t['what']}")
        out.append(f"- **适合谁**：{t['who']}")
        out.append(f"- **Stars / 协议 / 最新版本**：{t['stars']} / {t['lic']} / {t['ver']}（{t['date']}）")
        if t["note"]: out.append(f"- **注意**：{t['note']}")
        out.append("- **三步使用**：")
        import re
        for i, s in enumerate(t["steps"], 1):
            out.append(f"  {i}. {re.sub('<[^>]+>', '`', s).replace('``','`')}")
        out.append("- **下载**：")
        out.append("  - 网盘整合包：`{{QUARK_LINK_%s}}`（待填写）" % t["token"])
        out.append(f"  - 官方 GitHub：<{gh}>（[Releases]({gh}/releases/latest)）")
        out.append(f"- 网页版教程：[{t['slug']}.html]({SITE}{t['slug']}.html)\n")
    out.append("## FAQ\n")
    for i, (q, a) in enumerate(FAQ, 1):
        out.append(f"**Q{i}. {q}**\n\n{re.sub('<[^>]+>', '`', a).replace('``','`')}\n")
    out.append("## 声明\n\n本仓库仅为中文导航与使用指南，不是任何所列项目的作者或官方渠道；软件版权与协议以原项目为准。")
    return "\n".join(out) + "\n"

os.makedirs("docs", exist_ok=True)
open("docs/index.html", "w").write(index())
for t in TOOLS: open(f"docs/{t['slug']}.html", "w").write(tool_page(t))
open("README.md", "w").write(readme())
open("docs/.nojekyll", "w").write("")
open("docs/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
urls = [""] + [t["slug"] + ".html" for t in TOOLS]
open("docs/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
