import asyncio
import logging

logger = logging.getLogger("vortex-ai")

async def run_agent(agent_id):

    while True:

        logger.info(f"Agent {agent_id} running task")

        await asyncio.sleep(10)


async def start_mega_orchestrator():

    logger.info("🧠 Mega Orchestrator Booting")

    tasks = []

    for i in range(500):

        tasks.append(asyncio.create_task(run_agent(i)))

    logger.info("⚡ 500 agents launched")

    await asyncio.gather(*tasks)
