import asyncio
import random

CITIES = [
    "Winnipeg",
    "Steinbach",
    "Regina",
    "Calgary"
]

CARS = [
    ("Toyota","Camry"),
    ("Honda","Civic"),
    ("Ford","F150"),
    ("Chevy","Silverado")
]

async def run_vehicle_agent():

    while True:

        city = random.choice(CITIES)
        car = random.choice(CARS)
        price = random.randint(5000, 20000)

        print(f"🚗 Vehicle scan {car[0]} {car[1]} in {city} price={price}")

        if price < 9000:
            print(f"🔥 FINANCE DEAL FOUND {car[0]} {car[1]} {price}")

        await asyncio.sleep(20)
