from celery_app import celery_app


@celery_app.task(name="tasks.scrape_properties")
def scrape_properties():
    print("Scraping properties...")
