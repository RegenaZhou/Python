"""
用牛顿迭代法求函数f(x)=x^4-4x^3+6x^2-4x+1的极值点
"""
def f(x):
    return pow(x,4)-4*pow(x,3)+6*pow(x,2)-4*x+1

def df(x):
    return 4*pow(x,3)-12*pow(x,2)+12*x-4

def d2f(x):
    return 12*pow(x,2)-24*x+12

deta=1e-15
x=10
count=0
while True:
    if abs(df(x))<deta:
        break
    else:
        x=x-df(x)/d2f(x)
        count+=1
print(f"迭代了{count}次,求得该函数在x={x}时取得极{"大" if d2f(x)<0 else "小"}值{f(x)}")