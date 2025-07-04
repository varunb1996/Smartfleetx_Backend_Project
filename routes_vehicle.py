from fastapi import APIRouter
from app.schemas import VehicleData

router = APIRouter()

@router.post("/telemetry")
def receive_data(data: VehicleData):
    if data.temperature > 100:
        return {"anomaly": True, "message": "Overheating detected!"}
    return {"anomaly": False, "status": "ok"}
