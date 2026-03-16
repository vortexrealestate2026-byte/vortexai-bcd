import asyncio
from src.tasks.property_task import run_property_agent
from src.tasks.vehicle_agent import run_vehicle_agent

async def launch_all_agents():

    print("🚀 Launching Vortex AI agents")

    agents = [
        asyncio.create_task(run_property_agent()),
        asyncio.create_task(run_vehicle_agent()),
    ]

    await asyncio.gather(*agents)
