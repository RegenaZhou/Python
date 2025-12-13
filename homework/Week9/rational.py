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

    def __str__(self):
        """字符串表示"""
        if self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"

def add(Rational1, Rational2):
    new_numerator = Rational1.numerator * Rational2.denominator + Rational2.numerator * Rational1.denominator
    new_denominator = Rational1.denominator * Rational2.denominator
    return Rational(new_numerator, new_denominator)

def mul(Rational1, Rational2):
    new_numerator = Rational1.numerator * Rational2.numerator
    new_denominator = Rational1.denominator * Rational2.denominator
    return Rational(new_numerator, new_denominator)

numerator = int(input("请输入第一个有理数的分子:"))
denominator = int(input("请输入第一个有理数的分母:"))
r1 = Rational(numerator, denominator)
numerator = int(input("请输入第二个有理数的分子:"))
denominator = int(input("请输入第二个有理数的分母:"))
r2 = Rational(numerator, denominator)

print(f"{r1} + {r2} = {add(r1, r2)}")
print(f"{r1} * {r2} = {mul(r1, r2)}")