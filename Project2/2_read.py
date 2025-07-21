"""
Python学习笔记
在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Pyhton知识，
其中每一行都以"In Python you can"打头。
将这个文件命名为 learning_python.txt，并存储到为完成本章练习而编写的程序所在的目录中。
编写一个程序，它读取这个文件，并将你所写的内容打印三次：
第一次打印时读取整个文件；第二次打印时先将所有行都存储在一个列表中，再遍历列表中的各行。
"""

from pathlib import  Path
path=Path(r".\learning_python.txt")
content=path.read_text()
print(content)

lines=content.splitlines()
for line in lines:
    print(line)