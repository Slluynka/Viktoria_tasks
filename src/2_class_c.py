'''Адміністратор - користувач з повними адміністративними привілеями.
Напишіть клас з ім’ям Admin, що успадковує від класу User.
Додайте атрибут privileges для зберігання списку рядків виду «Allowed to add message»,
«Allowed to delete users», «Allowed to ban users» і т. д.
Напишіть метод show_privileges() для виведення набору привілеїв адміністратора.
Створіть екземпляр Admin і викличте метод.'''
class User:
    def __init__(self, first_name, last_name, birth_date, gender,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"Повне ім'я користувача: {self.first_name} {self.last_name}")
    def greeting_user(self):
        print(f"Вітаємо, {self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
class Admin(User):
    def __init__(self, first_name, last_name, birth_date, gender, login_attempts):
        super().__init__(first_name, last_name, birth_date, gender, login_attempts)
        self.privileges = ['Allowed to add message',
              'Allowed to delete message', 'Allowed to ban users']
    def show_privileges(self):
        print(self.privileges)
admin = Admin("Victoria", "Yeremitsa",
              '06.11.2008', 'female',3)
admin.show_privileges()