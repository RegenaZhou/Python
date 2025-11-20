def gcd(a, b):
    if b>a:
        a,b=b,a
    ys=a%b
    while ys!=0:
        a,b=b,ys
        ys=a%b
    return b

def lcm(a,b):
    return a*b//gcd(a,b)

a,b=map(int,input("本程序用于计算最大公约数和最小公倍数\n请输入两个整数:").split())
print(f"最大公约数为:{gcd(a,b)}")
print(f"最小公倍数为:{lcm(a,b)}")