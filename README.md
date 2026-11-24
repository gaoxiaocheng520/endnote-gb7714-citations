# EndNote GB/T 7714 Citation Workflow

A local workflow project for turning manually typed numbered citations in a Word manuscript into live, editable EndNote Cite While You Write (CWYW) citations, then generating a GB/T 7714 bibliography.

This repository contains a read-only DOCX citation inventory tool and the EndNote/Word workflow instructions. Manuscripts and EndNote libraries stay on the user's computer and are not uploaded by this project.

## Requirements

- Python 3.9 or later for the inventory script
- A compatible desktop version of Microsoft Word with the EndNote Cite While You Write add-in
- EndNote desktop with the target library and requested GB/T 7714 style
- A Codex agent with browser and desktop UI access for the assisted workflow

## Quick start

Clone this repository. To let Codex perform the complete assisted workflow, copy the repository folder into your Codex skills directory (`$CODEX_HOME/skills`, or `~/.codex/skills` when `CODEX_HOME` is unset), then start a new Codex task and ask it to use `endnote-gb7714-citations`.

Inventory a manuscript with:

```bash
python3 scripts/inventory_docx.py /path/to/manuscript.docx --output citation-inventory.json
```

The JSON report lists bracketed numeric citation groups, numbered reference entries, and numbers that could not be matched to an entry. The script only reads the DOCX; it never changes it.

## Assisted conversion workflow

Follow [SKILL.md](SKILL.md). The agent:

1. Reviews a copy of the manuscript and inventories its citations and reference list.
2. Matches each reference against Google Scholar and downloads the verified EndNote citation file.
3. Opens the intended EndNote library, locates the downloaded `.enw` file, and double-clicks it in Finder (macOS) or File Explorer (Windows). This opens the file with EndNote. The agent performs the click and verifies the imported record; it does not ask the user to click or use EndNote's Import toolbar/menu for this file.
4. Inserts each verified record at the original citation location using Word's installed EndNote CWYW controls.
5. Selects the requested GB/T 7714 style, updates the citations and bibliography, reviews the live fields, and saves the document.

The workflow adapts to the visible UI and capabilities of the installed Word and EndNote releases. EndNote 2025's documented Word compatibility differs between Windows and macOS; see the official [Windows compatibility list](https://docs.endnote.com/docs/endnote/2025/windows/v1/content/09word/word_processor_comptblty.htm) and [macOS CWYW installation notes](https://docs.endnote.com/docs/endnote/2025/v1/macos/en/content/09word/installing_cwywsprtinword.htm). These lists apply to EndNote 2025; check Clarivate's documentation for other EndNote releases. If CWYW is unavailable in the user's installed combination, the agent reports that limitation rather than pretending plain-text citations are live EndNote fields.

The workflow never fabricates CWYW fields or types citation numbers and bibliography entries by hand. A public web server cannot create live fields in a user's local Word document; the final insertion runs locally through Word and EndNote.

## Limitations

The inventory script recognizes bracketed numeric citations such as `[2]`, `[2, 4]`, and `[2-4]`, plus numbered reference entries such as `[2] ...` or `2. ...`. It is a review aid, not a bibliographic matcher. Author-date citations, footnotes, tables with unusual structures, and unnumbered bibliographies may need manual review.

EndNote field codes should be inserted and updated in a compatible Word environment. Word desktop, Word for the web, and Google Docs may handle EndNote field codes differently; switching editors can break citation links. For cross-platform editing, use a Word version that EndNote documents as compatible with the installed EndNote release.

## 中文说明

本项目用于把 Word 论文中手打的数字引用，转换为真正可编辑、可更新的 EndNote CWYW 引文，并由 EndNote 按 GB/T 7714 生成文末书目。

项目含有只读 DOCX 引用清单提取脚本和 Word/EndNote 操作流程。论文和文献库都保留在用户本机，不会由本项目上传。转换时，agent 会通过 Google Scholar 核对文献并下载 EndNote 格式文件，然后先打开指定文库，再在 macOS 的 Finder 或 Windows 文件资源管理器中双击下载的 `.enw` 文件，由 EndNote 接收导入。agent 会核对导入结果，不会要求用户点击，也不使用 EndNote 的 Import 工具栏/菜单导入此文件。

Word 和 EndNote 不同版本的选项卡、菜单名和位置会变化。agent 会先识别系统和应用版本，再根据实际可用的 CWYW 插入、更新功能操作，而不依赖固定坐标或固定界面布局。EndNote 2025 在 Windows 与 macOS 上公布的 Word 兼容范围不同；其他 EndNote 版本应以 Clarivate 对该版本的说明为准。如果当前组合无法插入可更新的 CWYW 引文域，agent 会说明具体限制，不会伪造普通文本引文为 EndNote 引文。

[查看兼容性说明](https://docs.endnote.com/docs/endnote/2025/windows/v1/content/09word/word_processor_comptblty.htm) · [macOS 安装 CWYW](https://docs.endnote.com/docs/endnote/2025/v1/macos/en/content/09word/installing_cwywsprtinword.htm)
