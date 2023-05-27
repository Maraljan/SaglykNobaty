from fastapi import APIRouter

from health_time.auth.models.user_model import UserGet, UserCreate

from health_time.core.storage.user_storage import UserStorageDepends
router = APIRouter(prefix='/user', tags=['User'])


@router.post('/')
async def create_user(user_create: UserCreate, storage: UserStorageDepends) -> UserGet:
    return await storage.create_object(user_create)


@router.get('/')
async def get_users(storage: UserStorageDepends) -> list[UserGet]:
    return await storage.get_objects()


@router.get('/{user_id}')
async def get_user(user_id: int, storage: UserStorageDepends) -> list[UserGet]:
    return await storage.get_obj(user_id)


@router.delete('/{user_id}')
async def delete_user(user_id: int, storage: UserStorageDepends):
    await storage.delete_object(user_id)
