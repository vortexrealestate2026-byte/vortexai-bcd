import asyncio
import random


async def marketing_agent(agent_id):

    print(f"📣 Marketing Agent {agent_id} promoting deals")

    await asyncio.sleep(random.uniform(0.5, 2))

    print(f"📣 Agent {agent_id} posted new campaign")


async def run_marketing_network():

    tasks = []

    for i in range(100):

        tasks.append(marketing_agent(i))

    await asyncio.gather(*tasks)
