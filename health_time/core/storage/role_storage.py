from typing import Annotated

import sqlmodel
from fastapi import Depends
from sqlmodel.sql.expression import SelectOfScalar

from .storage import Storage
from health_time.auth.models.role_model import (
    Role,
    RoleCreate,
    RoleName,
    RoleFilter,
)


class RoleStorage(Storage[Role, RoleCreate, RoleFilter]):
    model = Role
    pk = Role.role_id

    async def get_by_name(self, role_name: RoleName) -> Role:
        statement = sqlmodel.select(Role).where(Role.role_name == role_name)
        response = await self.session.execute(statement)
        return response.scalar()

    def _apply_filter(
        self,
        statement: SelectOfScalar,
        filters: RoleFilter
    ) -> SelectOfScalar:
        return statement


RoleStorageDepends = Annotated[RoleStorage, Depends(RoleStorage)]
