"""
冰激凌小店是一种特殊的餐馆。编写一个名为IceCreamStand的类。
让它继承Restaurant类。
添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。
编写一个显示这些冰激凌的方法。IceCreamStand实例，并调用这个方法。
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐厅名：{self.restaurant_name}")
        print(f"菜系：{self.cuisine_type}")

    def open_restaurant(self):
        print("餐厅开始营业...")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "甜品")
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)

so_sweet=IceCreamStand("So Sweet",["香蕉","草莓","哈密瓜","开心果"])
so_sweet.describe_restaurant()
so_sweet.show_flavors()