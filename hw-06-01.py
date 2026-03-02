from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self._is_valid_phone(value):
            raise ValueError("Phone number must have exactly 10 digits")
        super().__init__(value)

    def _is_valid_phone(self, value):
        digits_only = "".join(ch for ch in value if ch.isdigit())
        if len(digits_only) == 10:
            return True
        return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                new_phone_obj = Phone(new_phone)
                phone.value = new_phone_obj.value
                return True
        return False

    def find_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                return phone
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False


if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    print("----- edit phone for John -----")
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")

    print("----- delete Jane -----")
    book.delete("Jane")

    for name, record in book.data.items():
        print(record)
        