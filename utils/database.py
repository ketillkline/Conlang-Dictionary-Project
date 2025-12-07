import sqlite3

class DatabaseManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.Connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS "{db_name}"(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emoji TEXT NOT NULL,
        defintion TEXT NOT NULL,
        example TEXT
        )""")

        self.connection.commit()

    def add_entry(self, emoji: str, definition: str, example: str):
        self.cursor.executemany(f'''
        INSERT INTO {self.db_name} (emoji, definition, example) VALUES (?, ?, ?)''',
                                (emoji, definition, example))
        self.connection.commit()

    def fetch_entries(self):
        self.cursor.execute(f'''
        SELECT emoji, meaning, example FROM {self.db_name}
        ''')
        return self.cursor.fetch_all()


