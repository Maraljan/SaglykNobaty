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
from health_time.auth.dependecies import CurrentDoctor

router = APIRouter(prefix='/doctor-appointment', tags=['Doctor-Appointment'])


@router.get('/get-my-appointments')
async def get_appointments(
    doctor: CurrentDoctor,
    storage: AppointmentStorageDepends,
) -> list[AppointmentGet]:
    filters = AppointmentFilter(
        doctor_id=doctor.user_id,
    )
    return await storage.get_objects(filters=filters)

