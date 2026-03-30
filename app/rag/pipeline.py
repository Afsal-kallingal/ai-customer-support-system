from app.rag.embedding import generate_embedding
from app.rag.retriever import retrieve_documents

def generate_answer(query: str) -> dict:
    """
    Main RAG pipeline entry point.
    """
    # 1. Generate embedding for user query
    query_embedding = generate_embedding(query)
    
    # 2. Retrieve relevant context from vector database
    documents = retrieve_documents(query_embedding)
    
    # 3. Formulate context (dummy implementation)
    context = "\\n".join([doc.content for doc in documents])
    
    # 4. Generate answer (In production, this calls an LLM)
    dummy_answer = f"Based on the context retrieved, here is the answer for '{query}'."
    
    return {
        "answer": dummy_answer,
        "sources": [{"id": doc.id, "source": doc.metadata.get("source")} for doc in documents]
    }
