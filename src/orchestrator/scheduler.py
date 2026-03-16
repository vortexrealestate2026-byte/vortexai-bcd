import asyncio
from src.orchestrator.agent_router import run_all_agents


async def run_scheduler():

    while True:

        print("⚡ Running 50-Agent Network")

        await run_all_agents()

        print("⚡ Cycle Complete")

        await asyncio.sleep(60)
