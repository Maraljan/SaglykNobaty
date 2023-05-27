from fastapi import APIRouter

from health_time.appointment_app.models.appointment_model import (
    Appointment,
    AppointmentGet,
    AppointmentCreate,
    AppointmentCreateByPatient,
)

from health_time.core.storage.appointment_storage import (
    AppointmentStorageDepends,
)
from health_time.auth.dependecies import CurrentPatient

router = APIRouter(prefix='/appointment', tags=['Appointment'])


@router.post('/')
async def create_appointment(
    patient: CurrentPatient,
    storage: AppointmentStorageDepends,
    appointment_create: AppointmentCreateByPatient,
) -> AppointmentGet:
    create_data = AppointmentCreate(
        patient_id=patient.user_id,
        **appointment_create.dict(),
    )
    return await storage.create_object(create_data)


@router.get('/')
async def get_appointments(
    storage: AppointmentStorageDepends,
) -> list[AppointmentGet]:
    return await storage.get_objects()


@router.get('/{appointment_id}')
async def get_appointment(
    appointment_id: int,
    storage: AppointmentStorageDepends,
) -> AppointmentGet:
    return await storage.get_obj(appointment_id)


@router.delete('/{appointment_id}')
async def delete_appointment(
    appointment_id: int,
    storage: AppointmentStorageDepends,
):
    await storage.delete_object(appointment_id)
