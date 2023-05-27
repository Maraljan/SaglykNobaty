from typing import Annotated
from fastapi import Depends
from sqlmodel.sql.expression import SelectOfScalar

from .storage import Storage
from health_time.appointment_app.models.hospital_model import Hospital, HospitalCreate, HospitalFilter
from ...appointment_app.models.city_model import City


class HospitalStorage(Storage[Hospital, HospitalCreate]):
    model = Hospital
    pk = Hospital.city_id

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
