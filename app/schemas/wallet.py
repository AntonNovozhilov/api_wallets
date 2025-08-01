from pydantic import BaseModel, Field, field_validator

from app.core.config import settings


class WalletBase(BaseModel):
    """Кошелек."""

    balance: float = Field(..., description="Баланс", ge=0)
    owner: int = Field(..., description="Владелец кошелька")


class WalletRead(WalletBase):
    """Информация по кошельку."""


class WalletUpdate(BaseModel):
    """Обновление кошелька."""

    operation_type: str = Field(
        ...,
        examples=[settings.DEPOSIT, settings.WITHDRAW],
        description="Действие",
    )
    amount: float = Field(..., description="Сумма", gt=0)

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
