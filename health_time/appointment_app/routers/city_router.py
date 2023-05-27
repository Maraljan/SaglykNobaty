from fastapi import APIRouter

from health_time.appointment_app.models.city_model import CityCreate, CityGet

from health_time.core.storage.city_storage import CityStorageDepends
router = APIRouter(prefix='/city', tags=['City'])


@router.post('/')
async def create_city(city_create: CityCreate, storage: CityStorageDepends) -> CityGet:
    return await storage.create_object(city_create)


@router.get('/')
async def get_cities(storage: CityStorageDepends) -> list[CityGet]:
    return storage.get_objects()


@router.delete('/{city_id}')
async def delete_city(city_id: int, storage: CityStorageDepends):
    await storage.delete_object(city_id)
