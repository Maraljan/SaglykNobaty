from sqlmodel import SQLModel, Field


class DepartmentCreate(SQLModel):
    department_name: str = Field(index=True)


class DepartmentGet(DepartmentCreate):
    department_id: int


class Department(DepartmentCreate, table=True):
    __tablename__ = 'department'
    department_id: int | None = Field(default=None, primary_key=True)
