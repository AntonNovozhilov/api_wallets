from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.TITLE, version="1.0", docs_url="/docs", redoc_url="/redoc"
)
