from fastapi import APIRouter
from .routers import (
    doctor_appointment,
)

router = APIRouter(prefix='/doctor-cabinet', tags=['Doctor Cabinet'])

router.include_router(doctor_appointment.router)