from sqlmodel import SQLModel, Field


class SpecialityCreate(SQLModel):
    speciality_name: str = Field(index=True)


class SpecialityGet(SpecialityCreate):
    speciality_id: int


class Speciality(SpecialityCreate, table=True):
    __tablename__ = 'speciality'
    speciality_id: int | None = Field(default=None, primary_key=True)


class SpecialityFilter(SQLModel):
    city: str | None = None