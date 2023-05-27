from sqlmodel import SQLModel, Field, Relationship

from .hospital_model import Hospital


class DepartmentCreate(SQLModel):
    department_name: str = Field(index=True)
    hospital_id: int = Field(foreign_key='hospital.hospital_id')


class DepartmentGet(DepartmentCreate):
    department_id: int


class Department(DepartmentCreate, table=True):
    __tablename__ = 'department'
    department_id: int | None = Field(default=None, primary_key=True)
    hospital: Hospital = Relationship(back_populates='departments')


class DepartmentFilter(SQLModel):
    pass
