from sqlmodel import SQLModel, Field, Relationship

from health_time.appointment_app.models.hospital_model import Hospital


class DepartmentCreate(SQLModel):
    department_name: str = Field(index=True)


class DepartmentGet(DepartmentCreate):
    department_id: int
    hospital_id: int


class Department(DepartmentCreate, table=True):
    __tablename__ = 'department'
    hospital_id: int = Field(foreign_key='hospital.hospital_id')
    department_id: int | None = Field(default=None, primary_key=True)
    hospitals: list[Hospital] = Relationship(back_populates='department')
