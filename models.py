from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String, index=True)
    speed = Column(Float)
    temperature = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
