from sqlmodel import SQLModel, Field, Relationship


from health_time.appointment_app.models.hospital_model import Hospital


class CityCreate(SQLModel):
    city_name: str = Field(index=True)


class CityGet(CityCreate):
    city_id: int
    hospital_id: int


class City(CityCreate, table=True):
    __tablename__ = 'city'
    hospital_id: int = Field(foreign_key='hospital.hospital_id')
    city_id: int | None = Field(default=None, primary_key=True)
    hospitals: list[Hospital] = Relationship(back_populates='city')

