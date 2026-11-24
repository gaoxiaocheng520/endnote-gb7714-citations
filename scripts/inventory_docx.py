#!/usr/bin/env python3
"""Read citation markers and numbered references from a DOCX without editing it."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

CITATION_RE = re.compile(r"(?<!\d)\[\s*(\d+(?:\s*[-–—,，]\s*\d+)*)\s*\](?!\d)")
REFERENCE_RE = re.compile(r"^\s*(?:\[(\d{1,3})\]|(\d{1,3})[.．、])\s*(\S.*)$")
REFERENCE_HEADINGS = ("参考文献", "references", "bibliography")


def paragraph_text(node: ET.Element) -> str:
    return "".join(t.text or "" for t in node.iter(W + "t")).strip()


def read_paragraphs(docx_path: Path) -> list[str]:
    with zipfile.ZipFile(docx_path) as archive:
        try:
            xml = archive.read("word/document.xml")
        except KeyError as exc:
            raise ValueError("Not a valid Word DOCX: word/document.xml is missing") from exc
    root = ET.fromstring(xml)
    return [paragraph_text(p) for p in root.iter(W + "p")]


def expand_group(raw: str) -> list[int]:
    numbers: list[int] = []
    for item in re.split(r"\s*[,，]\s*", raw):
        range_match = re.fullmatch(r"\s*(\d+)\s*[-–—]\s*(\d+)\s*", item)
        if range_match:
            start, end = map(int, range_match.groups())
            if end >= start and end - start <= 100:
                numbers.extend(range(start, end + 1))
            else:
                numbers.extend((start, end))
        else:
            number_match = re.fullmatch(r"\s*(\d+)\s*", item)
            if number_match:
                numbers.append(int(number_match.group(1)))
    return list(dict.fromkeys(numbers))


def inventory(docx_path: Path) -> dict:
    paragraphs = read_paragraphs(docx_path)
    heading_index = next(
        (i for i, text in enumerate(paragraphs)
         if text.strip().casefold() in REFERENCE_HEADINGS),
        None,
    )
    body_end = heading_index if heading_index is not None else len(paragraphs)

    citations = []
    cited_numbers: set[int] = set()
    for paragraph_index, text in enumerate(paragraphs[:body_end]):
        for match in CITATION_RE.finditer(text):
            numbers = expand_group(match.group(1))
            if not numbers:
                continue
            cited_numbers.update(numbers)
            citations.append({
                "paragraph": paragraph_index + 1,
                "marker": match.group(0),
                "reference_numbers": numbers,
                "context": text[:240],
            })

    references: dict[int, str] = {}
    duplicate_reference_numbers: list[int] = []
    if heading_index is not None:
        for text in paragraphs[heading_index + 1:]:
            match = REFERENCE_RE.match(text)
            if not match:
                continue
            number = int(match.group(1) or match.group(2))
            if number in references:
                duplicate_reference_numbers.append(number)
            references[number] = match.group(3).strip()

    warnings = []
    if heading_index is None:
        warnings.append("No standalone References/参考文献 heading was found; citation groups were scanned through the end of the document.")
    unresolved = sorted(cited_numbers - references.keys()) if heading_index is not None else sorted(cited_numbers)
    if unresolved:
        warnings.append("Some cited numbers have no numbered entry after the reference heading. Review the source document and any non-numeric references.")

    return {
        "source_file": docx_path.name,
        "reference_heading_paragraph": heading_index + 1 if heading_index is not None else None,
        "citation_group_count": len(citations),
        "unique_cited_numbers": sorted(cited_numbers),
        "citations": citations,
        "references": [
            {"number": number, "text": text}
            for number, text in sorted(references.items())
        ],
        "unresolved_reference_numbers": unresolved,
        "duplicate_reference_numbers": sorted(set(duplicate_reference_numbers)),
        "warnings": warnings,
        "note": "Read-only inventory. It does not edit the DOCX or create EndNote fields.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path, help="Input .docx document")
    parser.add_argument("-o", "--output", type=Path, help="Write JSON to this path (default: stdout)")
    args = parser.parse_args()

    if not args.docx.is_file():
        parser.error(f"file not found: {args.docx}")
    try:
        result = inventory(args.docx)
        rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (zipfile.BadZipFile, ET.ParseError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
