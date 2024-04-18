'''Додайте метод з ім’ям set_number_of_units(), що дозволяє задати кількість видів товару.
Викличте метод з новим числом, знову виведіть значення. Додайте метод з ім’ям increment_number_of_units(),
який збільшує кількість видів товару на задану величину. Викличте цей метод.'''
class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f'shop_name : {self.shop_name},  store_type: {self.store_type}')

    def open_shop(self):
        print(f'Магазин: "{self.shop_name}" відкритий')
    def set_number_of_units(self, number_of_units):
        self.number_of_units =  number_of_units
        print('Нова кількість видів товару: ',store.number_of_units)
    def increment_number_of_units(self, inc):
        self.number_of_units = self.number_of_units + inc
        print('Нова кількість видів товару: ', store.number_of_units)



#store = Shop("Папая", "Одяг", 500)
store = Shop("Папая", "Одяг", 1000)
a = int(input("Введіть к-сть: "))
store.set_number_of_units(a)
a = int(input("Введіть к-сть: "))
store.increment_number_of_units(a)