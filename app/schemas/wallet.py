from core.config import settings
from pydantic import BaseModel, Field, PositiveInt, field_validator


class WalletBase(BaseModel):
    """Кошелек."""

    balance: PositiveInt = Field(..., description="Баланс")
    owner: int = Field(..., description="Владелец кошелька")


class WalletRead(WalletBase):
    """Информация по кошельку."""


class WalletUpdate(BaseModel):
    """Обновление кошелька."""

    operation_type: str = Field(..., description="Действие")
    amount: PositiveInt = Field(..., description="Сумма")

    @field_validator("operation_type")
    @classmethod
    def operation_type_validator(cls, value: str):
        """Проверка, что значение operation_type допустимо."""
        if value not in (settings.DEPOSIT, settings.WITHDRAW):
            raise ValueError("Несуществующий метод.")
        return value


class WalletDB(WalletBase):
    """Данные кошелька из БД."""

    id: int

    class Config:
        orm_mode = True
