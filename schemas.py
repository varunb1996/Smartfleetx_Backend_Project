from pydantic import BaseModel

class VehicleData(BaseModel):
    vehicle_id: str
    speed: float
    temperature: float
    latitude: float
    longitude: float
