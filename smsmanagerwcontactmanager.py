import re
import time

def info_logger(func):
    def wrapper(*args, **kwargs):
        print(f"\n[{func.__name__}] funksiyasi chaqirildi.")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Amal bajarilish vaqti: {round(end_time - start_time, 4)} soniya\n")
        return result
    return wrapper

class ContactManager:
    def __init__(self):
        self.contacts = []

    @info_logger
    def add_contact(self, name, phone):
        if not re.fullmatch(r"[A-Za-z\s]+", name):
            print("Xatolik! Ism faqat harflardan iborat bo'lishi kerak.")
            return
        if not re.fullmatch(r"(\+998)?\d{9}", phone):
            print("Xatolik! Telefon raqam noto'g'ri kiritildi.")
            return

        self.contacts.append({"name": name, "phone": phone})
        print(f"Kontakt qo'shildi: Ism: {name}, Telefon: {phone}")

    @info_logger
    def view_contacts(self):
        if not self.contacts:
            print("Kontaktlar ro'yxati bo'sh.")
        else:
            print("\nKontaktlar ro'yxati:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone']}")

    @info_logger
    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            removed = self.contacts.pop(index)
            print(f"Kontakt o'chirildi: {removed['name']} - {removed['phone']}")
        else:
            print("Xatolik! Noto'g'ri indeks kiritildi.")

class SMSManager(ContactManager):
    def __init__(self):
        super().__init__()
        self.messages = []

    def send_messages(self):
        if not self.contacts:
            print("Kontaktlar yo‘q.")
            return
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        tanlov = int(input("Qaysi kontaktga SMS yubormoqchisiz (raqamini kiriting): ")) - 1
        if 0 <= tanlov < len(self.contacts):
            sms_text = input("SMS matnini kiriting: ")
            msg = {"to": self.contacts[tanlov], "text": sms_text}
            self.messages.append(msg)
            print("SMS yuborildi!")
        else:
            print("Noto‘g‘ri tanlov.")

    def view_messages(self):
        if not self.messages:
            print("SMSlar ro'yxati bo'sh.")
        else:
            for i, msg in enumerate(self.messages, 1):
                print(f"{i}. {msg['to']['name']} - {msg['text']}")

    def delete_message(self, index):
        if 0 <= index < len(self.messages):
            deleted = self.messages.pop(index)
            print(f"{deleted['to']['name']} ga yuborilgan SMS o‘chirildi.")
        else:
            print("Xatolik! Noto‘g‘ri indeks.")

sms_manager = SMSManager()

while True:
    print("\n1. Kontakt menejer")
    print("2. SMS")
    print("3. Chiqish")

    choice = input("Tanlovni kiriting (1-3): ")

    if choice == '1':
        while True:
            print("\n-Kontakt menejer-")
            print("1. Kontakt qo'shish")
            print("2. Barcha kontaktlarni ko'rish")
            print("3. Kontakt o'chirish")
            print("4. Orqaga")

            choice = input("Tanlovni kiriting (1-4): ")

            if choice == '1':
                name = input("Ismni kiriting: ")
                phone = input("Telefon raqamni kiriting: ")
                sms_manager.add_contact(name, phone)

            elif choice == '2':
                sms_manager.view_contacts()

            elif choice == '3':
                sms_manager.view_contacts()
                try:
                    idx = int(input("O'chirmoqchi bo'lgan kontakt raqamini kiriting: ")) - 1
                    sms_manager.delete_contact(idx)
                except ValueError:
                    print("Xatolik! Raqam kiritilishi kerak edi.")

            elif choice == '4':
                break
            else:
                print("Noto'g'ri tanlov.")

    elif choice == '2':
        while True:
            print("\n-----SMS-----")
            print("1. SMS yuborish")
            print("2. SMSlar ro'yxati")
            print("3. SMS o'chirish")
            print("4. Orqaga")

            choice = input("Tanlovni kiriting (1-4): ")

            if choice == '1':
                sms_manager.send_messages()

            elif choice == '2':
                sms_manager.view_messages()

            elif choice == '3':
                sms_manager.view_messages()
                try:
                    idx = int(input("Qaysi SMSni o'chirmoqchisiz (raqamini kiriting): ")) - 1
                    sms_manager.delete_message(idx)
                except ValueError:
                    print("Xatolik! Raqam kiritilishi kerak edi.")
            elif choice == '4':
                break
            else:
                print("Noto‘g‘ri tanlov.")
    elif choice == '3':
        print("Dastur tugadi.")
        break
    else:
        print("Noto‘g‘ri tanlov.")
