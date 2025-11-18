from sqlalchemy import Column, Integer, String, Text, DECIMAL
from app.db.DBConnection import Base

class Test(Base):
    __tablename__ = "tests"

    test_id = Column(Integer, primary_key=True, autoincrement=True)
    test_name = Column(String(100))
    description = Column(Text)
    price = Column(DECIMAL(8,2))
    duration_minutes = Column(Integer)
    preparation = Column(Text)
