from class_privileges_admin import *

'''Збережіть клас User в одному модулі, а класи Privileges і Admin у іншому модулі.
В окремому файлі створіть екземпляр admin і викличте метод show_privileges(),
щоб перевірити, що все працює правильно.'''

admin = Admin("Victoria", "Yeremitsa",
              '06.11.2008', 'female',3)
admin.show_privileges()
