from app.core.db import Base
from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Wallet(Base):
    """Кошелек."""

    balance = Column(Integer, nullable=False, default=0)
    owner = Column(ForeignKey("user.id"))

    user = relationship("User", back_populates="wallets")

    __table_args__ = (CheckConstraint("balance >= 0"),)
