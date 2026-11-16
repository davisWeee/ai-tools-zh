# AI 翻译/字幕工具中文整合包导航

> 非官方镜像 / 使用指南（unofficial mirror/guide）；所有权利归原作者所有，详见 [NOTICE](NOTICE)。

站点：https://davisweee.github.io/ai-tools-zh/　·　数据核对日期：2026-11-14（GitHub API）

## 工具列表

### PDFMathTranslate (pdf2zh)

- **是什么**：保留公式与排版的 PDF 论文全文双语翻译，支持 Google / DeepL / Ollama / OpenAI 等翻译服务，提供命令行、图形界面、Docker。
- **适合谁**：读英文论文的学生、科研人员；需要把整本 PDF 翻成中文又不想破坏公式和图表的人。
- **Stars / 协议 / 最新版本**：38,408 / AGPL-3.0 / v1.9.11（2025-07-11）
- **注意**：该项目使用 AGPL-3.0 协议：若你再分发或提供网络服务，需遵守其源码公开义务。
- **三步使用**：
  1. 到官方 Releases 下载 Windows 压缩包（如 pdf2zh-v1.9.11-win64.zip）解压；或安装 Python 3.11–3.12 后执行 `pip install pdf2zh`。
  2. 运行 `pdf2zh -i` 打开网页界面（默认 7860 端口），上传 PDF。
  3. 选择翻译服务并填写所需 API Key（用免费服务则无需），点击翻译，得到中英双语 PDF。
- **下载**：
  - 网盘整合包：`https://github.com/davisWeee/ai-tools-zh/releases/download/packs-v1/pdf2zh-v1.9.11-win64.zip`（待填写）
  - 官方 GitHub：<https://github.com/PDFMathTranslate/PDFMathTranslate>（[Releases](https://github.com/PDFMathTranslate/PDFMathTranslate/releases/latest)）
