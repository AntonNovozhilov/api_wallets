import enum
from fastapi import APIRouter, Depends
from app.schemas.wallet import WalletDB, WalletUpdate
from app.models.wallet import Wallet
from app.repositories.wallet import wallet_repositories
from app.core.users import current_superuser, current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.core.config import settings
from app.services.wallet import wallet_operation

router = APIRouter(prefix="/wallets", tags=["Wallets"])

@router.post("/{WALLET_UUID}/operation", response_model=WalletDB, dependencies=[Depends(current_user)])
async def operation_on_wallet(pk: int, date: WalletUpdate, session: AsyncSession=Depends(get_async_session)):
    wallet = await wallet_repositories.get_by_id(pk=pk, session=session)
    update_wallet = await wallet_operation._operations(wallet, date.operation_type, date.amount)
    return update_wallet

@router.get("/{WALLET_UUID}", response_model=WalletDB, dependencies=[Depends(current_user)])
async def get_wallet(pk: int, session: AsyncSession=Depends(get_async_session)):
    wallet = await wallet_repositories.get_by_id(pk=pk, session=session)
    return wallet.balance

