from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlmodel.sql.expression import SelectOfScalar

from .storage import Storage
from .user_storage import UserStorage
from health_time.auth.models.user_model import User
from health_time.appointment_app.models.appointment_model import (
    Appointment,
    AppointmentCreate,
    AppointmentFilter,
)


class AppointmentStorage(
    Storage[Appointment, AppointmentCreate, AppointmentFilter],
):
    model = Appointment
    pk = Appointment.appointment_id

    async def _create_instance(
        self,
        create_data: AppointmentCreate,
    ) -> Appointment:
        user_storage = UserStorage(self.session)
        doctor = await user_storage.get_doctor_by_pk(create_data.doctor_id)

        if doctor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Could not found such doctor',
            )

        appointment = Appointment(
            doctor=doctor,
            **create_data.dict(),
        )
        return appointment

    def _apply_filter(
        self,
        statement: SelectOfScalar,
        filters: AppointmentFilter,
    ) -> SelectOfScalar:

        if filters.patient_id is not None:
            statement = (
                statement.join(User, Appointment.patient_id == User.user_id)
                .where(Appointment.patient_id == filters.patient_id)
            )

        if filters.doctor_id is not None:
            statement = (
                statement.join(User, Appointment.doctor_id == User.user_id)
                .where(Appointment.doctor_id == filters.doctor_id)
            )

        return statement


AppointmentStorageDepends = Annotated[
    AppointmentStorage,
    Depends(AppointmentStorage),
]