from models import Wallet
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from storage import Repositories


class WalletRepositories(Repositories):

    def __init__(self):
        self.model = Wallet

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

    async def update_object(self, obj, data: dict, session: AsyncSession):
        """Обновление объекта."""
        up_data = data.dict(exclude_unset=True)
        for filed, value in up_data.items():
            setattr(obj, filed, value)
        await session.commit()
        await session.refresh(obj)
        return obj


wallet_repositories = WalletRepositories()