- 网页版教程：[pdfmathtranslate.html](https://davisweee.github.io/ai-tools-zh/pdfmathtranslate.html)

### Buzz

- **是什么**：基于 OpenAI Whisper 的本地音视频转写与翻译桌面软件，离线运行，音视频文件不必上传到云端。
- **适合谁**：需要给会议录音、网课、播客、视频生成文字稿或字幕的普通用户。
- **Stars / 协议 / 最新版本**：22,739 / MIT / v1.4.5（2026-08-23）
- **三步使用**：
  1. 到官方 Releases 下载对应系统安装包（Windows 的 .exe、macOS 的 .dmg），安装并打开。
  2. 首次使用时选择并下载 Whisper 模型（模型越大越准确也越慢），导入音频或视频文件。
  3. 选择语言与任务（转写 / 翻译），开始处理，完成后导出 SRT、VTT 或 TXT。
- **下载**：
  - 网盘整合包：`{{QUARK_LINK_BUZZ}}`（待填写）
  - 官方 GitHub：<https://github.com/chidiwilliams/buzz>（[Releases](https://github.com/chidiwilliams/buzz/releases/latest)）
- 网页版教程：[buzz.html](https://davisweee.github.io/ai-tools-zh/buzz.html)

### SmartSub（妙幕）

- **是什么**：视频转字幕、字幕翻译、字幕烧录一站式桌面工具，用本地 Whisper / FunASR 等模型离线识别，支持批量处理。
- **适合谁**：做视频字幕、搬运翻译、需要批量处理视频的创作者；想要中文界面桌面工具的用户。
- **Stars / 协议 / 最新版本**：6,028 / MIT / v3.12.2（2026-11-05）
- **三步使用**：
  1. 到官方 Releases 下载对应系统安装包（Windows .exe、macOS .dmg、Linux AppImage/.deb）并安装。
  2. 在软件内选择语音识别模型，并在翻译设置里选择翻译服务、填写 API 信息。
  3. 拖入视频，选择源语言与目标语言，开始处理，导出字幕文件或烧录进视频。
- **下载**：
  - 网盘整合包：`https://github.com/davisWeee/ai-tools-zh/releases/download/packs-v1/SmartSub_Windows_3.12.2_x64.exe`（待填写）
  - 官方 GitHub：<https://github.com/buxuku/SmartSub>（[Releases](https://github.com/buxuku/SmartSub/releases/latest)）
- 网页版教程：[smartsub.html](https://davisweee.github.io/ai-tools-zh/smartsub.html)

### VideoLingo

- **是什么**：一键全自动的视频字幕切割、翻译、对齐，并可选配音的 AI 字幕工具，Streamlit 网页界面操作。
- **适合谁**：想把外语视频做成中文字幕或配音版本的创作者；愿意折腾一点环境配置的进阶用户。
- **Stars / 协议 / 最新版本**：19,240 / Apache-2.0 / v3.2.0（2026-11-13）
- **注意**：官方 Releases 未提供预编译安装包（经 API 核对，该版本无附件），需通过源码包运行，对网络和硬件要求较高，详见官方 README。
- **三步使用**：
  1. Windows：下载官方仓库源码包，解压后双击 `OneKeyStart.bat`，首次运行会自动安装 uv、Python、依赖与 FFmpeg（需联网）。也可用 Docker 部署。
  2. 浏览器打开 Streamlit 页面，在侧边栏填写大模型 API 与语音识别、目标语言等设置。
  3. 上传或粘贴视频链接，一键运行，得到字幕（及可选配音）视频。
- **下载**：
  - 网盘整合包：`{{QUARK_LINK_VIDEOLINGO}}`（待填写）
  - 官方 GitHub：<https://github.com/Huanshere/VideoLingo>（[Releases](https://github.com/Huanshere/VideoLingo/releases/latest)）
- 网页版教程：[videolingo.html](https://davisweee.github.io/ai-tools-zh/videolingo.html)

### comic-translate

- **是什么**：漫画 / 条漫翻译桌面软件，自动检测文字气泡、识别、翻译并回填，支持图片、PDF、EPUB、CBR、CBZ 等格式。
- **适合谁**：想看生肉漫画的读者、汉化与嵌字爱好者。
- **Stars / 协议 / 最新版本**：3,008 / Apache-2.0 / v3.0.3（2026-11-09）
- **三步使用**：
  1. 到官方 Releases 下载安装包（Windows 为 ct-3.0.3-win-setup.exe，macOS 为 ct-3.0.3-mac.dmg）并安装。
  2. 在设置里选择源语言、目标语言以及翻译服务（填写对应 API Key）。
  3. 导入漫画图片或压缩包，运行自动翻译，检查并微调后导出。
- **下载**：
  - 网盘整合包：`https://github.com/davisWeee/ai-tools-zh/releases/download/packs-v1/ct-3.0.3-win-setup.exe`（待填写）
  - 官方 GitHub：<https://github.com/ogkalu2/comic-translate>（[Releases](https://github.com/ogkalu2/comic-translate/releases/latest)）
- 网页版教程：[comic-translate.html](https://davisweee.github.io/ai-tools-zh/comic-translate.html)

## FAQ

**Q1. GitHub 下载太慢 / 打不开怎么办？**

优先使用本站每个工具页上的网盘链接（整合包上线后填入）；也可以换网络环境、使用下载工具续传。无论从哪里下载，建议与官方 Releases 页面的文件名和大小对照。

**Q2. 怎么配置翻译 API？**

在对应软件的「翻译 / 服务设置」里选择服务商，填入 API Key（部分需要填写 Base URL 与模型名），保存后用一小段文本测试。OpenAI 兼容接口通常只需 Base URL + Key + 模型名三项。API Key 属于个人密钥，不要发给他人，也不要提交到公开仓库。

**Q3. 免费翻译服务怎么选？**

三类思路：①软件内置的 Google / Bing 等免费网页接口，不用 Key 但可能限速、不稳定；②本地模型（如 Ollama），不花钱但吃显存和内存；③各大模型平台的免费额度或低价模型，额度和政策以平台官网当前说明为准。论文、术语多的内容建议用大模型，日常字幕用免费接口即可。

**Q4. 常见报错有哪些？**

①Connection / Timeout：网络或代理问题，检查网络并重试；②401 / 403：API Key 填错或无权限；③429：请求过快或额度用完，降低并发或换服务；④找不到 FFmpeg：安装 FFmpeg 并加入 PATH（VideoLingo 一键脚本会自动安装）；⑤CUDA / 显存不足：换小模型或改用 CPU；⑥macOS 提示无法验证开发者：在「系统设置 → 隐私与安全性」中选择仍要打开。仍无法解决请到对应项目的 GitHub Issues 搜索原文。

**Q5. 如何更新到新版本？**

桌面软件（Buzz、SmartSub、comic-translate）：下载新版安装包覆盖安装，设置一般会保留；pip 安装的 PDFMathTranslate：`pip install -U pdf2zh`；VideoLingo：重新下载源码包或在仓库目录执行 `git pull`。本站「最新版本」数据核对日期见各页，请以官方 Releases 为准。

## 声明

本仓库仅为中文导航与使用指南，不是任何所列项目的作者或官方渠道；软件版权与协议以原项目为准。
