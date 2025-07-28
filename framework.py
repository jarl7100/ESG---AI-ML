import os
from PyPDF2 import PdfReader

pdf_dir = "data/ESG_frameworks"  # Update this path if needed
output_dir = "data/ESG_frameworks_txt"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(pdf_dir):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        txt_path = os.path.join(output_dir, filename.replace(".pdf", ".txt"))
        with open(txt_path, "w", encoding="utf-8") as out_f:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    out_f.write(text + "\n")

print("✅ PDF extraction complete. Text files saved to", output_dir)