from typing import Annotated
from fastapi import Depends

from .storage import Storage
from health_time.appointment_app.models.department_model import Department, DepartmentCreate


class DepartmentStorage(Storage[Department, DepartmentCreate]):
    model = Department
    pk = Department.department_id


DepartmentStorageDepends = Annotated[DepartmentStorage, Depends(DepartmentStorage)]

