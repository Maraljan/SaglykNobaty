import typing
from enum import StrEnum

from sqlmodel import SQLModel, Field, Relationship

if typing.TYPE_CHECKING:
    from .user_model import User


class RoleName(StrEnum):
    ADMIN = 'admin'
    PATIENT = 'patient'
    DOCTOR = 'doctor'


class RoleCreate(SQLModel):
    role_name: str = Field(index=True)


class RoleGet(RoleCreate):
    role_id: int


class Role(RoleCreate, table=True):
    __tablename__ = 'role'
    role_id: int | None = Field(default=None, primary_key=True)
    users: list['User'] = Relationship(back_populates='user_role')


class RoleFilter(SQLModel):
    pass