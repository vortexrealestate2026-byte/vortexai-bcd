def submit_to_bank(application):

    print("🏦 Submitting application to bank...")

    loan_amount = application["loan_amount"]

    # simple decision logic
    if loan_amount <= 40000:
        decision = "approved"
    elif loan_amount <= 70000:
        decision = "review"
    else:
        decision = "declined"

    application["status"] = decision

    print("🏦 Bank decision:", decision)

    return application
