from pathlib import Path

def load_markdown_files(directory):
    files = list(Path(directory).rglob("*.md"))
    docs = []
    for file in files:
        text = file.read_text(encoding="utf-8")
        docs.append({"filename": file.name, "text": text})
    return docs