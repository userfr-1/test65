import sqlite3
from datetime import datetime

DB = 'todo.db'

def create_db():
    with sqlite3.connect(DB) as con:
        c = con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        password TEXT
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS task (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        task TEXT,
                        time TEXT,
                        is_active INTEGER DEFAULT 1
                    )""")
        con.commit()

def register():
    print("\n=== Ro'yxatdan o'tish ===")
    username = input("Username: ")
    password = input("Parol: ")
    with sqlite3.connect(DB) as con:
        c = con.cursor()
        c.execute("SELECT * FROM user WHERE username = ?", (username,))
        if c.fetchone():
            print("Bu username allaqachon band.")
            return
        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        con.commit()
        print("Foydalanuvchi yaratildi.")

def login():
    print("\n=== Login ===")
    login_type = input("ID orqali (1) yoki username orqali (2)? ")
    with sqlite3.connect(DB) as con:
        c = con.cursor()
        if login_type == '1':
            try:
                user_id = int(input("ID kiriting: "))
                password = input("Parol: ")
                c.execute("SELECT * FROM user WHERE id = ? AND password = ?", (user_id, password))
            except:
                return None
        else:
            username = input("Username: ")
            password = input("Parol: ")
            c.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        if user:
            print(f"Xush kelibsiz, {user[1]}!")
            return user[0]
        else:
            print("Login yoki parol noto'g'ri.")
            return None

def add_task(user_id):
    task = input("Taskni kiriting: ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    with sqlite3.connect(DB) as con:
        c = con.cursor()
        c.execute("INSERT INTO task (user_id, task, time, is_active) VALUES (?, ?, ?, 1)",
                  (user_id, task, now))
        con.commit()
        print("Task qo‘shildi.")

def view_tasks(user_id):
    with sqlite3.connect(DB) as con:
        c = con.cursor()
        c.execute("SELECT id, task, time FROM task WHERE user_id = ? AND is_active = 1", (user_id,))
        tasks = c.fetchall()
        if tasks:
            print("\n--- Tasklar ---")
            for t in tasks:
                print(f"{t[0]}. {t[1]} ({t[2]})")
        else:
            print("Aktiv task yo'q.")

def delete_task(user_id):
    view_tasks(user_id)
    try:
        task_id = int(input("O'chiriladigan task ID: "))
        with sqlite3.connect(DB) as con:
            c = con.cursor()
            c.execute("UPDATE task SET is_active = 0 WHERE id = ? AND user_id = ?", (task_id, user_id))
            con.commit()
            print("Task o'chirildi.")
    except:
        print("Xatolik.")

def update_task(user_id):
    view_tasks(user_id)
    try:
        task_id = int(input("Tahrir qilinadigan task ID: "))
        new_task = input("Yangi task matni: ")
        with sqlite3.connect(DB) as con:
            c = con.cursor()
            c.execute("UPDATE task SET task = ? WHERE id = ? AND user_id = ?", (new_task, task_id, user_id))
            con.commit()
            print("Task yangilandi.")
    except:
        print("Xatolik.")

def task_menu(user_id):
    while True:
        print("\n--- Task Menyu ---")
        print("1. Ko'rish")
        print("2. Qo'shish")
        print("3. Yangilash")
        print("4. O'chirish")
        print("5. Orqaga")
        tanlov = input("Tanlov: ")
        if tanlov == '1':
            view_tasks(user_id)
        elif tanlov == '2':
            add_task(user_id)
        elif tanlov == '3':
            update_task(user_id)
        elif tanlov == '4':
            delete_task(user_id)
        elif tanlov == '5':
            break
        else:
            print("Xato tanlov.")

def main_menu():
    while True:
        print("\n=== TO DO LIST ===")
        print("1. Login")
        print("2. Chiqish")
        print("3. Ro'yxatdan o'tish")
        tanlov = input("Tanlov: ")
        if tanlov == '1':
            user_id = login()
            if user_id:
                task_menu(user_id)
        elif tanlov == '2':
            break
        elif tanlov == '3':
            register()
        else:
            print("Xato tanlov.")

create_db()
main_menu()
