from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Пользователь."""


class UserCreate(schemas.BaseUserCreate):
    """Создание пользователя."""


class UserUpdate(schemas.BaseUserUpdate):
    """Обновление пользователя."""
