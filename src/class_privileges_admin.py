from class_user import *
class Admin(User):
    def __init__(self, first_name, last_name, birth_date, gender, login_attempts):
        super().__init__(first_name, last_name, birth_date, gender, login_attempts)
        self.privileges = ['Allowed to add message',
              'Allowed to delete message', 'Allowed to ban users']
        self.priv = Privileges()
    def show_privileges(self):
        print(self.privileges)
class Privileges:
    def __init__(self):
        self.privileges = ['Allowed to add message1',
              'Allowed to delete message1', 'Allowed to ban users1']
    def show_privileges(self):
        print(self.privileges)