from pydantic import BaseModel
from datetime import datetime


class APIResponse(BaseModel):
    success: bool = True
    message: str | None = None
    data: dict | list | None = None


class Timestamped(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None
