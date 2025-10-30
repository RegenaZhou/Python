class Student:
    # name=None
    # age=None
    # tel=None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu=Student("周杰伦",3,"18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)