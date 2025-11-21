import random
target=random.randint(0,1000)
print("欢迎进入猜数字游戏")
count=0
while True:
    guess=eval(input("请输入一个0~1000之间的整数:"))
    while type(guess) != int:
        print("输入内容必须为整数!")
        guess=eval(input("请重新输入一个0~1000之间的整数:"))
    count+=1
    if guess>target:
        print("猜大了")
    elif guess<target:
        print("猜小了")
    else:
        print(f"你猜了{count}次,猜对了,真厉害.")
        break