import datetime as dt

from sqlalchemy.orm import relationship
from sqlmodel import SQLModel, Field, Relationship

from health_time.auth.models.user_model import User


class AppointmentCreateByPatient(SQLModel):
    service_name: str
    start_time: dt.datetime = Field(default_factory=dt.datetime.utcnow)
    duration: int = Field(
        default=30,
        gt=0,
        le=3 * 60,
        description='Duration in minutes',
    )
    doctor_id: int = Field(foreign_key='user.user_id')


class AppointmentCreate(AppointmentCreateByPatient):
    patient_id: int = Field(foreign_key='user.user_id')


class AppointmentGet(AppointmentCreate):
    appointment_id: int


class Appointment(AppointmentCreate, table=True):
    __tablename__ = 'appointment'
    appointment_id: int | None = Field(default=None, primary_key=True)

    doctor: User = Relationship(
        sa_relationship=relationship(
            'user',
            foreign_keys='appointment.doctor_id',
            primaryjoin='user.user_id == appointment.doctor_id',
        ),
    )
    patient: User = Relationship(
        sa_relationship=relationship(
            'user',
            foreign_keys='appointment.patient_id',
            primaryjoin='user.user_id == appointment.patient_id',
        ),
    )


class AppointmentFilter(SQLModel):
    doctor_id: int | None = None
    patient_id: int | None = None
