from sqlalchemy import CheckConstraint, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Wallet(Base):
    """Кошелек."""

    balance = Column(Float, nullable=False, default=0)
    owner = Column(ForeignKey("user.id"))

    user = relationship("User", back_populates="wallets")

    __table_args__ = (CheckConstraint("balance >= 0"),)
