from fastapi import APIRouter

router = APIRouter(prefix="/api/properties", tags=["properties"])


@router.get("/")
def get_properties():
    return {"properties": []}


@router.get("/{property_id}")
def get_property(property_id: int):
    return {"id": property_id}


@router.post("/")
def create_property(data: dict):
    return {"message": "property created"}
