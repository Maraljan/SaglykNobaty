from pydantic import EmailStr

from sqlmodel import SQLModel, Field, Relationship

from .role_model import Role


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: EmailStr = Field(index=True, unique=True)
    user_image: str | None = None
    phone_number: str | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserGet(UserBase):
    user_id: int
    user_role: Role


class User(UserCreate, table=True):
    __tablename__ = 'user'
    user_id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    role_id: int = Field(foreign_key='role.role_id')
    user_role: Role = Relationship(back_populates='users', sa_relationship_kwargs={'lazy': 'selectin'})

