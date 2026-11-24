---
name: endnote-gb7714-citations
description: Import cited literature into an EndNote library from Google Scholar EndNote exports, then replace document citations and format them in the requested GB/T 7714 style.
---

# EndNote GB/T 7714 citations

Convert a document's existing literature citations into real EndNote citations and a matching bibliography, using the user's target EndNote library and GB/T 7714 output style.

## Workflow

1. **Inspect the document and target.** Identify every in-text citation, its location, and any corresponding bibliography entry. Determine the intended EndNote library and the document's required GB/T 7714 variant (for example, numeric or author-date, and any institution or journal requirements). Preserve citation order and meaning. If the target library or required style is unclear, ask only for the missing choice. Work on a copy by default; edit the original in place only when requested.

2. **Resolve each cited work.** Search Google Scholar using the exact title when available; otherwise search a distinctive title phrase plus known author or year. Open the candidate record and compare title, author list, year, venue, and DOI or other identifier against the document's reference list and available source. A similar title alone is not enough. If Scholar returns multiple plausible records, incomplete metadata, or no reliable match, leave that citation unresolved and report what is needed instead of importing a guess.

3. **Download the EndNote citation.** For each verified Scholar record, use its **Cite** action and choose **EndNote** to download the citation file (commonly `.enw`). Keep a clear association between each downloaded file and the in-text citation it represents. Review the exported metadata before import; correct material errors against the document's reference list or reliable source details. Do not invent missing fields.

4. **Import into the intended library.** In EndNote, select the user's target library and import each downloaded citation file using the EndNote import option/filter. Check duplicate detection before adding records. Reuse a matching existing record where appropriate; avoid creating duplicate records merely because a Scholar export differs slightly. Confirm the imported record's bibliographic fields and DOI, if present.

5. **Replace citations through EndNote.** In the document editor, use EndNote's Cite While You Write (CWYW) search/insert command to insert the imported library records at the corresponding citation locations. Remove the old manually typed citation marker only after the EndNote citation is in place. Preserve the sentence, punctuation, citation grouping, and original citation order. Do not type citation numbers or a bibliography by hand, and do not convert citation fields to plain text during editing.

   In Word, either use **EndNote > Insert Citation > Find & Insert** or place the cursor at the marker, choose **Go to EndNote**, select the matching library record, and use EndNote's **Insert Citation** toolbar button. Both routes must create a CWYW field. Before inserting, verify the selected result's author, title, and year in the result/details pane; a matching search string alone is not proof that the right record is selected. For multi-source citation groups, insert each verified record at the same citation location and confirm Word combines them into one grouped citation.

6. **Apply and refresh the style.** Set the document's bibliography/output style to the required GB/T 7714 style available in EndNote, then use CWYW to update/format citations and bibliography. Honor the requested variant and superscript requirement; GB/T 7714 style files can differ in numbering, punctuation, author truncation, and superscript behavior. If the needed style is absent, locate or install an appropriate EndNote style only when available and appropriate, then select it in the document. Do not manually alter generated citation fields to imitate a style.

7. **Review the result.** Check that every original citation is represented by a live EndNote field, each field resolves to the intended library record, in-text numbering follows the selected style, and the generated bibliography contains the cited records with correct metadata. Check that no old manual markers or duplicate bibliography entries remain and that nearby text and punctuation are intact. Save the converted document and report the library used, style used, output file, and any unresolved citations or metadata issues.

## Operating rules

- Use the user's existing EndNote library when specified. Never silently import into a different library.
- Google Scholar provides candidate records and export files; verify their metadata against the document before relying on them.
- Preserve the document's wording and citation placement. Change citation apparatus and generated bibliography only, except for metadata corrections needed in the EndNote records.
- Keep EndNote/CWYW fields editable so users can later change styles or update references.
- When a CWYW search returns no exact match, an ambiguous result, or a stale previously selected record, stop and resolve the record before inserting; never treat a successful button click as proof of a correct citation.
- If CWYW is unavailable or a source document cannot retain EndNote fields, explain the limitation and produce only the compatible result the user requested; do not claim it contains live EndNote citations when it does not.
- Summarize unresolved citations explicitly. Do not silently omit, fabricate, or substitute a source.
