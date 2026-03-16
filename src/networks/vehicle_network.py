import asyncio
import random


async def vehicle_agent(agent_id):

    print(f"🚗 Vehicle Agent {agent_id} scanning inventory")

    await asyncio.sleep(random.uniform(0.5, 2))

    print(f"🚗 Agent {agent_id} found financing opportunity")


async def run_vehicle_network():

    tasks = []

    for i in range(100):

        tasks.append(vehicle_agent(i))

    await asyncio.gather(*tasks)
