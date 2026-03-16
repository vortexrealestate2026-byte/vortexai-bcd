from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "vortex_agents",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

celery_app.conf.timezone = "UTC"

celery_app.conf.beat_schedule = {

    # Real estate scrapers every 3 hours
    "run-real-estate-agents": {
        "task": "app.tasks.scheduler.launch_real_estate_agents",
        "schedule": crontab(minute=0, hour="*/3"),
    },

    # Vehicle scrapers every 2 hours
    "run-vehicle-agents": {
        "task": "app.tasks.scheduler.launch_vehicle_agents",
        "schedule": crontab(minute=0, hour="*/2"),
    },

    # Deal analyzer every 2 hours
    "run-deal-analyzers": {
        "task": "app.tasks.scheduler.launch_deal_analyzers",
        "schedule": crontab(minute=30, hour="*/2"),
    },
}
