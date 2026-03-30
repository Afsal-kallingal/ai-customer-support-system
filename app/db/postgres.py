from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class DatabaseSession:
    """
    Placeholder for async SQLAlchemy or Psycopg connection pool
    """
    def __init__(self, db_url: str):
        self.db_url = db_url

    async def connect(self):
        logger.info(f"Connecting to database at {self.db_url}")

    async def disconnect(self):
        logger.info("Disconnecting from database")

db = DatabaseSession(settings.DATABASE_URL)
