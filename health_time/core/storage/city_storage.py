from typing import Annotated
from fastapi import Depends
from sqlmodel.sql.expression import SelectOfScalar

from .storage import Storage, _FilterModel
from health_time.appointment_app.models.city_model import (
    City,
    CityCreate,
    CityFilter,
)


class CityStorage(Storage[City, CityCreate, CityFilter]):
    model = City
    pk = City.city_id

    def _apply_filter(
        self, statement: SelectOfScalar,
        filters: CityFilter,
    ) -> SelectOfScalar:
        return statement


CityStorageDepends = Annotated[CityStorage, Depends(CityStorage)]
