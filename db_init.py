import asyncio

from fastapi_users.password import PasswordHelper
from sqlalchemy import select

from app.core.db import AsyncSession
from app.models.users import User
from app.models.wallet import Wallet

user_email = "test@test.ru"
password = "test"


async def init_db():
    async with AsyncSession() as session:
        user = await session.execute(
            select(User).where(User.email == user_email)
        )
        user = user.scalars().first()
        if not user:
            pas = PasswordHelper()
            hashed_pw = pas.hash(password)
            user = User(
                email=user_email,
                hashed_password=hashed_pw,
                is_superuser=True,
                is_active=True,
                is_verified=True,
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            wallet = Wallet(owner=user.id, balance=1000)
            session.add(wallet)
            await session.commit()
        else:
            return


if __name__ == "__main__":
    asyncio.run(init_db())
