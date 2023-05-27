from fastapi import APIRouter
from .routers import role_router, user_router, auth_router

router = APIRouter(prefix='/auth')

router.include_router(role_router.router)
router.include_router(user_router.router)
router.include_router(auth_router.router)
