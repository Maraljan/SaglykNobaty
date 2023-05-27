from typing import Annotated

import sqlmodel
from fastapi import Depends

from .storage import Storage
from health_time.auth.models.user_model import User, UserCreate
from .role_storage import RoleStorageDepends
from ...auth.models.role_model import RoleName
from health_time.auth.auth import AUTH


class UserStorage(Storage[User, UserCreate]):
    model = User
    pk = User.user_id

    async def _create_instance(self, create_data: UserCreate) -> User:
        role_storage = RoleStorageDepends(self.session)
        patient_role = await role_storage.get_by_name(RoleName.PATIENT)
        user = User(user_role=patient_role, hashed_password=AUTH.hash_password(create_data.password), **create_data.dict())
        return user

    async def get_by_email(self, email: str) -> User | None:
        statement = sqlmodel.select(User).where(User.email == email)
        response = await self.session.execute(statement)
        return response.scalar_one_or_none()


UserStorageDepends = Annotated[UserStorage, Depends(UserStorage)]

