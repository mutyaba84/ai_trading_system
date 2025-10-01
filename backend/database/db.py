import sqlite3

def get_db():
    conn = sqlite3.connect("trades.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            side TEXT,
            qty INTEGER,
            price REAL,
            timestamp TEXT,
            status TEXT
        )
    """)
    conn.commit()
