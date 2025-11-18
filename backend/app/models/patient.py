from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.DBConnection import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    phone_number = Column(String(15))
    date_of_birth = Column(Date)
    gender = Column(Enum('Male', 'Female', 'Other'))
    created_at = Column(DateTime, default=datetime.now)

    appointments = relationship("Appointment", back_populates="patient")
