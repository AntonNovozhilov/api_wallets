from fastapi import APIRouter

from app.core.users import auth_backend, fastapi_user
from app.schemas.users import UserCreate, UserRead

router = APIRouter()

router.include_router(
    fastapi_user.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_user.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
