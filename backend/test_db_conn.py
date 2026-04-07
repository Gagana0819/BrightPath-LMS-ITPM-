import os
import psycopg2
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

db_url = os.environ.get('SUPABASE_DB_URL')
print(f"Testing connection to: {db_url}")

try:
    config = dj_database_url.parse(db_url)
    print(f"Parsed config: {config}")
    conn = psycopg2.connect(
        dbname=config['NAME'],
        user=config['USER'],
        password=config['PASSWORD'],
        host=config['HOST'],
        port=config['PORT']
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
