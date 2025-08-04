import pytest
import pytest_asyncio
from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base, get_async_session
from app.core.users import current_superuser, current_user
from app.main import app
from app.models.users import User
from app.models.wallet import Wallet

TEST_DB = "test.db"
SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///{str(TEST_DB)}"
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    bind=engine,
)


async def override_db():
    async with TestingSessionLocal() as session:
        yield session


@pytest_asyncio.fixture
async def test_user():
    async with TestingSessionLocal() as session:
        user = User(
            id=1,
            email="user@example.com",
            hashed_password="123",
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


@pytest_asyncio.fixture
async def test_superuser():
    async with TestingSessionLocal() as session:
        user = User(
            id=2,
            email="user2@example.com",
            hashed_password="1232",
            is_active=True,
            is_superuser=True,
            is_verified=True,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


@pytest_asyncio.fixture
async def test_wallet():
    async with TestingSessionLocal() as session:
        wallet = Wallet(id=1, balance=1000, owner=1)
        session.add(wallet)
        await session.commit()
        await session.refresh(wallet)
        return wallet


@pytest_asyncio.fixture(autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


def override_user(user):
    return user


def override_super_user(user):
    return user


def raise_forbidden():
    raise HTTPException(status_code=403, detail="Forbidden")


@pytest.fixture
def not_auth_test_client():
    app.dependency_overrides[get_async_session] = override_db
    app.dependency_overrides[current_user] = lambda: None
    app.dependency_overrides[current_superuser] = lambda: None
    with TestClient(app) as client:
        yield client


@pytest.fixture
def test_client(test_user):
    app.dependency_overrides = {}
    app.dependency_overrides[get_async_session] = override_db
    app.dependency_overrides[current_user] = lambda: test_user
    app.dependency_overrides[current_superuser] = lambda: raise_forbidden
    with TestClient(app) as client:
        yield client


@pytest.fixture
def client_with_superuser(test_superuser):
    app.dependency_overrides = {}
    app.dependency_overrides[get_async_session] = override_db
    app.dependency_overrides[current_user] = lambda: test_superuser
    app.dependency_overrides[current_superuser] = lambda: test_superuser
    with TestClient(app) as client:
        yield client
