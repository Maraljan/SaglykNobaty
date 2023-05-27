from fastapi import APIRouter, Depends

from health_time.core.queries import Pagination
from health_time.core.storage.hospital_storage import HospitalStorageDepends
from health_time.appointment_app.models.hospital_model import (
    HospitalGet,
    HospitalCreate,
    Hospital,
    HospitalFilter,
)

router = APIRouter(prefix='/hospital', tags=['Hospital'])


@router.post('/')
async def create_hospital(
    hospital_create: HospitalCreate,
    storage: HospitalStorageDepends,
) -> HospitalGet:
    return await storage.create_object(hospital_create)


@router.get('/')
async def get_hospitals(
    storage: HospitalStorageDepends,
    pagination: Pagination = Depends(Pagination),
    filters: HospitalFilter = Depends(HospitalFilter),
) -> list[Hospital]:
    return await storage.get_objects(
        pagination=pagination,
        filters=filters,
    )


@router.delete('/{hospital_id}')
async def delete_hospital(hospital_id: int, storage: HospitalStorageDepends):
    await storage.delete_object(hospital_id)