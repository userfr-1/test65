from contextlib import contextmanager

@contextmanager
def my_context():
    print("Context ichiga kirdik")
    try:
        yield
    finally:
        print("contextdan chiqdik")

with my_context():
    print("context manager ishlamoqda")
    
@contextmanager
def file_manager(file_name,mode):
    f = None
    try:
        if "." not in file_name:
            raise NameError
        print("Fayl '{file_name}' ochilyapti")
        f = open(file_name, mode)
        yield f
    finally:
        if f:
            print(f"Fayl {file_name} yoplimoqda")
            f.close()

with file_manager('avtosalon.py','r') as file:
    f = file.read()