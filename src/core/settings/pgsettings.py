from pydantic import BaseModel, PostgresDsn


class PostgreSQLSettings(BaseModel):
    """Database Settings"""

    echo: bool = False

    url: PostgresDsn = 'postgresql+asyncpg://postgres:password@localhost:5432/postgresdb' # noqa
    url_test: PostgresDsn = 'postgresql+asyncpg://postgres:password@localhost:5432/postgresdb_test' # noqa

    pool_size: int = 1
    max_overflow: int = 5
    pool_timeout: int = 30
    pool_recycle: int = -1
    pool_pre_ping: bool = False
