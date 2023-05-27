from fastapi import APIRouter

from health_time.appointment_app.models.speciality_model import SpecialityCreate, SpecialityGet

from health_time.core.storage.specialty_storage import SpecialtyStorageDepends
router = APIRouter(prefix='/specialty', tags=['Specialty'])


@router.post('/')
async def create_specialty(specialty_create: SpecialityCreate, storage: SpecialtyStorageDepends) -> SpecialityGet:
    return await storage.create_object(specialty_create)


@router.get('/')
async def get_specialties(storage: SpecialtyStorageDepends) -> list[SpecialityGet]:
    return await storage.get_objects()


@router.delete('/{specialty_id}')
async def specialty_city(specialty_id: int, storage: SpecialtyStorageDepends):
    await storage.delete_object(specialty_id)
