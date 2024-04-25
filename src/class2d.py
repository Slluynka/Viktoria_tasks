'''Напишіть клас Privileges.
Клас повинен містити всього один атрибут privileges зі списком, який треба забрати із класу Admin.
Водночас, необхідно перемістити метод show_privileges() у клас Privileges із класу Admin.
Створіть екземпляр priv як атрибут класу Admin.
Створіть новий екземпляр admin і використайте метод для виведення списку привілеїв.'''
class Privileges:
    def __init__(self):
        self.privileges = ['Allowed to add message1',
              'Allowed to delete message1', 'Allowed to ban users1']
    def show_privileges(self):
        print(self.privileges)



