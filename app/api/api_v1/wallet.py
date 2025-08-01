from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import validate
from app.core.config import settings
from app.core.db import get_async_session
from app.core.users import current_superuser, current_user
from app.models.users import User
from app.repositories.wallet import wallet_repositories
from app.schemas.wallet import WalletDB, WalletUpdate
from app.services.wallet import wallet_operation

router = APIRouter(prefix="/wallets", tags=["Wallets"])


@router.get(
    "/",
    response_model=list[WalletDB],
    dependencies=[Depends(current_superuser)],
)
async def get_all_wallets(session: AsyncSession = Depends(get_async_session)):
    """Получить все кошельки списком."""
    wallet = await wallet_repositories.get_multy(session=session)
    return wallet


@router.get("/{WALLET_UUID}", response_model=WalletDB)
async def get_wallet_balance(
    pk: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Получить кошельек по id."""
    wallet = await wallet_repositories.get_by_id(pk=pk, session=session)
    await validate.owner_wallet(wallet.owner, user.id)
    return wallet


@router.post("/{WALLET_UUID}/operation", response_model=WalletDB)
async def operation_on_wallet(
    pk: int,
    method: WalletUpdate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Проищвести операцию с кошельком."""
    await validate.method_operations(method.operation_type)
    wallet = await wallet_repositories.get_by_id(pk=pk, session=session)
    if method.operation_type == settings.WITHDRAW:
        await validate.owner_wallet(wallet.owner, user.id)
        updated_wallet = await wallet_operation.withdraw(
            wallet, method.operation_type, method.amount, session
        )
    else:
        updated_wallet = await wallet_operation.deposit(
            wallet, method.operation_type, method.amount, session
        )
    return updated_wallet
