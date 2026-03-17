from sqlalchemy import create_engine

engine = create_engine("postgresql://user:pass@db/vortex")

def save_deal(data):

    with engine.connect() as conn:

        conn.execute(
            "INSERT INTO deals (address, price, score) VALUES (%s,%s,%s)",
            (data["address"], data["price"], data["score"])
        )
