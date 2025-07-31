from core.config import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.TITLE, version="1.0", docs_url="/docs", redoc_url="/redoc"
)
