async def score_property(property_data):

    arv = property_data["price"] * 1.7
    repair = 30000

    profit = arv - property_data["price"] - repair

    score = 0

    if profit > 40000:
        score = 90
    elif profit > 20000:
        score = 70
    else:
        score = 40

    print("📊 Deal Score:", score)

    return score
