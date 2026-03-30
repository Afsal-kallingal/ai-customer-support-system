from pydantic import BaseModel
from typing import Optional, List

class Document(BaseModel):
    id: Optional[str] = None
    content: str
    metadata: dict = {}
    embedding: Optional[List[float]] = None

class ChatRequest(BaseModel):
    query: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str
    sources: List[dict] = []
