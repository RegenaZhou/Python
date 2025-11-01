class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法 用于实现类对象转字符串的行为
    def __str__(self):
        return f"Student类对象，name: {self.name}, age: {self.age}"

    # __lt__魔术方法 用于2个类对象进行小于或大于比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法 用于2个类对象进行小于等于或大于等于比较
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法 用于2个类对象进行相等比较
    def __eq__(self, other):
        return self.age == other.age

stu1=Student("周杰伦",31)
stu2=Student("林俊杰",36)
print(stu1==stu2) # ==符号 如果没有实现eq这个魔术方法 它默认比较内存地址 两个独立的对象内存地址不同
print(stu1<=stu2)
print(stu1) #if not __str__ print <__main__.Student object at 0x0000016E915FC6E0>
print(str(stu1)) # if not __str__ print <__main__.Student object at 0x0000016E915FC6E0>