''''Створіть клас з ім’ям User.
Створіть два атрибути first_name і last_name, а потім ще кілька атрибутів, які зазвичай зберігаються
у профілі користувача. Напишіть метод describe_user який виводить повне ім’я користувача.
Створіть ще один метод greeting_user() для виведення персонального вітання для користувача.
Створіть кілька
примірників, які представляють різних користувачів. Викличте обидва методи для кожного користувача.'''
class User:
    def __init__(self, first_name, last_name, birth_date, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
    def describe_user(self):
        print(f"Повне ім'я користувача: {self.first_name} {self.last_name}")
    def greeting_user(self):
        print(f"Вітаємо, {self.first_name} {self.last_name}!")
user1 = User('Nastia', 'Yeremitsa', '06.11.2008', 'female')
user2 = User('Victoria', 'Yeremitsa', '14.10.2005', 'female')
user3 = User('Igor', 'Romanchuk', '07.07.2006', 'male')
user1.describe_user()
user2.describe_user()
user3.describe_user()
user1.greeting_user()
user2.greeting_user()
user3.greeting_user()