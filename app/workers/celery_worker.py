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

@celery_app.task(name="app.workers.celery_worker.process_document")
def process_document(document_id: str):
    # This is a placeholder for async background ingestion/processing task
    print(f"Processing document {document_id} in background...")
    return True
