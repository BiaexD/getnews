import sqlite3

def connection():
    return sqlite3.connect('news.db')

def create_database():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            link TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()