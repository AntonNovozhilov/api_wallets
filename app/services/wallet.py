from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import validate
from app.core.config import settings


class WalletOperation:

    def __init__(self, valida):
        self.validate = valida

    async def deposit(
        self, obj, method: str, ammount: int, session: AsyncSession
    ):
        if method == settings.DEPOSIT:
            obj.balance += ammount
        await session.commit()
        await session.refresh(obj)
        return obj

    async def withdraw(
        self, obj, method: str, ammount: int, session: AsyncSession
    ):
        if method == settings.WITHDRAW:
            obj.balance -= ammount
        await self.validate.positive_balance(obj.balance)
        await session.commit()
        await session.refresh(obj)
        return obj


wallet_operation = WalletOperation(validate)
