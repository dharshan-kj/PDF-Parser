import os
from pdf_parser.extractor import PDFExtractor
from pdf_parser.json_output import save_jsonl, save_metadata_jsonl
from pdf_parser.validator import TOCValidator
from pdf_parser.report_generator import create_xls_report

PDF_PATH = os.path.join(os.path.dirname(__file__), "USB_PD_R3_2 V1.1 2024-10.pdf")
OUT_DIR = os.path.dirname(__file__)

def main():
    extractor = PDFExtractor(PDF_PATH)

    # 1) Extract ToC + sections
    toc = extractor.extract_toc()
    sections = extractor.extract_sections()

    # 2) Write JSONL outputs
    save_jsonl(toc, os.path.join(OUT_DIR, "usb_pd_toc.jsonl"))
    save_jsonl(sections, os.path.join(OUT_DIR, "usb_pd_spec.jsonl"))
    save_metadata_jsonl(PDF_PATH, "USB Power Delivery Specification (guessed)", os.path.join(OUT_DIR, "usb_pd_metadata.jsonl"))

    # 3) Validate (here we just validate the parsed ToC against itself as a demo;
    #    in a stricter workflow you'd load a ground-truth spec ToC if provided)
    validator = TOCValidator(toc)
    result = validator.validate(toc)

    # 4) Excel report
    create_xls_report(result, os.path.join(OUT_DIR, "usb_pd_validation.xlsx"))

    print("Done.")
    print("Outputs:")
    print(" - usb_pd_toc.jsonl")
    print(" - usb_pd_spec.jsonl")
    print(" - usb_pd_metadata.jsonl")
    print(" - usb_pd_validation.xlsx")

if __name__ == "__main__":
    main()
