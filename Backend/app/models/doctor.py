from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.DBConnection import Base

class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(10))
    first_name = Column(String(50))
    last_name = Column(String(50))
    specialty = Column(String(100))
    email = Column(String(100))
    phone_number = Column(String(15))
    available_days = Column(String(50))
    available_times = Column(String(50))
    experience_years = Column(Integer)
    room_number = Column(String(10))

    appointments = relationship("Appointment", back_populates="doctor")
