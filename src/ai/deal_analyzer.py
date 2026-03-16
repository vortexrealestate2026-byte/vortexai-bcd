import logging

logger = logging.getLogger("vortex-ai")

def analyze_property(property):

    price = property["price"]
    sqft = property.get("sqft", 1)

    price_per_sqft = price / sqft

    arv = price * 1.3
    repair_cost = price * 0.1
    wholesale_margin = arv - price - repair_cost

    score = 0

    if wholesale_margin > 50000:
        score += 5

    if price_per_sqft < 120:
        score += 3

    if wholesale_margin > 100000:
        score += 2

    return {
        "arv": arv,
        "repair_cost": repair_cost,
        "wholesale_margin": wholesale_margin,
        "deal_score": score
    }
