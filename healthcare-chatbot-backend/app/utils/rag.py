import json
import faiss
from sentence_transformers import SentenceTransformer


def retrieve_relevant_chunks(query, top_k=3):
    index = None
    metadata = []
    index_path = "vector_store/faiss_index.idx"
    metadata_path = "vector_store/metadata.json"
    model_name = "all-MiniLM-L6-v2"

    print(f"\nRetrieving relevant chunks for query: '{query}'")

    try:
        print(f"Attempting to load FAISS index from: {index_path}")
        index = faiss.read_index(index_path)
        print("FAISS index loaded successfully.")
    except Exception as e:
        print(f"Error loading FAISS index: {e}")

    try:
        print(f"Attempting to load metadata from: {metadata_path}")
        with open(metadata_path) as f:
            metadata = json.load(f)
        print(f"Metadata loaded successfully. Contains {len(metadata)} entries.")
    except Exception as e:
        print(f"Error loading metadata: {e}")

    if index is None or not metadata:
        print("Warning: FAISS index or metadata is not loaded. Returning empty context.")
        return ""

    try:
        model = SentenceTransformer(model_name)
        query_vector = model.encode([query]).astype("float32")
        distances, indices = index.search(query_vector, top_k)
        print(f"FAISS search results - Distances: {distances}, Indices: {indices}")
        results = [metadata[i]["text"] for i in indices[0] if i < len(metadata)]
        print(f"Retrieved relevant chunks (count: {len(results)}):\n{results}")
        return "\n".join(results)
    except Exception as e:
        print(f"Error during retrieval: {e}")
        return ""

if __name__ == '__main__':
    # Example usage (for testing)
    test_query = "What are the symptoms of diabetes?"
    relevant_info = retrieve_relevant_chunks(test_query)
    print(f"\nRelevant Information for '{test_query}':\n{relevant_info}")