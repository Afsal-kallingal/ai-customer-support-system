from fastapi import APIRouter
from app.db.models import ChatRequest, ChatResponse
from app.agents.support_agent import run_agent

router = APIRouter()



@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Accepts a user query, triggers the support agent, and returns the generated answer.
    """
    agent_result = run_agent(request.query)
    return ChatResponse(
        answer=agent_result["answer"],
        sources=agent_result["sources"]
    )
