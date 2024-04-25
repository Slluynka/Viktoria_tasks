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