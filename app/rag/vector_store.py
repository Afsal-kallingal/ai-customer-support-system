import faiss
import numpy as np

dimension = 384  # for MiniLM model

index = faiss.IndexFlatL2(dimension)

documents = []   # stores text
metadata_store = []  # stores filename or info

print("Initialized FAISS index and in-memory stores")
print("Index is trained:", index)
print("Current number of documents in index:", index.ntotal)
print("Current documents:", documents)
print("Current metadata:", metadata_store)



def retrieve_documents(query_embedding, top_k=3):
    query_vector = np.array([query_embedding]).astype("float32")

    D, I = index.search(query_vector, top_k)

    return [documents[i] for i in I[0]]