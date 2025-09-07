from math import sqrt
def equation(a,b,c):
    deta=b*b-4*a*c
    if deta<0:
        x1=(-b+sqrt(-deta)*1j)/(2*a)
        x2=(-b-sqrt(-deta)*1j)/(2*a)
        print("x1={:.2f} x2={:.2f}".format(x1,x2))
    elif deta==0:
        x=(-b+sqrt(deta))/(2*a)
        print("x={:.2f}".format(x))
    else:
        x1=(-b+sqrt(deta))/(2*a)
        x2=(-b-sqrt(deta))/(2*a)
        print("x1={:.2f} x2={:.2f}".format(x1,x2))

a,b,c=map(eval,input("请分别输入ax^2+bx+c=0的系数a,b,c:").split())
equation(a,b,c)