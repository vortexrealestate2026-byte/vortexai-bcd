async def submit_to_bank(application):

    print("🏦 Sending to bank")

    if application["loan_amount"] < 40000:
        decision = "approved"
    else:
        decision = "review"

    application["status"] = decision

    print("🏦 Decision:", decision)

    return application
