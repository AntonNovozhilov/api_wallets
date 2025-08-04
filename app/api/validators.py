from http import HTTPStatus

from fastapi import HTTPException

from app.core.config import settings
from app.models.users import User


class Validators:
    """Валидаторы."""

    async def positive_balance(self, balance: float):
        """Проверяем, что баланс положительный после операции."""
        if balance < 0:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Недостаточно средств на счёте.",
            )

    async def owner_wallet(self, wallet_owner: int, current_user_id: int):
        """Проверяем владельца кошелька."""
        if wallet_owner != current_user_id:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Вы не владелец кошелька.",
            )

    async def method_operations(self, method: str):
        """Проверяем тип операции."""
        if method not in (settings.DEPOSIT, settings.WITHDRAW):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Неверный тип операции.",
            )

    async def super_user(self, user: User):
        """Проверяем администратора."""
        if user.is_superuser is False:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Доступно только администратору.",
            )


validate = Validators()
