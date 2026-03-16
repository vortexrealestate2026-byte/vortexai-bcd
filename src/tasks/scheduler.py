import asyncio
from src.tasks.agent_scheduler import launch_all_agents


async def start_scheduler():
    print("⏱ Scheduler started")

    while True:
        await launch_all_agents()
        await asyncio.sleep(300)  # run every 5 minutes
