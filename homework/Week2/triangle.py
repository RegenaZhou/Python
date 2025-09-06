from math import sqrt
a,b,c=map(eval,input("请输入三角形的3条边长:").split())
if a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
    circumference=a+b+c
    p=(a+b+c)/2
    area=sqrt(p*(p-a)*(p-b)*(p-c))
    print("三角形的周长为:{:.2f}".format(circumference))
    print("三角形的面积为:{:.2f}".format(area))
else:
    print("无法构成三角形")