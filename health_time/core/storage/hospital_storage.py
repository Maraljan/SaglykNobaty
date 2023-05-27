from typing import Annotated
from fastapi import Depends
from sqlmodel.sql.expression import SelectOfScalar

from .storage import Storage
from health_time.appointment_app.models.city_model import City
from health_time.appointment_app.models.hospital_model import (
    Hospital,
    HospitalCreate,
    HospitalFilter,
)


class HospitalStorage(Storage[Hospital, HospitalCreate, HospitalFilter]):
    model = Hospital
    pk = Hospital.hospital_id

    def _apply_filter(
        self,
        statement: SelectOfScalar,
        filters: HospitalFilter,
    ) -> SelectOfScalar:
        if filters.city is not None:
            statement = (
                statement.join(City)
                .where(City.city_name == filters.city)
            )
        return statement


HospitalStorageDepends = Annotated[HospitalStorage, Depends(HospitalStorage)]


