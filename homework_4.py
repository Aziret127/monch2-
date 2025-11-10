
class Contact:
    def __init__(self, name, phone_name):
        self.name = name
        self.phone_name = phone_name
    @staticmethod
    def validate_phone_number(phone_number):
        phone_number = phone_number.replace('-', '').replace("-", "")
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False
class ContactList:
    all_contacts = []
    @classmethod
    def add_contact( cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):

           new_contact = Contact(name, phone_number)
           ContactList.all_contacts.append(new_contact)
           print(f"Контакт {name} успешно добавлен!")
        else:
           print (ValueError("Номер должен содержать ровно 10 цифр:"))

print(ContactList.all_contacts) # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_name)
    # Вася Пупкин 0700100200
    # Виктор Цой 0500123456
ContactList.add_contact("John Doe", "5551234") # Error

