async def generate_loan(vehicle):

    price = vehicle["price"]

    down = int(price * 0.10)
    loan = price - down

    application = {

        "vehicle": vehicle,
        "down_payment": down,
        "loan_amount": loan,
        "status": "pending"

    }

    print("💰 Loan created:", application)

    return application
