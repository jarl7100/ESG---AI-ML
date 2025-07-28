import os
import re
import html
from sec_api import ExtractorApi

API_KEY = "8"
OUTPUT_FOLDER = os.path.join("data", "apiData")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

extractor = ExtractorApi(API_KEY)
filing_url = (
    "https://www.sec.gov/Archives/edgar/data/"
    "1318605/000156459021004599/tsla-10k_20201231.htm"
)


# Items to extract: (item code, default title, output filename)
items = [
    ("1", "ITEM 1. BUSINESS", "tsla_10k_item1.md"),
    ("1A", "ITEM 1A. RISK FACTORS", "tsla_10k_item1A.md"),
    ("7", "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS", "tsla_10k_item7.md"),
    ("7A", "ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK", "tsla_10k_item7A.md"),
]

for code, default_title, filename in items:
    raw = extractor.get_section(filing_url, code, "text")
    text = html.unescape(raw)
    text = re.sub(r'##TABLE_.*?\n', '', text)
    text = text.replace('\u00A0', ' ')
    text = re.sub(r'\n\s*\n+', '\n\n', text).strip()

    lines = text.split('\n')
    if lines and lines[0].strip().upper().startswith(f"ITEM {code}"):
        title = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
    else:
        title = default_title
        body = text

    markdown = f"# {title}\n\n{body}\n"
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ Markdown file saved to: {output_path}")
