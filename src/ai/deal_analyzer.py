import logging

logger = logging.getLogger("vortex-ai")


def analyze_property(property):

    price = property.get("price", 0)
    sqft = property.get("sqft", 1)

    if sqft == 0:
        sqft = 1

    price_per_sqft = price / sqft

    # Estimated After Repair Value
    arv = price * 1.3

    # Estimated repair cost
    repair_cost = price * 0.1

    # Estimated wholesale profit
    wholesale_margin = arv - price - repair_cost

    score = 0

    if wholesale_margin > 50000:
        score += 5

    if price_per_sqft < 120:
        score += 3

    if wholesale_margin > 100000:
        score += 2

    logger.info(
        f"Deal analyzed | price:{price} | margin:{wholesale_margin} | score:{score}"
    )

    return {
        "price": price,
        "sqft": sqft,
        "price_per_sqft": price_per_sqft,
        "arv": arv,
        "repair_cost": repair_cost,
        "wholesale_margin": wholesale_margin,
        "deal_score": score
    }
