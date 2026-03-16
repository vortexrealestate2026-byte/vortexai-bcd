import asyncio
from src.tasks.property_task import run_property_agent

async def launch_all_agents():

    print("🚀 Launching Vortex AI agents")

    agents = [
        asyncio.create_task(run_property_agent()),
    ]

    await asyncio.gather(*agents)
