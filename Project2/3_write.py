"""
访客薄
编写一个while循环，提示用户输入其名字。收集用户输入的所有名字，
将其写入guest_book.txt，并确保这个文件中的每记录都独占一行。
"""
from pathlib import  Path

names=""
user_input=input("请输入访客的名字（完成所有名字输入后，请输入q终止程序）：")
while user_input!="q":
    names+=user_input+"\n"
    user_input = input("请输入访客的名字（完成所有名字输入后，请输入q终止程序）：")
path=Path(r".\guest_book.txt")
path.write_text(names)