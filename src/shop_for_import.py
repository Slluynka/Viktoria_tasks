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