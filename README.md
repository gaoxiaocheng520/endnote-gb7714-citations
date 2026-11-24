# EndNote GB/T 7714 Citation Workflow

A local workflow project for turning manually typed numbered citations in a Word manuscript into live, editable EndNote Cite While You Write (CWYW) citations, then generating a GB/T 7714 bibliography.

This repository contains a read-only DOCX citation inventory tool and the EndNote/Word workflow instructions. It does not upload manuscripts or libraries to a server.

## Requirements

- Python 3.9 or later for the inventory script
- Microsoft Word with the EndNote Cite While You Write add-in
- EndNote desktop with the target library and requested GB/T 7714 style
- A Codex agent that can interact with the local Word and EndNote apps for the assisted workflow

## Quick start

Clone this repository, then inventory a manuscript:

```bash
python3 scripts/inventory_docx.py /path/to/manuscript.docx --output citation-inventory.json
```

The JSON report lists bracketed numeric citation groups, numbered reference entries, and numbers that could not be matched to an entry. The script only reads the DOCX; it never changes it.

To perform the conversion, open a copy of the manuscript in Word and the intended EndNote library. Follow [SKILL.md](SKILL.md):

1. Match each reference against the document's bibliography and, when needed, Google Scholar. Download the Scholar EndNote citation export and import it into the intended library, checking for duplicates.
2. At each original marker, insert the verified library record through Word's EndNote **Find & Insert Citation** command, or use **Go to EndNote**, select the record, and click EndNote's **Insert Citation** button.
3. Confirm each selected record by author, title, and year before inserting. Keep grouped sources in one citation field.
4. Select the requested GB/T 7714 numeric style and run **Update Citations and Bibliography** in Word.
5. Verify the live citation fields and generated bibliography. Save the converted copy.

The workflow never fabricates CWYW fields or types citation numbers and bibliography entries by hand. A public web server cannot create live fields in a user's local Word document; the final insertion runs locally through Word and EndNote.

## Limitations

The inventory script recognizes bracketed numeric citations such as `[2]`, `[2, 4]`, and `[2-4]`, plus numbered reference entries such as `[2] ...` or `2. ...`. It is a review aid, not a bibliographic matcher. Author-date citations, footnotes, tables with unusual structures, and unnumbered bibliographies may need manual review.

## 中文说明

本项目用于把 Word 论文中手打的数字引用，转换为真正可编辑、可更新的 EndNote CWYW 引文，并由 EndNote 按 GB/T 7714 生成文末书目。

项目含有只读 DOCX 引用清单提取脚本和 Word/EndNote 操作流程。文件始终在本机处理，不上传论文或文献库。最终可点击、可更新的引文域必须通过本机安装的 Word EndNote 插件插入；网页服务器不能代替本机 CWYW。

先运行清单脚本，再按照 [SKILL.md](SKILL.md) 核对文献、通过 Google Scholar 下载 EndNote 格式并导入目标库、在 Word 中插入引文、选择 GB/T 7714 样式并更新书目。每条记录都要核对作者、标题和年份。脚本只做引用盘点，不修改原文，也不负责猜测或替代文献信息。
