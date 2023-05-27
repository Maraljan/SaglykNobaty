from typing import Annotated
from fastapi import Depends
from sqlmodel.sql.expression import SelectOfScalar

from .storage import Storage
from health_time.appointment_app.models.department_model import Department, DepartmentCreate, DepartmentFilter


class DepartmentStorage(Storage[Department, DepartmentCreate]):
    model = Department
    pk = Department.department_id

    def _apply_filter(
            self, statement: SelectOfScalar,
            filters: DepartmentFilter
    ) -> SelectOfScalar:
        return statement


DepartmentStorageDepends = Annotated[DepartmentStorage, Depends(DepartmentStorage)]

