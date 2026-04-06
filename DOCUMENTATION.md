# AI Customer Support RAG System

## Overview
This project implements a prototype customer support system using Retrieval-Augmented Generation (RAG). It is built with FastAPI and includes:
- a chat API endpoint for answering user support queries,
- a document ingestion endpoint for uploading knowledge sources,
- a minimal RAG pipeline that embeds queries, retrieves documents, and generates answers,
- a placeholder database connection layer,
- and a Celery worker stub for background document processing.

The system is designed for customer support use cases such as FAQ answering, account help, password resets, and other support knowledge retrieval.

## Architecture

1. `app/main.py`
   - Creates the FastAPI application.
   - Uses a lifespan manager to connect/disconnect from the database.
   - Includes API routers for chat and ingestion.
   - Provides a `GET /health` endpoint.

2. `app/api/chat.py`
   - Defines `POST /api/v1/chat`.
   - Accepts `ChatRequest` containing `query`.
   - Calls `app.agents.support_agent.run_agent` to get an answer.

3. `app/api/ingestion.py`
   - Defines `POST /api/v1/upload`.
   - Accepts file uploads and triggers a background ingestion task.
   - Current ingestion is a stub that prints ingestion activity.

4. `app/agents/support_agent.py`
   - Acts as the agent entrypoint.
   - Currently always delegates to the RAG pipeline.
   - Designed to later route between tools, chaining, and intelligent decision making.

5. `app/rag/pipeline.py`
   - Main RAG workflow.
   - Generates query embeddings with `app.rag.embedding.generate_embedding`.
   - Retrieves relevant documents with `app.rag.retriever.retrieve_documents`.
   - Builds a context from retrieved documents.
   - Generates a dummy answer string.

6. `app/rag/embedding.py`
   - Contains embedding generation logic.
   - Currently returns a dummy 768-dimensional vector.
   - Placeholder for integration with real embedding providers.

7. `app/rag/retriever.py`
   - Simulates document retrieval from a vector database.
   - Returns hard-coded support documents.
   - Placeholder for real vector search with embeddings.

8. `app/db/models.py`
   - Defines Pydantic models: `Document`, `ChatRequest`, and `ChatResponse`.
   - `Document` includes `content`, `metadata`, and optional `embedding`.

9. `app/db/postgres.py`
   - Contains a placeholder `DatabaseSession` class.
   - Simulates connection/disconnection logging.
   - Uses `DATABASE_URL` from settings.

10. `app/workers/celery_worker.py`
    - Defines a Celery application configured with broker/backend from settings.
    - Contains a placeholder task `process_document`.
    - Intended for asynchronous ingestion or document processing.

11. `app/core/config.py`
    - Loads configuration values with `pydantic-settings`.
    - Defines `PROJECT_NAME`, API prefix, database URL, and Celery broker/backend.

## Current State and Implementation Notes
- The chat endpoint is wired to a RAG-style workflow, but actual LLM generation is not integrated.
- Embeddings are dummy vectors and document retrieval is static.
- Document ingestion currently accepts uploads but does not store or index them.
- The database layer is a stub with log-only connect/disconnect logic.
- Celery worker exists but is not yet connected to the ingestion pipeline.

## Recommended Next Steps
1. Integrate a real embedding service
   - OpenAI embeddings, Hugging Face, or another vector model.

2. Implement document storage and vector index
   - Use Pinecone, Milvus, Weaviate, or SQLite/PG + vector extension.

3. Replace the dummy retriever
   - Query the vector index using the query embedding.

4. Connect ingestion to actual processing
   - Parse uploaded documents, chunk text, embed chunks, and store them.

5. Add LLM generation
   - Use an LLM to formulate the answer using retrieved context.

6. Improve the agent
   - Add routing logic to decide when to use RAG, external APIs, or fallback policies.

## How to Run
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Start the FastAPI app:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Use the endpoints:
   - `POST /api/v1/chat` with `{"query": "..."}`
   - `POST /api/v1/upload` with a file upload

## File Summary
- `requirements.txt` — Python dependencies.
- `app/main.py` — FastAPI app and route registration.
- `app/core/config.py` — environment settings.
- `app/api/chat.py` — chat API router.
- `app/api/ingestion.py` — document ingestion router.
- `app/agents/support_agent.py` — support agent orchestration.
- `app/rag/embedding.py` — query embedding stub.
- `app/rag/retriever.py` — document retrieval stub.
- `app/rag/pipeline.py` — RAG pipeline orchestration.
- `app/db/models.py` — Pydantic data schemas.
- `app/db/postgres.py` — database connection stub.
- `app/workers/celery_worker.py` — Celery background worker stub.

## Goal
This project is a customer support RAG system prototype that can evolve into a full knowledge-driven support assistant by replacing stubs with real embedding, retrieval, and LLM generation components.
