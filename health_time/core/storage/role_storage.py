from typing import Annotated

import sqlmodel
from fastapi import Depends

from .storage import Storage
from health_time.auth.models.role_model import Role, RoleCreate, RoleName


class RoleStorage(Storage[Role, RoleCreate]):
    model = Role
    pk = Role.role_id

    async def get_by_name(self, role_name: RoleName) -> Role:
        statement = sqlmodel.select(Role).where(Role.role_name == role_name)
        response = await self.session.execute(statement)
        return response.scalar()


RoleStorageDepends = Annotated[RoleStorage, Depends(RoleStorage)]
