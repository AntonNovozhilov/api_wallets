from http import HTTPStatus

from fastapi import HTTPException

from app.core.config import settings
from app.models.users import User


class Validators:

    async def positive_balance(self, balance: int):
        if balance < 0:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Недостаточно средств на счете",
            )

    async def owner_wallet(self, wallet_owner: int, current_user: User):
        if wallet_owner != current_user:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Вы не владелец кошелька.",
            )

    async def method_operations(self, method):
        if method not in (settings.DEPOSIT, settings.WITHDRAW):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Неверный тип операции.",
            )


validate = Validators()
