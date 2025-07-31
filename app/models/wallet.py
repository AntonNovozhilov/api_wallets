from sqlalchemy import CheckConstraint, Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base




class Wallet(Base):
    """Кошелек."""

    balance = Column(Integer, nullable=False, default=0)
    owner = Column(ForeignKey("user.id"))

    user = relationship("User", back_populates="wallets")

    __table_args__ = (CheckConstraint('balance >= 0'))
