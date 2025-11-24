import string

s=input("请输入字符串:")
w=input("请输入你要检查的单词:")
flag=False

# string.punctuation是Python标准库中的一个字符串常量，包含所有英文标点符号：!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`
for char in string.punctuation:
    s=s.replace(char,' ')

# print(s)
s=s.split()
# print(s)

for i in s:
    if i.lower()==w.lower():
        flag=True

if flag:
    print("YES")
else:
    print("NO")
