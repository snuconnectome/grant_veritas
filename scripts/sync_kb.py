import os
import re
import json
from datetime import datetime

def process_notebooklm_exports(input_dir, output_index):
    """
    Processes markdown/text files exported from NotebookLM and creates a structured index.
    """
    insights = []
    
    if not os.path.exists(input_dir):
        print(f"Error: Directory {input_dir} not found.")
        return

    for filename in os.listdir(input_dir):
        if filename.endswith((".md", ".txt")):
            filepath = os.path.join(input_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Extract potential title (First H1 or filename)
                title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
                title = title_match.group(1) if title_match else filename
                
                # Extract potential tags or keywords (Mock extraction for now)
                # In real use, we could look for specific patterns
                
                insights.append({
                    "title": title,
                    "filename": filename,
                    "path": filepath,
                    "last_synced": datetime.now().isoformat(),
                    "summary_snippet": content[:200] + "..."
                })

    # Save index for AI search assistance
    with open(output_index, 'w', encoding='utf-8') as f:
        json.dump(insights, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully indexed {len(insights)} insights to {output_index}")

if __name__ == "__main__":
    BASE_DIR = "/Users/jiookcha/Library/CloudStorage/OneDrive-Personal/_Documents/_그랜트/00베리타스"
    INSIGHTS_DIR = os.path.join(BASE_DIR, "01summaries/notebooklm_insights")
    INDEX_FILE = os.path.join(BASE_DIR, "01summaries/notebooklm_insights/KNOWLEDGE_INDEX.json")
    
    process_notebooklm_exports(INSIGHTS_DIR, INDEX_FILE)
