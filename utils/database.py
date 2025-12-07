import sqlite3

class DatabaseManager:
    def __init__(self, db_name: str):
        self.connection = sqlite3.Connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {db_name}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emoji TEXT NOT NULL,
        defintion TEXT NOT NULL
        )
        """)