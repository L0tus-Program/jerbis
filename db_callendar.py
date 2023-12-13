import sqlite3

conn = sqlite3.connect('callendar.db')
cursor = conn.cursor()

query = '''CREATE TABLE IF NOT EXISTS Eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    descricao TEXT
);'''

cursor.execute(query)
conn.commit()
conn.close()