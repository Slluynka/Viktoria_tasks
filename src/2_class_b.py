'''Додайте атрибут login_attempts у клас User.
Напишіть метод increment_login_attempts(), що збільшує значення login_attempts на 1.
Напишіть інший метод з ім’ям reset_login_attempts(), обнуляє значення login_attempts.
Створіть екземпляр класу User і викличте increment_login_attempts() кілька разів.
Виведіть значення login_attempts, щоб переконатися у тому, що значення було змінено правильно,
а потім викличте reset_login_attempts(). Знову виведіть login_attempts і переконайтеся у тому,
що значення обнулилося.'''
class User:
    def __init__(self, first_name, last_name, birth_date, gender,login_attempts=0):
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
    def reset_login_attempts(self):
        self.login_attempts = 0
#що воно закидує у метод з одни атрибутом селф?
user1 = User('Nastia', 'Yeremitsa', '06.11.2008', 'female')
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)