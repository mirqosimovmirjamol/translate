import sqlite3


def create_db():
    conn = sqlite3.connect('test.db')
    curr = conn.cursor()

    curr.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        user_id INTEGER UNIQUE
    )

    """)
    conn.commit()
    conn.close()