from sqlalchemy import Column, Integer, ForeignKey, Date, Time, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.DBConnection import Base


class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"))
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    created_at = Column(DateTime, default=datetime.now)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
