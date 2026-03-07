import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

_connection = None

def get_db_connection(with_db=True):
    global _connection
    
    # Try to reuse the global connection if it's healthy
    if _connection:
        try:
            _connection.ping(reconnect=True)
            return _connection
        except Exception:
            try:
                _connection.close()
            except:
                pass
            _connection = None

    try:
        config = {
            'host': os.getenv('DB_HOST', '127.0.0.1'),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', ''),
            'port': int(os.getenv('DB_PORT', 3306)),
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor if with_db else None,
            'connect_timeout': 10,
            'read_timeout': 10,
            'write_timeout': 10,
            'autocommit': True
        }
        
        ssl_ca = os.getenv('DB_SSL_CA')
        if ssl_ca:
            config['ssl'] = {'ca': ssl_ca}

        if with_db:
            config['database'] = os.getenv('DB_NAME', 'fitness_db')
        
        _connection = pymysql.connect(**config)
        return _connection
    except Exception as e:
        print(f"Error connecting to Database: {e}")
        return None

def init_db():
    # First, connect without a database to create it if it doesn't exist
    conn = get_db_connection(with_db=False)
    if not conn:
        print("Failed to connect to MySQL server. Ensure MySQL is running and credentials are correct.")
        return
    
    cursor = conn.cursor()
    db_name = os.getenv('DB_NAME', 'fitness_db')
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    conn.commit()
    cursor.close()
    conn.close()

    # Now connect with the database to create tables
    conn = get_db_connection(with_db=True)
    if not conn:
        print("Failed to initialize database tables.")
        return
    cursor = conn.cursor()
    
    # Create Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create Profiles Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        user_id INT PRIMARY KEY,
        age INT NOT NULL,
        gender VARCHAR(10) NOT NULL,
        weight FLOAT NOT NULL,
        height FLOAT NOT NULL,
        activity_level VARCHAR(50) NOT NULL,
        goal VARCHAR(50) NOT NULL,
        diet_type VARCHAR(20) DEFAULT 'non_vegetarian',
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)

    # Create User Progress Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_progress (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        entry_date DATE NOT NULL,
        diet_completed BOOLEAN DEFAULT FALSE,
        workout_completed BOOLEAN DEFAULT FALSE,
        streak_count INT DEFAULT 0,
        UNIQUE KEY user_date (user_id, entry_date),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully.")
