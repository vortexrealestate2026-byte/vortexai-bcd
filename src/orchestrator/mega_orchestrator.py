import asyncio
from src.agents.property_agent import run_property_agent

async def start_mega_orchestrator():

    while True:

        run_property_agent()

        await asyncio.sleep(60)
