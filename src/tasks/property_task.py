import asyncio
import random
from src.services.deal_analyzer import analyze_property

CITIES = [
    "Atlanta",
    "Dallas",
    "Houston",
    "Phoenix",
    "Tampa"
]

async def run_property_agent():

    while True:

        city = random.choice(CITIES)

        price = random.randint(90000,250000)
        arv = random.randint(250000,400000)

        result = analyze_property(price,arv)

        print(f"🔎 Property scan {city} price={price} arv={arv}")

        if result["score"] >= 7:
            print(f"🔥 DEAL FOUND {city} profit={result['margin']}")

        await asyncio.sleep(15)
