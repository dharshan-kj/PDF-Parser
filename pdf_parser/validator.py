import json

class TOCValidator:
    """
    Compares a spec ToC (from the parsed ToC JSONL-like list)
    to an 'observed' set (e.g., sections/pages you extracted).
    For simplicity, we compare by (title -> first page occurrence).
    """
    def __init__(self, spec_toc_list):
        # spec_toc_list: list of dicts with at least {'title','page'}
        self.spec_map = {x["title"]: x["page"] for x in spec_toc_list if "title" in x and "page" in x}

    def validate(self, extracted_toc_list):
        observed = {x["title"]: x["page"] for x in extracted_toc_list if "title" in x and "page" in x}

        missing = [t for t in self.spec_map if t not in observed]
        extras = [t for t in observed if t not in self.spec_map]

        mismatched_pages = []
        for t in self.spec_map:
            if t in observed and observed[t] != self.spec_map[t]:
                mismatched_pages.append({"title": t, "expected": self.spec_map[t], "observed": observed[t]})

        return {
            "match": (not missing and not extras and not mismatched_pages),
            "missing_titles": missing,
            "extra_titles": extras,
            "mismatched_pages": mismatched_pages
        }
