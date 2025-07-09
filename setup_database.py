import sqlite3

db = sqlite3.connect('bankomat_data.db')
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS cards (
    card_number TEXT PRIMARY KEY,
    pin TEXT,
    balance INTEGER,
    owner TEXT
)
''')

cards = [
    ("8600123412341234", "1111", 300000, "Shavkat Normurodov"),
    ("8600987698769876", "2222", 450000, "Dilshod Beknazarov"),
    ("8600555566667777", "3333", 1000000, "Malika Alimova"),
    ("8600111122223333", "4444", 150000, "Jasur Qodirov"),
    ("8600444433332222", "5555", 600000, "Rayhona Usmonova")
]

cur.executemany("INSERT OR REPLACE INTO cards VALUES (?, ?, ?, ?)", cards)
db.commit()
db.close()

print("Bazaga ma'lumotlar qo‘shildi.")