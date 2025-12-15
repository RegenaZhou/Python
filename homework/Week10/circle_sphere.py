import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"周长 = {self.perimeter():.2f}\n面积 = {self.area():.2f}"

class Sphere(Circle):

    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return 4*math.pi * self.radius ** 2

    def volume(self):
        return 4/3 * math.pi * self.radius ** 3

    def __str__(self):
        return f"表面积 = {self.area():.2f}\n体积 = {self.volume():.2f}"


radius=eval(input("请输入圆的半径: "))
circle=Circle(radius)
print(circle)

radius=eval(input("请输入球的半径: "))
sphere=Sphere(radius)
print(sphere)