import json

def save_jsonl(rows, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def save_metadata_jsonl(pdf_path: str, doc_title: str, output_path: str):
    meta = {
        "pdf_path": pdf_path,
        "doc_title": doc_title
    }
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")
