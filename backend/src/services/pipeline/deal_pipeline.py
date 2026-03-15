import time
from workers.ingestion_worker import ingest_source
from workers.ai_analysis_worker import process_property
from workers.cleanup_worker import cleanup_logs, cleanup_expired_deals
from database import SessionLocal
from models import Property
from ingestion.sources import fetch_zillow, fetch_realtor, fetch_craigslist

class DealPipeline:
    def __init__(self):
        self.db = SessionLocal()

    def ingest(self):
        print("[Pipeline] Starting ingestion phase")
        ingest_source(self.db, "zillow", fetch_zillow)
        ingest_source(self.db, "realtor", fetch_realtor)
        ingest_source(self.db, "craigslist", fetch_craigslist)

    def analyze(self):
        print("[Pipeline] Starting AI analysis phase")
        unprocessed = (
            self.db.query(Property)
            .filter(Property.processed == False)
            .all()
        )

        for prop in unprocessed:
            process_property(self.db, prop)
            prop.processed = True
            self.db.commit()

    def cleanup(self):
        print("[Pipeline] Starting cleanup phase")
        cleanup_logs(self.db)
        cleanup_expired_deals(self.db)

    def run_once(self):
        print("[Pipeline] Running full pipeline once")
        self.ingest()
        self.analyze()
        self.cleanup()
        print("[Pipeline] Completed")

    def run_forever(self, interval=30):
        print("[Pipeline] Running continuous pipeline")
        while True:
            self.run_once()
            time.sleep(interval)

if __name__ == "__main__":
    pipeline = DealPipeline()
    pipeline.run_forever()
