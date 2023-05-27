from fastapi import APIRouter

from ..models.hospital_model import HospitalGet, HospitalCreate
from health_time.core.storage.hospital_storage import HospitalStorageDepends

router = APIRouter(prefix='/hospital', tags=['Hospital'])


@router.post('/')
async def create_hospital(hospital_create: HospitalCreate, storage: HospitalStorageDepends) -> HospitalGet:
    return storage.create_object(hospital_create)


@router.get('/')
async def get_hospitals(storage: HospitalStorageDepends) -> list[HospitalGet]:
    return storage.get_objects()


@router.delete('/{hospital_id}')
async def delete_hospital(hospital_id: int, storage: HospitalStorageDepends):
    await storage.delete_object(hospital_id)
