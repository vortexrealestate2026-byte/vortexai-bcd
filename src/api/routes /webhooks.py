from fastapi import APIRouter, Request

router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])


@router.post("/lead")
async def lead_webhook(request: Request):
    data = await request.json()
    return {"received": data}
