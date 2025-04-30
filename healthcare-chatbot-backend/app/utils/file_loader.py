import os

def load_markdown_files(root_dir):
    md_texts = []
    print(f"Starting to walk directory: {root_dir}")
    for subdir, _, files in os.walk(root_dir):
        print(f"  Currently in subdirectory: {subdir}")
        print(f"    Files found: {files}")
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(subdir, file)
                print(f"    Processing Markdown file: {filepath}")
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        md_texts.append({"text": content, "source": filepath}) # Changed to dictionary format
                        print(f"      Successfully read (first 50 chars): {content[:50]}")
                except Exception as e:
                    print(f"      Error reading file {filepath}: {e}")
        print("-" * 30)
    print(f"Total number of documents loaded: {len(md_texts)}")
    return md_texts