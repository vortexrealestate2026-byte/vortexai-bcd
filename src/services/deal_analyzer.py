def analyze_property(price, arv):

    margin = arv - price
    score = 0

    if price < arv * 0.6:
        score = 10
    elif price < arv * 0.7:
        score = 7
    elif price < arv * 0.8:
        score = 5

    return {
        "margin": margin,
        "score": score
    }


def analyze_vehicle(price, market):

    margin = market - price
    score = 0

    if price < market * 0.6:
        score = 10
    elif price < market * 0.75:
        score = 7
    elif price < market * 0.9:
        score = 5

    return {
        "margin": margin,
        "score": score
    }
