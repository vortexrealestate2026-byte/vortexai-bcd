import asyncio
import logging

from src.scrapers.property_api import get_properties
from src.scrapers.vehicle_api import get_vehicles
from src.ai.deal_analyzer import analyze_property

logger = logging.getLogger("vortex-ai")


async def run_agent(agent_id):

    logger.info(f"Agent {agent_id} started")

    while True:

        try:

            # ----------------------
            # PROPERTY SCAN
            # ----------------------
            properties = get_properties()

            for p in properties:

                analysis = analyze_property(p)

                if analysis["deal_score"] >= 6:

                    logger.info(
                        f"🔥 DEAL FOUND | Agent {agent_id} | "
                        f"Price: {analysis['price']} | "
                        f"Margin: {analysis['wholesale_margin']} | "
                        f"Score: {analysis['deal_score']}"
                    )

            # ----------------------
            # VEHICLE SCAN
            # ----------------------
            vehicles = get_vehicles()

            logger.info(
                f"Agent {agent_id} scanned {len(vehicles)} vehicles"
            )

        except Exception as e:

            logger.error(f"Agent {agent_id} error: {str(e)}")

        await asyncio.sleep(30)


async def start_mega_orchestrator():

    logger.info("🧠 Mega Orchestrator Booting")

    tasks = []

    for i in range(500):
        tasks.append(asyncio.create_task(run_agent(i)))

    logger.info("⚡ 500 agents launched")

    await asyncio.gather(*tasks)
