from fastapi import FastAPI
import asyncio

from src.orchestrator.master_orchestrator import start_orchestrator

app = FastAPI()


@app.on_event("startup")
async def start_ai_system():

    print("🚀 Launching Vortex AI System")

    asyncio.create_task(start_orchestrator())


@app.get("/")
def root():
    return {"status": "Vortex AI Running"}
