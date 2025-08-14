# 📄 PDF Parser

## Overview
The **PDF Parser** project is a Jupyter Notebook-based solution for extracting structured information from PDF documents.  
It is designed with a focus on technical specifications such as the **USB Power Delivery (USB PD) Specification**, but can be adapted for other complex, structured PDFs.

The parser reads a PDF, extracts the **Table of Contents (ToC)** and section details, and outputs the information into **JSONL** format, making it machine-readable and ready for search, analysis, or integration with other tools.

---

## ✨ Features
- **PDF Reading & Text Extraction** using libraries like `pdfplumber` or `PyMuPDF`.
- **Table of Contents Parsing** to identify:
  - Section numbers (e.g., `2.1.2`)
  - Titles
  - Page numbers
  - Hierarchical relationships
- **Structured Output** in JSON Lines (`.jsonl`) format.
- **Support for Metadata Extraction** (document title, tags, etc.).
- **Extensible** for parsing additional document features such as tables and diagrams.

---

## Install Dependencies

pip install -r requirements.txt

##🛠 Technologies Used

- Python 3
- Jupyter Notebook
- pdfplumber / PyMuPDF – PDF text extraction
- pandas – Data handling & exporting
- jsonlines – Writing structured data to .jsonl format
