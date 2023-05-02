import psycopg2

try:
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    print("Connection working!")

except Exception as e:
    print(f"An error occurred: {e}")

try:
    cur = conn.cursor()
    print("Connection working!")
except Exception as e:
    print(f"An error occurred: {e}")


