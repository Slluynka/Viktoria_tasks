"""Напишіть клас Discount(), що успадковує від класу Shop().
Додайте атрибут з ім’ям discount_products для зберігання списку товарів, на які встановлена знижка.
Напишіть метод get_discounts_ptoducts,
який виводить цей список. Створіть екземпляр store_discount і викличте цей метод."""
class Shop:
    def __init__(self, shop_name, store_type, number_of_units):
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
class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units, discount_products):
        super().__init__(shop_name, store_type, number_of_units)
        self.discount_products = discount_products
    def get_discounts_products(self):
        print(self.discount_products)



#store = Shop("Папая", "Одяг", 500)
store_discount = Discount("Папая", "Одяг",
             1000, ["Кроп-топ", "Спідниця", "Чокер"])
store_discount.get_discounts_products()