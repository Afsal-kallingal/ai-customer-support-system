from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "support_worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery_app.conf.task_routes = {
    "app.workers.celery_worker.process_document": "main-queue"
}


@celery_app.task(name="app.workers.celery_worker.process_document", bind=True, max_retries=3)
def process_document(self, filename: str, content: bytes):
    """Celery task: parses, chunks, embeds and indexes a document."""
    try:
        print(f"[celery] Starting ingestion: {filename}")
        from app.rag.pipeline import ingestion_task
        ingestion_task(filename, content)
        print(f"[celery] Done: {filename}")
    except Exception as exc:
        print(f"[celery] Failed: {filename} — {exc}. Retrying...")
        raise self.retry(exc=exc, countdown=5)
