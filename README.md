# PDF Parser

## Overview

The PDF Parser project is a Jupyter Notebook-based solution for extracting structured information from PDF documents. It is designed with a focus on technical specifications such as the USB Power Delivery (USB PD) Specification but can be adapted for other complex, structured PDFs.

The parser reads a PDF, extracts the Table of Contents (ToC) and section details, and outputs the information into JSONL format, making it machine-readable and ready for search, analysis, or integration with other tools.

## Features

* **PDF Reading & Text Extraction**: Utilizes libraries like `pdfplumber` or `PyMuPDF` to extract text content from PDFs.
* **Table of Contents Parsing**: Identifies and extracts:

  * Section numbers (e.g., `2.1.2`)
  * Titles
  * Page numbers
  * Hierarchical relationships between sections
* **Output Format**: Exports parsed data into JSONL format for easy consumption by other tools or systems.

## Project Structure

* `PDF PARSER.ipynb`: The main Jupyter Notebook containing the parsing logic and examples.
* `requirements.txt`: Lists the Python dependencies required to run the notebook.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed. Then, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/dharshan-kj/PDF-Parser.git
cd PDF-Parser
```

2. Open the `PDF PARSER.ipynb` notebook in Jupyter Notebook or JupyterLab.
3. Follow the instructions within the notebook to load your PDF and parse its Table of Contents.

## Example Output

After parsing a PDF, the extracted Table of Contents might look like:

```json
[
  {
    "section_id": "2.1.2",
    "title": "Power Delivery Contract Negotiation",
    "page": 53,
    "level": 3,
    "parent_id": "2.1",
    "full_path": "2.1.2 Power Delivery Contract Negotiation",
    "tags": []
  }
]
```

Each line in the JSONL file represents a section, capturing its hierarchical structure and metadata.

## Customization

The script is designed to be adaptable:

* **Page Range**: Modify the loop range in the script to change the pages processed.
* **Document Title**: Update the `doc_title` variable in the script to reflect the title of your document.
* **Tags**: Customize the `tags` field to categorize sections as needed.
