from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Wallet
from app.repositories.storage import Repositories


class WalletRepositories(Repositories):

    def __init__(self, model):
        self.model = model

    async def get_by_id(self, pk: int, session: AsyncSession):
        """Получаем объект по pk."""
        obj = await session.execute(
            select(self.model).where(self.model.id == pk)
        )
        return obj.scalar()

    async def get_multy(self, session: AsyncSession) -> list:
        """Получаем несколько объектов."""
        objects = await session.execute(select(self.model))
        return objects.scalars().all()


wallet_repositories = WalletRepositories(Wallet)
