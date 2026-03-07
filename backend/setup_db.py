from config.db import init_db
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    print("Starting database initialization for cloud DB...")
    try:
        init_db()
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")
