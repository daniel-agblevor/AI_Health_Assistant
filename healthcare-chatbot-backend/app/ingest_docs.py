import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.file_loader import load_markdown_files
from pathlib import Path

# Load and chunk
docs = load_markdown_files("../docs")
print(f"Number of loaded documents: {len(docs)}")
print(f"First few loaded documents: {docs[:2]}")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
print(f"Type of docs: {type(docs)}") # Check the type of 'docs'
if docs and isinstance(docs[0], dict) and "text" in docs[0]:
    chunks = splitter.create_documents([d["text"] for d in docs])
else:
    print("Warning: 'docs' is empty or not in the expected format. Skipping chunking.")
    chunks = []
print(f"Number of chunks created: {len(chunks)}")
texts = [chunk.page_content for chunk in chunks]
print(f"Number of texts to embed: {len(texts)}")
print(f"First few texts: {texts[:2]}")

# Embed
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts)
print(f"Shape of embeddings: {embeddings.shape}")

# Store FAISS index
if embeddings.size > 0:
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    Path("vector_store").mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, "vector_store/faiss_index.idx")

    # Save metadata
    with open("vector_store/metadata.json", "w") as f:
        json.dump([{"text": t} for t in texts], f)
    print("FAISS index and metadata saved successfully.")
else:
    print("No embeddings generated. FAISS index and metadata not saved.")

print("Ingestion process completed.")