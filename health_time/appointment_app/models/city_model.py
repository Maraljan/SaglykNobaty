from sqlmodel import SQLModel, Field, Relationship


from .hospital_model import Hospital


class CityCreate(SQLModel):
    city_name: str = Field(index=True)


class CityGet(CityCreate):
    city_id: int


class City(CityCreate, table=True):
    __tablename__ = 'city'
    city_id: int | None = Field(default=None, primary_key=True)
    hospitals: list[Hospital] = Relationship(back_populates='city')


class CityFilter(SQLModel):
    pass