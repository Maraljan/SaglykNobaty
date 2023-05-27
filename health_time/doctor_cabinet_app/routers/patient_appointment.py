from fastapi import APIRouter

from health_time.appointment_app.models.appointment_model import (
    Appointment,
    AppointmentGet,
    AppointmentCreate,
    AppointmentFilter,
    AppointmentCreateByPatient,
)

from health_time.core.storage.appointment_storage import (
    AppointmentStorageDepends,
)
from health_time.auth.dependecies import CurrentPatient

router = APIRouter(prefix='/patient-appointment', tags=['Patient-Appointment'])


@router.get('/get-my-appointments')
async def get_appointments(
    patient: CurrentPatient,
    storage: AppointmentStorageDepends,
) -> list[AppointmentGet]:
    filters = AppointmentFilter(
        patient_id=patient.user_id,
    )
    return await storage.get_objects(filters=filters)
