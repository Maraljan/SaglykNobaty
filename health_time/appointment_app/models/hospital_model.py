import typing

from sqlmodel import SQLModel, Field, Relationship

if typing.TYPE_CHECKING:
    from .city_model import City
    from .department_model import Department


class HospitalCreate(SQLModel):
    hospital_name: str = Field(index=True)
    hospital_address: str = Field(index=True)
    hospital_photo: str | None = None
    city_id: int = Field(foreign_key='city.city_id')


class HospitalGet(HospitalCreate):
    hospital_id: int


class Hospital(HospitalCreate, table=True):
    __tablename__ = 'hospital'
    hospital_id: int | None = Field(default=None, primary_key=True)
    city: 'City' = Relationship(back_populates='hospitals')
    departments: list['Department'] = Relationship(back_populates='hospital')


class HospitalFilter(SQLModel):
    city: str | None = None