from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.tasks.scheduler import launch_all_agents
from app.database import engine
from app.models import Base

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="VORTEX API")

# -------------------------------
# CORS
# -------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Health Check
# -------------------------------

@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------------------
# Start AI Agents
# -------------------------------

@app.get("/start-agents")
def start_agents():
    launch_all_agents.delay()
    return {"status": "AI agents launched"}

# -------------------------------
# Real Estate API
# -------------------------------

@app.get("/properties")
def get_properties():
    return []

@app.get("/deals")
def get_deals(min_score: int | None = None, max_price: int | None = None):
    return []

# -------------------------------
# Buyers
# -------------------------------

@app.get("/buyers")
def get_buyers():
    return []

@app.post("/buyers")
def create_buyer(buyer: dict):
    return {**buyer, "id": "temp-id"}

# -------------------------------
# Vehicle System
# -------------------------------

@app.get("/vehicles")
def get_vehicles():
    return []

@app.get("/leads")
def get_leads():
    return []

# -------------------------------
# Financing approvals
# -------------------------------

@app.get("/approvals")
def get_approvals():
    return []
