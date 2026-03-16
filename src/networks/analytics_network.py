import asyncio
import random


async def analytics_agent(agent_id):

    print(f"📊 Analytics Agent {agent_id} analyzing markets")

    await asyncio.sleep(random.uniform(0.5, 2))

    print(f"📊 Agent {agent_id} produced insights")


async def run_analytics_network():

    tasks = []

    for i in range(100):

        tasks.append(analytics_agent(i))

    await asyncio.gather(*tasks)
