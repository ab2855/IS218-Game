"""Validate research-site local links; this does not execute a browser."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.references = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.references.append(attrs[attr])

root = Path(__file__).resolve().parents[1]
path = root / "docs" / "index.html"
page = Page()
page.feed(path.read_text(encoding="utf-8"))
errors = []
if len(page.ids) != len(set(page.ids)):
    errors.append("Duplicate HTML IDs")
for reference in page.references:
    parts = urlsplit(reference)
    if parts.scheme or parts.netloc:
        continue
    target = path.parent / unquote(parts.path) if parts.path else path
    if not target.exists():
        errors.append(f"Missing local file: {reference}")
    if target == path and parts.fragment and parts.fragment not in page.ids:
        errors.append(f"Missing fragment: {reference}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(page.ids)} unique IDs; {len(page.references)} references inspected; all local targets exist.")
print("Not tested: external availability, browser layout, peer review or game behavior.")
