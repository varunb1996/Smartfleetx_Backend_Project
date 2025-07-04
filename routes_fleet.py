from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_fleets():
    return {"fleets": ["Fleet A", "Fleet B"]}
