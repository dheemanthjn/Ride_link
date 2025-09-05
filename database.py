from server.models import RideRequest


# Simulate DB connection (replace with actual Postgres connection if needed)
def save_ride(ride: RideRequest):
    try:
        # TODO: integrate with real Postgres (psycopg2 / SQLAlchemy)
        print("We will store this data in Postgres now:")
        print(ride.dict())
    except Exception as e:
        print("Database save failed:", e)
