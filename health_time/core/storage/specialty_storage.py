from typing import Annotated
from fastapi import Depends

from .storage import Storage
from health_time.appointment_app.models.speciality_model import Speciality, SpecialityCreate


class SpecialtyStorage(Storage[Speciality, SpecialityCreate]):
    model = Speciality


SpecialtyStorageDepends = Annotated[SpecialtyStorage, Depends(SpecialtyStorage)]






