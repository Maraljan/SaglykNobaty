from fastapi import APIRouter
from .routers import city_router, hospital_router, department_router

router = APIRouter(prefix='/appointment_app')

router.include_router(city_router.router)
router.include_router(hospital_router.router)
router.include_router(department_router.router)
