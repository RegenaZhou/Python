"""
雇员
编写一个名为Employee的类，其方法__init__()接受名、姓和年薪，并将它们存储在属性中。
编写一个名为give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。
为Employee编写一个测试用例，其中包含两个测试方法：
test_give_default_raise()和test_give_custom_raise()。
在不使用夹具的情况下编写这两个测试，并确保它们都通过了。
然后，编写一个夹具，以免在每个测试函数中都创建一个Employee对象。
重新运行测试，确认两个测试都通过了。
"""

class Employee:
    def __init__(self, first_nane, last_name, salary):
        self.fist_nane = first_nane
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

