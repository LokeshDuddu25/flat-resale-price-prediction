import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

def execute(sql, data=None, fetch=False):
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)

    if fetch:
        return cursor.fetchall()

    conn.commit()
