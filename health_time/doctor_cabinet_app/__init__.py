from fastapi import APIRouter
from .routers import (
    patient_appointment,
)

router = APIRouter(prefix='/patient-cabinet', tags=['User Cabinet'])

router.include_router(patient_appointment.router)