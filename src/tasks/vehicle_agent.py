import asyncio
import random
from src.services.deal_analyzer import analyze_vehicle

CARS = [
    ("Toyota","Camry"),
    ("Honda","Civic"),
    ("Ford","F150"),
    ("Chevy","Silverado")
]

async def run_vehicle_agent():

    while True:

        car = random.choice(CARS)

        price = random.randint(4000,18000)
        market = random.randint(12000,25000)

        result = analyze_vehicle(price,market)

        print(f"🚗 Vehicle scan {car[0]} {car[1]} price={price} market={market}")

        if result["score"] >= 7:
            print(f"🔥 FINANCE DEAL {car[0]} {car[1]} profit={result['margin']}")

        await asyncio.sleep(20)
