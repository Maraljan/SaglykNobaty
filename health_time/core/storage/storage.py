from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type

import sqlmodel
from sqlmodel.sql.expression import SelectOfScalar
from fastapi import HTTPException, status

from health_time.core.queries import Pagination
from health_time.core.database import DbSession

_DbModel = TypeVar('_DbModel', bound=sqlmodel.SQLModel)
_CreateModel = TypeVar('_CreateModel', bound=sqlmodel.SQLModel)
_FilterModel = TypeVar('_FilterModel', bound=sqlmodel.SQLModel)


class Storage(Generic[_DbModel, _CreateModel, _FilterModel], ABC):

    model: Type[_DbModel] = NotImplemented
    pk = NotImplemented

    def __init__(self, session:  DbSession):
        self.session = session

    async def get_objects(
        self,
        pagination: Pagination | None = None,
        filters: _FilterModel | None = None,
    ) -> list[_DbModel]:
        pagination = pagination or Pagination()
        statement = (
            sqlmodel.select(self.model)
            .offset(pagination.offset)
            .limit(pagination.limit)
        )

        if filters:
            statement = self._apply_filter(statement, filters)

        response = await self.session.execute(statement)
        return response.scalars().all()

    async def get_obj(self, pk: int) -> _DbModel:
        obj = await self.session.get(self.model, pk)
        if obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return obj

    async def create_object(self, create_data: _CreateModel) -> _DbModel:
        create_obj = await self._create_instance(create_data)
        self.session.add(create_obj)
        await self.session.commit()
        await self.session.refresh(create_obj)
        return create_obj

    async def delete_object(self, pk: int):
        statement = sqlmodel.delete(self.model).where(self.pk == pk)
        await self.session.execute(statement)
        await self.session.commit()

    async def _create_instance(self, create_data: _CreateModel) -> _DbModel:
        return self.model.from_orm(create_data)

    @abstractmethod
    def _apply_filter(
        self,
        statement: SelectOfScalar,
        filters: _FilterModel,
    ) -> SelectOfScalar:
        pass
