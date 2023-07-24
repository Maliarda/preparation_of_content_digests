import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from starlette.testclient import TestClient

from src.core.database import get_async_session
from src.core.settings import settings
from src.main import app
from src.models.models import Base, User


test_engine = create_async_engine(
    settings.postgres.url_test,
    future=True,
    echo=True,
    poolclass=NullPool,
)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def override_db():
    async with TestingSessionLocal() as session:
        user = User(
            name="sneakyfox",
            user_id="a29e7712-c6aa-4833-bfd0-79522cd5c3ae",
        )
        session.add(user)
        await session.commit()
        yield session


@pytest_asyncio.fixture(autouse=True, scope="function")
async def init_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def client():
    app.dependency_overrides = {get_async_session: override_db}
    with TestClient(app) as client:
        yield client
