from fastapi import APIRouter

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

vehicles_db = []

@router.get("/")
def get_vehicles():
    return {"vehicles": vehicles_db}

@router.post("/")
def add_vehicle(data: dict):
    vehicles_db.append(data)
    return {"message": "vehicle added", "vehicle": data}
