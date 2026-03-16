async def find_vehicle_buyers():

    print("🚗 Searching for car buyers")

    buyers = [
        {"name": "Alex Brown", "city": "Toronto"},
        {"name": "Sara White", "city": "Calgary"}
    ]

    for buyer in buyers:
        print("Vehicle buyer lead:", buyer)
