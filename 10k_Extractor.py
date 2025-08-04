import os
import re
import html
from sec_api import ExtractorApi

API_KEY = ""
OUTPUT_FOLDER = os.path.join("data", "apiData")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

extractor = ExtractorApi(API_KEY)

companies = [
    # (ticker, 10-K URL)
   # ("tsla", "https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm"),
   # ("aapl", "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm"),
   # ("amzn", "https://www.sec.gov/ix?doc=/Archives/edgar/data/0001018724/000101872425000036/amzn-20250331.htm"),
   # ("google", "https://www.sec.gov/Archives/edgar/data/1288776/000165204416000012/goog10-k2015.htm"),
    #("nke", "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000320187/000032018725000047/nke-20250531.htm"),
    ("wmt", "https://www.sec.gov/Archives/edgar/data/104169/000010416924000022/wmt-20240131.htm"),
    ("f",   "https://www.sec.gov/Archives/edgar/data/37996/000003799624000033/f-20231231.htm"),
    ("blk", "https://www.sec.gov/Archives/edgar/data/1364742/000156459024003436/blk-10k_20231231.htm"),
    ("nee", "https://www.sec.gov/Archives/edgar/data/753308/000075330824000037/nee-20231231.htm"),
    ("pfe", "https://www.sec.gov/Archives/edgar/data/78003/000007800324000005/pfe-20231231.htm")
   # ("fdx", "https://www.sec.gov/Archives/edgar/data/1048911/000104891124000038/fdx-20240531.htm"),
]

items = [
    ("1", "ITEM 1. BUSINESS", "item1.md"),
    ("1A", "ITEM 1A. RISK FACTORS", "item1A.md"),
    ("7", "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS", "item7.md"),
    ("7A", "ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK", "item7A.md"),
]

for ticker, filing_url in companies:
    for code, default_title, suffix in items:
        try:
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
            output_filename = f"{ticker}_10k_{suffix}"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"✅ Markdown file saved to: {output_path}")
        except Exception as e:
            print(f"❌ Error extracting {ticker} item {code}: {e}")
