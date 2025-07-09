import sqlite3

db = sqlite3.connect('bankomat_data.db')
cur = db.cursor()

def authenticate():
    card = input("Karta raqamini kiriting: ")
    pin_code = input("PIN kodini kiriting: ")
    cur.execute("SELECT * FROM cards WHERE card_number=? AND pin=?", (card, pin_code))
    info = cur.fetchone()
    if info:
        print(f"Salom, {info[3]}")
        return info
    else:
        print("Xatolik: noto‘g‘ri karta yoki PIN.")
        return None

def show_balance(client):
    print(f"Balansingiz: {client[2]} so‘m")

def add_funds(client):
    try:
        summa = int(input("Kiritiladigan summa: "))
        total = client[2] + summa
        cur.execute("UPDATE cards SET balance=? WHERE card_number=?", (total, client[0]))
        db.commit()
        print(f"{summa} so‘m qo‘shildi. Yangi balans: {total} so‘m")
        return (client[0], client[1], total, client[3])
    except:
        print("Xatolik: noto‘g‘ri qiymat")
        return client

def withdraw_funds(client):
    try:
        amount = int(input("Yechiladigan summa: "))
        if amount > client[2]:
            print("Balans yetarli emas.")
        else:
            total = client[2] - amount
            cur.execute("UPDATE cards SET balance=? WHERE card_number=?", (total, client[0]))
            db.commit()
            print(f"{amount} so‘m yechildi. Qolgan balans: {total} so‘m")
            return (client[0], client[1], total, client[3])
    except:
        print("Xatolik: noto‘g‘ri qiymat")
    return client

def run_atm():
    print("Bankomat tizimi")
    user = None
    while not user:
        user = authenticate()
    while True:
        print("\n1. Balansni ko‘rish")
        print("2. Pul yechish")
        print("3. Pul qo‘shish")
        print("4. Chiqish")
        tanlov = input("Tanlang: ")
        if tanlov == "1":
            show_balance(user)
        elif tanlov == "2":
            user = withdraw_funds(user)
        elif tanlov == "3":
            user = add_funds(user)
        elif tanlov == "4":
            print("Tizimdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    run_atm()