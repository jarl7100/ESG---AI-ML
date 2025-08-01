import os
import re
import html
from sec_api import ExtractorApi

API_KEY = "a00eca1166f1a30861e85045ca7616ef57159cd44124213d86a7dcb9f89b01c8"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
OUTPUT_FOLDER = os.path.join(DATA_DIR, "jpmorganchase")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

extractor = ExtractorApi(API_KEY)
# JPMorgan Chase CIK: 0000019617, Example 10-K filing for 2024
filing_url = (
    "https://www.sec.gov/Archives/edgar/data/"
    "19617/000001961725000270/jpm-20241231.htm"
)


# Items to extract: (item code, default title, output filename)
items = [
    ("1", "ITEM 1. BUSINESS", "jpmorganchase_10k_item1.md"),
    ("1A", "ITEM 1A. RISK FACTORS", "jpmorganchase_10k_item1A.md"),
    ("7", "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS", "jpmorganchase_10k_item7.md"),
    ("7A", "ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK", "jpmorganchase_10k_item7A.md")
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