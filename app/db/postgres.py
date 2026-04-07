from app.core.config import settings


class DatabaseSession:
    """Placeholder for async DB connection (SQLAlchemy / psycopg pool)."""

    def __init__(self, db_url: str):
        self.db_url = db_url

    async def connect(self):
        print(f"[db] Connecting to database at {self.db_url}")

    async def disconnect(self):
        print("[db] Disconnecting from database")


db = DatabaseSession(settings.DATABASE_URL)
