from typing import List
from app.db.models import Document

def retrieve_documents(query_embedding: List[float], top_k: int = 3) -> List[Document]:
    """
    Simulate retrieving semantically related documents from a vector database.
    """
    dummy_docs = [
        Document(id="doc1", content="Refunds take 3-5 business days to process.", metadata={"source": "faq"}),
        Document(id="doc2", content="To reset your password, click the 'Forgot Password' link.", metadata={"source": "manual"}),
        Document(id="doc3", content="Our support hours are 24/7.", metadata={"source": "website"}),
    ]
    return dummy_docs[:top_k]
