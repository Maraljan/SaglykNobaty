from fastapi import APIRouter

from health_time.appointment_app.models.department_model import DepartmentCreate, DepartmentGet

from health_time.core.storage.department_storage import DepartmentStorageDepends
router = APIRouter(prefix='/department', tags=['Department'])


@router.post('/')
async def create_department(department_create: DepartmentCreate, storage: DepartmentStorageDepends) -> DepartmentGet:
    return await storage.create_object(department_create)


@router.get('/')
async def get_departments(storage: DepartmentStorageDepends) -> list[DepartmentGet]:
    return await storage.get_objects()


@router.delete('/{department_id}')
async def delete_department(department_id: int, storage: DepartmentStorageDepends):
    await storage.delete_object(department_id)
