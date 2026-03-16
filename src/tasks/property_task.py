import asyncio
import random

US_CITIES = [
    "Atlanta",
    "Houston",
    "Dallas",
    "Phoenix",
    "Tampa",
    "Orlando",
    "Charlotte"
]

async def run_property_agent():

    while True:

        city = random.choice(US_CITIES)

        print(f"🔎 Scanning properties in {city}")

        # simulate deal detection
        price = random.randint(90000, 250000)
        arv = random.randint(250000, 400000)

        if price < arv * 0.6:
            print(f"🔥 DEAL FOUND in {city} price={price} arv={arv}")

        await asyncio.sleep(15)
