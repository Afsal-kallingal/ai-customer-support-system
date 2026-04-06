import numpy as np
from app.agents.llm import call_llm
from app.rag.embedding import generate_embedding
from app.rag.retriever import retrieve_documents
# from app.rag.embedding import generate_embedding
from app.rag.vector_store import index, documents, metadata_store
from app.rag.parser import parse_file,chunk_text


def generate_answer(query: str):
    query_embedding = generate_embedding(query)
    print("Query Embedding:", query_embedding)  # Debugging
    docs = retrieve_documents(query_embedding)
    print("Retrieved Documents:", docs)  # Debugging
    context = "\n".join([doc["content"] for doc in docs])
    print("Retrieved Context:", context)  # Debugging

    prompt = f"""
Answer ONLY from the context below.
If not found, say "I don't know".

Context:
{context}

Question:
{query}
"""

    answer = call_llm(prompt)

    return {
        "answer": answer,
        "sources": docs
    }



def ingestion_task(filename: str, content: bytes):
    text = parse_file(filename, content)

    chunks = chunk_text(text)

    vectors = []
    
    for chunk in chunks:
        emb = generate_embedding(chunk)
        vectors.append(emb)

        documents.append(chunk)
        metadata_store.append({"source": filename})

    # Convert to numpy
    vectors_np = np.array(vectors).astype("float32")

    # Add to FAISS
    index.add(vectors_np)

    print(f"✅ Ingested {len(chunks)} chunks from {filename}")