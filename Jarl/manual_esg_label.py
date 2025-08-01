import os
import json

# Directory containing the extracted 10-K files
extracted_dir = "data/10k_extracted/"

# List all .md files in the directory
files = [f for f in os.listdir(extracted_dir) if f.endswith(".md")]

esg_scores = {}

print("Manual ESG labeling. Enter a score for each company file (e.g., 1-10, or low/medium/high):\n")


for filename in files:
    company_name = os.path.splitext(filename)[0]
    print(f"\nFile: {filename}")
    e = input(f"Enter Environmental (E) score for {company_name} (0-100): ")
    s = input(f"Enter Social (S) score for {company_name} (0-100): ")
    g = input(f"Enter Governance (G) score for {company_name} (0-100): ")
    esg_scores[company_name] = {
        "E": int(e),
        "S": int(s),
        "G": int(g)
    }

# Save the results as a JSON file
with open("data/esg_scores.json", "w") as f:
    json.dump(esg_scores, f, indent=2)

print("\nESG scores saved to data/esg_scores.json")
