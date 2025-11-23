def f(x,num):
    return pow(x,2)-num

def df(x):
    return 2*x

num=int(input("请输入您要开根的正整数:"))
deta=1e-5
x=num
count=0
while True:
    if abs(f(x,num))<deta:
        break
    else:
        x=x-f(x,num)/df(x)
        count+=1
print(f"迭代了{count}次,求得{num}的平方根为{x}\n误差为{abs(x-num**0.5)}")
