class Rational:
    def __init__(self, numerator=1, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为零")
        gcd = self._gcd(numerator, denominator)
        # print(gcd)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        """加法运算"""
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        """减法运算"""
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        """乘法运算"""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        """除法运算"""
        if other.numerator == 0:
            raise ZeroDivisionError("除零错误")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __str__(self):
        """字符串表示"""
        if self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"


numerator = int(input("请输入第一个有理数的分子:"))
denominator = int(input("请输入第一个有理数的分母:"))
r1 = Rational(numerator, denominator)
numerator = int(input("请输入第二个有理数的分子:"))
denominator = int(input("请输入第二个有理数的分母:"))
r2 = Rational(numerator, denominator)

print(f"有理数1: {r1}")
print(f"有理数2: {r2}")

print(f"加法: {r1} + {r2} = {r1 + r2}")
print(f"减法: {r1} - {r2} = {r1 - r2}")
print(f"减法: {r2} - {r1} = {r2 - r1}")
print(f"乘法: {r1} * {r2} = {r1 * r2}")
print(f"除法: {r1} ÷ {r2} = {r1 / r2}")
print(f"除法: {r2} ÷ {r1} = {r2 / r1}")
