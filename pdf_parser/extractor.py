import re
from PyPDF2 import PdfReader

class PDFExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.reader = PdfReader(pdf_path)

    def extract_toc(self):
        """
        Very simple ToC extractor:
        - Looks for a page that mentions "Table of Contents"
        - Then parses lines that look like: <section id/ title> ..... <page>
        Returns a list of dicts: [{ "section_id": "2.1.2", "title": "Foo", "page": 53, "level": 3, "parent_id": "2.1"}]
        """
        toc = []
        toc_start_found = False
        # Matches things like:
        # 2.1.2  Power Delivery Contract Negotiation .......... 53
        # or     Introduction ................................ 1
        line_pattern = re.compile(r"^\s*([0-9]+(?:\.[0-9]+)*)?\s*(.+?)\s+(\d+)\s*$")

        for page_idx, page in enumerate(self.reader.pages[:20]):  # scan first 20 pages for ToC
            text = page.extract_text() or ""
            if not text.strip():
                continue

            if not toc_start_found and "table of contents" in text.lower():
                toc_start_found = True
                continue

            if toc_start_found:
                for raw in text.splitlines():
                    m = line_pattern.match(raw.strip())
                    if not m:
                        continue
                    sec_num, title, page_no = m.groups()
                    page_no = int(page_no)
                    sec_num = (sec_num or "").strip()
                    title = title.strip()

                    level = sec_num.count(".") + 1 if sec_num else 1
                    parent_id = ".".join(sec_num.split(".")[:-1]) if sec_num and "." in sec_num else (sec_num if sec_num else None)

                    toc.append({
                        "section_id": sec_num if sec_num else None,
                        "title": title,
                        "page": page_no,
                        "level": level,
                        "parent_id": parent_id,
                        "full_path": f"{sec_num} {title}".strip() if sec_num else title
                    })

                # Heuristic stop: if we collected a reasonable amount and hit a non-ToC-looking page
                if len(toc) > 20:
                    break

        return toc

    def extract_sections(self):
        """
        Minimal section extractor: returns page-wise text (you can improve to split by headings).
        Output schema is intentionally simple and compatible with jsonl writing:
        [{ "page": 1, "content": "..."}]
        """
        sections = []
        for i, page in enumerate(self.reader.pages, start=1):
            txt = page.extract_text() or ""
            sections.append({"page": i, "content": txt.strip()})
        return sections
