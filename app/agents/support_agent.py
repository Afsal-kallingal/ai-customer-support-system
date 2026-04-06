
from app.rag.pipeline import generate_answer

def run_agent(query: str) -> dict:
    """
    Agent entry point. Decides whether to use tools, query RAG, or just chat.
    Currently, strictly calls the RAG pipeline.
    """
    # Later: Use LLM loop here to decide routing (e.g., RAG vs database query vs API call)

    rag_result = generate_answer(query)
    return rag_result

