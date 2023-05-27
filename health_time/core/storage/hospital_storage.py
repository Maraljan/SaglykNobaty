from typing import Annotated
from fastapi import Depends

from .storage import Storage
from health_time.appointment_app.models.hospital_model import Hospital, HospitalCreate


class HospitalStorage(Storage[Hospital, HospitalCreate]):
    model = Hospital
    pk = Hospital.city_id


HospitalStorageDepends = Annotated[HospitalStorage, Depends(HospitalStorage)]






