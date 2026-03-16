from celery import shared_task

from tasks.agents_launcher import (
    zillow_scraper,
    redfin_scraper,
    autotrader_scraper,
    kijiji_vehicle_scraper,
    deal_analyzer
)

US_CITIES = [
    "Atlanta",
    "Houston",
    "Dallas",
    "Phoenix",
    "Tampa"
]

CANADA_CITIES = [
    "Winnipeg",
    "Steinbach",
    "Regina"
]


@shared_task
def launch_all_agents():

    for city in US_CITIES:
        zillow_scraper.delay(city)
        redfin_scraper.delay(city)

    for city in CANADA_CITIES:
        autotrader_scraper.delay(city)
        kijiji_vehicle_scraper.delay(city)

    for _ in range(5):
        deal_analyzer.delay()

    return "All agents launched"
