from fastapi import APIRouter

router = APIRouter(prefix="/api/contracts", tags=["contracts"])


@router.get("/")
def get_contracts():
    return {"contracts": []}


@router.post("/")
def create_contract(data: dict):
    return {"message": "contract created"}
