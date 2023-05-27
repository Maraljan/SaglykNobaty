from fastapi import APIRouter

from health_time.auth.models.role_model import RoleCreate, RoleGet

from health_time.core.storage.role_storage import RoleStorageDepends
router = APIRouter(prefix='/role', tags=['Role'])


@router.post('/')
async def role_city(role_create: RoleCreate, storage: RoleStorageDepends) -> RoleGet:
    return await storage.create_object(role_create)


@router.get('/')
async def get_roles(storage: RoleStorageDepends) -> list[RoleGet]:
    return await storage.get_objects()


@router.delete('/{role_id}')
async def delete_city(role_id: int, storage: RoleStorageDepends):
    await storage.delete_object(role_id)
