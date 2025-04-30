import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("app/vector_store/faiss_index.idx")
with open("app/vector_store/metadata.json") as f:
    metadata = json.load(f)

def retrieve_relevant_chunks(query, top_k=3):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), top_k)
    results = [metadata[i]["text"] for i in indices[0] if i < len(metadata)]
    return "\n".join(results)
