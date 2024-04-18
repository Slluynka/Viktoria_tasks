'''Додайте атрибут number_of_units зі значенням за замовчуванням 0;
він представляє кількість видів товару у магазині. Створіть екземпляр з ім’ям store.
Виведіть значення number_of_units, а потім змініть number_of_units і виведіть знову.'''
class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f'shop_name : {self.shop_name},  store_type: {self.store_type}')

    def open_shop(self):
        print(f'Магазин: "{self.shop_name}" відкритий')


#store = Shop("Папая", "Одяг", 500)
store = Shop("Папая", "Одяг", 1000)
print(store.number_of_units)