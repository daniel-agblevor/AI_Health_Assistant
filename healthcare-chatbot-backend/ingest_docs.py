import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.file_loader import load_markdown_files
from pathlib import Path

# Load and chunk
docs = load_markdown_files("docs")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.create_documents([d["text"] for d in docs])

# Embed
model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [chunk.page_content for chunk in chunks]
embeddings = model.encode(texts)

# Store FAISS index
dim = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))
Path("app/vector_store").mkdir(parents=True, exist_ok=True)
faiss.write_index(index, "app/vector_store/faiss_index.idx")

# Save metadata
with open("app/vector_store/metadata.json", "w") as f:
    json.dump([{"text": t} for t in texts], f)
