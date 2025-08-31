import os, json
from pdf_parser.json_output import save_jsonl, save_metadata_jsonl

def test_save_jsonl(tmp_path):
    data = [{"title": "Intro", "page": 1}]
    out = tmp_path / "out.jsonl"
    save_jsonl(data, str(out))

    lines = out.read_text().splitlines()
    assert len(lines) == 1
    obj = json.loads(lines[0])
    assert obj["title"] == "Intro"

def test_save_metadata_jsonl(tmp_path):
    out = tmp_path / "meta.jsonl"
    save_metadata_jsonl("file.pdf", "Doc Title", str(out))
    meta = json.loads(out.read_text())
    assert meta["doc_title"] == "Doc Title"
