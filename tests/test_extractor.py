import os
from pdf_parser.extractor import PDFExtractor

PDF_PATH = os.path.join(os.path.dirname(__file__), "../USB_PD_R3_2 V1.1 2024-10.pdf")

def test_extract_toc_runs():
    extractor = PDFExtractor(PDF_PATH)
    toc = extractor.extract_toc()
    assert isinstance(toc, list)
    if toc:  # if something was extracted
        first = toc[0]
        assert "title" in first
        assert "page" in first

def test_extract_sections_runs():
    extractor = PDFExtractor(PDF_PATH)
    sections = extractor.extract_sections()
    assert isinstance(sections, list)
    if sections:
        assert "page" in sections[0]
        assert "content" in sections[0]
