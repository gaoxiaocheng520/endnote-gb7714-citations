---
name: endnote-gb7714-citations
description: Import cited literature into an EndNote library from Google Scholar EndNote exports, then replace document citations and format them in the requested GB/T 7714 style.
---

# EndNote GB/T 7714 citations

Convert a document's existing literature citations into real EndNote citations and a matching bibliography, using the user's target EndNote library and GB/T 7714 output style.

## Workflow

1. **Inspect the document, computer, and target.** If the repository's `scripts/inventory_docx.py` helper is available, run it to create a read-only inventory of numeric citation markers and numbered references. Review the report against the document because it cannot resolve bibliographic identity or every citation style. Identify every in-text citation, its location, and any corresponding bibliography entry. Detect the operating system, Word version, EndNote desktop version, active library, and whether Word's Cite While You Write (CWYW) add-in is available. Determine the required GB/T 7714 variant. Preserve citation order and meaning. Work on a copy by default; edit the original in place only when requested.

2. **Resolve each cited work.** Search Google Scholar using the exact title when available; otherwise search a distinctive title phrase plus known author or year. Open the candidate record and compare title, author list, year, venue, and DOI or other identifier against the document's reference list and available source. A similar title alone is not enough. If Scholar returns multiple plausible records, incomplete metadata, or no reliable match, leave that citation unresolved and report what is needed instead of importing a guess.

3. **Download and verify the EndNote citation.** For each verified Scholar record, use its **Cite** action and choose **EndNote** to download the citation file (commonly `.enw`). Keep a clear association between each downloaded file and the in-text citation it represents. Review the exported metadata before import; correct material errors against the document's reference list or reliable source details. Do not invent missing fields.

4. **Import by opening the downloaded file.** The agent performs this step. First make the intended EndNote library active. Then locate the exact downloaded `.enw` file in the browser's download list or the operating system's Downloads folder and open it by double-clicking it in Finder (macOS) or File Explorer (Windows). If the operating system asks which app to use, choose EndNote. Do not use EndNote's Import toolbar/menu for Google Scholar `.enw` files; this workflow relies on opening the downloaded file, which invokes EndNote's file handler. Do not ask the user to perform the click when the agent can operate the desktop.

   After opening the file, wait for EndNote to finish and verify the record appears in the intended library. Check its title, authors, year, and journal against the Scholar export and manuscript. Check for an existing matching record first. If a duplicate already exists, reuse the correct record instead of opening/importing the same export again. If an accidental duplicate was created, keep the record used by the document and move the unused duplicate to EndNote's recoverable Trash only after confirming it is not cited elsewhere.

5. **Replace citations through EndNote.** In Word, use the installed CWYW search/insert command to add the verified library record at the corresponding citation location. Remove the old manually typed citation marker only after the EndNote citation is in place. Preserve the sentence, punctuation, citation grouping, and original citation order. Do not type citation numbers or a bibliography by hand, and do not convert citation fields to plain text during editing.

   Prefer Word's EndNote **Insert Citation / Find & Insert** command when available. If that route is absent in the detected version, use the available CWYW equivalent or **Go to EndNote**, select the verified record, and activate EndNote's **Insert Citation** command. Find commands by their function in the actual UI; ribbon tabs, translated labels, menus, dialogs, and control locations vary by Word/EndNote release and operating system. Do not rely on fixed screen coordinates or assume one ribbon layout. Before inserting, verify the selected result's author, title, and year in the result/details pane. For multi-source groups, insert each verified record at the same citation location and confirm Word combines them into one grouped citation.

6. **Apply and refresh the style.** In the detected Word/CWYW interface, select the requested GB/T 7714 numeric style, including superscript behavior if requested, then use the available **Update Citations and Bibliography** command. Style names and dropdown locations can vary. Use an installed style that matches the requested variant; do not manually alter generated citation fields to imitate a style.

7. **Review the result.** Check that every original citation is represented by a live EndNote field, each field resolves to the intended library record, in-text numbering follows the selected style, and the generated bibliography contains the cited records with correct metadata. Check that no old manual markers or duplicate bibliography entries remain and that nearby text and punctuation are intact. Save the converted document and library, and report the library used, style used, output file, and any unresolved citations or metadata issues.

## Version and platform compatibility

- Adapt to the installed applications rather than assuming a single version. At the start, identify macOS or Windows, the Word release, the EndNote release, and whether desktop CWYW is active. Use the controls actually exposed in that installation; names and placement can differ between releases, languages, and platforms.
- For EndNote 2025, Clarivate documents CWYW for Word 2010, 2013, 2016, 2019, 2021, and Microsoft 365 on Windows, and Word 2016, 2019, 2021, and Microsoft 365 desktop on macOS. Treat these as the EndNote 2025 compatibility lists, not as a guarantee for every EndNote release or Word build. For another EndNote release, follow that release's current Clarivate compatibility documentation.
- Word for the web, desktop Word, and Google Docs do not all preserve the same EndNote citation encoding. Keep CWYW citation insertion and updating in a compatible Word environment. If a document has been edited in an incompatible editor and its fields no longer resolve, do not claim the citations remain live.
- If CWYW is missing or the detected app combination cannot insert and update EndNote fields, make reasonable UI checks for the add-in and report the exact limitation. Do not fake EndNote fields or silently replace them with plain text. Do not make the user click the downloaded file when the agent has desktop control; if desktop control is unavailable, explain that specific blocker.

## Operating rules

- Use the user's existing EndNote library when specified. Never silently import into a different library.
- Google Scholar provides candidate records and export files; verify their metadata against the document before relying on them.
- Preserve the document's wording and citation placement. Change citation apparatus and generated bibliography only, except for metadata corrections needed in the EndNote records.
- Keep EndNote/CWYW fields editable so users can later change styles or update references.
- When a CWYW search returns no exact match, an ambiguous result, or a stale previously selected record, stop and resolve the record before inserting; never treat a successful button click as proof of a correct citation.
- If a compatible CWYW environment is unavailable, explain the limitation and produce only the compatible result the user requested; do not claim it contains live EndNote citations when it does not.
- Summarize unresolved citations explicitly. Do not silently omit, fabricate, or substitute a source.

## Official compatibility references

- [EndNote 2025 Word processor compatibility](https://docs.endnote.com/docs/endnote/2025/windows/v1/content/09word/word_processor_comptblty.htm)
- [Installing CWYW in Word for macOS](https://docs.endnote.com/docs/endnote/2025/v1/macos/en/content/09word/installing_cwywsprtinword.htm)
- [EndNote 2025/21 Word and Google Docs citation compatibility](https://supportcenter.clarivate.com/s/article/EndNote-21-Google-Docs-and-Microsoft-Word-citations-compatibility?language=en_US)
