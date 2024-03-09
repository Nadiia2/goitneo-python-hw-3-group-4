from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        if len(phone) ==  10 and phone.isdigit():
            super().__init__(phone)
        else:
            print('Must be 10 numbers')



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
        # return "Phone added"

    def edit_phone(self, old_phone, phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = phone
            #     return "Phone changed"
            # else: 
            #     return "This phone already exists"
            
    
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
            # else:
            #     return "Not found"

    def find_phone(self, search_phone):
        for p in self.phones:
            if p.value == search_phone:
                return p
            # else:
            #     return "Not found"


    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"
    


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        name = record.name.value
        self.data.update({name : record})
    
    def find(self, name):
        if name in self.data:
            return self.data.get(name)
        else:
            return "Not found"
            
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return "Not found"



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("1111111111")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
john.remove_phone("1111111111")
# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
print(john)

# Видалення запису Jane
book.delete("Jane")