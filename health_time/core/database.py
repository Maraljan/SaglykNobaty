from typing import AsyncIterator, Annotated

from fastapi import Depends
from sqlmodel import SQLModel

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession, AsyncConnection, create_async_engine

DB_TYPE = 'postgresql+asyncpg'
USERNAME = 'postgres'
PASSWORD = '3101'
HOST = '127.0.0.1'
PORT = '5432'
DB = 'HealthTime'


class DataBase:
    def __init__(self):

        self._engine = create_async_engine(f"{ DB_TYPE }://{ USERNAME }:{ PASSWORD }@{ HOST }:{ PORT }/{ DB }")
        self._session_factory = sessionmaker(self._engine, class_=AsyncSession, expire_on_commit=False)

    async def get_session(self) -> AsyncIterator[AsyncSession]:
        async with self._session_factory() as session:
            yield session

    async def connect(self):
        async with self._engine.begin() as connection:  # type: AsyncConnection
            await connection.run_sync(SQLModel.metadata.create_all)


DATA_BASE = DataBase()

DbSession = Annotated[AsyncSession, Depends(DATA_BASE.get_session)]
