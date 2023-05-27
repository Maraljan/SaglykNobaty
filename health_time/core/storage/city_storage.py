from typing import Annotated
from fastapi import Depends

from .storage import Storage
from health_time.appointment_app.models.city_model import City, CityCreate


class CityStorage(Storage[City, CityCreate]):
    model = City
    pk = City.city_id


CityStorageDepends = Annotated[CityStorage, Depends(CityStorage)]






