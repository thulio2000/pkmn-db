import psycopg2
from decouple import config
import time

print("Starting...")
time.sleep(10)
try:
    conn = psycopg2.connect(
        dbname=config("POSTGRES_DB", default="my_database"),
        user=config("POSTGRES_USER", default="postgres_user"),
        password=config("POSTGRES_PASSWORD", default="postgres_password"),
        host=config("POSTGRES_HOST", default="postgres_db")
    )
    print("Connection working!")

except Exception as e:
    print(f"An error occurred: {e}")

try:
    cur = conn.cursor()
    print("Connection working!")
except Exception as e:
    print(f"An error ocurred: {e}")
