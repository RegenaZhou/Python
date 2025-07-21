"""
加法运算
提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。
在此情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
编写一个程序，提示用户输入两个数，再将其相加并打印结果。
在用户输入的任何一个值不是数时都捕获ValueError异常，并打印一条友好的错误消息。
对你编写的程序进行测试时：先输入两个数，再输入一些文本而不是数。
"""

user_input1=input("请输入第一个数字：")
user_input2=input("请输入第二个数字：")
try:
    result=int(user_input1)+int(user_input2)
except ValueError:
    print("请输入合理的数字。")
else:
    print(result)