from pdf_parser.validator import TOCValidator

def test_validator_detects_missing_and_mismatch():
    spec = [{"title": "Intro", "page": 1}, {"title": "Chapter 1", "page": 5}]
    parsed = [{"title": "Intro", "page": 1}, {"title": "Chapter 1", "page": 6}]

    v = TOCValidator(spec)
    results = v.validate(parsed)

    assert not results["match"]
    assert "Chapter 1" in [m["title"] for m in results["mismatched_pages"]]
