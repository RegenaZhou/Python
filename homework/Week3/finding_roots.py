"""
用牛顿迭代法求方程e^(2x)+x-4=0区间[0.5,1]内根的近似值
"""
import math
def f(x):
    return pow(math.e,2*x)+x-4

def df(x):
    return 2*pow(math.e,2*x)+1

deta=1e-5
x=1
count=0
while True:
    if abs(f(x))<deta:
        break
    else:
        x=x-f(x)/df(x)
        count+=1
print(f"迭代了{count}次,求得该方程的根为{x}")