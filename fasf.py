

import os
import re
from pdfminer.high_level import extract_text

PDF_DIR = 'data/10k'
OUTPUT_DIR = 'data/10k_extracted'

def clean_text(text):
    # Remove form feed characters
    text = text.replace('\f', '').replace('\x0c', '')
    # Remove lines that are just page numbers or headers/footers
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        # Remove lines that are just numbers or look like page numbers (e.g., '65/161')
        if re.match(r'^\d+\s*/\s*\d+$', line):
            continue
        # Remove lines that are just dates or times
        if re.match(r'\d{2}/\d{2}/\d{4}', line):
            continue
        # Remove lines that are just table of contents or file names
        if line.lower() in {'table of contents', 'nvda-20250126'}:
            continue
        # Remove SEC links and similar URLs
        if re.match(r'https://www\.sec\.gov/Archives/edgar/.*', line):
            continue
        # Remove empty lines
        if not line:
            continue
        cleaned_lines.append(line)
    # Remove consecutive duplicate lines
    final_lines = []
    prev = None
    for line in cleaned_lines:
        if line != prev:
            final_lines.append(line)
        prev = line
    return '\n'.join(final_lines)

def extract_pdf_to_md(pdf_path, md_path):
    text = extract_text(pdf_path)
    cleaned = clean_text(text)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(PDF_DIR, filename)
            md_filename = os.path.splitext(filename)[0] + '.md'
            md_path = os.path.join(OUTPUT_DIR, md_filename)
            print(f'Extracting {pdf_path} to {md_path}')
            extract_pdf_to_md(pdf_path, md_path)

if __name__ == '__main__':
    main()
