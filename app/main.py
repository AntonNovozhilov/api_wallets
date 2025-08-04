from fastapi import FastAPI

from app.api.main_router import main_router
from app.core.config import settings

app = FastAPI(
    title=settings.TITLE,
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
app.include_router(main_router)
