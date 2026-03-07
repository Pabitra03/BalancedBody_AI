from config.db import init_db
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    print("Starting database initialization for TiDB Cloud...")
    try:
        init_db()
        print("Successfully initialized tables in the cloud!")
    except Exception as e:
        print(f"Error during initialization: {e}")
