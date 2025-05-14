from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from core import settings


class DBConnection:
    def __init__(self, url: str, echo: bool = False):
        engine = create_async_engine(url, echo=echo)
        self.async_session = async_sessionmaker(
            engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    async def get_async_session(self):
        async with self.async_session() as session:
            yield session


db_connection = DBConnection(
    url=settings.postgres.url.encoded_string(),
    echo=settings.postgres.echo,
)
