class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print(f'shop_name : {self.shop_name},  store_type: {self.store_type}')

    def open_shop(self):
        print(f'Магазин : "{self.shop_name}" відкритий')

store = Shop("Папая", "Одяг")
#store1 = Shop()
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()