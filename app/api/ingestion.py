from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from pydantic import BaseModel

router = APIRouter()

class IngestResponse(BaseModel):
    message: str
    filename: str

@router.post("/upload", response_model=IngestResponse)
async def upload_document(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    """
    Accepts a document (PDF, TXT), saves it temporarily, and triggers background ingestion.
    """
    # Read file content (stub)
    content = await file.read()
    
    # Trigger background task for chunking, embedding, and storing
    background_tasks.add_task(dummy_ingestion_task, file.filename, len(content))
    
    return IngestResponse(
        message="Document uploaded successfully. Processing in background.",
        filename=file.filename
    )

def dummy_ingestion_task(filename: str, size: int):
    # Stub for actual ingestion pipeline call (or Celery task)
    print(f"Ingesting file {filename} of size {size} bytes in background")
