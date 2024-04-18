#Створіть три різних екземпляри класу, викличте для кожного екземпляру метод describe_shop().
class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print(f'shop_name : {self.shop_name},  store_type: {self.store_type}')

    def open_shop(self):
        print(f'Магазин: "{self.shop_name}" відкритий')


store1 = Shop("Папая", "Одяг")
store2 = Shop("Нива","Продуктовий")
store3 = Shop("Zara","Одяг")

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()
