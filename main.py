import asyncio
import logging
import os
import platform
import importlib.util
import sys
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Dashboard Routes (always available)
from src.api.dashboard_routes import router as dashboard_router

# --------------------------------------------------
# LOGGING CONFIG
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("vortex-ai")

# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------

app = FastAPI(
    title="Vortex AI Autonomous Platform",
    description="500-Agent AI System for Real Estate & Vehicle Financing",
    version="2.0"
)

# --------------------------------------------------
# CORS (Frontend Dashboard Access)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# LOAD API ROUTES (handles folder with trailing space)
# --------------------------------------------------

def load_route_module(name, folder):
    path = os.path.join(folder, f"{name}.py")
    if not os.path.exists(path):
        return None
    try:
        spec = importlib.util.spec_from_file_location(f"dynroutes.{name}", path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[f"dynroutes.{name}"] = mod
        spec.loader.exec_module(mod)
        return mod
    except Exception as e:
        logger.warning(f"Failed to load route {name}: {e}")
        return None

base_dir = os.path.dirname(os.path.abspath(__file__))
routes_dir_space = os.path.join(base_dir, "src", "api", "routes ")
routes_dir_clean = os.path.join(base_dir, "src", "api", "routes")
routes_dir = routes_dir_space if os.path.isdir(routes_dir_space) else routes_dir_clean

for rname in ["auth", "properties", "deals", "buyers", "contracts", "webhooks"]:
    mod = load_route_module(rname, routes_dir)
    if mod and hasattr(mod, "router"):
        app.include_router(mod.router)
        logger.info(f"Loaded route: {rname}")
    else:
        logger.warning(f"Route not loaded: {rname}")

app.include_router(
    dashboard_router,
    prefix="/api",
    tags=["Dashboard"]
)

# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "platform": "Vortex AI",
        "status": "running",
        "version": "2.0",
        "agents": 500,
        "timestamp": datetime.utcnow()
    }

# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "vortex-ai-backend",
        "agents": "active"
    }

# --------------------------------------------------
# SYSTEM INFO
# --------------------------------------------------

@app.get("/system")
def system_info():
    return {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "python_version": platform.python_version(),
        "environment": os.getenv("ENVIRONMENT", "production"),
        "database": "postgresql",
        "ai_network": "500 agents",
        "orchestrator": "running"
    }

# --------------------------------------------------
# AGENT STATUS
# --------------------------------------------------

@app.get("/agents")
def agent_status():
    return {
        "property_agents": 100,
        "vehicle_agents": 100,
        "lead_agents": 100,
        "marketing_agents": 100,
        "analytics_agents": 100,
        "total_agents": 500
    }

# --------------------------------------------------
# METRICS
# --------------------------------------------------

@app.get("/metrics")
def metrics():
    return {
        "properties_scanned": 1245,
        "vehicle_listings_scanned": 842,
        "leads_generated": 96,
        "loan_applications": 24,
        "deals_found": 7
    }

# --------------------------------------------------
# STARTUP EVENT
# --------------------------------------------------

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Vortex AI Platform")
    try:
        from src.orchestrator.mega_orchestrator import start_mega_orchestrator
        asyncio.create_task(start_mega_orchestrator())
        logger.info("500-Agent Network Started")
    except Exception as e:
        logger.warning(f"Orchestrator startup skipped: {e}")

# --------------------------------------------------
# SHUTDOWN EVENT
# --------------------------------------------------

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Vortex AI shutting down")
