import os
import json
import faiss
import numpy as np

FAISS_INDEX_PATH = "faiss_index.bin"
DOCUMENTS_PATH = "faiss_documents.json"

dimension = 384

# Load from disk if exists, otherwise create fresh
if os.path.exists(FAISS_INDEX_PATH):
    index = faiss.read_index(FAISS_INDEX_PATH)
    print(f"[vector_store] Loaded FAISS index from disk ({index.ntotal} vectors)")
else:
    index = faiss.IndexFlatL2(dimension)
    print("[vector_store] Created new FAISS index")

if os.path.exists(DOCUMENTS_PATH):
    with open(DOCUMENTS_PATH, "r") as f:
        data = json.load(f)
        documents = data["documents"]
        metadata_store = data["metadata"]
    print(f"[vector_store] Loaded {len(documents)} documents from disk")
else:
    documents = []
    metadata_store = []


def save_to_disk():
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(DOCUMENTS_PATH, "w") as f:
        json.dump({"documents": documents, "metadata": metadata_store}, f)
    print(f"[vector_store] Saved {index.ntotal} vectors to disk")


def retrieve_documents(query_embedding, top_k=3):
    if index.ntotal == 0:
        return []
    query_vector = np.array([query_embedding]).astype("float32")
    D, I = index.search(query_vector, min(top_k, index.ntotal))
    results = []
    for i in I[0]:
        if i != -1 and i < len(documents):
            results.append({"content": documents[i], "source": metadata_store[i].get("source", "")})
    return results
