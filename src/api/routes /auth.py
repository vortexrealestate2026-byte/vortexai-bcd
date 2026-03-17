from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.core.security import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(data: LoginRequest):

    # Example authentication logic
    if data.email != "admin@example.com":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user_id="1")

    return {
        "access_token": token,
        "token_type": "bearer"
    }
