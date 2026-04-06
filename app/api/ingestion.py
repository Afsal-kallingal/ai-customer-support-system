from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.workers.celery_worker import process_document

router = APIRouter()

ALLOWED_EXTENSIONS = {".txt", ".pdf"}


class IngestResponse(BaseModel):
    message: str
    files_queued: int
    filenames: list[str]


def _validate_file(filename: str) -> None:
    if not filename:
        raise HTTPException(status_code=400, detail="A file is missing a filename")
    ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{ext}' for '{filename}'. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )


@router.post("/upload", response_model=IngestResponse)
async def upload_documents(
    files: list[UploadFile] = File(...),
):
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")

    queued: list[str] = []
    for file in files:
        _validate_file(file.filename)
        content = await file.read()
        process_document.delay(file.filename, content)  # send to Celery queue
        queued.append(file.filename)
        print(f"[upload] Sent to Celery: {file.filename}")

    return IngestResponse(
        message="Files uploaded and processing started",
        files_queued=len(queued),
        filenames=queued,
    )
