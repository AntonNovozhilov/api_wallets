from fastapi import APIRouter
from app.api.api_v1.wallet import router

main_router = APIRouter()
main_router.include_router(router)