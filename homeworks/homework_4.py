
class Contact:
    def __init__(self, name, phone_name, id):
        self.name = name
        self.phone_name = phone_name
        self.id = id
    @staticmethod
    def validate_phone_number(phone_number):
        phone_number = phone_number.replace('-', '').replace("-", "")
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False
class ContactList:
    all_contacts = []
    last_id = 0
    @classmethod
    def add_contact(cls, name, phone_number, id):
        if Contact.validate_phone_number(phone_number):
           cls.id = +1
           new_contact = Contact(name, phone_number, cls.last_id)

           cls.all_contacts.append(new_contact)
           print(f"Контакт {name} успешно добавлен! Добавлен контакт: {new_contact.name} (ID: {new_contact.id})")
        else:
           print (ValueError("Номер должен содержать ровно 10 цифр:"))
    @classmethod
    def remove_contact(cls, contact_id):
        for contact in cls.all_contacts:
            if contact_id == contact_id:
                cls.all_contacts.remove(contact)
                cls.last_id = contact.id
                print(f"Контакт с ID {contact_id} удалён.")
                return
        print(f"Контакт с ID {contact_id} не найден.")

print(ContactList.last_id) # 0

ContactList.add_contact("Вася Пупкин", "0700100200", 5498465454)
ContactList.add_contact("Виктор Цой", "0500123456",65486689654)
print(ContactList.last_id) # 2

ContactList.remove_contact(1)

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_name, contact.id)

# print(ContactList.all_contacts) # []
#
# ContactList.add_contact("Вася Пупкин", "0700100200",5646132165)
# ContactList.add_contact("Виктор Цой", "0500123456",544646468)
#
# for contact in ContactList.all_contacts:
#     print(contact.name, contact.phone_name)
#     # Вася Пупкин 0700100200
#     # Виктор Цой 0500123456
# ContactList.add_contact("John Doe", "5551234",16545461) # Error
#















# data = []
# while True:
#     time = input('ведите веремя:').lower()
#     data.append(time)
#     if time == 'stop':
#         print('exit..')
#         break
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'вечер' or time == 'вечер':
#         print('good evening')
#     else:
#         print('hello (точное время суток не распознано)')
#     print(data)
#

