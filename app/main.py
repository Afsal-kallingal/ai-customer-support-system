from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.chat import router as chat_router
from app.api.ingestion import router as ingestion_router
from app.core.config import settings
from app.db.postgres import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: connect to db
    await db.connect()
    yield
    # Shutdown: disconnect from db
    await db.disconnect()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Include API routers
app.include_router(chat_router, prefix=f"{settings.API_V1_STR}", tags=["Chat"])
app.include_router(ingestion_router, prefix=f"{settings.API_V1_STR}", tags=["Ingestion"])

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/debug/vectorstore", tags=["Debug"])
async def debug_vectorstore():
    from app.rag.vector_store import index, documents, metadata_store
    return {
        "total_vectors": index.ntotal,
        "total_documents": len(documents),
        "samples": [
            {"chunk": documents[i][:100], "source": metadata_store[i]}
            for i in range(min(5, len(documents)))
        ]
    }
