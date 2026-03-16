from celery import shared_task
import random
import time

# =========================
# REAL ESTATE SCRAPER AGENTS
# =========================

@shared_task
def zillow_scraper(city):
    print(f"Scraping Zillow in {city}")
    time.sleep(2)

@shared_task
def redfin_scraper(city):
    print(f"Scraping Redfin in {city}")
    time.sleep(2)

@shared_task
def facebook_property_scraper(city):
    print(f"Scraping Facebook Marketplace properties in {city}")
    time.sleep(2)

@shared_task
def foreclosure_scraper(city):
    print(f"Scraping foreclosure deals in {city}")
    time.sleep(2)


# =========================
# VEHICLE INVENTORY AGENTS
# =========================

@shared_task
def autotrader_scraper(city):
    print(f"Scraping AutoTrader vehicles in {city}")
    time.sleep(2)

@shared_task
def kijiji_vehicle_scraper(city):
    print(f"Scraping Kijiji Autos vehicles in {city}")
    time.sleep(2)

@shared_task
def facebook_vehicle_scraper(city):
    print(f"Scraping Facebook Marketplace vehicles in {city}")
    time.sleep(2)


# =========================
# DEAL ANALYZER AGENTS
# =========================

@shared_task
def deal_analyzer():
    score = random.randint(70, 100)
    print(f"Deal scored: {score}")
    return score
