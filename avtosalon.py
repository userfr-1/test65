import sqlite3

DB_NAME = "avtosalon.db"

def baza_yarat():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS salon (id INTEGER PRIMARY KEY, nom TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS mashina (id INTEGER PRIMARY KEY, nom TEXT, salon_id INTEGER)")
    con.commit()
    con.close()

def boshlangich_salonlar():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM salon")
    if cur.fetchone()[0] == 0:
        names = ["Avto City", "Turbo Auto", "Fast Motors", "Mega Car", "Lux Avto"]
        for name in names:
            cur.execute("INSERT INTO salon (nom) VALUES (?)", (name,))
    con.commit()
    con.close()


def salon_korish():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("SELECT * FROM salon")
    for s in cur.fetchall():
        print(f"{s[0]}. {s[1]}")
    con.close()


def mashina_korish(salon_id):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("SELECT * FROM mashina WHERE salon_id = ?", (salon_id,))
    mashinalar = cur.fetchall()
    if mashinalar:
        for m in mashinalar:
            print(f"{m[0]}. {m[1]}")
    else:
        print("Mashina yo'q.")
    con.close()


def mashina_qosh(salon_id):
    nom = input("Mashina nomi: ")
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("INSERT INTO mashina (nom, salon_id) VALUES (?, ?)", (nom, salon_id))
    con.commit()
    con.close()
    print("Mashina qo‘shildi.")

def mashina_ochir(salon_id):
    mashina_korish(salon_id)
    id = int(input("O'chiriladigan mashina ID: "))
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("DELETE FROM mashina WHERE id = ? AND salon_id = ?", (id, salon_id))
    con.commit()
    con.close()
    print("O'chirildi.")

def mashina_tahrir(salon_id):
    mashina_korish(salon_id)
    id = int(input("Tahrirlanadigan mashina ID: "))
    yangi_nomi = input("Yangi nom: ")
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("UPDATE mashina SET nom = ? WHERE id = ? AND salon_id = ?", (yangi_nomi, id, salon_id))
    con.commit()
    con.close()
    print("Tahrirlandi.")

def salon_qoshish():
    nom = input("Yangi avtosalon nomi: ")
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("INSERT INTO salon (nom) VALUES (?)", (nom,))
    con.commit()
    con.close()
    print("Salon qo‘shildi.")


def salon_ochirish():
    salon_korish()
    id = int(input("O‘chiriladigan salon ID: "))
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("DELETE FROM mashina WHERE salon_id = ?", (id,))
    cur.execute("DELETE FROM salon WHERE id = ?", (id,))
    con.commit()
    con.close()
    print("Salon va mashinalar o‘chirildi.")

def salon_panel(salon_id):
    while True:
        print("\n1. Mashinalarni ko‘rish")
        print("2. Mashina qo‘shish")
        print("3. Mashina o‘chirish")
        print("4. Mashina tahrirlash")
        print("5. Orqaga")
        tanlov = input("Tanlov: ")
        if tanlov == '1':
            mashina_korish(salon_id)
        elif tanlov == '2':
            mashina_qosh(salon_id)
        elif tanlov == '3':
            mashina_ochir(salon_id)
        elif tanlov == '4':
            mashina_tahrir(salon_id)
        elif tanlov == '5':
            break
        else:
            print("Xato tanlov!")

def menyu():
    while True:
        print("\n=== Avtosalon Panel ===")
        print("1. Salonlar ro'yxati")
        print("2. Yangi salon qo‘shish")
        print("3. Salonni o‘chirish")
        print("4. Chiqish")
        tanlov = input("Tanlov: ")
        if tanlov == '1':
            salon_korish()
            id = int(input("Salon ID kiriting (orqaga = 0): "))
            if id != 0:
                salon_panel(id)
        elif tanlov == '2':
            salon_qoshish()
        elif tanlov == '3':
            salon_ochirish()
        elif tanlov == '4':
            print("Dastur tugadi.")
            break
        else:
            print("Xato tanlov!")

baza_yarat()
boshlangich_salonlar()
menyu()
